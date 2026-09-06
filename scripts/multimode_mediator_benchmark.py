"""Hosted benchmark for NMIR passive linear multi-mode mediator gate."""

from __future__ import annotations

import json
import math
import random

from nmir.multimode_mediator import (
    diagonal_energy_scale,
    diagonal_null_mode_classification,
    equilibrium_energy_scales,
    rotate_2d_matrix,
    rotate_2d_vector,
)


def spd_from_random(rng: random.Random, n: int):
    a = [[rng.uniform(-1.0, 1.0) for _ in range(n)] for _ in range(n)]
    k = [[sum(a[m][i] * a[m][j] for m in range(n)) for j in range(n)] for i in range(n)]
    for i in range(n):
        k[i][i] += 0.25
    return k


def main() -> None:
    rng = random.Random(20260906)
    max_square_rel = 0.0
    max_energy_rel = 0.0
    for _ in range(100):
        k = spd_from_random(rng, 5)
        b = [rng.uniform(-1.0, 1.0) for _ in range(5)]
        out = equilibrium_energy_scales(k, b)
        scale = max(1.0, abs(float(out["induced_effective_energy"])))
        max_square_rel = max(max_square_rel, abs(float(out["square_completion_residual"])) / scale)
        max_energy_rel = max(
            max_energy_rel,
            abs(float(out["field_energy"]) + float(out["induced_effective_energy"])) / scale,
        )

    k2 = [[2.7, 0.35], [0.35, 0.9]]
    b2 = [1.4, -0.6]
    base = float(equilibrium_energy_scales(k2, b2)["induced_effective_energy"])
    max_basis_rel = 0.0
    for theta in [i * 0.071 for i in range(1, 41)]:
        got = float(
            equilibrium_energy_scales(
                rotate_2d_matrix(k2, theta), rotate_2d_vector(b2, theta)
            )["induced_effective_energy"]
        )
        max_basis_rel = max(max_basis_rel, abs(got - base) / max(1.0, abs(base)))

    lam_hi = 1.0
    lam_lo = 1.0e-9
    source = [1.0, 0.0]
    e_hi = diagonal_energy_scale([lam_hi, 3.0], source)
    e_lo = diagonal_energy_scale([lam_lo, 3.0], source)
    soft_gain = e_lo / e_hi

    unstable_status = diagonal_null_mode_classification([0.0, 1.0], [1.0, 0.0])
    decoupled_status = diagonal_null_mode_classification([0.0, 1.0], [0.0, 2.0])
    decoupled_energy = diagonal_energy_scale([0.0, 1.0], [0.0, 2.0])

    status = "PASS_MULTIMODE_LINEAR_BUDGET"
    if not (
        max_square_rel < 1e-12
        and max_energy_rel < 1e-12
        and max_basis_rel < 1e-12
        and math.isclose(soft_gain, 1.0e9, rel_tol=1e-9)
        and unstable_status == "UNSTABLE_NO_PASSIVE_EQUILIBRIUM"
        and decoupled_status == "FINITE_POSITIVE_SUBSPACE"
        and math.isclose(decoupled_energy, 2.0, rel_tol=1e-15)
    ):
        status = "FAIL_MULTIMODE_LINEAR_BUDGET"

    result = {
        "status": status,
        "random_spd_trials": 100,
        "max_square_completion_relative_error": max_square_rel,
        "max_field_vs_induced_relative_error": max_energy_rel,
        "max_basis_invariance_relative_error": max_basis_rel,
        "soft_mode_lambda_high": lam_hi,
        "soft_mode_lambda_low": lam_lo,
        "soft_mode_energy_gain": soft_gain,
        "soft_mode_field_gain": soft_gain,
        "soft_mode_gain_ratio_field_to_induced": 1.0,
        "null_mode_with_source": unstable_status,
        "null_mode_decoupled": decoupled_status,
        "null_mode_decoupled_energy": decoupled_energy,
        "interpretation": (
            "For any passive stable linear multimode mediator, square completion makes the mediator "
            "displacement-energy scale exactly equal to the magnitude of the induced collective "
            "interaction. Softening or adding modes cannot produce a free parametrically larger "
            "induced interaction; an exactly coupled zero-stiffness mode has no stable passive equilibrium."
        ),
        "scope": (
            "finite passive linear multimode quadratic mediators; nonlinear, driven/active, higher-body, "
            "BSM and gravity excluded"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if status != "PASS_MULTIMODE_LINEAR_BUDGET":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
