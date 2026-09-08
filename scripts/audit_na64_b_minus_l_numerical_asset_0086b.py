#!/usr/bin/env python3
"""NMIR 0086b — NA64 B-L numerical asset/materialization authority audit.

This gate inventories and hashes exact arXiv source bytes before any geometry
interpretation. It may establish source-native numerical/vector authority but
MUST NOT transform coordinates, interpolate curves, compute areas, or compose
constraints.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import tarfile
import tempfile
import urllib.request
from pathlib import Path
from typing import Iterable

ARXIV_ID = "2606.17320v2"
DEFAULT_URLS = (
    f"https://export.arxiv.org/e-print/{ARXIV_ID}",
    f"https://arxiv.org/e-print/{ARXIV_ID}",
)
NUMERICAL_EXTS = {".csv", ".dat", ".json", ".npy", ".npz", ".root", ".tsv"}
CODE_EXTS = {".py", ".c", ".cc", ".cpp", ".cxx", ".C", ".m", ".nb"}
VECTOR_EXTS = {".eps", ".svg", ".pgf", ".tikz"}
PDF_EXTS = {".pdf"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download_source(urls: Iterable[str] = DEFAULT_URLS) -> tuple[bytes, str]:
    errors = []
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-source-audit/0086b"})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) < 1024:
                raise RuntimeError(f"source payload unexpectedly small: {len(data)} bytes")
            return data, url
        except Exception as exc:  # pragma: no cover - network-dependent
            errors.append(f"{url}: {type(exc).__name__}: {exc}")
    raise RuntimeError("all source download URLs failed: " + " | ".join(errors))


def _safe_members(tf: tarfile.TarFile):
    for m in tf.getmembers():
        name = m.name.replace("\\", "/")
        if m.isfile() and not name.startswith("/") and "../" not in name:
            yield m


def unpack_inventory(source: bytes, out_dir: Path) -> list[dict]:
    rows = []
    with tarfile.open(fileobj=io.BytesIO(source), mode="r:*") as tf:
        for m in _safe_members(tf):
            raw = tf.extractfile(m).read()  # type: ignore[union-attr]
            dest = out_dir / m.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(raw)
            rows.append({
                "path": m.name,
                "size": len(raw),
                "sha256": sha256_bytes(raw),
                "ext": Path(m.name).suffix,
            })
    return sorted(rows, key=lambda x: x["path"])


def tex_evidence(out_dir: Path, inventory: list[dict]) -> dict:
    tex_paths = [r["path"] for r in inventory if r["ext"].lower() == ".tex"]
    evidence = []
    graphics = []
    include_re = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
    for rel in tex_paths:
        text = (out_dir / rel).read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        for i, line in enumerate(lines, 1):
            low = line.lower()
            if any(k in low for k in ("b-l", "b_{-l}", "b_{\\! - \\! l}", "g_{b-l}", "g_{b\\! - \\! l}")) or "confidence" in low or "exclu" in low or "90\\%" in low or "90 %" in low:
                evidence.append({"file": rel, "line": i, "text": line[:800]})
        for m in include_re.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            lo, hi = max(1, line_no - 6), min(len(lines), line_no + 6)
            context = "\n".join(lines[lo - 1:hi])
            graphics.append({
                "file": rel,
                "line": line_no,
                "target": m.group(1),
                "context": context[:4000],
                "bl_context": bool(re.search(r"B\s*[-\\]\s*L|B-L|g_\{B", context, flags=re.I)),
                "limit_context": bool(re.search(r"exclu|limit|constraint|confidence|90\\?%|90\s*%", context, flags=re.I)),
            })
    return {"tex_files": tex_paths, "evidence": evidence, "graphics": graphics}


def resolve_graphic_target(target: str, inventory: list[dict]) -> list[dict]:
    norm = target.strip().replace("\\", "/")
    target_path = Path(norm)
    candidates = []
    for row in inventory:
        p = Path(row["path"])
        if target_path.suffix:
            match = p.as_posix().endswith(target_path.as_posix())
        else:
            match = p.with_suffix("").as_posix().endswith(target_path.as_posix())
        if match:
            candidates.append(row)
    return candidates


def inspect_pdf_vector(path: Path) -> dict:
    result = {"available": False, "pages": 0, "drawing_count": 0, "image_count": 0, "error": None}
    try:
        import fitz  # PyMuPDF, installed by hosted workflow
        doc = fitz.open(path)
        drawings = 0
        images = 0
        for page in doc:
            drawings += len(page.get_drawings())
            images += len(page.get_images(full=True))
        result.update({"available": True, "pages": len(doc), "drawing_count": drawings, "image_count": images})
    except Exception as exc:  # pragma: no cover - optional runtime dependency
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


def classify(out_dir: Path, inventory: list[dict], tex: dict) -> dict:
    rows_by_path = {r["path"]: r for r in inventory}
    source_native_numeric = [r for r in inventory if r["ext"].lower() in NUMERICAL_EXTS]
    source_native_code = [r for r in inventory if r["ext"] in CODE_EXTS or r["ext"].lower() in {x.lower() for x in CODE_EXTS}]

    linked_assets = []
    for g in tex["graphics"]:
        for row in resolve_graphic_target(g["target"], inventory):
            item = dict(row)
            item.update({"source_tex": g["file"], "source_line": g["line"], "bl_context": g["bl_context"], "limit_context": g["limit_context"]})
            ext = row["ext"].lower()
            if ext in PDF_EXTS:
                item["pdf_vector_probe"] = inspect_pdf_vector(out_dir / row["path"])
            linked_assets.append(item)

    vector_candidates = []
    for item in linked_assets:
        ext = item["ext"].lower()
        if not (item["bl_context"] and item["limit_context"]):
            continue
        if ext in VECTOR_EXTS:
            vector_candidates.append(item)
        elif ext in PDF_EXTS:
            probe = item.get("pdf_vector_probe", {})
            if probe.get("available") and probe.get("drawing_count", 0) > 0:
                vector_candidates.append(item)

    # Semantic authority is deliberately conservative: source text must contain
    # B-L, an exclusion/limit statement, and an explicit confidence-level token.
    ev_text = "\n".join(e["text"] for e in tex["evidence"])
    has_bl = bool(re.search(r"B\s*[-\\]\s*L|B-L|g_\{B", ev_text, flags=re.I))
    has_limit = bool(re.search(r"exclu|limit|constraint", ev_text, flags=re.I))
    has_cl = bool(re.search(r"90\\?%|90\s*%|confidence", ev_text, flags=re.I))
    semantics_ok = has_bl and has_limit and has_cl

    if semantics_ok and (source_native_numeric or vector_candidates):
        classification = "PASS_NA64_B_L_NUMERICAL_ASSET_AUTHORITY"
    elif semantics_ok and source_native_code:
        classification = "PASS_NA64_B_L_NUMERICAL_ASSET_AUTHORITY"
    else:
        pdf_limit_candidates = [x for x in linked_assets if x["bl_context"] and x["limit_context"] and x["ext"].lower() == ".pdf"]
        if pdf_limit_candidates:
            classification = "BLOCKED_NA64_B_L_RASTER_ONLY_GEOMETRY"
        else:
            classification = "BLOCKED_NA64_B_L_ASSET_ACCESS"

    return {
        "classification": classification,
        "semantics": {"has_bl": has_bl, "has_limit": has_limit, "has_cl": has_cl, "ok": semantics_ok},
        "numerical_assets": source_native_numeric,
        "code_assets": source_native_code,
        "linked_assets": linked_assets,
        "vector_candidates": vector_candidates,
    }


def run(source: bytes, source_url: str) -> dict:
    with tempfile.TemporaryDirectory(prefix="nmir0086b-") as td:
        root = Path(td)
        inventory = unpack_inventory(source, root)
        tex = tex_evidence(root, inventory)
        result = classify(root, inventory, tex)
        return {
            "gate": "0086b",
            "arxiv_id": ARXIV_ID,
            "source_url": source_url,
            "archive_size": len(source),
            "archive_sha256": sha256_bytes(source),
            "file_count": len(inventory),
            "inventory_sha256": sha256_bytes(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()),
            "inventory": inventory,
            "tex_authority": tex,
            **result,
            "guards": {
                "coordinate_transform_performed": False,
                "interpolation_performed": False,
                "area_calculation_performed": False,
                "cross_family_composition_performed": False,
                "manual_or_ocr_digitization_performed": False,
            },
        }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--output", default="na64_b_minus_l_asset_audit_0086b.json")
    p.add_argument("--source-file", default=None, help="Optional already-frozen source archive")
    args = p.parse_args()
    if args.source_file:
        source = Path(args.source_file).read_bytes()
        source_url = f"file:{args.source_file}"
    else:
        source, source_url = download_source()
    result = run(source, source_url)
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("gate", "classification", "archive_sha256", "archive_size", "file_count", "inventory_sha256")}, indent=2))
    print("vector_candidates", len(result["vector_candidates"]))
    print("numerical_assets", len(result["numerical_assets"]))
    print("code_assets", len(result["code_assets"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
