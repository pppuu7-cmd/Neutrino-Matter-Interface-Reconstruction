#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

RSUN_CM = 6.957e10
B = 0.024
M_U_G = 1.66053906892e-24
SIGMA_TOTAL_AUTH = 2.9324883602905845e12
LIMITED_SHA_AUTH = "65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_limited(path: Path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        p = s.split()
        rows.append((float(p[0]), float(p[2])))
    a = np.asarray(rows, dtype=float)
    order = np.argsort(a[:, 0])
    r = a[order, 0]
    rho = a[order, 1]
    u, idx = np.unique(r, return_index=True)
    return u, rho[idx]


def parse_fgong(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 8:
        raise ValueError("GONG file too short")
    hdr = [int(x) for x in lines[3].split()]
    if len(hdr) != 4:
        raise ValueError("unexpected integer header")
    nn, iconst, ivar, ivers = hdr
    vals = np.fromstring(" ".join(lines[4:]), sep=" ")
    need = iconst + nn * ivar
    if vals.size != need:
        raise ValueError(f"GONG payload length mismatch: {vals.size} != {need}")
    glob = vals[:iconst]
    var = vals[iconst:].reshape(nn, ivar)
    return {"nn": nn, "iconst": iconst, "ivar": ivar, "ivers": ivers}, glob, var


def simpson_uniform(y: np.ndarray, h: float) -> float:
    n = y.size - 1
    if n <= 0 or n % 2:
        raise ValueError("Simpson requires positive even panel count")
    return h / 3.0 * (y[0] + y[-1] + 4.0 * np.sum(y[1:-1:2]) + 2.0 * np.sum(y[2:-2:2]))


def calc(limited: Path, fgong: Path, fmt: Path, n: int):
    r_l, rho_l = parse_limited(limited)
    header, glob, var = parse_fgong(fgong)
    if header != {"nn": 2482, "iconst": 15, "ivar": 25, "ivers": 210}:
        raise ValueError(f"frozen GONG header mismatch: {header}")
    r_abs = var[:, 0]
    xh = var[:, 5]
    z = var[:, 16]
    r_global = float(glob[1])
    rr = r_abs / r_global
    order = np.argsort(rr)
    rr, xh, z = rr[order], xh[order], z[order]
    rr_u, idx = np.unique(rr, return_index=True)
    rr, xh, z = rr_u, xh[idx], z[idx]
    yhe = 1.0 - xh - z
    if not (np.all(np.isfinite(xh)) and np.all(np.isfinite(z)) and np.all(np.isfinite(yhe))):
        raise ValueError("non-finite composition")
    if np.min(xh) < 0 or np.min(z) < 0 or np.min(yhe) < 0:
        raise ValueError("negative composition fraction")
    closure_point = float(np.max(np.abs(xh + yhe + z - 1.0)))
    if closure_point > 5e-10:
        raise ValueError("pointwise composition closure failure")

    xmax = np.sqrt(1.0 - B * B)
    xx = np.linspace(0.0, xmax, n + 1)
    rnorm = np.sqrt(B * B + xx * xx)
    rho = np.interp(rnorm, r_l, rho_l)
    X = np.interp(rnorm, rr, xh)
    Z = np.interp(rnorm, rr, z)
    Y = 1.0 - X - Z
    h = xmax / n
    fac = 2.0 * RSUN_CM
    sig_h = fac * simpson_uniform(rho * X, h)
    sig_he = fac * simpson_uniform(rho * Y, h)
    sig_z = fac * simpson_uniform(rho * Z, h)
    sig_sum = sig_h + sig_he + sig_z
    return {
        "n_panels": n,
        "sigma_H_g_cm2": sig_h,
        "sigma_He_g_cm2": sig_he,
        "sigma_Z_g_cm2": sig_z,
        "sigma_sum_g_cm2": sig_sum,
        "closure_rel_to_0092": abs(sig_sum - SIGMA_TOTAL_AUTH) / SIGMA_TOTAL_AUTH,
        "N_H_nuclei_cm2": sig_h / M_U_G,
        "N_He_nuclei_cm2": sig_he / (4.0 * M_U_G),
        "composition_at_b": {
            "X": float(np.interp(B, rr, xh)),
            "Y": float(1.0 - np.interp(B, rr, xh) - np.interp(B, rr, z)),
            "Z": float(np.interp(B, rr, z)),
        },
        "pointwise_fraction_closure_max_abs": closure_point,
        "gong_global_radius_cm": r_global,
        "gong_header": header,
    }


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limited", required=True, type=Path)
    ap.add_argument("--fgong", required=True, type=Path)
    ap.add_argument("--format", required=True, type=Path)
    ap.add_argument("--output", default="g9_0092b_a1_model_s_composition.json", type=Path)
    args = ap.parse_args()

    if sha256(args.limited) != LIMITED_SHA_AUTH:
        raise SystemExit("limited Model-S SHA mismatch")
    coarse = calc(args.limited, args.fgong, args.format, 131072)
    fine = calc(args.limited, args.fgong, args.format, 262144)
    refinements = {k: rel(coarse[k], fine[k]) for k in ("sigma_H_g_cm2", "sigma_He_g_cm2", "sigma_Z_g_cm2")}
    status = "PASS_G9_0092B_MODEL_S_COMPOSITION_AUTHORITY"
    reason = "all frozen provenance/format/composition/refinement/closure checks pass"
    if max(refinements.values()) > 1e-4 or fine["closure_rel_to_0092"] > 1e-8:
        status = "BLOCKED_G9_0092B_COMPOSITION_NUMERICS"
        reason = "frozen component refinement or column closure threshold exceeded"

    out = {
        "schema": "nmir.g9.model_s_composition.0092b_a1.v1",
        "prereg": "research/prereg/0092b_g9_ccsn_mev_solar_transmission_authority.md",
        "amendment": "research/amendments/0092b_a1_model_s_gong_composition_authority.md",
        "status": status,
        "reason": reason,
        "provenance": {
            "archive_landing_url": "https://users-phys.au.dk/jcd/solar_models/",
            "limited_model_s_sha256": sha256(args.limited),
            "fgong_model_s_sha256": sha256(args.fgong),
            "gong_format_pdf_sha256": sha256(args.format),
            "fgong_url": "https://users-phys.au.dk/jcd/solar_models/fgong.l5bi.d.15c",
            "format_url": "https://users-phys.au.dk/jcd/solar_models/file-format.pdf",
        },
        "frozen_geometry": {"b_over_rsun": B, "rsun_cm": RSUN_CM},
        "coarse": coarse,
        "fine": fine,
        "component_refinement_relative": refinements,
        "guards": [
            "GONG file supplies X/Z composition only; 0092 limited file remains density authority",
            "no representative metal nucleus selected",
            "no MeV cross-section or optical-depth classification in this subgate",
        ],
    }
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.output.read_text(encoding="utf-8"), end="")
    if status != "PASS_G9_0092B_MODEL_S_COMPOSITION_AUTHORITY":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
