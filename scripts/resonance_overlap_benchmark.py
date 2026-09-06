#!/usr/bin/env python3
"""Hosted numerical benchmark for the preregistered NMIR G8 formal gate."""

from __future__ import annotations

import json
import math

from nmir.resonance_overlap import (
    breit_wigner_area,
    breit_wigner_peak,
    dimensionless_numeric_area,
    entrance_width_area_bound,
    gaussian_profile,
    lorentzian_profile,
)


def overlap_numeric(profile, *, gamma_total=1.0, steps=200_000, t_max=1e4):
    k_res = 10.0
    gamma_in = 1e-20
    gamma_out = 0.5 * gamma_total
    h = 2.0 * t_max / steps
    prefactor = 2.0 * math.pi / (k_res * k_res) * gamma_in * gamma_out / gamma_total
    total = 0.0
    for i in range(steps + 1):
        t = -t_max + i * h
        de = 0.5 * gamma_total * t
        w = 0.5 if i in (0, steps) else 1.0
        total += w * profile(de) / (1.0 + t * t)
    return prefactor * h * total


def main():
    widths = [1e-3, 1e-6, 1e-9, 1e-12, 1e-15]
    gamma_in = 1e-20
    area_checks = []
    for width in widths:
        analytic = breit_wigner_area(
            k_res=10.0,
            statistical_factor=1.0,
            gamma_in=gamma_in,
            gamma_out=0.5 * width,
            gamma_total=width,
        )
        numeric = dimensionless_numeric_area(
            k_res=10.0,
            statistical_factor=1.0,
            gamma_in=gamma_in,
            gamma_out=0.5 * width,
            gamma_total=width,
        )
        area_checks.append({
            "gamma_total": width,
            "analytic_area": analytic,
            "numeric_area": numeric,
            "relative_error": abs(numeric / analytic - 1.0),
        })

    broad = 1e-6
    narrow = 1e-12
    broad_area = breit_wigner_area(
        k_res=10.0, statistical_factor=1.0, gamma_in=gamma_in,
        gamma_out=0.5 * broad, gamma_total=broad,
    )
    narrow_area = breit_wigner_area(
        k_res=10.0, statistical_factor=1.0, gamma_in=gamma_in,
        gamma_out=0.5 * narrow, gamma_total=narrow,
    )
    broad_peak = breit_wigner_peak(
        k_res=10.0, statistical_factor=1.0, gamma_in=gamma_in,
        gamma_out=0.5 * broad, gamma_total=broad,
    )
    narrow_peak = breit_wigner_peak(
        k_res=10.0, statistical_factor=1.0, gamma_in=gamma_in,
        gamma_out=0.5 * narrow, gamma_total=narrow,
    )

    area = broad_area
    gaussian_ratios = []
    for offset in (0.0, 0.5, 3.0, 8.0):
        sigma_src = 3.0
        overlap = overlap_numeric(lambda de, o=offset: gaussian_profile(de, center=o, sigma=sigma_src))
        rho_max = gaussian_profile(offset, center=offset, sigma=sigma_src)
        gaussian_ratios.append(overlap / (rho_max * area))

    lorentzian_ratios = []
    for offset in (0.0, 1.0, 5.0):
        hwhm = 2.0
        overlap = overlap_numeric(lambda de, o=offset: lorentzian_profile(de, center=o, half_width=hwhm))
        rho_max = lorentzian_profile(offset, center=offset, half_width=hwhm)
        lorentzian_ratios.append(overlap / (rho_max * area))

    max_area_error = max(row["relative_error"] for row in area_checks)
    area_invariance_error = abs(narrow_area / broad_area - 1.0)
    peak_gain = narrow_peak / broad_peak
    entrance_bound = entrance_width_area_bound(k_res=10.0, statistical_factor=1.0, gamma_in=gamma_in)
    max_overlap_ratio = max(gaussian_ratios + lorentzian_ratios)

    status = "G8_FORMAL_PASS" if (
        max_area_error <= 1e-4
        and area_invariance_error <= 1e-12
        and peak_gain >= 1e5
        and broad_area <= entrance_bound
        and max_overlap_ratio <= 1.0 + 1e-8
    ) else "G8_FORMAL_FAIL"

    result = {
        "status": status,
        "area_checks": area_checks,
        "max_area_relative_error": max_area_error,
        "fixed_branch_area_invariance_relative_error": area_invariance_error,
        "peak_gain_when_width_narrows_1e6": peak_gain,
        "area_to_entrance_width_bound_ratio": broad_area / entrance_bound,
        "gaussian_overlap_to_supremum_bound_ratios": gaussian_ratios,
        "lorentzian_overlap_to_supremum_bound_ratios": lorentzian_ratios,
        "max_overlap_to_supremum_bound_ratio": max_overlap_ratio,
        "scope": "formal isolated-resonance identity only; target Gamma_in and physical solar line profile still required for G3 power authority",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
