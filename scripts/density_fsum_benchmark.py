#!/usr/bin/env python3
"""Hosted benchmark for the preregistered NMIR density f-sum gate."""

from __future__ import annotations

import json
import math

from nmir.density_fsum import (
    deposition_proxy,
    energy_weighted_strength,
    identical_constituent_fsum,
    response_from_shape,
    single_mode_response,
    unweighted_strength,
)


def relerr(a: float, b: float) -> float:
    return abs(a - b) / max(abs(b), 1e-300)


def main() -> None:
    m1 = 1.23456789
    responses = {
        "single_particle_like": single_mode_response(m1, 1.0e-3),
        "collective_low_energy": single_mode_response(m1, 1.0e-9),
        "multi_peak": response_from_shape(m1, [2e-8, 4e-6, 7e-4, 2e-2], [2.0, 5.0, 3.0, 1.0]),
        "narrow_family_1e-3": response_from_shape(m1, [0.999, 1.0, 1.001], [1.0, 4.0, 1.0]),
        "narrow_family_1e-9": response_from_shape(m1, [1.0 - 1e-9, 1.0, 1.0 + 1e-9], [1.0, 4.0, 1.0]),
    }

    m1_errors = {name: relerr(energy_weighted_strength(r), m1) for name, r in responses.items()}
    unit_dep_errors = {name: relerr(deposition_proxy(r, lambda _: 1.0), m1) for name, r in responses.items()}

    kmax = 4.0
    kernels = [
        lambda e: 0.25 * kmax,
        lambda e: kmax / (1.0 + e),
        lambda e: kmax * (0.5 + 0.5 * math.exp(-e)),
    ]
    kernel_bound_ratios = []
    for response in responses.values():
        for kernel in kernels:
            kernel_bound_ratios.append(deposition_proxy(response, kernel) / (kmax * m1))

    high = single_mode_response(m1, 1.0)
    low = single_mode_response(m1, 1e-6)
    unweighted_gain = unweighted_strength(low) / unweighted_strength(high)
    energy_gain = deposition_proxy(low, lambda _: 1.0) / deposition_proxy(high, lambda _: 1.0)

    q = 0.01
    mass = 938.0
    coupling = 1.0
    one = identical_constituent_fsum(q, mass, coupling, 1)
    million = identical_constituent_fsum(q, mass, coupling, 1_000_000)
    n_scaling = million / one

    passed = (
        max(m1_errors.values()) <= 1e-12
        and max(unit_dep_errors.values()) <= 1e-12
        and max(kernel_bound_ratios) <= 1.0 + 1e-12
        and unweighted_gain >= 1e6
        and abs(energy_gain - 1.0) <= 1e-12
        and abs(n_scaling / 1e6 - 1.0) <= 1e-12
    )

    result = {
        "status": "PASS_DENSITY_FSUM" if passed else "FAIL",
        "m1_reference": m1,
        "max_m1_relative_error": max(m1_errors.values()),
        "max_unit_kernel_deposition_relative_error": max(unit_dep_errors.values()),
        "max_bounded_kernel_ratio_to_Kmax_m1": max(kernel_bound_ratios),
        "collective_mode_unweighted_strength_gain": unweighted_gain,
        "collective_mode_energy_weighted_gain": energy_gain,
        "N_1_to_1e6_fsum_gain": n_scaling,
        "narrowing_characteristic_scale_ratio": 1e6,
        "scope": "coordinate-local passive density response only; spin/CC/nonlocal/active/BSM/gravity excluded",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
