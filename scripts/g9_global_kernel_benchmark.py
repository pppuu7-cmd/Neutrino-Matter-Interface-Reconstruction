#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import urllib.request

from nmir.g9_ccsn_lens import annular_point_source_receiver_mu
from nmir.g9_global_kernel import (
    cumulative_kernel_point,
    find_signed_roots,
    refine_grid_once,
)
from nmir.gravity_extended import combined_scan_grid, focal_distance_au, parse_model_s_text

MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB_SHA = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = "https://raw.githubusercontent.com/ramses-organisation/ramses/" + MODEL_S_COMMIT + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
R_SUN_CM = 6.96e10
ROOT_CONTROLS = (0.020, 0.024, 0.030)
RADII_CM = tuple(10.0**i for i in range(10))  # 1 cm ... 1e9 cm; includes 1,10,100 m controls.
ROOT_TOL = 1.0e-10
LOCAL_REL_TOL = 0.005
REFINE_REL_TOL = 0.005


def git_blob_sha1(payload: bytes) -> str:
    return hashlib.sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def relerr(a: float, b: float) -> float:
    if a == b == 0.0:
        return 0.0
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def main() -> None:
    with urllib.request.urlopen(MODEL_S_URL, timeout=30) as response:
        payload = response.read()
    blob = git_blob_sha1(payload)
    profile = parse_model_s_text(payload.decode())
    focal = lambda b: focal_distance_au(profile, b, R_SUN_CM)
    base_grid = combined_scan_grid()
    fine_grid = refine_grid_once(base_grid)

    branches = []
    max_refine_rel = 0.0
    all_area_ok = True
    all_root_ok = True
    all_unique_ok = True
    local_checks = []
    try:
        for generating_root in ROOT_CONTROLS:
            z = focal(generating_root)
            roots_base = find_signed_roots(z, focal, R_SUN_CM, base_grid, explicit_roots=(generating_root,))
            roots_fine = find_signed_roots(z, focal, R_SUN_CM, fine_grid, explicit_roots=(generating_root,))
            nearest = min(roots_base, key=lambda x: abs(x - generating_root))
            root_error = abs(nearest - generating_root)
            all_root_ok = all_root_ok and root_error <= ROOT_TOL and all(1e-4 <= r <= 1.0 for r in roots_base)
            all_unique_ok = all_unique_ok and all(abs(a - b) > 1e-9 for a, b in zip(roots_base, roots_base[1:]))

            base_points = []
            fine_points = []
            prev_area = -1.0
            for radius in RADII_CM:
                area_b, mu_b, intervals_b = cumulative_kernel_point(radius, z, focal, R_SUN_CM, base_grid, roots_base)
                area_f, mu_f, intervals_f = cumulative_kernel_point(radius, z, focal, R_SUN_CM, fine_grid, roots_fine)
                rr = relerr(area_b, area_f)
                max_refine_rel = max(max_refine_rel, rr)
                area_ceiling = math.pi * R_SUN_CM**2
                area_ok = math.isfinite(area_b) and area_b >= 0.0 and area_b + 1e-10 * area_ceiling >= prev_area and area_b <= area_ceiling * (1.0 + 1e-10)
                all_area_ok = all_area_ok and area_ok
                prev_area = area_b
                base_points.append({"radius_cm": radius, "area_cm2": area_b, "mu_aperture": mu_b, "interval_count": len(intervals_b)})
                fine_points.append({"radius_cm": radius, "area_cm2": area_f, "mu_aperture": mu_f, "interval_count": len(intervals_f), "base_refine_relative_difference": rr})

            branches.append({
                "generating_root_b_over_Rsun": generating_root,
                "observer_distance_au": z,
                "roots_base": roots_base,
                "roots_refined": roots_fine,
                "generating_root_recovery_error": root_error,
                "base_kernel": base_points,
                "refined_kernel": fine_points,
            })

            if generating_root == 0.024:
                for receiver_cm in (100.0, 1000.0, 10000.0):
                    area, global_mu, intervals = cumulative_kernel_point(receiver_cm, z, focal, R_SUN_CM, base_grid, roots_base)
                    exact_ring = annular_point_source_receiver_mu(generating_root, receiver_cm, R_SUN_CM, focal)[3]
                    containing = [iv for iv in intervals if iv[0] <= generating_root <= iv[1]]
                    if len(containing) != 1:
                        local_ratio = None
                        local_rel = float("inf")
                    else:
                        lo, hi = containing[0]
                        local_ratio = R_SUN_CM**2 * (hi * hi - lo * lo) / receiver_cm**2
                        local_rel = relerr(local_ratio, exact_ring)
                    local_checks.append({
                        "receiver_radius_cm": receiver_cm,
                        "global_mu_aperture": global_mu,
                        "exact_one_ring_mu": exact_ring,
                        "containing_interval_mu": local_ratio,
                        "containing_interval_relative_error": local_rel,
                        "global_contains_one_ring": global_mu + 1e-12 >= exact_ring,
                    })
    except ValueError as exc:
        result = {
            "status": "BLOCKED_G9_GLOBAL_MULTIIMAGE_KERNEL",
            "reason": str(exc),
            "model_s_git_blob_sha1": blob,
            "branches_completed": branches,
        }
        Path("g9_global_kernel_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    local_ok = all(
        row["global_contains_one_ring"]
        and row["containing_interval_relative_error"] is not None
        and row["containing_interval_relative_error"] <= LOCAL_REL_TOL
        for row in local_checks
    )
    refine_ok = max_refine_rel <= REFINE_REL_TOL
    model_ok = blob == MODEL_S_BLOB_SHA
    passed = model_ok and all_root_ok and all_unique_ok and all_area_ok and local_ok and refine_ok
    status = "PASS_G9_GLOBAL_MULTIIMAGE_KERNEL" if passed else "SCIENTIFIC_FAIL_G9_GLOBAL_MULTIIMAGE_KERNEL"
    result = {
        "status": status,
        "contract": "iteration 0076 prereg 05a3354dd2f8cdbba1f2dd04342161b515a10304",
        "model_s_commit": MODEL_S_COMMIT,
        "model_s_git_blob_sha1": blob,
        "impact_domain_b_over_Rsun": [base_grid[0], base_grid[-1]],
        "base_grid_nodes": len(base_grid),
        "refined_grid_nodes": len(fine_grid),
        "radii_cm": RADII_CM,
        "branches": branches,
        "local_authority_checks": local_checks,
        "max_base_refined_area_relative_difference": max_refine_rel,
        "criteria": {
            "root_tolerance_b_over_Rsun": ROOT_TOL,
            "local_one_ring_relative_tolerance": LOCAL_REL_TOL,
            "grid_refinement_relative_tolerance": REFINE_REL_TOL,
            "root_recovery_pass": all_root_ok,
            "root_uniqueness_pass": all_unique_ok,
            "area_invariants_pass": all_area_ok,
            "local_authority_pass": local_ok,
            "grid_refinement_pass": refine_ok,
        },
        "scope": "global transparent-solar-aperture radial geometry only; no finite-source utility classification, named-source scan, detector gain, interaction gain, or neutrino-energy gain",
    }
    Path("g9_global_kernel_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
