#!/usr/bin/env python3
"""Hosted benchmark for the preregistered NMIR full Model-S projected lens gate."""

from __future__ import annotations

import hashlib
import json
import math
import urllib.request

from nmir.gravity_extended import (
    RadialDensityProfile,
    focal_distance_au_from_projected_mass,
    parse_model_s_text,
    projected_mass_g,
    scan_focal_profile,
    total_mass_g,
    uniform_sphere_projected_fraction,
)

MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB_SHA = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = (
    "https://raw.githubusercontent.com/ramses-organisation/ramses/"
    + MODEL_S_COMMIT
    + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
)
R_MODEL_CM = 6.96e10
M_MODEL_G = 1.989e33
PUBLISHED_FOCUS_AU = 23.5
PUBLISHED_INNER_PROJECTED_FRACTION = 0.0137
B_CHECK = 0.024


def relerr(value: float, reference: float) -> float:
    return abs(value / reference - 1.0)


def git_blob_sha1(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()


def fetch_pinned_model_s() -> tuple[str, str]:
    with urllib.request.urlopen(MODEL_S_URL, timeout=30) as response:
        payload = response.read()
    return payload.decode("utf-8"), git_blob_sha1(payload)


def uniform_sphere_control() -> float:
    n = 16001
    rho = 2.5
    radii = tuple(i / (n - 1) for i in range(n))
    profile = RadialDensityProfile(radii, tuple(rho for _ in radii))
    total = total_mass_g(profile, 1.0e10)
    errors = []
    for bfrac in (0.01, 0.024, 0.05, 0.2, 0.5, 0.9):
        numeric = projected_mass_g(profile, bfrac, 1.0e10) / total
        exact = uniform_sphere_projected_fraction(bfrac)
        errors.append(relerr(numeric, exact))
    return max(errors)


def main() -> None:
    text, actual_blob_sha = fetch_pinned_model_s()
    profile = parse_model_s_text(text)

    uniform_max_error = uniform_sphere_control()
    mass_g = total_mass_g(profile, R_MODEL_CM)
    mass_rel_error = relerr(mass_g, M_MODEL_G)

    mproj_check = projected_mass_g(profile, B_CHECK, R_MODEL_CM)
    projected_fraction = mproj_check / M_MODEL_G
    projected_fraction_rel_error = relerr(
        projected_fraction, PUBLISHED_INNER_PROJECTED_FRACTION
    )
    focus_check_au = focal_distance_au_from_projected_mass(
        mproj_check, B_CHECK, R_MODEL_CM
    )
    focus_check_rel_error = relerr(focus_check_au, PUBLISHED_FOCUS_AU)

    scan = scan_focal_profile(profile, R_MODEL_CM)
    min_bfrac, min_mproj, min_focus_au = min(scan, key=lambda row: row[2])
    min_focus_rel_error = relerr(min_focus_au, PUBLISHED_FOCUS_AU)

    passed = (
        actual_blob_sha == MODEL_S_BLOB_SHA
        and uniform_max_error <= 2e-3
        and mass_rel_error <= 0.02
        and projected_fraction_rel_error <= 0.15
        and focus_check_rel_error <= 0.07
        and min_focus_rel_error <= 0.07
    )

    result = {
        "status": "MODEL_S_ROBUSTNESS_PASS" if passed else "MODEL_S_ROBUSTNESS_FAIL",
        "model_s_commit": MODEL_S_COMMIT,
        "expected_git_blob_sha1": MODEL_S_BLOB_SHA,
        "actual_git_blob_sha1": actual_blob_sha,
        "profile_points": len(profile.radius_fraction),
        "profile_rmax_fraction": profile.radius_fraction[-1],
        "uniform_sphere_max_projected_mass_relative_error": uniform_max_error,
        "integrated_mass_g": mass_g,
        "integrated_mass_relative_error_to_1p989e33": mass_rel_error,
        "b_check_fraction": B_CHECK,
        "projected_mass_at_b_check_g": mproj_check,
        "projected_mass_fraction_of_model_mass": projected_fraction,
        "projected_fraction_relative_error_to_0p0137": projected_fraction_rel_error,
        "focus_at_b_check_au": focus_check_au,
        "focus_at_b_check_relative_error_to_23p5": focus_check_rel_error,
        "minimum_scanned_b_fraction": min_bfrac,
        "minimum_scanned_projected_mass_g": min_mproj,
        "minimum_scanned_focus_au": min_focus_au,
        "minimum_focus_relative_error_to_23p5": min_focus_rel_error,
        "scan_points": len(scan),
        "scope": (
            "Model-S density-profile robustness for transparent-Sun focal geometry; "
            "not an extended-source magnification or usable neutrino-power gain"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
