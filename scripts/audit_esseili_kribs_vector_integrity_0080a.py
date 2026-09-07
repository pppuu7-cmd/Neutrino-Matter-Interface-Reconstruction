#!/usr/bin/env python3
import hashlib
import io
import json
import re
import tarfile
import urllib.request
from collections import Counter

import pymupdf

SOURCE_URL = "https://export.arxiv.org/e-print/2308.07955v2"
SOURCE_SHA256 = "484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c"
ASSETS = [
    "Presentation/CnstrntPlotMajoranaNeff.pdf",
    "Presentation/CnstrntPlotDiracNeff.pdf",
    "Presentation/CnstrntPlotMajoranaYp.pdf",
    "Presentation/CnstrntPlotDiracYp.pdf",
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_source() -> bytes:
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "NMIR-vector-integrity/0080a"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def color_key(c):
    if c is None:
        return None
    return tuple(round(float(x), 6) for x in c)


def inspect_pdf(data: bytes, name: str):
    doc = pymupdf.open(stream=data, filetype="pdf")
    pages = len(doc)
    page = doc[0] if pages else None
    images = page.get_images(full=True) if page else []
    drawings = page.get_drawings() if page else []
    words_raw = page.get_text("words") if page else []
    words = [
        {"x0": w[0], "y0": w[1], "x1": w[2], "y1": w[3], "text": w[4], "block": w[5], "line": w[6], "word": w[7]}
        for w in words_raw
    ]
    item_count = sum(len(d.get("items", [])) for d in drawings)
    stroke_counts = Counter(str(color_key(d.get("color"))) for d in drawings if d.get("color") is not None)
    fill_counts = Counter(str(color_key(d.get("fill"))) for d in drawings if d.get("fill") is not None)
    tick_like = [w for w in words if re.search(r"10|−|-|\d", w["text"])]
    result = {
        "asset": name,
        "asset_sha256": sha256(data),
        "bytes": len(data),
        "page_count": pages,
        "page_size": [page.rect.width, page.rect.height] if page else None,
        "image_xobject_count": len(images),
        "drawing_count": len(drawings),
        "path_item_count": item_count,
        "word_count": len(words),
        "stroke_color_counts": dict(stroke_counts),
        "fill_color_counts": dict(fill_counts),
        "tick_like_words": tick_like,
        "words": words,
    }
    result["integrity_pass"] = (
        pages == 1 and len(images) == 0 and len(drawings) > 0 and item_count > 0 and len(words) > 0
    )
    result["vector_native_pass"] = pages == 1 and len(images) == 0 and len(drawings) > 0 and item_count > 0
    return result


def audit():
    raw = fetch_source()
    if sha256(raw) != SOURCE_SHA256:
        raise RuntimeError(f"source SHA mismatch: {sha256(raw)}")
    records = []
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tf:
        by_norm = {m.name.lstrip("./"): m for m in tf.getmembers() if m.isfile()}
        for asset in ASSETS:
            if asset not in by_norm:
                raise RuntimeError(f"missing frozen asset: {asset}")
            fh = tf.extractfile(by_norm[asset])
            if fh is None:
                raise RuntimeError(f"cannot extract frozen asset: {asset}")
            records.append(inspect_pdf(fh.read(), asset))
    all_vector = all(r["vector_native_pass"] for r in records)
    all_text = all(r["word_count"] > 0 for r in records)
    if all_vector and all_text:
        classification = "PASS_COSMOLOGY_B_L_VECTOR_INTEGRITY"
    elif all_vector:
        classification = "PARTIAL_COSMOLOGY_B_L_VECTOR_TEXT_BLOCKED"
    else:
        classification = "SCIENTIFIC_FAIL_COSMOLOGY_B_L_VECTOR_INTEGRITY"
    return {
        "iteration": "0080a",
        "classification": classification,
        "source_url": SOURCE_URL,
        "source_sha256": SOURCE_SHA256,
        "assets": records,
        "all_four_vector_native": all_vector,
        "all_four_text_extractable": all_text,
        "guard": "Vector integrity/machine structure only; no axis calibration, contour-color selection, threshold selection, scenario union, envelope union, or response scan.",
    }


def main():
    result = audit()
    with open("esseili_kribs_vector_integrity_0080a.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["classification"].startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
