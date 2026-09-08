#!/usr/bin/env python3
"""Prospectively frozen 0089d B0 bulk/scalar conformance preflight.

This script adds the mass half of amendment 33f7b72 without changing any
scientific 0089d criterion. The bulk evaluator remains validation-only.
"""
from __future__ import annotations

import hashlib
import importlib.util
import math
from pathlib import Path
import urllib.request

from nmir.g9_continuous_projection import continuous_focal_distance_au, continuous_projected_mass_g
from nmir.gravity_extended import AU_CM, C_CGS, G_CGS, parse_model_s_text

AMENDMENT = "33f7b72b7429993b09321cd5674fa1eff3219812"
MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = f"https://raw.githubusercontent.com/ramses-organisation/ramses/{MODEL_S_COMMIT}/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
R = 6.96e10
XMIN, XMAX = 1e-4, 1.0
LIMIT = 2e-11


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load_benchmark_module():
    path = Path(__file__).with_name("g9_continuous_map_monotone_kernel_0089d.py")
    spec = importlib.util.spec_from_file_location("g9_0089d_benchmark", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load 0089d benchmark module")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def symrel(a: float, b: float) -> float:
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def main():
    payload = urllib.request.urlopen(MODEL_S_URL, timeout=30).read()
    if git_blob_sha1(payload) != MODEL_S_BLOB:
        raise SystemExit("INFRASTRUCTURE_FAIL_G9_0089D_BULK_EVALUATOR_CONFORMANCE: Model-S blob mismatch")
    profile = parse_model_s_text(payload.decode())
    mod = load_benchmark_module()
    bulk = mod._bulk_focal_factory(profile)

    rs = [r for r in profile.radius_fraction if XMIN < r < XMAX]
    anchors = sorted(set([XMIN, *rs, XMAX]))
    cells = [(a, b) for a, b in zip(anchors, anchors[1:]) if b > a]
    pts = [1e-4, 3e-4, 1e-3, 0.003, 0.01, 0.02, 0.024, 0.03, 0.05, 0.1, 0.2, 0.4, 0.7, 0.9, 0.99, 0.99999825]
    for j in range(64):
        idx = round(j * (len(cells) - 1) / 63)
        a, b = cells[idx]
        pts.append(0.5 * (a + b))
    pts = sorted(set(pts))

    focals = bulk(pts)
    max_f = 0.0
    max_m = 0.0
    for x, bf in zip(pts, focals):
        bf = float(bf)
        sf = continuous_focal_distance_au(profile, x, R)
        sm = continuous_projected_mass_g(profile, x, R)
        # Algebraic inverse of the same frozen focal definition; this checks the
        # bulk mass represented by F against the scalar accepted mass authority.
        bm = x * x * R * R * C_CGS * C_CGS / (4.0 * G_CGS * bf * AU_CM)
        max_f = max(max_f, symrel(bf, sf))
        max_m = max(max_m, symrel(bm, sm))
    print(f"B0 point_count={len(pts)} max_mass_symrel={max_m:.17g} max_focal_symrel={max_f:.17g} limit={LIMIT:.17g}")
    if max_m > LIMIT or max_f > LIMIT:
        raise SystemExit("INFRASTRUCTURE_FAIL_G9_0089D_BULK_EVALUATOR_CONFORMANCE")


if __name__ == "__main__":
    main()
