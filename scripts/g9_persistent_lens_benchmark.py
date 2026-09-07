#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import urllib.request

from nmir.g9_ccsn_lens import annular_point_source_receiver_mu
from nmir.g9_persistent_lens import (
    AU_CM,
    R_SUN_CM,
    build_local_branch_grid,
    large_source_ring_excess_upper,
    one_ring_receiver_mu,
    perfect_whole_sun_mu_upper,
)
from nmir.gravity_extended import focal_distance_au, parse_model_s_text

MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB_SHA = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = "https://raw.githubusercontent.com/ramses-organisation/ramses/" + MODEL_S_COMMIT + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
ROOTS = (0.020, 0.024, 0.030)
RECEIVER_M = (1.0, 10.0, 100.0)
THETA_RAD = tuple(10.0 ** (-18 + i) for i in range(13))
DELTA_M = (0.0, 0.01, 0.1, 1.0, 10.0, 100.0)
THRESHOLDS = (2.0, 10.0, 1000.0)
POINT_GRID_REL_TOL = 0.03
SOURCE_QUAD_REL_TOL = 0.05


def git_blob_sha1(payload: bytes) -> str:
    return hashlib.sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def main() -> None:
    with urllib.request.urlopen(MODEL_S_URL, timeout=30) as response:
        model_payload = response.read()
    blob = git_blob_sha1(model_payload)
    profile = parse_model_s_text(model_payload.decode())
    focal = lambda b: focal_distance_au(profile, b, R_SUN_CM)

    branch_grids = {}
    branches = []
    try:
        for root in ROOTS:
            z = focal(root)
            max_radius = z * AU_CM * max(THETA_RAD) + max(DELTA_M) * 100.0 + max(RECEIVER_M) * 100.0
            z2, grid = build_local_branch_grid(root, max_radius, focal, R_SUN_CM, points_per_decade=24)
            branch_grids[root] = grid
            branches.append({"root_b_over_Rsun": root, "observer_distance_au": z2, "grid_nodes": len(grid), "max_supported_image_radius_cm": max(y for _, y in grid)})
    except ValueError as exc:
        result = {
            "status": "BLOCKED_G9_PERSISTENT_GEOMETRY",
            "reason": str(exc),
            "model_s_git_blob_sha1": blob,
            "branches_completed": branches,
        }
        Path("g9_persistent_lens_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    # Pre-result numerical validation: the geometric branch integration must recover
    # the already validated exact point-source annulus to within the frozen 3% tolerance.
    point_validation = []
    max_point_rel = 0.0
    for root in ROOTS:
        grid = branch_grids[root]
        for a_m in RECEIVER_M:
            a = a_m * 100.0
            exact_ring = annular_point_source_receiver_mu(root, a, R_SUN_CM, focal)[3]
            grid_ring = one_ring_receiver_mu(grid, a, 0.0, 0.0, R_SUN_CM, 1, 1) - 1.0
            rel = abs(grid_ring - exact_ring) / exact_ring
            max_point_rel = max(max_point_rel, rel)
            point_validation.append({"root_b_over_Rsun": root, "receiver_radius_m": a_m, "exact_ring_mu": exact_ring, "grid_ring_mu": grid_ring, "relative_error": rel})

    rows = []
    by_key = {}
    max_mu = 0.0
    min_mu = float("inf")
    upper_ok = True
    finite_ok = True
    survivor = False
    for root in ROOTS:
        z = focal(root)
        grid = branch_grids[root]
        for a_m in RECEIVER_M:
            a = a_m * 100.0
            mu_upper = perfect_whole_sun_mu_upper(a, R_SUN_CM)
            for theta in THETA_RAD:
                s = z * AU_CM * theta
                for delta_m in DELTA_M:
                    d = delta_m * 100.0
                    mu = one_ring_receiver_mu(grid, a, s, d, R_SUN_CM, 6, 12)
                    row = {
                        "root_b_over_Rsun": root,
                        "observer_distance_au": z,
                        "receiver_radius_m": a_m,
                        "theta_s_rad": theta,
                        "source_footprint_cm": s,
                        "delta_y_m": delta_m,
                        "mu_real": mu,
                        "mu_upper_duty1_whole_sun": mu_upper,
                    }
                    rows.append(row)
                    by_key[(root, a_m, theta, delta_m)] = mu
                    max_mu = max(max_mu, mu)
                    min_mu = min(min_mu, mu)
                    finite_ok = finite_ok and math.isfinite(mu) and mu >= 1.0
                    upper_ok = upper_ok and mu <= mu_upper * (1.0 + 1e-12)
                    # PASS must not rely on the exact zero-error control.
                    if delta_m >= 0.01 and mu >= 2.0:
                        survivor = True

    # Deterministic source-quadrature refinement on extremes and transition scales.
    refinement = []
    max_ref_rel = 0.0
    for root in (0.024,):
        z = focal(root)
        grid = branch_grids[root]
        for a_m in (1.0, 100.0):
            a = a_m * 100.0
            for theta in (1e-12, 1e-8, 1e-6):
                s = z * AU_CM * theta
                for delta_m in (0.0, 100.0):
                    coarse = by_key[(root, a_m, theta, delta_m)]
                    fine = one_ring_receiver_mu(grid, a, s, delta_m * 100.0, R_SUN_CM, 10, 24)
                    rel = abs(fine - coarse) / max(1.0, abs(fine))
                    max_ref_rel = max(max_ref_rel, rel)
                    refinement.append({"receiver_radius_m": a_m, "theta_s_rad": theta, "delta_y_m": delta_m, "coarse_mu": coarse, "fine_mu": fine, "relative_difference": rel})

    # Grid-certified finite position tolerances.  If the threshold survives the 100-m
    # edge, this is deliberately reported as a certified >=100 m region, not extrapolated.
    tolerances = []
    for root in ROOTS:
        for a_m in RECEIVER_M:
            for theta in THETA_RAD:
                for threshold in THRESHOLDS:
                    good = [d for d in DELTA_M if by_key[(root, a_m, theta, d)] >= threshold]
                    tolerances.append({
                        "root_b_over_Rsun": root,
                        "receiver_radius_m": a_m,
                        "theta_s_rad": theta,
                        "threshold_mu": threshold,
                        "certified_position_tolerance_m": max(good) if good else None,
                        "edge_limited_lower_bound": bool(good and max(good) == max(DELTA_M)),
                    })

    # The mandatory whole-Sun aperture ceiling is independent of blur by construction:
    # allowing every source element to use the full solar aperture is the most optimistic
    # possible redirection.  Hence no finite critical theta is certified by this ceiling.
    critical_theta = []
    for a_m in RECEIVER_M:
        upper = perfect_whole_sun_mu_upper(a_m * 100.0, R_SUN_CM)
        for threshold in THRESHOLDS:
            critical_theta.append({"receiver_radius_m": a_m, "threshold_mu": threshold, "critical_theta_s_rad_under_whole_sun_ceiling": None if upper >= threshold else 0.0, "note": "no finite critical theta from deliberately impossible full-aperture ceiling"})

    # Explicit asymptotic invariant: for a uniform source much wider than the solar
    # aperture, any one-ring excess is <= (Rsun/s)^2 and therefore tends to zero.
    asymptotic = []
    for s_over_r in (10.0, 100.0, 1000.0):
        bound = large_source_ring_excess_upper(s_over_r * R_SUN_CM, R_SUN_CM)
        asymptotic.append({"source_radius_over_Rsun": s_over_r, "ring_excess_upper": bound, "total_mu_upper_from_ring_plus_baseline": 1.0 + bound})
    asymptotic_ok = all(asymptotic[i+1]["ring_excess_upper"] < asymptotic[i]["ring_excess_upper"] for i in range(len(asymptotic)-1)) and asymptotic[-1]["ring_excess_upper"] <= 1e-6

    invariants_ok = blob == MODEL_S_BLOB_SHA and finite_ok and upper_ok and asymptotic_ok and max_point_rel <= POINT_GRID_REL_TOL and max_ref_rel <= SOURCE_QUAD_REL_TOL
    if not invariants_ok:
        status = "SCIENTIFIC_FAIL_G9_PERSISTENT_INVARIANT"
    elif survivor:
        status = "PASS_G9_PERSISTENT_KNOWN_DIRECTION_SURVIVOR"
    else:
        status = "PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_PERSISTENT"

    result = {
        "status": status,
        "contract": "iteration 0075 prereg 60dfd94c269e8d5b3a23f73043c779099cd15783",
        "model_s_commit": MODEL_S_COMMIT,
        "model_s_git_blob_sha1": blob,
        "branches": branches,
        "receiver_radius_m_grid": RECEIVER_M,
        "theta_s_rad_grid": THETA_RAD,
        "delta_y_m_grid": DELTA_M,
        "rows": rows,
        "threshold_tolerances": tolerances,
        "critical_theta_under_optimistic_ceiling": critical_theta,
        "point_annulus_validation": point_validation,
        "source_quadrature_refinement": refinement,
        "max_point_annulus_relative_error": max_point_rel,
        "max_source_quadrature_relative_difference": max_ref_rel,
        "max_mu_real": max_mu,
        "min_mu_real": min_mu,
        "survivor_exists_with_nonzero_error": survivor,
        "asymptotic_large_source_guard": asymptotic,
        "duty_accounting": "instantaneous actively-positioned known-direction geometry; duty=1 is an explicit upper bound only; no time-averaged duty is claimed without positioning dynamics",
        "gain_accounting": "event/fluence focusing only; no interaction, detector, resonance, material, metastable, or neutrino-energy gain multiplication",
    }
    Path("g9_persistent_lens_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if status.startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
