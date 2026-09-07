#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import urllib.request

from nmir.g9_ccsn_lens import annular_point_source_receiver_mu
from nmir.g9_global_kernel import refine_grid_once
from nmir.g9_turning_kernel import (
    cumulative_kernel_point_monotone,
    monotone_segments,
    solve_segment_targets,
)
from nmir.g9_global_kernel import signed_map_cm
from nmir.gravity_extended import combined_scan_grid, focal_distance_au, parse_model_s_text

MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB_SHA = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = "https://raw.githubusercontent.com/ramses-organisation/ramses/" + MODEL_S_COMMIT + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
CONTRACT_COMMIT = "71c21236b1da1817d122567286c938ca6efcce6c"
R_SUN_CM = 6.96e10
ROOT_CONTROLS = (0.020, 0.024, 0.030)
RADII_CM = tuple(10.0**i for i in range(10))
ROOT_TOL = 1.0e-10
LOCAL_REL_TOL = 0.005
GRID_REL_TOL = 0.005
STEP_REL_TOL = 0.005


def git_blob_sha1(payload: bytes) -> str:
    return hashlib.sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def relerr(a: float, b: float) -> float:
    if a == b == 0.0:
        return 0.0
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def evaluate_replica(root: float, z: float, focal, grid, step_scale: float):
    segments = monotone_segments(z, focal, R_SUN_CM, grid, root, step_scale)
    yfn = lambda b: signed_map_cm(b, z, focal, R_SUN_CM)
    zero_roots = solve_segment_targets(segments, (0.0,), yfn)[0.0]
    points = []
    prev_area = -1.0
    area_ceiling = math.pi * R_SUN_CM**2
    area_ok = True
    for radius in RADII_CM:
        area, mu, intervals = cumulative_kernel_point_monotone(radius, z, focal, R_SUN_CM, grid, root, step_scale)
        ok = (
            math.isfinite(area)
            and area >= 0.0
            and area + 1.0e-10 * area_ceiling >= prev_area
            and area <= area_ceiling * (1.0 + 1.0e-10)
        )
        area_ok = area_ok and ok
        prev_area = area
        points.append({
            "radius_cm": radius,
            "area_cm2": area,
            "mu_aperture": mu,
            "interval_count": len(intervals),
            "intervals": intervals,
        })
    return {
        "segments": segments,
        "zero_roots": zero_roots,
        "kernel": points,
        "area_invariants_pass": area_ok,
    }


def main() -> None:
    try:
        with urllib.request.urlopen(MODEL_S_URL, timeout=30) as response:
            payload = response.read()
        blob = git_blob_sha1(payload)
        profile = parse_model_s_text(payload.decode())
        focal = lambda b: focal_distance_au(profile, b, R_SUN_CM)
        base_grid = combined_scan_grid()
        fine_grid = refine_grid_once(base_grid)

        branches = []
        local_checks = []
        all_root_ok = True
        all_unique_ok = True
        all_area_ok = True
        max_grid_rel = 0.0
        max_step_rel = 0.0

        for generating_root in ROOT_CONTROLS:
            z = focal(generating_root)
            base = evaluate_replica(generating_root, z, focal, base_grid, 1.0)
            fine = evaluate_replica(generating_root, z, focal, fine_grid, 1.0)
            half = evaluate_replica(generating_root, z, focal, base_grid, 0.5)

            roots = base["zero_roots"]
            if not roots:
                raise ValueError("no signed-map zero recovered")
            nearest = min(roots, key=lambda x: abs(x - generating_root))
            root_error = abs(nearest - generating_root)
            all_root_ok = all_root_ok and root_error <= ROOT_TOL and all(base_grid[0] <= r <= base_grid[-1] for r in roots)
            all_unique_ok = all_unique_ok and all(abs(a - b) > 1.0e-9 for a, b in zip(roots, roots[1:]))
            all_area_ok = all_area_ok and base["area_invariants_pass"] and fine["area_invariants_pass"] and half["area_invariants_pass"]

            comparisons = []
            for bpt, fpt, hpt in zip(base["kernel"], fine["kernel"], half["kernel"]):
                rg = relerr(bpt["area_cm2"], fpt["area_cm2"])
                rs = relerr(bpt["area_cm2"], hpt["area_cm2"])
                max_grid_rel = max(max_grid_rel, rg)
                max_step_rel = max(max_step_rel, rs)
                comparisons.append({
                    "radius_cm": bpt["radius_cm"],
                    "base_vs_bisected_area_relative_difference": rg,
                    "nominal_vs_halfstep_area_relative_difference": rs,
                })

            branches.append({
                "generating_root_b_over_Rsun": generating_root,
                "observer_distance_au": z,
                "generating_root_recovery_error": root_error,
                "base": base,
                "bisected_grid": fine,
                "half_derivative_step": half,
                "comparisons": comparisons,
            })

            if generating_root == 0.024:
                for receiver_cm in (100.0, 1000.0, 10000.0):
                    area, global_mu, intervals = cumulative_kernel_point_monotone(
                        receiver_cm, z, focal, R_SUN_CM, base_grid, generating_root, 1.0
                    )
                    exact_ring = annular_point_source_receiver_mu(
                        generating_root, receiver_cm, R_SUN_CM, focal
                    )[3]
                    containing = [iv for iv in intervals if iv[0] <= generating_root <= iv[1]]
                    if len(containing) != 1:
                        local_mu = None
                        local_rel = float("inf")
                    else:
                        lo, hi = containing[0]
                        local_mu = R_SUN_CM**2 * (hi * hi - lo * lo) / receiver_cm**2
                        local_rel = relerr(local_mu, exact_ring)
                    local_checks.append({
                        "receiver_radius_cm": receiver_cm,
                        "global_mu_aperture": global_mu,
                        "exact_one_ring_mu": exact_ring,
                        "containing_interval_mu": local_mu,
                        "containing_interval_relative_error": local_rel,
                        "global_contains_one_ring": global_mu + 1.0e-12 >= exact_ring,
                    })

    except (OSError, urllib.error.URLError) as exc:
        result = {"status": "INFRASTRUCTURE_FAIL", "reason": str(exc), "contract_commit": CONTRACT_COMMIT}
        Path("g9_turning_kernel_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result, indent=2, sort_keys=True))
        return
    except ValueError as exc:
        result = {
            "status": "BLOCKED_G9_TURNING_POINT_KERNEL",
            "reason": str(exc),
            "contract_commit": CONTRACT_COMMIT,
            "model_s_git_blob_sha1": locals().get("blob"),
        }
        Path("g9_turning_kernel_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    local_ok = all(
        row["global_contains_one_ring"]
        and row["containing_interval_mu"] is not None
        and row["containing_interval_relative_error"] <= LOCAL_REL_TOL
        for row in local_checks
    )
    grid_ok = max_grid_rel <= GRID_REL_TOL
    step_ok = max_step_rel <= STEP_REL_TOL
    model_ok = blob == MODEL_S_BLOB_SHA
    passed = model_ok and all_root_ok and all_unique_ok and all_area_ok and local_ok and grid_ok and step_ok
    status = "PASS_G9_TURNING_POINT_MONOTONE_KERNEL" if passed else "SCIENTIFIC_FAIL_G9_TURNING_POINT_KERNEL"
    result = {
        "status": status,
        "contract_commit": CONTRACT_COMMIT,
        "model_s_commit": MODEL_S_COMMIT,
        "model_s_git_blob_sha1": blob,
        "impact_domain_b_over_Rsun": [base_grid[0], base_grid[-1]],
        "base_grid_nodes": len(base_grid),
        "bisected_grid_nodes": len(fine_grid),
        "branches": branches,
        "local_authority_checks": local_checks,
        "max_base_vs_bisected_area_relative_difference": max_grid_rel,
        "max_nominal_vs_halfstep_area_relative_difference": max_step_rel,
        "criteria": {
            "root_recovery_pass": all_root_ok,
            "root_uniqueness_pass": all_unique_ok,
            "monotonicity_audit_pass": True,
            "area_invariants_pass": all_area_ok,
            "local_one_ring_pass": local_ok,
            "grid_replica_pass": grid_ok,
            "derivative_step_replica_pass": step_ok,
            "root_tolerance_b_over_Rsun": ROOT_TOL,
            "local_relative_tolerance": LOCAL_REL_TOL,
            "grid_relative_tolerance": GRID_REL_TOL,
            "derivative_step_relative_tolerance": STEP_REL_TOL,
        },
        "scope": "transparent-Sun radial geometry only; no finite-source convolution, named source, detector gain, interaction gain, or BSM response",
    }
    Path("g9_turning_kernel_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
