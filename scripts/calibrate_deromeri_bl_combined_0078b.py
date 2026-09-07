#!/usr/bin/env python3
from __future__ import annotations

import colorsys
import hashlib
import io
import itertools
import json
import math
import re
import tarfile
import tempfile
import urllib.request
from pathlib import Path

import fitz

ARXIV_ID = "2603.00554"
SOURCE_URLS = (f"https://export.arxiv.org/e-print/{ARXIV_ID}", f"https://arxiv.org/e-print/{ARXIV_ID}")
SOURCE_SHA256 = "09ab22f753ac3f5fbde5be65ac50926de67b0638550366d158aadcfde8e92564"
ASSET = "vector_BL_PnX_XnT_LZ_combined.pdf"
ASSET_SHA256 = "ace761499623535907263e780a6e96a17474adf418d3f9363dae8e28bc5e7a39"
X_EXPS = (-5, -4, -3, -2, -1, 0, 1)
Y_EXPS = (-8, -7, -6, -5, -4, -3, -2)
MARGIN_DECADE = 0.05
MAX_FIT_RESID = 0.015
MAX_LOO_RESID = 0.03


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download() -> tuple[str, bytes]:
    last = None
    for url in SOURCE_URLS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-vector-calibration/1.0"})
            with urllib.request.urlopen(req, timeout=45) as r:
                data = r.read()
            if data:
                return url, data
        except Exception as exc:
            last = repr(exc)
    raise RuntimeError(f"source download failed: {last}")


def safe_extract(tf: tarfile.TarFile, root: Path) -> None:
    rr = root.resolve()
    for member in tf.getmembers():
        target = (root / member.name).resolve()
        if rr not in target.parents and target != rr:
            raise RuntimeError("unsafe tar member")
    tf.extractall(root)


def fit_affine(coords, exps):
    n = len(coords)
    mc = sum(coords) / n
    me = sum(exps) / n
    den = sum((c - mc) ** 2 for c in coords)
    if den <= 0:
        raise ValueError("degenerate axis coordinates")
    a = sum((c - mc) * (e - me) for c, e in zip(coords, exps)) / den
    b = me - a * mc
    residuals = [a * c + b - e for c, e in zip(coords, exps)]
    loo = []
    for k in range(n):
        cc = [c for i, c in enumerate(coords) if i != k]
        ee = [e for i, e in enumerate(exps) if i != k]
        aa, bb, _, _ = fit_affine_no_loo(cc, ee)
        loo.append(aa * coords[k] + bb - exps[k])
    return a, b, residuals, loo


def fit_affine_no_loo(coords, exps):
    n = len(coords)
    mc = sum(coords) / n
    me = sum(exps) / n
    den = sum((c - mc) ** 2 for c in coords)
    if den <= 0:
        raise ValueError("degenerate axis coordinates")
    a = sum((c - mc) * (e - me) for c, e in zip(coords, exps)) / den
    b = me - a * mc
    residuals = [a * c + b - e for c, e in zip(coords, exps)]
    return a, b, residuals, []


def numeric_tick_words(page):
    out = []
    for w in page.get_text("words"):
        x0, y0, x1, y1, text = w[:5]
        norm = text.strip().replace("−", "-").replace("–", "-").replace(" ", "")
        if re.fullmatch(r"10-?\d+", norm):
            out.append({"text": norm, "x0": x0, "y0": y0, "x1": x1, "y1": y1,
                        "xc": 0.5 * (x0 + x1), "yc": 0.5 * (y0 + y1)})
    return out


def identify_axes(page, ticks):
    W, H = page.rect.width, page.rect.height
    xsets = []
    for comb in itertools.combinations(range(len(ticks)), 7):
        pts = [ticks[i] for i in comb]
        ys = [p["yc"] for p in pts]
        xs = sorted(p["xc"] for p in pts)
        if max(ys) - min(ys) <= 0.02 * H and xs[-1] - xs[0] >= 0.45 * W:
            xsets.append(tuple(comb))
    if len(xsets) != 1:
        raise ValueError(f"x-axis tick subset not unique: {len(xsets)} candidates")
    xset = set(xsets[0])
    remaining = [i for i in range(len(ticks)) if i not in xset]
    ysets = []
    for comb in itertools.combinations(remaining, 7):
        pts = [ticks[i] for i in comb]
        xrights = [p["x1"] for p in pts]
        ys = sorted(p["yc"] for p in pts)
        if max(xrights) - min(xrights) <= 0.03 * W and ys[-1] - ys[0] >= 0.45 * H:
            ysets.append(tuple(comb))
    if len(ysets) != 1:
        raise ValueError(f"y-axis tick subset not unique: {len(ysets)} candidates")
    xpts = sorted((ticks[i] for i in xsets[0]), key=lambda p: p["xc"])
    ypts = sorted((ticks[i] for i in ysets[0]), key=lambda p: p["yc"], reverse=True)  # bottom -> top in PDF
    return xpts, ypts


def color_is_magenta(rgb):
    if rgb is None or len(rgb) < 3:
        return False
    r, g, b = (max(0.0, min(1.0, float(v))) for v in rgb[:3])
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    deg = h * 360.0
    return 285.0 <= deg <= 345.0 and s >= 0.35 and v >= 0.35


def item_points(item):
    pts = []
    for obj in item[1:]:
        if isinstance(obj, fitz.Point):
            pts.append((float(obj.x), float(obj.y)))
        elif isinstance(obj, fitz.Rect):
            pts.extend([(obj.x0, obj.y0), (obj.x1, obj.y0), (obj.x1, obj.y1), (obj.x0, obj.y1)])
        elif isinstance(obj, fitz.Quad):
            pts.extend([(p.x, p.y) for p in (obj.ul, obj.ur, obj.lr, obj.ll)])
    return pts


def main():
    try:
        used_url, source = download()
        if sha256(source) != SOURCE_SHA256:
            raise ValueError("source SHA256 mismatch")
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            with tarfile.open(fileobj=io.BytesIO(source), mode="r:*") as tf:
                safe_extract(tf, root)
            pdf_bytes = (root / ASSET).read_bytes()
            if sha256(pdf_bytes) != ASSET_SHA256:
                raise ValueError("asset SHA256 mismatch")
            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            if doc.page_count != 1:
                raise ValueError(f"unexpected page count {doc.page_count}")
            page = doc[0]

            # Stage A: no drawings/colors accessed before this block has passed.
            ticks = numeric_tick_words(page)
            xpts, ypts = identify_axes(page, ticks)
            xcoords = [p["xc"] for p in xpts]
            ycoords = [p["yc"] for p in ypts]
            ax, bx, xres, xloo = fit_affine(xcoords, X_EXPS)
            ay, by, yres, yloo = fit_affine(ycoords, Y_EXPS)
            stage_a = {
                "tick_candidate_count": len(ticks),
                "x_ticks": xpts,
                "y_ticks": ypts,
                "x_fit": {"a": ax, "b": bx, "residuals_decade": xres, "loo_residuals_decade": xloo,
                          "max_abs_residual_decade": max(map(abs, xres)), "max_abs_loo_decade": max(map(abs, xloo))},
                "y_fit": {"a": ay, "b": by, "residuals_decade": yres, "loo_residuals_decade": yloo,
                          "max_abs_residual_decade": max(map(abs, yres)), "max_abs_loo_decade": max(map(abs, yloo))},
            }
            stage_a_pass = (max(map(abs, xres)) <= MAX_FIT_RESID and max(map(abs, yres)) <= MAX_FIT_RESID
                            and max(map(abs, xloo)) <= MAX_LOO_RESID and max(map(abs, yloo)) <= MAX_LOO_RESID)
            stage_a["pass"] = stage_a_pass
            if not stage_a_pass:
                result = {"iteration": "0078b", "status": "SCIENTIFIC_FAIL_B_L_VECTOR_CALIBRATION",
                          "source_url": used_url, "stage_a": stage_a, "reason": "axis calibration residual gate failed"}
            else:
                # Stage B/C begin only after Stage A PASS.
                drawings = page.get_drawings()
                candidates = []
                W, H = page.rect.width, page.rect.height
                roundtrip_max = 0.0
                for idx, d in enumerate(drawings):
                    colors = [d.get("color"), d.get("fill")]
                    if not any(color_is_magenta(c) for c in colors):
                        continue
                    points = []
                    for item in d.get("items", ()): points.extend(item_points(item))
                    physical = []
                    inside = []
                    for x, y in points:
                        lx, ly = ax * x + bx, ay * y + by
                        physical.append((lx, ly))
                        if X_EXPS[0] - MARGIN_DECADE <= lx <= X_EXPS[-1] + MARGIN_DECADE and Y_EXPS[0] - MARGIN_DECADE <= ly <= Y_EXPS[-1] + MARGIN_DECADE:
                            inside.append((lx, ly, x, y))
                    if len(inside) < 2:
                        continue
                    lxs = [p[0] for p in inside]; lys = [p[1] for p in inside]
                    span_x, span_y = max(lxs) - min(lxs), max(lys) - min(lys)
                    scientific_span = span_x >= 2.0 or span_y >= 1.0
                    for lx, ly, x, y in inside:
                        xr = (lx - bx) / ax; yr = (ly - by) / ay
                        roundtrip_max = max(roundtrip_max, abs(xr-x)/max(W,1.0), abs(yr-y)/max(H,1.0))
                    candidates.append({
                        "drawing_index": idx,
                        "stroke_color": d.get("color"), "fill_color": d.get("fill"),
                        "point_count": len(points), "inside_point_count": len(inside),
                        "span_log10_mGeV": span_x, "span_log10_gBL": span_y,
                        "scientific_span_pass": scientific_span,
                        "physical_bbox": [min(lxs), min(lys), max(lxs), max(lys)],
                        "points_log10": [[p[0], p[1]] for p in inside],
                    })
                scientific = [c for c in candidates if c["scientific_span_pass"]]
                transform_ok = roundtrip_max <= 1e-10
                if scientific and transform_ok:
                    status = "PASS_COMBINED_SOLAR_CEVNS_B_L_VECTOR_CALIBRATION"
                elif candidates and transform_ok:
                    status = "PARTIAL_B_L_VECTOR_CALIBRATION"
                else:
                    status = "SCIENTIFIC_FAIL_B_L_VECTOR_CALIBRATION"
                result = {
                    "iteration": "0078b", "status": status, "source_url": used_url,
                    "source_sha256": SOURCE_SHA256, "asset": ASSET, "asset_sha256": ASSET_SHA256,
                    "page_size": [W, H], "stage_a": stage_a,
                    "magenta_candidate_count": len(candidates), "scientific_magenta_path_count": len(scientific),
                    "roundtrip_max_normalized_page": roundtrip_max,
                    "magenta_candidates": candidates,
                    "guard": "Combined solar-CEvNS B-L vector calibration only; no excluded-side inference, external-envelope combination, manual digitization, or BSM response scan."
                }
    except (OSError, urllib.error.URLError, RuntimeError) as exc:
        result = {"iteration": "0078b", "status": "INFRASTRUCTURE_FAIL", "reason": repr(exc)}
    except (ValueError, fitz.FileDataError) as exc:
        result = {"iteration": "0078b", "status": "SCIENTIFIC_FAIL_B_L_VECTOR_CALIBRATION", "reason": repr(exc)}

    Path("deromeri_bl_combined_calibration_0078b.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    compact = dict(result)
    if "magenta_candidates" in compact:
        compact["magenta_candidates"] = [{k:v for k,v in c.items() if k != "points_log10"} for c in compact["magenta_candidates"]]
    print(json.dumps(compact, indent=2, sort_keys=True))
    if result.get("status", "").startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
