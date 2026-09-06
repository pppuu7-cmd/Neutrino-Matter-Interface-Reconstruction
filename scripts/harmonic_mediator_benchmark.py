#!/usr/bin/env python3
"""Hosted benchmark for the preregistered NMIR passive harmonic-mediator gate."""

from __future__ import annotations

import json

from nmir.harmonic_mediator import (
    completed_square_hamiltonian,
    effective_pair_scale,
    field_energy_at_minimum,
    induced_energy_magnitude,
    mediator_hamiltonian,
    per_particle_energy_gain,
)


def relerr(a: float, b: float) -> float:
    return abs(a - b) / max(abs(b), 1e-300)


def main() -> None:
    n1, n2 = 1_000.0, 1_000_000.0
    o, g0, kappa = 0.5, 1.0, 2.0

    # Completion-of-square identity away from the minimum.
    x = 3.7
    direct = mediator_hamiltonian(n1, o, x, g0, 0.37, kappa)
    completed = completed_square_hamiltonian(n1, o, x, g0, 0.37, kappa)
    square_identity_error = relerr(direct, completed)

    rows = {}
    max_field_induced_error = 0.0
    max_gain_error = 0.0
    for gamma in (0.0, 0.25, 0.5, 0.75):
        f1 = field_energy_at_minimum(n1, o, g0, gamma, kappa)
        f2 = field_energy_at_minimum(n2, o, g0, gamma, kappa)
        i1 = induced_energy_magnitude(n1, o, g0, gamma, kappa)
        i2 = induced_energy_magnitude(n2, o, g0, gamma, kappa)
        max_field_induced_error = max(
            max_field_induced_error, relerr(f1, i1), relerr(f2, i2)
        )
        field_gain = (f2 / n2) / (f1 / n1)
        induced_gain = (i2 / n2) / (i1 / n1)
        analytic_gain = per_particle_energy_gain(n1, n2, gamma)
        max_gain_error = max(
            max_gain_error,
            relerr(field_gain, induced_gain),
            relerr(induced_gain, analytic_gain),
        )
        rows[str(gamma)] = {
            "field_energy_per_particle_gain": field_gain,
            "induced_energy_per_particle_gain": induced_gain,
            "analytic_gain": analytic_gain,
            "field_energy_N2": f2,
            "induced_energy_magnitude_N2": i2,
        }

    dicke_gain_error = abs(rows["0.5"]["induced_energy_per_particle_gain"] - 1.0)
    j1 = effective_pair_scale(n1, g0, 0.5, kappa)
    j2 = effective_pair_scale(n2, g0, 0.5, kappa)
    pair_ratio = j2 / j1
    pair_ratio_error = relerr(pair_ratio, n1 / n2)

    passed = (
        square_identity_error <= 1e-15
        and max_field_induced_error <= 1e-15
        and max_gain_error <= 1e-12
        and dicke_gain_error <= 1e-12
        and pair_ratio_error <= 1e-12
    )

    result = {
        "status": "PASS_HARMONIC_MEDIATOR_BUDGET" if passed else "FAIL_HARMONIC_MEDIATOR_BUDGET",
        "N1": n1,
        "N2": n2,
        "square_identity_relative_error": square_identity_error,
        "max_field_vs_induced_energy_relative_error": max_field_induced_error,
        "max_per_particle_gain_relative_error": max_gain_error,
        "gamma_rows": rows,
        "gamma_half_per_particle_gain_abs_error_to_1": dicke_gain_error,
        "gamma_half_effective_pair_ratio": pair_ratio,
        "gamma_half_pair_ratio_relative_error_to_N1_over_N2": pair_ratio_error,
        "interpretation": (
            "A passive stable harmonic mediator produces an induced collective energy and a "
            "mediator displacement-energy scale with the same g_N^2 N^2 scaling. "
            "The 1/sqrt(N) Dicke scaling makes both extensive and yields J_eff~1/N."
        ),
        "scope": (
            "single passive stable harmonic mediator; multi-mode/gapless/nonlinear/driven fields, "
            "higher-body interactions, BSM and gravity excluded"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
