#!/usr/bin/env python3
"""Diagnostic-only probe for frozen NMIR 0086c.

Outputs source-native PDF text spans and vector drawing metadata. It performs no
axis calibration, curve naming, coordinate transform, interpolation, or
scientific classification. Its sole purpose is parser-conformance inspection
under the already frozen 0086c contract.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import tarfile
import urllib.request
from pathlib import Path

ARXIV_ID = "2606.17320v2"
ARCHIVE_SHA256 = "4981fbe374836ed52c24c26955f90fa118295ff86aeab69f9f5f3449e60a3b9e"
TARGET = "bminusl_unbroken.pdf"
TARGET_SHA256 = "d4b0ba8aa1cb05dad76f12c1fc6c8f98eb5c6e72dd53a6d47402b9d21b023393"
URLS = (f"https://export.arxiv.org/e-print/{ARXIV_ID}", f"https://arxiv.org/e-print/{ARXIV_ID}")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download() -> tuple[bytes, str]:
    errs=[]
    for u in URLS:
        try:
            req=urllib.request.Request(u,headers={"User-Agent":"NMIR-0086c-probe"})
            with urllib.request.urlopen(req,timeout=90) as r:
                data=r.read()
            if sha(data)!=ARCHIVE_SHA256:
                raise RuntimeError(f"archive hash mismatch {sha(data)}")
            return data,u
        except Exception as e:
            errs.append(f"{u}: {type(e).__name__}: {e}")
    raise RuntimeError(" | ".join(errs))


def extract_target(archive: bytes) -> bytes:
    with tarfile.open(fileobj=io.BytesIO(archive),mode="r:*") as tf:
        members=[m for m in tf.getmembers() if m.isfile() and Path(m.name).name==TARGET]
        if len(members)!=1:
            raise RuntimeError(f"expected exactly one {TARGET}, got {len(members)}")
        data=tf.extractfile(members[0]).read()
    if sha(data)!=TARGET_SHA256:
        raise RuntimeError(f"target hash mismatch {sha(data)}")
    return data


def drawing_item(item):
    op=item[0]
    vals=[]
    for v in item[1:]:
        if hasattr(v,"x") and hasattr(v,"y"):
            vals.append([float(v.x),float(v.y)])
        elif hasattr(v,"x0"):
            vals.append([float(v.x0),float(v.y0),float(v.x1),float(v.y1)])
        else:
            try: vals.append(float(v))
            except Exception: vals.append(str(v))
    return [op,*vals]


def main() -> int:
    import fitz
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="na64_vector_probe_0086c.json")
    args=ap.parse_args()
    archive,url=download()
    pdf=extract_target(archive)
    doc=fitz.open(stream=pdf,filetype="pdf")
    pages=[]
    for pno,page in enumerate(doc):
        td=page.get_text("dict")
        spans=[]
        for block in td.get("blocks",[]):
            for line in block.get("lines",[]):
                for sp in line.get("spans",[]):
                    spans.append({
                        "text":sp.get("text",""),
                        "bbox":[float(x) for x in sp.get("bbox",[])],
                        "origin":[float(x) for x in sp.get("origin",[])],
                        "size":float(sp.get("size",0.0)),
                        "font":sp.get("font"),
                        "flags":sp.get("flags"),
                    })
        drawings=[]
        for i,d in enumerate(page.get_drawings()):
            drawings.append({
                "index":i,
                "rect":[float(d["rect"].x0),float(d["rect"].y0),float(d["rect"].x1),float(d["rect"].y1)],
                "color":list(d.get("color")) if d.get("color") is not None else None,
                "fill":list(d.get("fill")) if d.get("fill") is not None else None,
                "width":float(d.get("width",0.0)),
                "dashes":d.get("dashes"),
                "closePath":bool(d.get("closePath",False)),
                "fill_opacity":float(d.get("fill_opacity",1.0)),
                "stroke_opacity":float(d.get("stroke_opacity",1.0)),
                "items":[drawing_item(it) for it in d.get("items",[])],
            })
        pages.append({
            "page":pno,
            "rect":[float(page.rect.x0),float(page.rect.y0),float(page.rect.x1),float(page.rect.y1)],
            "text_spans":spans,
            "drawings":drawings,
            "images":len(page.get_images(full=True)),
        })
    out={
        "gate":"0086c-diagnostic",
        "source_url":url,
        "archive_sha256":sha(archive),
        "target":TARGET,
        "target_sha256":sha(pdf),
        "pages":pages,
        "guards":{
            "axis_calibration_performed":False,
            "curve_identity_assigned":False,
            "coordinate_transform_performed":False,
            "interpolation_performed":False,
            "manual_or_ocr_digitization_performed":False,
            "scientific_classification_performed":False,
        },
    }
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True),encoding="utf-8")
    print(json.dumps({
        "archive_sha256":out["archive_sha256"],
        "target_sha256":out["target_sha256"],
        "pages":len(pages),
        "text_spans":sum(len(p["text_spans"]) for p in pages),
        "drawings":sum(len(p["drawings"]) for p in pages),
        "images":sum(p["images"] for p in pages),
    },indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
