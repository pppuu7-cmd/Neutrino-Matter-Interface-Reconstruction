#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import io
import json
import re
import tarfile
import tempfile
import unicodedata
import urllib.request
from pathlib import Path

import fitz  # PyMuPDF

ARXIV_ID = "2603.00554"
SOURCE_URLS = (
    f"https://export.arxiv.org/e-print/{ARXIV_ID}",
    f"https://arxiv.org/e-print/{ARXIV_ID}",
    f"https://arxiv.org/src/{ARXIV_ID}",
)
SOURCE_SHA256 = "09ab22f753ac3f5fbde5be65ac50926de67b0638550366d158aadcfde8e92564"
ASSETS = {
    "vector_BL_PnX_XnT_LZ_combined.pdf": "ace761499623535907263e780a6e96a17474adf418d3f9363dae8e28bc5e7a39",
    "BL_vector_PnX_XnT_LZ.pdf": "06092f863d59cb9e7318384d44f8eb7b3421c79ee9c56fd9b64aed42f3e32071",
}
MIN_PATH_CONSTRUCTION = 100
MIN_PATH_PAINT = 20
MASS_TOKENS = ("mass", "mev", "gev", "ev")
OTHER_TOKENS = ("b-l", "xenon", "pandax", "lz", "coherent", "coupling")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download() -> tuple[str, bytes]:
    last = None
    for url in SOURCE_URLS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-reproducibility-audit/1.0"})
            with urllib.request.urlopen(req, timeout=45) as r:
                payload = r.read()
            if payload:
                return url, payload
        except Exception as exc:
            last = repr(exc)
    raise RuntimeError(f"all source endpoints failed: {last}")


def safe_extract(tf: tarfile.TarFile, root: Path) -> None:
    rr = root.resolve()
    for member in tf.getmembers():
        target = (root / member.name).resolve()
        if rr not in target.parents and target != rr:
            raise RuntimeError("unsafe tar member")
    tf.extractall(root)


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower().replace("−", "-").replace("–", "-")
    return re.sub(r"\s+", " ", text)


def audit_pdf(pdf_bytes: bytes) -> dict:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    if doc.page_count < 1:
        raise ValueError("PDF has no pages")
    image_count = 0
    drawing_count = 0
    path_item_count = 0
    texts = []
    pages = []
    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        images = page.get_images(full=True)
        drawings = page.get_drawings()
        text = page.get_text("text") or ""
        image_count += len(images)
        drawing_count += len(drawings)
        path_items = sum(len(d.get("items", ())) for d in drawings)
        path_item_count += path_items
        texts.append(text)
        pages.append({
            "page_index": page_index,
            "image_xobjects": len(images),
            "vector_drawings": len(drawings),
            "path_construction_items": path_items,
            "text_characters": len(text),
        })
    norm = normalize_text("\n".join(texts))
    mass_hits = sorted({tok for tok in MASS_TOKENS if tok in norm})
    # Include a conservative standalone m token only when it appears as a mathematical word boundary.
    if re.search(r"(?:^|\W)m(?:$|\W)", norm):
        mass_hits.append("m")
    other_hits = sorted({tok for tok in OTHER_TOKENS if tok in norm})
    if re.search(r"(?:^|\W)g(?:$|\W)", norm):
        other_hits.append("g")
    return {
        "page_count": doc.page_count,
        "recursive_image_xobject_count": image_count,
        "path_paint_proxy_vector_drawing_count": drawing_count,
        "path_construction_operation_proxy_count": path_item_count,
        "extracted_text_characters": len(norm),
        "normalized_text_excerpt": norm[:2000],
        "mass_token_hits": sorted(set(mass_hits)),
        "coupling_model_experiment_token_hits": sorted(set(other_hits)),
        "pages": pages,
    }


def main() -> None:
    try:
        used_url, payload = download()
        actual_source_sha = sha256(payload)
        if actual_source_sha != SOURCE_SHA256:
            raise ValueError(f"source SHA256 mismatch: {actual_source_sha}")
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            with tarfile.open(fileobj=io.BytesIO(payload), mode="r:*") as tf:
                safe_extract(tf, root)
            results = {}
            all_hash = True
            all_pages = True
            all_no_images = True
            all_paths = True
            all_text = True
            for name, expected_sha in ASSETS.items():
                path = root / name
                if not path.is_file():
                    raise ValueError(f"missing frozen asset: {name}")
                data = path.read_bytes()
                actual_sha = sha256(data)
                audit = audit_pdf(data)
                checks = {
                    "asset_sha256_match": actual_sha == expected_sha,
                    "page_present": audit["page_count"] >= 1,
                    "zero_image_xobjects": audit["recursive_image_xobject_count"] == 0,
                    "path_construction_threshold": audit["path_construction_operation_proxy_count"] >= MIN_PATH_CONSTRUCTION,
                    "path_paint_threshold": audit["path_paint_proxy_vector_drawing_count"] >= MIN_PATH_PAINT,
                    "text_nonempty": audit["extracted_text_characters"] > 0,
                }
                all_hash &= checks["asset_sha256_match"]
                all_pages &= checks["page_present"]
                all_no_images &= checks["zero_image_xobjects"]
                all_paths &= checks["path_construction_threshold"] and checks["path_paint_threshold"]
                all_text &= checks["text_nonempty"]
                results[name] = {
                    "expected_sha256": expected_sha,
                    "actual_sha256": actual_sha,
                    "checks": checks,
                    **audit,
                }

            combined = results["vector_BL_PnX_XnT_LZ_combined.pdf"]
            semantic_ok = bool(combined["mass_token_hits"]) and bool(combined["coupling_model_experiment_token_hits"])
            structure_ok = all_hash and all_pages and all_no_images and all_paths and all_text
            if structure_ok and semantic_ok:
                status = "PASS_PRIMARY_B_L_VECTOR_ASSET_INTEGRITY"
            elif structure_ok:
                status = "PARTIAL_VECTOR_ASSET_INTEGRITY"
            else:
                status = "SCIENTIFIC_FAIL_VECTOR_ASSET_INTEGRITY"

            result = {
                "iteration": "0078a",
                "status": status,
                "source_url": used_url,
                "source_sha256": actual_source_sha,
                "source_sha256_match": actual_source_sha == SOURCE_SHA256,
                "combined_semantic_token_check": semantic_ok,
                "thresholds": {
                    "image_xobjects_exact": 0,
                    "min_path_construction_proxy": MIN_PATH_CONSTRUCTION,
                    "min_path_paint_proxy": MIN_PATH_PAINT,
                },
                "assets": results,
                "guard": "Integrity audit only: no axis calibration, contour coordinate extraction, numerical limit readout, manual/raster interpretation, or post-result semantic reassignment.",
            }
    except (OSError, urllib.error.URLError, RuntimeError) as exc:
        result = {"iteration": "0078a", "status": "INFRASTRUCTURE_FAIL", "reason": repr(exc)}
    except (ValueError, fitz.FileDataError) as exc:
        result = {"iteration": "0078a", "status": "SCIENTIFIC_FAIL_VECTOR_ASSET_INTEGRITY", "reason": repr(exc)}

    Path("deromeri_2603_vector_integrity_0078a.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    compact = dict(result)
    for asset in compact.get("assets", {}).values():
        asset.pop("normalized_text_excerpt", None)
    print(json.dumps(compact, indent=2, sort_keys=True))
    if result.get("status") == "SCIENTIFIC_FAIL_VECTOR_ASSET_INTEGRITY":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
