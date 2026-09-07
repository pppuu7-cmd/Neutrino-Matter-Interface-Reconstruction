#!/usr/bin/env python3
from pathlib import Path
import argparse, json, hashlib, math
import fitz
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fit_line(coords, vals):
    a, b = np.polyfit(np.array(coords, float), np.array(vals, float), 1)
    pred = a * np.array(coords) + b
    return float(a), float(b), float(np.max(np.abs(pred - np.array(vals))))


def dedup(points, tol=1e-4):
    out = []
    for point in points:
        if not any(abs(point[0] - old[0]) < tol and abs(point[1] - old[1]) < tol for old in out):
            out.append(point)
    return out


def extract_fig3(path):
    doc = fitz.open(path)
    page = doc[0]
    drawings = page.get_drawings()
    rects = [
        d["rect"] for d in drawings
        if d["color"] == (0.0, 0.0, 0.0)
        and d["fill"] is None
        and len(d["items"]) == 4
        and d["rect"].width > 250
        and d["rect"].height > 400
        and d["rect"].x1 < 400
    ]
    if not rects:
        raise RuntimeError("Fig3 top-panel frame not found")
    frame = rects[0]

    energy_ticks = [frame.y1]
    for d in drawings:
        r = d["rect"]
        if (
            len(d["items"]) == 1
            and d["items"][0][0] == "l"
            and r.height < 1e-3
            and abs(r.x1 - frame.x1) < 0.05
            and 8 < r.width < 12
        ):
            energy_ticks.append(r.y0)
    energy_ticks = sorted(set(round(x, 6) for x in energy_ticks), reverse=True)
    majors = []
    for y in energy_ticks:
        if not majors or abs(y - majors[-1]) > 100:
            majors.append(y)
    majors = majors[:4]
    e_slope, e_intercept, e_residual = fit_line(majors, [0, 10, 20, 30])

    rate_coords = []
    for d in drawings:
        r = d["rect"]
        if (
            len(d["items"]) == 1
            and d["items"][0][0] == "l"
            and r.width < 1e-3
            and abs(r.y1 - frame.y1) < 0.05
            and 17 < r.height < 19
            and frame.x0 < r.x0 < frame.x1
        ):
            rate_coords.append(round(r.x0, 6))
    rate_coords = sorted(set(rate_coords), reverse=True)
    r_slope, r_intercept, r_residual = fit_line(rate_coords, [20, 40, 60, 80, 100, 120])

    points = []
    for d in drawings:
        r = d["rect"]
        if (
            d["fill"] == (0.0, 0.0, 0.0)
            and 7 < r.width < 8
            and 5 < r.height < 6
            and frame.x0 <= r.x0
            and r.x1 <= frame.x1
            and frame.y0 <= r.y0
            and r.y1 <= frame.y1
        ):
            points.append(((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))
    points = dedup(points)
    candidates = []
    for x, y in points:
        energy = e_slope * y + e_intercept
        rate = r_slope * x + r_intercept
        if 0 <= energy <= 30 and abs((energy - 0.5) - round(energy - 0.5)) < 0.01:
            candidates.append((energy, rate, x, y))
    candidates.sort()
    counts = [int(round(row[1])) for row in candidates]
    integer_max = max(abs(row[1] - round(row[1])) for row in candidates)
    centers = [row[0] for row in candidates]
    center_max = max(abs(value - (i + 0.5)) for i, value in enumerate(centers))

    histograms = []
    for i, d in enumerate(drawings):
        if (
            len(d["items"]) in (58, 60)
            and d["color"] is not None
            and d["fill"] is None
            and d["rect"].x1 <= frame.x1 + 0.1
            and d["rect"].y0 >= frame.y0 - 0.1
            and d["rect"].y1 <= frame.y1 + 0.1
        ):
            histograms.append(
                {
                    "drawing_index": i,
                    "color": [round(float(c), 6) for c in d["color"]],
                    "items": len(d["items"]),
                    "rect": [
                        float(d["rect"].x0),
                        float(d["rect"].y0),
                        float(d["rect"].x1),
                        float(d["rect"].y1),
                    ],
                }
            )
    words = [word[4] for word in page.get_text("words")]
    grouped_minor = "Neutron" in words and "accidental" in words and "wall" in words

    return {
        "frame": [float(frame.x0), float(frame.y0), float(frame.x1), float(frame.y1)],
        "energy_calibration": {
            "tick_coords_page_y": majors,
            "tick_values_keV": [0, 10, 20, 30],
            "slope": e_slope,
            "intercept": e_intercept,
            "max_residual_keV": e_residual,
        },
        "rate_calibration": {
            "tick_coords_page_x": rate_coords,
            "tick_values_events_per_keV": [20, 40, 60, 80, 100, 120],
            "slope": r_slope,
            "intercept": r_intercept,
            "max_residual_events_per_keV": r_residual,
        },
        "observed": {
            "bin_centers_keV": [round(value, 9) for value in centers],
            "counts": counts,
            "sum": sum(counts),
            "integer_max_residual": integer_max,
            "center_max_residual_keV": center_max,
            "n_bins": len(counts),
        },
        "histogram_families": histograms,
        "published_grouped_minor_background_label_present": grouped_minor,
        "raster_images": len(page.get_images(full=True)),
    }


def extract_fig1(path):
    doc = fitz.open(path)
    page = doc[0]
    drawings = page.get_drawings()
    rects = [
        d["rect"] for d in drawings
        if d["color"] == (0.0, 0.0, 0.0)
        and d["fill"] is None
        and len(d["items"]) == 4
        and d["rect"].width > 300
        and d["rect"].height > 400
    ]
    if not rects:
        raise RuntimeError("Fig1 frame not found")
    frame = rects[0]

    energy_coords = [frame.y1]
    for d in drawings:
        r = d["rect"]
        if (
            len(d["items"]) == 1
            and d["items"][0][0] == "l"
            and r.height < 1e-3
            and abs(r.x1 - frame.x1) < 0.05
            and 8 < r.width < 10
            and frame.y0 <= r.y0 <= frame.y1
        ):
            energy_coords.append(r.y0)
    energy_coords = sorted(set(round(x, 6) for x in energy_coords), reverse=True)
    majors = []
    for y in energy_coords:
        if not majors or abs(y - majors[-1]) > 100:
            majors.append(y)
    majors = majors[:4]
    e_slope, e_intercept, e_residual = fit_line(majors, [0, 10, 20, 30])

    eff_coords = []
    for d in drawings:
        r = d["rect"]
        if (
            len(d["items"]) == 1
            and d["items"][0][0] == "l"
            and r.width < 1e-3
            and abs(r.y0 - frame.y0) < 0.05
            and 9 < r.height < 10
            and frame.x0 <= r.x0 <= frame.x1
        ):
            eff_coords.append(round(r.x0, 6))
    eff_coords = sorted(set(eff_coords), reverse=True)[:6]
    f_slope, f_intercept, f_residual = fit_line(eff_coords, [0, 0.2, 0.4, 0.6, 0.8, 1.0])

    curves = []
    for i, d in enumerate(drawings):
        if (
            d["color"] == (0.0, 0.0, 0.0)
            and d["fill"] is None
            and len(d["items"]) == 300
            and d["rect"].x0 > frame.x0
            and d["rect"].x1 <= frame.x1 + 0.1
        ):
            curves.append((i, d))
    if not curves:
        raise RuntimeError("efficiency central curve not found")
    curve = curves[0][1]
    raw = []
    for item in curve["items"]:
        if item[0] == "l":
            for point in item[1:]:
                if hasattr(point, "x"):
                    raw.append((point.x, point.y))
        elif item[0] == "c":
            for point in item[1:]:
                if hasattr(point, "x"):
                    raw.append((point.x, point.y))
    raw = dedup(raw, 1e-5)
    values = sorted(
        [(e_slope * y + e_intercept, f_slope * x + f_intercept, x, y) for x, y in raw],
        key=lambda row: row[0],
    )
    energy_monotone = all(values[i + 1][0] >= values[i][0] - 1e-8 for i in range(len(values) - 1))
    errors = []
    for energy, efficiency, x, y in values:
        x_roundtrip = (efficiency - f_intercept) / f_slope
        y_roundtrip = (energy - e_intercept) / e_slope
        errors.append(math.hypot(x_roundtrip - x, y_roundtrip - y))

    return {
        "frame": [float(frame.x0), float(frame.y0), float(frame.x1), float(frame.y1)],
        "energy_calibration": {
            "tick_coords_page_y": majors,
            "tick_values_keV": [0, 10, 20, 30],
            "slope": e_slope,
            "intercept": e_intercept,
            "max_residual_keV": e_residual,
        },
        "efficiency_calibration": {
            "tick_coords_page_x": eff_coords,
            "tick_values": [0, 0.2, 0.4, 0.6, 0.8, 1.0],
            "slope": f_slope,
            "intercept": f_intercept,
            "max_residual_abs": f_residual,
        },
        "efficiency_curve": {
            "n_points": len(values),
            "energy_monotone_parameterization": energy_monotone,
            "points_EkeV_eff": [[round(row[0], 9), round(row[1], 9)] for row in values],
            "roundtrip_rms_pt": float(math.sqrt(sum(err * err for err in errors) / len(errors))),
            "roundtrip_max_pt": float(max(errors)),
            "min_eff": float(min(row[1] for row in values)),
            "max_eff": float(max(row[1] for row in values)),
        },
        "raster_images": len(page.get_images(full=True)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir")
    parser.add_argument("output")
    args = parser.parse_args()
    source = Path(args.source_dir)
    fig1_path = source / "Fig1EffAndXsec.pdf"
    fig3_path = source / "Fig3_bestFit_gpu.pdf"
    fig1 = extract_fig1(fig1_path)
    fig3 = extract_fig3(fig3_path)

    checks = {
        "zero_rasters": fig1["raster_images"] == 0 and fig3["raster_images"] == 0,
        "fig3_energy_calibration_pass": fig3["energy_calibration"]["max_residual_keV"] <= 0.02,
        "fig3_rate_calibration_pass": fig3["rate_calibration"]["max_residual_events_per_keV"] <= 0.25,
        "fig1_efficiency_calibration_pass": fig1["efficiency_calibration"]["max_residual_abs"] <= 0.002,
        "observed_30_bins": fig3["observed"]["n_bins"] == 30,
        "observed_sum_matches_1058": fig3["observed"]["sum"] == 1058,
        "observed_integer_quantization": fig3["observed"]["integer_max_residual"] <= 0.01,
        "efficiency_energy_parameterization_monotone": fig1["efficiency_curve"]["energy_monotone_parameterization"],
        "roundtrip_pass": fig1["efficiency_curve"]["roundtrip_rms_pt"] <= 0.25 and fig1["efficiency_curve"]["roundtrip_max_pt"] <= 0.75,
        "minor_backgrounds_grouped_in_primary_figure": fig3["published_grouped_minor_background_label_present"],
    }
    core = all(value for key, value in checks.items() if key != "minor_backgrounds_grouped_in_primary_figure")
    if core and checks["minor_backgrounds_grouped_in_primary_figure"]:
        classification = "PARTIAL_PASS_VECTOR_DATA_EFFICIENCY_ONLY"
        blocker = (
            "Fig3 publishes neutron + 8B + accidental + wall/surface as one grouped vector family, "
            "while De-Romeri/PandaX assign distinct nuisance normalizations; individual per-bin arrays "
            "are not recoverable from this primary source package."
        )
    elif not core:
        classification = "SCIENTIFIC_FAIL_VECTOR_CALIBRATION"
        blocker = "One or more frozen vector extraction/calibration criteria failed."
    else:
        classification = "PASS_PANDAX_VECTOR_INPUTS_EXTRACTED"
        blocker = None

    result = {
        "classification": classification,
        "source": {
            "arxiv": "2206.02339v3",
            "fig1_sha256": sha(fig1_path),
            "fig3_sha256": sha(fig3_path),
        },
        "fig1": fig1,
        "fig3": fig3,
        "checks": checks,
        "blocker": blocker,
    }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
