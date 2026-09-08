#!/usr/bin/env python3
"""NMIR 0092b-a1: Model-S H/He/Z chord-composition authority.

This subgate evaluates composition only.  It deliberately reuses the already
validated limited Model-S density profile and uses the extensive GONG file only
for X(r) and Z(r), exactly as frozen in amendment 0092b-a1.
"""
from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import math
import re
from pathlib import Path

B_OVER_RSUN = 0.024
RSUN_CM = 6.957e10
M_U_G = 1.66053906892e-24
SIGMA_0092 = 2.9324883602905845e12
EXPECTED_DENSITY_SHA256 = "65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc"
EXPECTED_HEADER = (2482, 15, 25, 210)
DENSITY_URL = "https://users-phys.au.dk/jcd/solar_models/cptrho.l5bi.d.15c"
FGONG_URL = "https://users-phys.au.dk/jcd/solar_models/fgong.l5bi.d.15c"
FORMAT_URL = "https://users-phys.au.dk/jcd/solar_models/file-format.pdf"

FLOAT_RE = re.compile(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)[Ee][+-]?\d+")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_density(path: Path):
    digest = sha256(path)
    if digest != EXPECTED_DENSITY_SHA256:
        raise ValueError(f"limited Model-S SHA256 mismatch: {digest}")
    rows = []
    for line_no, rawline in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        line = rawline.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 3:
            raise ValueError(f"density line {line_no}: expected >=3 columns")
        r, rho = float(parts[0]), float(parts[2])
        if not (math.isfinite(r) and math.isfinite(rho) and r >= 0.0 and rho >= 0.0):
            raise ValueError(f"density line {line_no}: invalid r/rho")
        rows.append((r, rho))
    rows.sort()
    out = []
    for r, rho in rows:
        if out and r == out[-1][0]:
            if rho != out[-1][1]:
                raise ValueError(f"density duplicate radius {r} inconsistent")
            continue
        out.append((r, rho))
    if not out or out[0][0] > B_OVER_RSUN or out[-1][0] < 1.0:
        raise ValueError("limited Model-S density does not cover frozen chord")
    return [v[0] for v in out], [v[1] for v in out], digest


def parse_fgong(path: Path):
    lines = path.read_text(encoding="ascii").splitlines()
    if len(lines) < 7:
        raise ValueError("FGONG file too short")
    try:
        header = tuple(int(v) for v in lines[3].split())
    except Exception as exc:
        raise ValueError("cannot parse FGONG integer header") from exc
    if header != EXPECTED_HEADER:
        raise ValueError(f"FGONG header {header} != frozen {EXPECTED_HEADER}")
    nn, iconst, ivar, ivers = header

    nums = [float(m.group(0)) for m in FLOAT_RE.finditer("\n".join(lines[4:]))]
    expected = iconst + nn * ivar
    if len(nums) != expected:
        raise ValueError(f"FGONG real count {len(nums)} != expected {expected}")
    glob = nums[:iconst]
    values = nums[iconst:]
    radius_global = glob[1]
    if not (math.isfinite(radius_global) and radius_global > 0.0):
        raise ValueError("invalid glob(2) photospheric radius")

    rows = []
    min_closure = float("inf")
    max_closure = 0.0
    for n in range(nn):
        row = values[n * ivar:(n + 1) * ivar]
        r_cm = row[0]       # var(1,n)
        x_h = row[5]        # var(6,n)
        z_met = row[16]     # var(17,n), valid for ivers=210
        y_he = 1.0 - x_h - z_met
        vals = (r_cm, x_h, y_he, z_met)
        if not all(math.isfinite(v) for v in vals):
            raise ValueError(f"non-finite FGONG composition at mesh {n}")
        if r_cm < 0.0 or x_h < 0.0 or y_he < 0.0 or z_met < 0.0:
            raise ValueError(f"unphysical FGONG composition at mesh {n}: {vals}")
        closure = abs((x_h + y_he + z_met) - 1.0)
        min_closure = min(min_closure, closure)
        max_closure = max(max_closure, closure)
        if closure > 5e-10:
            raise ValueError(f"FGONG fraction closure failed at mesh {n}: {closure}")
        rows.append((r_cm / radius_global, x_h, z_met))

    rows.sort(key=lambda t: t[0])
    dedup = []
    for r, x_h, z_met in rows:
        if dedup and r == dedup[-1][0]:
            if x_h != dedup[-1][1] or z_met != dedup[-1][2]:
                raise ValueError(f"FGONG duplicate normalized radius {r} inconsistent")
            continue
        dedup.append((r, x_h, z_met))
    if dedup[0][0] > B_OVER_RSUN or dedup[-1][0] < 1.0:
        raise ValueError("FGONG composition does not cover frozen chord")

    return {
        "header": header,
        "global_radius_cm": radius_global,
        "r": [v[0] for v in dedup],
        "x": [v[1] for v in dedup],
        "z": [v[2] for v in dedup],
        "sha256": sha256(path),
        "rows": len(dedup),
        "max_fraction_closure": max_closure,
    }


def interp(r: float, grid, vals) -> float:
    if r <= grid[0]:
        return vals[0]
    if r >= grid[-1]:
        return vals[-1]
    j = bisect.bisect_right(grid, r)
    r0, r1 = grid[j - 1], grid[j]
    y0, y1 = vals[j - 1], vals[j]
    t = (r - r0) / (r1 - r0)
    return y0 + t * (y1 - y0)


def component_columns(n: int, dens_r, dens_rho, comp_r, comp_x, comp_z):
    if n <= 0 or n % 2:
        raise ValueError("Simpson N must be a positive even integer")
    b = B_OVER_RSUN
    xmax = math.sqrt(1.0 - b * b)
    h = xmax / n

    sums = [0.0, 0.0, 0.0, 0.0]  # total, H, He, Z
    closest = None
    for i in range(n + 1):
        xx = i * h
        r = math.sqrt(b * b + xx * xx)
        rho = interp(r, dens_r, dens_rho)
        x_h = interp(r, comp_r, comp_x)
        z_met = interp(r, comp_r, comp_z)
        y_he = 1.0 - x_h - z_met
        if min(x_h, y_he, z_met) < -1e-12:
            raise ValueError(f"interpolated negative composition at r={r}")
        f = (rho, rho * x_h, rho * y_he, rho * z_met)
        w = 1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)
        for k in range(4):
            sums[k] += w * f[k]
        if i == 0:
            closest = {"r_over_rsun": r, "rho_g_cm3": rho, "X": x_h, "Y": y_he, "Z": z_met}
    factor = 2.0 * RSUN_CM * h / 3.0
    return [s * factor for s in sums], closest


def rel(a: float, b: float) -> float:
    return abs(a - b) / max(abs(b), 1e-300)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--density", required=True, type=Path)
    ap.add_argument("--fgong", required=True, type=Path)
    ap.add_argument("--format-pdf", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--n-coarse", type=int, default=131072)
    ap.add_argument("--n-fine", type=int, default=262144)
    args = ap.parse_args()

    dens_r, dens_rho, density_hash = parse_density(args.density)
    fg = parse_fgong(args.fgong)
    format_hash = sha256(args.format_pdf)

    coarse, closest_c = component_columns(
        args.n_coarse, dens_r, dens_rho, fg["r"], fg["x"], fg["z"]
    )
    fine, closest = component_columns(
        args.n_fine, dens_r, dens_rho, fg["r"], fg["x"], fg["z"]
    )
    names = ("total", "H", "He", "Z")
    refinement = {names[i]: rel(coarse[i], fine[i]) for i in range(4)}
    component_sum = fine[1] + fine[2] + fine[3]
    closure_against_internal_total = rel(component_sum, fine[0])
    closure_against_0092 = rel(component_sum, SIGMA_0092)
    density_reproduction = rel(fine[0], SIGMA_0092)

    physical_ok = (
        all(v <= 1e-4 for k, v in refinement.items() if k in ("H", "He", "Z"))
        and closure_against_0092 <= 1e-8
        and density_reproduction <= 1e-8
    )
    status = (
        "PASS_G9_0092B_MODEL_S_COMPOSITION_AUTHORITY"
        if physical_ok
        else "BLOCKED_G9_0092B_COMPOSITION_NUMERICS"
    )

    result = {
        "schema": "nmir.g9.ccsn_mev_composition.0092b_a1.v1",
        "status": status,
        "authority": {
            "density_url": DENSITY_URL,
            "density_sha256": density_hash,
            "fgong_url": FGONG_URL,
            "fgong_sha256": fg["sha256"],
            "format_url": FORMAT_URL,
            "format_pdf_sha256": format_hash,
            "fgong_header": list(fg["header"]),
            "fgong_global_radius_cm": fg["global_radius_cm"],
            "fgong_canonical_rows": fg["rows"],
            "fgong_max_fraction_closure": fg["max_fraction_closure"],
        },
        "frozen_geometry": {
            "b_over_rsun": B_OVER_RSUN,
            "rsun_cm": RSUN_CM,
            "sigma_0092_g_cm2": SIGMA_0092,
        },
        "closest_approach": closest,
        "integration": {
            "method": "composite Simpson; validated limited-file rho times linearly interpolated FGONG X,Z; Y=1-X-Z",
            "n_coarse": args.n_coarse,
            "n_fine": args.n_fine,
            "coarse_g_cm2": dict(zip(names, coarse)),
            "fine_g_cm2": dict(zip(names, fine)),
            "relative_refinement": refinement,
            "component_closure_vs_internal_total": closure_against_internal_total,
            "component_closure_vs_frozen_0092_total": closure_against_0092,
            "density_reproduction_vs_0092": density_reproduction,
        },
        "columns": {
            "Sigma_H_g_cm2": fine[1],
            "Sigma_He_g_cm2": fine[2],
            "Sigma_Z_g_cm2": fine[3],
            "N_H_nuclei_cm2": fine[1] / M_U_G,
            "N_He_nuclei_cm2": fine[2] / (4.0 * M_U_G),
            "metal_mass_column_only_g_cm2": fine[3],
        },
        "guards": [
            "composition subgate only; no MeV cross-section fold",
            "validated limited Model-S density retained",
            "no representative metal nucleus selected",
            "no detector/material/BSM gain fold",
        ],
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if status.startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
