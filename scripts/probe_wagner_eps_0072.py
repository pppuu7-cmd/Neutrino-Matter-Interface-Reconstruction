#!/usr/bin/env python3
"""Non-numerical structural probe of primary WEP_figure6.eps for NMIR 0072.

This does not digitize a contour. It records PostScript structure needed to freeze a
prospective calibrated-vector extraction contract before any contour coordinates are
computed.
"""
from __future__ import annotations
import argparse, hashlib, io, json, re, tarfile, urllib.request
from collections import Counter

URL = "https://arxiv.org/e-print/1207.2442"
TARGET = "WEP_figure6.eps"


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", required=True); args = ap.parse_args()
    req = urllib.request.Request(URL, headers={"User-Agent":"NMIR-0072-eps-probe/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read(); final_url = r.geturl()
    with tarfile.open(fileobj=io.BytesIO(body), mode="r:gz") as tf:
        m = tf.getmember(TARGET); eps = tf.extractfile(m).read()
    text = eps.decode("latin-1", errors="replace")
    lines = text.splitlines()
    bbox = [x for x in lines if x.startswith("%%BoundingBox") or x.startswith("%%HiResBoundingBox")]
    # Capture explicit RGB commands and common shorthand definitions/usages.
    rgb = re.findall(r"(?<![\w.])([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s+([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s+([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s+(?:setrgbcolor|srgb)\b", text)
    rgb_counts = Counter(tuple(float(v) for v in t) for t in rgb)
    # Keep only text-bearing lines relevant to axis/curve labels, not arbitrary binary content.
    keys = ("EW", "Princeton", "Moscow", "LLR", "EXCLUDED", "lambda", "alpha", "B-L")
    label_lines = []
    for i, line in enumerate(lines, 1):
        if any(k.lower() in line.lower() for k in keys):
            label_lines.append({"line":i, "text":line[:500]})
    # Operator frequency helps identify whether paths are direct moveto/lineto vector paths.
    ops = {}
    for op in ("moveto","lineto","curveto","stroke","setrgbcolor","show"," M"," L"," C"):
        ops[op.strip()] = text.count(op)
    out = {
        "iteration":"0072",
        "source":"Wagner et al. arXiv:1207.2442v1 / WEP_figure6.eps",
        "purpose":"vector-structure probe only; no contour coordinates",
        "archive_sha256":hashlib.sha256(body).hexdigest(),
        "eps_sha256":hashlib.sha256(eps).hexdigest(),
        "eps_bytes":len(eps),
        "final_url":final_url,
        "bounding_box_lines":bbox,
        "explicit_rgb_counts":[{"rgb":list(k),"count":v} for k,v in sorted(rgb_counts.items())],
        "label_lines":label_lines,
        "operator_counts":ops,
        "header_lines":lines[:40],
    }
    with open(args.output,"w",encoding="utf-8") as f: json.dump(out,f,indent=2,sort_keys=True); f.write("\n")
    print(json.dumps(out,sort_keys=True))
    return 0
if __name__ == "__main__": raise SystemExit(main())
