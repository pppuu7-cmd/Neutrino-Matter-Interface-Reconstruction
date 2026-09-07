#!/usr/bin/env python3
import hashlib
import io
import json
import math
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
BBN_LEVEL_TEXTS = {"0.002", "0.003", "0.004", "0.006", "0.008"}
FIT_TOL_DECADE = 0.015
CROSS_TOL_DECADE = 1e-5


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_source() -> bytes:
    req = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "NMIR-BBN-axis-calibration/0081a"})
    with urllib.request.urlopen(req, timeout=90) as response:
        return response.read()


def ols(xs, ys):
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("OLS requires equal lists with >=2 points")
    n = len(xs)
    xm = sum(xs) / n
    ym = sum(ys) / n
    sxx = sum((x - xm) ** 2 for x in xs)
    if sxx == 0:
        raise ValueError("zero coordinate variance")
    a = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sxx
    b = ym - a * xm
    residuals = [a * x + b - y for x, y in zip(xs, ys)]
    return a, b, residuals


def loo_residuals(xs, ys):
    out = []
    for i in range(len(xs)):
        xx = xs[:i] + xs[i + 1 :]
        yy = ys[:i] + ys[i + 1 :]
        a, b, _ = ols(xx, yy)
        out.append(a * xs[i] + b - ys[i])
    return out


def word_records(page):
    out = []
    for w in page.get_text("words"):
        out.append(
            {
                "text": w[4],
                "x0": w[0],
                "y0": w[1],
                "x1": w[2],
                "y1": w[3],
                "xc": (w[0] + w[2]) / 2,
                "yc": (w[1] + w[3]) / 2,
            }
        )
    return out


def unique_by_exponent(candidates, expected_exponents):
    buckets = {e: [] for e in expected_exponents}
    for c in candidates:
        if c["exponent"] in buckets:
            buckets[c["exponent"]].append(c)
    unique = all(len(buckets[e]) == 1 for e in expected_exponents)
    ordered = [buckets[e][0] for e in expected_exponents if len(buckets[e]) == 1]
    return unique, ordered, {str(e): len(buckets[e]) for e in expected_exponents}


def fit_axis(ticks, coord_key):
    coords = [t[coord_key] for t in ticks]
    exps = [t["exponent"] for t in ticks]
    a, b, residuals = ols(coords, exps)
    loo = loo_residuals(coords, exps)
    return {
        "a": a,
        "b": b,
        "residuals_decade": residuals,
        "loo_residuals_decade": loo,
        "max_abs_residual_decade": max(map(abs, residuals)),
        "max_abs_loo_decade": max(map(abs, loo)),
    }


def inspect_panel(data: bytes, asset: str):
    doc = pymupdf.open(stream=data, filetype="pdf")
    if len(doc) != 1:
        raise RuntimeError(f"expected one page in {asset}")
    page = doc[0]
    width = float(page.rect.width)
    height = float(page.rect.height)
    words = word_records(page)

    # Relative-position guards only; no coordinates or affine coefficients are borrowed
    # from the CMB panels. Axis labels live along the bottom and left page margins.
    x_raw = [
        {**w, "exponent": X_TEXT_TO_EXP[w["text"]]}
        for w in words
        if w["text"] in X_TEXT_TO_EXP and w["yc"] >= 0.84 * height
    ]
    y_raw = [
        {**w, "exponent": Y_TEXT_TO_EXP[w["text"]]}
        for w in words
        if w["text"] in Y_TEXT_TO_EXP and w["xc"] <= 0.105 * width and w["yc"] < 0.90 * height
    ]

    x_expected = list(range(-6, 4))
    y_expected = list(range(-17, -2))
    x_unique, x_ticks, x_multiplicity = unique_by_exponent(x_raw, x_expected)
    y_unique, y_ticks, y_multiplicity = unique_by_exponent(y_raw, y_expected)

    x_fit = fit_axis(x_ticks, "xc") if x_unique else None
    y_fit = fit_axis(y_ticks, "yc") if y_unique else None

    inventory = [w for w in words if w["text"] in BBN_LEVEL_TEXTS]
    inventory = sorted(inventory, key=lambda z: (float(z["text"]), z["yc"], z["xc"]))

    checks = {
        "x_complete_unique_exponents": x_unique and [t["exponent"] for t in x_ticks] == x_expected,
        "y_complete_unique_exponents": y_unique and [t["exponent"] for t in y_ticks] == y_expected,
        "x_fit_residual_le_0p015": bool(x_fit and x_fit["max_abs_residual_decade"] <= FIT_TOL_DECADE),
        "x_loo_residual_le_0p015": bool(x_fit and x_fit["max_abs_loo_decade"] <= FIT_TOL_DECADE),
        "y_fit_residual_le_0p015": bool(y_fit and y_fit["max_abs_residual_decade"] <= FIT_TOL_DECADE),
        "y_loo_residual_le_0p015": bool(y_fit and y_fit["max_abs_loo_decade"] <= FIT_TOL_DECADE),
    }
    return {
        "asset": asset,
        "asset_sha256": sha256(data),
        "page_size": [width, height],
        "word_count": len(words),
        "x_candidate_multiplicity": x_multiplicity,
        "y_candidate_multiplicity": y_multiplicity,
        "x_ticks": x_ticks,
        "y_ticks": y_ticks,
        "x_fit": x_fit,
        "y_fit": y_fit,
        "bbn_contour_text_inventory": inventory,
        "checks": checks,
        "independent_panel_pass": all(checks.values()),
    }


def transform_difference(fit_a, fit_b, coords):
    return [(fit_a["a"] * x + fit_a["b"]) - (fit_b["a"] * x + fit_b["b"]) for x in coords]


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
            actual_sha = sha256(data)
            if actual_sha != expected_sha:
                raise RuntimeError(f"asset SHA mismatch {asset}: {actual_sha}")
            panels[scenario] = inspect_panel(data, asset)

    maj = panels["majorana"]
    drc = panels["dirac"]
    cross = {
        "evaluated": False,
        "x_differences_decade": [],
        "y_differences_decade": [],
        "max_abs_x_difference_decade": math.inf,
        "max_abs_y_difference_decade": math.inf,
        "x_pass_le_1e-5": False,
        "y_pass_le_1e-5": False,
    }
    if maj["independent_panel_pass"] and drc["independent_panel_pass"]:
        xcoords = [t["xc"] for t in maj["x_ticks"]]
        ycoords = [t["yc"] for t in maj["y_ticks"]]
        dx = transform_difference(maj["x_fit"], drc["x_fit"], xcoords)
        dy = transform_difference(maj["y_fit"], drc["y_fit"], ycoords)
        cross = {
            "evaluated": True,
            "x_differences_decade": dx,
            "y_differences_decade": dy,
            "max_abs_x_difference_decade": max(map(abs, dx)),
            "max_abs_y_difference_decade": max(map(abs, dy)),
            "x_pass_le_1e-5": max(map(abs, dx)) <= CROSS_TOL_DECADE,
            "y_pass_le_1e-5": max(map(abs, dy)) <= CROSS_TOL_DECADE,
        }

    passes = [p["independent_panel_pass"] for p in panels.values()]
    if all(passes) and cross["x_pass_le_1e-5"] and cross["y_pass_le_1e-5"]:
        classification = "PASS_COSMOLOGY_B_L_BBN_AXIS_CALIBRATION"
    elif any(passes):
        classification = "PARTIAL_PASS_BBN_SINGLE_PANEL_CALIBRATION"
    else:
        classification = "SCIENTIFIC_FAIL_COSMOLOGY_B_L_BBN_AXIS_CALIBRATION"

    return {
        "iteration": "0081a",
        "classification": classification,
        "source_sha256": SOURCE_SHA256,
        "fit_tolerance_decade": FIT_TOL_DECADE,
        "cross_panel_tolerance_decade": CROSS_TOL_DECADE,
        "panels": panels,
        "cross_panel_replication": cross,
        "guard": "Independent BBN axis calibration and text-level contour inventory only; no CMB affine input, no path/color identity, no DeltaYp=0.008 vector selection, no excluded polygon, no scenario union, no CMB/BBN or global-envelope union, no response scan.",
    }


def main():
    result = audit()
    with open("esseili_kribs_bbn_axis_calibration_0081a.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["classification"].startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
