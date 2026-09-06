#!/usr/bin/env python3
"""Hosted benchmark for the preregistered NMIR long-range budget gate."""

from __future__ import annotations

import json

from nmir.long_range_budget import (
    all_to_all_pair_budget,
    finite_n_per_particle_gain,
    first_moment_pair_bound,
    kac_normalized_factor,
    per_particle,
    power_law_budget_factor,
)


def relerr(a: float, b: float) -> float:
    return abs(a - b) / max(abs(b), 1e-300)


def main() -> None:
    n1, n2 = 1_000, 1_000_000
    j0 = 1.0
    o0 = 0.5

    rows = {}
    max_gain_mismatch = 0.0
    for kappa in (0.0, 0.5, 1.0):
        w1 = all_to_all_pair_budget(n1, j0, kappa)
        w2 = all_to_all_pair_budget(n2, j0, kappa)
        m1 = first_moment_pair_bound(w1, o0)
        m2 = first_moment_pair_bound(w2, o0)
        budget_gain = per_particle(w2, n2) / per_particle(w1, n1)
        response_gain = per_particle(m2, n2) / per_particle(m1, n1)
        analytic_gain = finite_n_per_particle_gain(n1, n2, kappa)
        mismatch = max(
            relerr(response_gain, budget_gain),
            relerr(budget_gain, analytic_gain),
        )
        max_gain_mismatch = max(max_gain_mismatch, mismatch)
        rows[str(kappa)] = {
            "budget_per_particle_N1": per_particle(w1, n1),
            "budget_per_particle_N2": per_particle(w2, n2),
            "budget_per_particle_gain": budget_gain,
            "response_bound_per_particle_gain": response_gain,
            "analytic_gain": analytic_gain,
        }

    identity_budget = 17.25
    identity_m1 = first_moment_pair_bound(identity_budget, o0)
    identity_rel_error = relerr(identity_m1, 8.0 * o0 * o0 * identity_budget)

    kac_change = abs(rows["1.0"]["budget_per_particle_gain"] - 1.0)
    unscaled_analytic_error = relerr(
        rows["0.0"]["budget_per_particle_gain"],
        (n2 - 1) / (n1 - 1),
    )

    powerlaw = {}
    max_kac_error = 0.0
    for alpha, dimension in ((1.0, 3.0), (2.0, 3.0), (3.0, 3.0), (4.0, 3.0)):
        raw1 = power_law_budget_factor(float(n1), alpha, dimension)
        raw2 = power_law_budget_factor(float(n2), alpha, dimension)
        norm1 = kac_normalized_factor(float(n1), alpha, dimension)
        norm2 = kac_normalized_factor(float(n2), alpha, dimension)
        max_kac_error = max(max_kac_error, abs(norm1 - 1.0), abs(norm2 - 1.0))
        powerlaw[f"alpha_{alpha}_d_{dimension}"] = {
            "raw_factor_N1": raw1,
            "raw_factor_N2": raw2,
            "raw_gain": raw2 / raw1,
            "kac_factor_N1": norm1,
            "kac_factor_N2": norm2,
        }

    passed = (
        identity_rel_error <= 1e-15
        and kac_change < 2e-3
        and unscaled_analytic_error <= 1e-12
        and max_gain_mismatch <= 1e-12
        and max_kac_error <= 1e-15
    )

    result = {
        "status": "PASS_LONG_RANGE_BUDGET" if passed else "FAIL_LONG_RANGE_BUDGET",
        "N1": n1,
        "N2": n2,
        "o0": o0,
        "first_moment_identity_relative_error": identity_rel_error,
        "kappa_rows": rows,
        "kac_kappa1_per_particle_change_abs": kac_change,
        "unscaled_kappa0_analytic_gain_relative_error": unscaled_analytic_error,
        "max_response_vs_budget_gain_mismatch": max_gain_mismatch,
        "power_law_scaling": powerlaw,
        "max_kac_normalized_factor_error": max_kac_error,
        "interpretation": (
            "Any superextensive first-moment bound in this passive pair-interaction class "
            "tracks a superextensive absolute interaction-norm budget; enforcing an O(N) "
            "budget removes the parametric per-particle gain."
        ),
        "scope": (
            "passive pair Hamiltonians + additive bounded neutrino-coupled observables; "
            "active pumping, omitted mediator-field energy, higher-body terms, BSM and gravity excluded"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
