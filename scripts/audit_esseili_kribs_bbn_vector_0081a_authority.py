#!/usr/bin/env python3
import hashlib
import io
import json
import math
import re
import tarfile
import urllib.request

import pymupdf

SOURCE_URL = "https://export.arxiv.org/e-print/2308.07955v2"
SOURCE_SHA256 = "484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c"
ASSETS = {
    "majorana": (
        "Presentation/CnstrntPlotMajoranaYp.pdf",
        "4326f3ac9ba29e515aa22afafef27d08c05d0e6be04db605c4706418c6cd8926",
    ),
    "dirac": (
        "Presentation/CnstrntPlotDiracYp.pdf",
        "14d9afe16f4c38f1d3c08f97ccf086a570739b18731b0b6ffee97fe4b9e63b15",
    ),
}
FIT_TOL = 0.015
CROSS_TOL = 0.015
COLOR_TOL = 1.0 / 255.0 + 1e-6
ADJACENCY_TOL_PT = 2.5
BBN_LEVELS = {"0.002", "0.003", "0.004", "0.006", "0.008"}
TARGET_LEVEL = "0.008"
X_TEXT_TO_EXP = {
    "10-6": -6,
    "10-5": -5,
    "10-4": -4,
    "10-3": -3,
    "10-2": -2,
    "0.1": -1,
    "1": 0,
    "10": 1,
    "102": 2,
    "103": 3,
}
Y_TEXT_TO_EXP = {f"10-{i}": -i for i in range(17, 2, -1)}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_source() -> bytes:
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "NMIR-BBN-vector-authority/0081a"})
    with urllib.request.urlopen(req, timeout=90) as response:
        return response.read()


def rgb_from_int(value):
    if value is None:
        return None
    value = int(value)
    return (
        ((value >> 16) & 255) / 255.0,
        ((value >> 8) & 255) / 255.0,
        (value & 255) / 255.0,
    )


def rgb_tuple(value):
    if value is None:
        return None
    return tuple(float(x) for x in value[:3])


def color_close(a, b, tol=COLOR_TOL):
    return a is not None and b is not None and all(abs(x - y) <= tol for x, y in zip(a, b))


def color_json(c):
    return None if c is None else [round(float(x), 8) for x in c]


def dash_is_non_solid(dashes):
    if dashes is None:
        return False
    clean = re.sub(r"\s+", "", str(dashes)).lower()
    return clean not in {"", "[]0", "none"}


def is_dashed_red_overlay(style):
    c = style["stroke_rgb"]
    return bool(
        c is not None
        and c[0] >= 0.7
        and c[1] <= 0.45
        and c[2] <= 0.45
        and dash_is_non_solid(style["dashes"])
    )


def style_key(drawing):
    stroke = rgb_tuple(drawing.get("color"))
    fill = rgb_tuple(drawing.get("fill"))
    return {
        "stroke_rgb": None if stroke is None else tuple(round(x, 6) for x in stroke),
        "fill_rgb": None if fill is None else tuple(round(x, 6) for x in fill),
        "dashes": str(drawing.get("dashes", "")),
        "width": round(float(drawing.get("width", 0.0) or 0.0), 4),
    }


def style_id(style):
    return json.dumps(
        {
            "stroke_rgb": color_json(style["stroke_rgb"]),
            "fill_rgb": color_json(style["fill_rgb"]),
            "dashes": style["dashes"],
            "width": style["width"],
        },
        sort_keys=True,
    )


def ols(xs, ys):
    n = len(xs)
    if n < 2 or n != len(ys):
        raise ValueError("invalid OLS inputs")
    xm = sum(xs) / n
    ym = sum(ys) / n
    sxx = sum((x - xm) ** 2 for x in xs)
    if sxx == 0:
        raise ValueError("zero x variance")
    a = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sxx
    b = ym - a * xm
    residuals = [a * x + b - y for x, y in zip(xs, ys)]
    return a, b, residuals


def fit_axis(ticks, coord_key):
    coords = [t[coord_key] for t in ticks]
    exps = [t["exponent"] for t in ticks]
    a, b, residuals = ols(coords, exps)
    loo = []
    for i in range(len(ticks)):
        xx = coords[:i] + coords[i + 1 :]
        yy = exps[:i] + exps[i + 1 :]
        aa, bb, _ = ols(xx, yy)
        loo.append(aa * coords[i] + bb - exps[i])
    return {
        "a": a,
        "b": b,
        "anchor_count": len(ticks),
        "max_abs_residual_decade": max(map(abs, residuals)),
        "max_abs_loo_decade": max(map(abs, loo)),
        "residuals_decade": residuals,
        "loo_residuals_decade": loo,
    }


def point_xy(p):
    return float(p.x), float(p.y)


def cubic_point(p0, p1, p2, p3, t):
    x0, y0 = point_xy(p0)
    x1, y1 = point_xy(p1)
    x2, y2 = point_xy(p2)
    x3, y3 = point_xy(p3)
    u = 1.0 - t
    return (
        u**3 * x0 + 3 * u * u * t * x1 + 3 * u * t * t * x2 + t**3 * x3,
        u**3 * y0 + 3 * u * u * t * y1 + 3 * u * t * t * y2 + t**3 * y3,
    )


def drawing_sample_points(drawing):
    pts = []
    for item in drawing.get("items", []):
        kind = item[0]
        try:
            if kind == "l":
                pts.extend([point_xy(item[1]), point_xy(item[2])])
            elif kind == "c":
                for i in range(33):
                    pts.append(cubic_point(item[1], item[2], item[3], item[4], i / 32.0))
            elif kind == "re":
                r = item[1]
                pts.extend([(float(r.x0), float(r.y0)), (float(r.x1), float(r.y0)), (float(r.x1), float(r.y1)), (float(r.x0), float(r.y1))])
            elif kind == "qu":
                q = item[1]
                for attr in ("ul", "ur", "lr", "ll"):
                    if hasattr(q, attr):
                        pts.append(point_xy(getattr(q, attr)))
        except Exception:
            continue
    return pts


def point_to_bbox_distance(point, bbox):
    x, y = point
    x0, y0, x1, y1 = bbox
    dx = 0.0 if x0 <= x <= x1 else min(abs(x - x0), abs(x - x1))
    dy = 0.0 if y0 <= y <= y1 else min(abs(y - y0), abs(y - y1))
    return math.hypot(dx, dy)


def drawing_bbox_distance(drawing, bbox):
    pts = drawing_sample_points(drawing)
    if not pts:
        return math.inf
    return min(point_to_bbox_distance(p, bbox) for p in pts)


def span_records(page):
    spans = []
    data = page.get_text("dict")
    for block in data.get("blocks", []):
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = str(span.get("text", "")).strip()
                bbox = tuple(float(x) for x in span.get("bbox", (0, 0, 0, 0)))
                spans.append(
                    {
                        "text": text,
                        "bbox": bbox,
                        "rgb": rgb_from_int(span.get("color")),
                        "size": float(span.get("size", 0.0)),
                    }
                )
    return spans


def word_records(page):
    out = []
    for w in page.get_text("words"):
        out.append(
            {
                "text": str(w[4]).strip(),
                "x0": float(w[0]),
                "y0": float(w[1]),
                "x1": float(w[2]),
                "y1": float(w[3]),
                "xc": (float(w[0]) + float(w[2])) / 2.0,
                "yc": (float(w[1]) + float(w[3])) / 2.0,
            }
        )
    return out


def unique_axis_ticks(candidates):
    by_exp = {}
    for c in candidates:
        by_exp.setdefault(c["exponent"], []).append(c)
    ticks = []
    ambiguous = {}
    for exp in sorted(by_exp):
        if len(by_exp[exp]) == 1:
            ticks.append(by_exp[exp][0])
        else:
            ambiguous[str(exp)] = len(by_exp[exp])
    return ticks, ambiguous


def axis_calibration(page):
    width = float(page.rect.width)
    height = float(page.rect.height)
    words = word_records(page)
    full_text = " ".join(w["text"] for w in words)
    normalized_title = re.sub(r"[^A-Za-z0-9\[\]]+", "", full_text)
    unit_evidence = "MeV" in full_text and ("mX" in normalized_title or "m_X" in full_text) and ("gX" in normalized_title or "g_X" in full_text)

    x_candidates = [
        {**w, "exponent": X_TEXT_TO_EXP[w["text"]]}
        for w in words
        if w["text"] in X_TEXT_TO_EXP and w["yc"] >= 0.82 * height
    ]
    y_candidates = [
        {**w, "exponent": Y_TEXT_TO_EXP[w["text"]]}
        for w in words
        if w["text"] in Y_TEXT_TO_EXP and w["xc"] <= 0.12 * width and w["yc"] < 0.90 * height
    ]
    x_ticks, x_ambiguous = unique_axis_ticks(x_candidates)
    y_ticks, y_ambiguous = unique_axis_ticks(y_candidates)
    x_fit = fit_axis(x_ticks, "xc") if len(x_ticks) >= 4 else None
    y_fit = fit_axis(y_ticks, "yc") if len(y_ticks) >= 4 else None
    missing = len(x_ticks) < 4 or len(y_ticks) < 4 or not unit_evidence
    residual_failure = bool(
        not missing
        and (
            x_fit["max_abs_residual_decade"] > FIT_TOL
            or x_fit["max_abs_loo_decade"] > FIT_TOL
            or y_fit["max_abs_residual_decade"] > FIT_TOL
            or y_fit["max_abs_loo_decade"] > FIT_TOL
        )
    )
    passed = bool(not missing and not residual_failure)
    return {
        "page_size": [width, height],
        "axis_title_text": full_text,
        "unit_log_semantics_recovered": unit_evidence,
        "x_ticks": x_ticks,
        "y_ticks": y_ticks,
        "x_ambiguous_multiplicity": x_ambiguous,
        "y_ambiguous_multiplicity": y_ambiguous,
        "x_fit": x_fit,
        "y_fit": y_fit,
        "missing_authority": missing,
        "residual_failure": residual_failure,
        "passed": passed,
    }


def style_inventory(drawings):
    styles = {}
    for idx, drawing in enumerate(drawings):
        style = style_key(drawing)
        sid = style_id(style)
        if sid not in styles:
            styles[sid] = {
                "style": {
                    "stroke_rgb": color_json(style["stroke_rgb"]),
                    "fill_rgb": color_json(style["fill_rgb"]),
                    "dashes": style["dashes"],
                    "width": style["width"],
                    "dashed_red_overlay": is_dashed_red_overlay(style),
                },
                "drawing_indices": [],
            }
        styles[sid]["drawing_indices"].append(idx)
    return styles


def semantic_identity(page):
    spans = span_records(page)
    drawings = page.get_drawings()
    styles = style_inventory(drawings)
    level_spans = [s for s in spans if s["text"] in BBN_LEVELS]
    target_spans = [s for s in level_spans if s["text"] == TARGET_LEVEL]

    style_objs = {}
    for idx, d in enumerate(drawings):
        sk = style_key(d)
        sid = style_id(sk)
        style_objs.setdefault(sid, {"style": sk, "drawing_indices": []})["drawing_indices"].append(idx)

    non_overlay = {sid for sid, rec in style_objs.items() if not is_dashed_red_overlay(rec["style"])}

    color_sets = []
    for s in target_spans:
        matches = set()
        for sid, rec in style_objs.items():
            if sid not in non_overlay:
                continue
            if color_close(s["rgb"], rec["style"]["stroke_rgb"]):
                matches.add(sid)
        color_sets.append(matches)
    color_intersection = set.intersection(*color_sets) if color_sets else set()

    route = None
    selected_sid = None
    adjacency_details = []
    if len(color_intersection) == 1:
        route = "text_color"
        selected_sid = next(iter(color_intersection))
    else:
        adjacency_sets = []
        for span in target_spans:
            qualifying = set()
            per_style = {}
            for sid, rec in style_objs.items():
                if sid not in non_overlay:
                    continue
                mind = math.inf
                for idx in rec["drawing_indices"]:
                    mind = min(mind, drawing_bbox_distance(drawings[idx], span["bbox"]))
                per_style[sid] = mind
                if mind <= ADJACENCY_TOL_PT:
                    qualifying.add(sid)
            adjacency_sets.append(qualifying)
            adjacency_details.append({"label_bbox": list(span["bbox"]), "style_min_distances_pt": per_style})
        adjacency_intersection = set.intersection(*adjacency_sets) if adjacency_sets else set()
        if len(adjacency_intersection) == 1:
            route = "label_adjacency"
            selected_sid = next(iter(adjacency_intersection))

    selected_drawing_indices = []
    seed_indices_by_label = []
    other_level_conflicts = []
    if selected_sid is not None:
        selected_drawing_indices = style_objs[selected_sid]["drawing_indices"]
        # Freeze local source-path seeds adjacent to threshold labels. These are not polygon construction.
        for span in target_spans:
            ranked = sorted(
                ((drawing_bbox_distance(drawings[idx], span["bbox"]), idx) for idx in selected_drawing_indices),
                key=lambda z: (z[0], z[1]),
            )
            seeds = [idx for dist, idx in ranked if dist <= ADJACENCY_TOL_PT]
            seed_indices_by_label.append({"label_bbox": list(span["bbox"]), "drawing_indices_within_2p5pt": seeds, "nearest": ranked[:3]})
        for span in [s for s in level_spans if s["text"] != TARGET_LEVEL]:
            near = [
                idx
                for idx in selected_drawing_indices
                if drawing_bbox_distance(drawings[idx], span["bbox"]) <= ADJACENCY_TOL_PT
            ]
            if near:
                other_level_conflicts.append({"level": span["text"], "bbox": list(span["bbox"]), "selected_style_near_indices": near})

    # A style can be shared across levels; then unique local path seeds may still provide path identity.
    path_seed_unique = bool(
        selected_sid is not None
        and target_spans
        and all(len(rec["drawing_indices_within_2p5pt"]) >= 1 for rec in seed_indices_by_label)
        and not other_level_conflicts
    )
    semantic_pass = bool(selected_sid is not None and (not other_level_conflicts or path_seed_unique))

    target_style_export = None
    if selected_sid is not None:
        st = style_objs[selected_sid]["style"]
        target_style_export = {
            "style_id": selected_sid,
            "stroke_rgb": color_json(st["stroke_rgb"]),
            "fill_rgb": color_json(st["fill_rgb"]),
            "dashes": st["dashes"],
            "width": st["width"],
            "dashed_red_overlay": is_dashed_red_overlay(st),
        }

    return {
        "level_text_spans": [
            {"text": s["text"], "bbox": list(s["bbox"]), "rgb": color_json(s["rgb"]), "size": s["size"]}
            for s in level_spans
        ],
        "target_label_count": len(target_spans),
        "style_inventory": styles,
        "color_candidate_style_ids": sorted(color_intersection),
        "identity_route": route,
        "selected_style": target_style_export,
        "selected_style_drawing_indices": selected_drawing_indices,
        "threshold_seed_paths": seed_indices_by_label,
        "other_level_conflicts": other_level_conflicts,
        "adjacency_diagnostics": adjacency_details,
        "semantic_identity_pass": semantic_pass,
    }


def inspect_panel(data: bytes, asset: str):
    doc = pymupdf.open(stream=data, filetype="pdf")
    if len(doc) != 1:
        raise RuntimeError(f"expected one page in {asset}")
    page = doc[0]
    return {
        "asset": asset,
        "asset_sha256": sha256(data),
        "axis": axis_calibration(page),
        "semantic_identity": semantic_identity(page),
    }


def eval_transform(fit, coord):
    return fit["a"] * coord + fit["b"]


def cross_panel_check(maj, drc):
    if not maj["axis"]["passed"] or not drc["axis"]["passed"]:
        return {"evaluated": False, "passed": False, "max_difference_decade": math.inf, "comparisons": []}
    comparisons = []
    # Compare transforms at every common exponent using the Majorana source-native tick coordinate.
    for axis_name, coord_key in (("x", "xc"), ("y", "yc")):
        maj_ticks = {t["exponent"]: t for t in maj["axis"][f"{axis_name}_ticks"]}
        drc_ticks = {t["exponent"]: t for t in drc["axis"][f"{axis_name}_ticks"]}
        for exp in sorted(set(maj_ticks) & set(drc_ticks)):
            coord = maj_ticks[exp][coord_key]
            a = eval_transform(maj["axis"][f"{axis_name}_fit"], coord)
            b = eval_transform(drc["axis"][f"{axis_name}_fit"], coord)
            comparisons.append({"axis": axis_name, "exponent": exp, "majorana_pdf_coordinate": coord, "difference_decade": a - b})
    maxdiff = max((abs(c["difference_decade"]) for c in comparisons), default=math.inf)
    return {"evaluated": True, "passed": maxdiff <= CROSS_TOL, "max_difference_decade": maxdiff, "comparisons": comparisons}


def classify(panels, cross):
    missing = any(p["axis"]["missing_authority"] for p in panels.values())
    residual_fail = any(p["axis"]["residual_failure"] for p in panels.values())
    semantic_missing = any(not p["semantic_identity"]["semantic_identity_pass"] for p in panels.values())
    if residual_fail or (cross["evaluated"] and not cross["passed"]):
        return "SCIENTIFIC_FAIL_COSMOLOGY_B_L_BBN_VECTOR_CALIBRATION_SEMANTIC_IDENTITY"
    if missing or semantic_missing or not cross["evaluated"]:
        return "BLOCKED_COSMOLOGY_B_L_BBN_VECTOR_CALIBRATION_SEMANTIC_IDENTITY"
    return "PASS_COSMOLOGY_B_L_BBN_VECTOR_CALIBRATION_SEMANTIC_IDENTITY"


def audit():
    raw = fetch_source()
    if sha256(raw) != SOURCE_SHA256:
        raise RuntimeError("source SHA mismatch")
    panels = {}
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tf:
        members = {m.name.lstrip("./"): m for m in tf.getmembers() if m.isfile()}
        for scenario, (asset, expected_sha) in ASSETS.items():
            if asset not in members:
                raise RuntimeError(f"missing asset {asset}")
            fh = tf.extractfile(members[asset])
            if fh is None:
                raise RuntimeError(f"cannot extract {asset}")
            data = fh.read()
            if sha256(data) != expected_sha:
                raise RuntimeError(f"asset SHA mismatch {asset}")
            panels[scenario] = inspect_panel(data, asset)
    cross = cross_panel_check(panels["majorana"], panels["dirac"])
    return {
        "iteration": "0081a",
        "authoritative_prereg_commit": "ad37205e6a30188f4129fdca8e0d49a156ab6e36",
        "implementation_freeze_commit": "27ac3703547c67f5e130baba9b884688ef176a13",
        "classification": classify(panels, cross),
        "source_sha256": SOURCE_SHA256,
        "fit_tolerance_decade": FIT_TOL,
        "cross_panel_tolerance_decade": CROSS_TOL,
        "color_tolerance": COLOR_TOL,
        "adjacency_tolerance_pdf_points": ADJACENCY_TOL_PT,
        "panels": panels,
        "cross_panel": cross,
        "guard": "No excluded polygon or excluded-side assignment; no CMB+BBN or Majorana/Dirac union; no response scan. Later competing 0081a prereg/workflow is non-authoritative and not consulted."
    }


def main():
    result = audit()
    with open("esseili_kribs_bbn_vector_0081a_authority.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["classification"].startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(3)
    if result["classification"].startswith("BLOCKED"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
