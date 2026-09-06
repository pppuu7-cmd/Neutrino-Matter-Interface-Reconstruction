#!/usr/bin/env python3
"""Hosted benchmark for the preregistered local spin-response sum-rule gate."""

from __future__ import annotations

import json

from nmir.spin_local_sum import (
    all_to_all_heisenberg_bound,
    bounded_coordination_heisenberg_bound,
    heisenberg_bond_operator_norm,
    local_spin_first_moment_bound,
    single_mode_unweighted_strength,
    spin_half_heisenberg_first_moment_bound,
)


def relerr(a: float, b: float) -> float:
    return abs(a - b) / max(abs(b), 1e-300)


def main() -> None:
    js = [0.1, 0.3, 0.7, 1.1]
    norms = [heisenberg_bond_operator_norm(j) for j in js]
    generic = local_spin_first_moment_bound(norms, [2] * len(norms))
    specialized = spin_half_heisenberg_first_moment_bound(js)
    specialization_error = relerr(generic, specialized)

    n_small = 1
    n_big = 1_000_000
    local_small = bounded_coordination_heisenberg_bound(n_small, 6.0, 1.0)
    local_big = bounded_coordination_heisenberg_bound(n_big, 6.0, 1.0)
    local_scaling = local_big / local_small

    m1 = 2.0
    high_e = 1.0
    low_e = 1e-6
    high_s0 = single_mode_unweighted_strength(m1, high_e)
    low_s0 = single_mode_unweighted_strength(m1, low_e)
    unweighted_gain = low_s0 / high_s0
    high_m1 = high_s0 * high_e
    low_m1 = low_s0 * low_e
    weighted_gain = low_m1 / high_m1

    n1, n2 = 1000, 1_000_000
    raw_all_to_all_gain = all_to_all_heisenberg_bound(n2, 1.0) / all_to_all_heisenberg_bound(n1, 1.0)
    kac_gain = all_to_all_heisenberg_bound(n2, 1.0, kac_scale=True) / all_to_all_heisenberg_bound(n1, 1.0, kac_scale=True)
    linear_gain = n2 / n1

    passed = (
        specialization_error <= 1e-12
        and abs(local_scaling / 1e6 - 1.0) <= 1e-12
        and unweighted_gain >= 1e6
        and abs(weighted_gain - 1.0) <= 1e-12
        and raw_all_to_all_gain > 9.0e5
        and abs(kac_gain / linear_gain - 1.0) <= 1e-12
    )

    result = {
        "status": "PASS_LOCAL_SPIN_SUM" if passed else "FAIL",
        "pair_specialization_relative_error": specialization_error,
        "heisenberg_bond_norm_for_J1": heisenberg_bond_operator_norm(1.0),
        "local_N_1_to_1e6_first_moment_gain": local_scaling,
        "soft_mode_unweighted_strength_gain": unweighted_gain,
        "soft_mode_energy_weighted_gain": weighted_gain,
        "all_to_all_N1000_to_N1e6_gain_unscaled": raw_all_to_all_gain,
        "all_to_all_N1000_to_N1e6_gain_Kac_scaled": kac_gain,
        "reference_linear_gain_N1000_to_N1e6": linear_gain,
        "scope": "passive bounded local-spin Hamiltonians; long-range/active/itinerant/CC/BSM/gravity excluded",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
