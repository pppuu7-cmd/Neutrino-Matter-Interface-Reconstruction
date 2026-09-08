#!/usr/bin/env python3
"""NMIR 0092: exact Model-S mass/nucleon column for the frozen G9 sentinel ray.

This script intentionally computes the solar-column authority only. Source-regime
cross-section folding is kept separate so the primary Model-S geometric result
cannot be silently changed by later interaction-authority choices.
"""
from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import math
from pathlib import Path

B_OVER_RSUN = 0.024
Z_AU = 24.073780819657056
RSUN_CM = 6.957e10  # IAU 2015 nominal solar radius, exact nominal value.
M_U_G = 1.66053906892e-24
MODEL_S_URL = "https://users-phys.au.dk/jcd/solar_models/cptrho.l5bi.d.15c"


def parse_model_s(path: Path):
    raw = path.read_bytes()
    sha256 = hashlib.sha256(raw).hexdigest()
    rows = []
    for line_no, rawline in enumerate(raw.decode("ascii").splitlines(), 1):
        line = rawline.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 3:
            raise ValueError(f"line {line_no}: expected >=3 columns")
        r = float(parts[0])
        rho = float(parts[2])
        if not (math.isfinite(r) and math.isfinite(rho) and r >= 0 and rho >= 0):
            raise ValueError(f"line {line_no}: invalid r/rho")
        rows.append((r, rho))
    if not rows:
        raise ValueError("no Model-S data rows")

    # The official file is surface-to-centre; canonicalize deterministically.
    rows.sort(key=lambda t: t[0])
    dedup = []
    for r, rho in rows:
        if dedup and r == dedup[-1][0]:
            # Exact duplicate radii are permitted only if densities agree.
            if rho != dedup[-1][1]:
                raise ValueError(f"duplicate radius {r} with inconsistent rho")
            continue
        dedup.append((r, rho))

    rs = [r for r, _ in dedup]
    rhos = [rho for _, rho in dedup]
    if rs[0] > B_OVER_RSUN:
        raise ValueError(f"Model-S minimum radius {rs[0]} exceeds frozen b={B_OVER_RSUN}")
    if rs[-1] < 1.0:
        raise ValueError(f"Model-S maximum radius {rs[-1]} does not reach photosphere")
    return raw, sha256, rs, rhos


def interp_linear(r: float, rs, rhos) -> float:
    if r <= rs[0]:
        return rhos[0]
    if r >= rs[-1]:
        return rhos[-1]
    j = bisect.bisect_right(rs, r)
    r0, r1 = rs[j - 1], rs[j]
    y0, y1 = rhos[j - 1], rhos[j]
    t = (r - r0) / (r1 - r0)
    return y0 + t * (y1 - y0)


def interp_logrho(r: float, rs, rhos) -> float:
    if r <= rs[0]:
        return rhos[0]
    if r >= rs[-1]:
        return rhos[-1]
    j = bisect.bisect_right(rs, r)
    r0, r1 = rs[j - 1], rs[j]
    y0, y1 = rhos[j - 1], rhos[j]
    if y0 <= 0 or y1 <= 0:
        return interp_linear(r, rs, rhos)
    t = (r - r0) / (r1 - r0)
    return math.exp(math.log(y0) + t * (math.log(y1) - math.log(y0)))


def simpson_column(n: int, rs, rhos, *, log_interp: bool = False) -> float:
    if n <= 0 or n % 2:
        raise ValueError("Simpson interval count must be a positive even integer")
    b = B_OVER_RSUN
    xmax = math.sqrt(1.0 - b * b)
    h = xmax / n
    interp = interp_logrho if log_interp else interp_linear

    def f(x: float) -> float:
        r = math.sqrt(b * b + x * x)
        return interp(r, rs, rhos)

    s = f(0.0) + f(xmax)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(i * h)
    half_dimensionless = s * h / 3.0
    return 2.0 * RSUN_CM * half_dimensionless


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model-s", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--n-coarse", type=int, default=131072)
    ap.add_argument("--n-fine", type=int, default=262144)
    args = ap.parse_args()

    raw, sha256, rs, rhos = parse_model_s(args.model_s)
    coarse = simpson_column(args.n_coarse, rs, rhos)
    fine = simpson_column(args.n_fine, rs, rhos)
    rel = abs(fine - coarse) / abs(fine)
    log_sensitivity = simpson_column(args.n_fine, rs, rhos, log_interp=True)
    log_rel = abs(log_sensitivity - fine) / abs(fine)
    n_nucleons = fine / M_U_G

    status = (
        "PASS_G9_0092_MODEL_S_COLUMN_AUTHORITY"
        if rel <= 1e-4
        else "INFRASTRUCTURE_FAIL_G9_0092"
    )
    result = {
        "schema": "nmir.g9.solar_transmission_column.0092.v1",
        "status": status,
        "prereg": "research/prereg/0092_g9_solar_transmission_authority.md",
        "model_s": {
            "authority_url": MODEL_S_URL,
            "sha256": sha256,
            "byte_count": len(raw),
            "parsed_rows": len(rs),
            "r_min": rs[0],
            "r_max": rs[-1],
            "rho_at_b_linear_g_cm3": interp_linear(B_OVER_RSUN, rs, rhos),
        },
        "frozen_geometry": {
            "b_over_rsun": B_OVER_RSUN,
            "z_au": Z_AU,
            "rsun_cm": RSUN_CM,
        },
        "integration": {
            "method": "composite Simpson in chord coordinate; linear interpolation in rho(r)",
            "n_coarse": args.n_coarse,
            "n_fine": args.n_fine,
            "sigma_coarse_g_cm2": coarse,
            "sigma_fine_g_cm2": fine,
            "coarse_fine_relative_difference": rel,
            "sigma_logrho_sensitivity_g_cm2": log_sensitivity,
            "linear_vs_logrho_relative_difference": log_rel,
        },
        "column": {
            "mass_column_g_cm2": fine,
            "atomic_mass_unit_g": M_U_G,
            "nucleon_column_cm2": n_nucleons,
        },
        "guards": [
            "column-only authority; no detector/material/power fold",
            "no source substitution",
            "cross-section/source-regime classifications remain a separate 0092 step",
        ],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if status.startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
