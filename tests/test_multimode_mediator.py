import math
import random

import pytest

from nmir.multimode_mediator import (
    diagonal_energy_scale,
    diagonal_null_mode_classification,
    equilibrium_energy_scales,
    rotate_2d_matrix,
    rotate_2d_vector,
)


def _spd_from_random(rng: random.Random, n: int):
    a = [[rng.uniform(-1.0, 1.0) for _ in range(n)] for _ in range(n)]
    k = [[sum(a[m][i] * a[m][j] for m in range(n)) for j in range(n)] for i in range(n)]
    for i in range(n):
        k[i][i] += 0.5
    return k


def test_random_spd_square_completion_and_energy_identity():
    rng = random.Random(1731)
    for _ in range(30):
        k = _spd_from_random(rng, 4)
        b = [rng.uniform(-2.0, 2.0) for _ in range(4)]
        out = equilibrium_energy_scales(k, b)
        scale = max(1.0, abs(float(out["induced_effective_energy"])))
        assert abs(float(out["square_completion_residual"])) / scale < 1e-12
        assert abs(float(out["field_energy"]) + float(out["induced_effective_energy"])) / scale < 1e-12


def test_two_mode_basis_invariance():
    k = [[3.0, 0.4], [0.4, 0.8]]
    b = [1.2, -0.7]
    base = equilibrium_energy_scales(k, b)
    for theta in [0.13, 0.71, 1.24, 2.0]:
        kp = rotate_2d_matrix(k, theta)
        bp = rotate_2d_vector(b, theta)
        got = equilibrium_energy_scales(kp, bp)
        denom = max(1.0, abs(float(base["induced_effective_energy"])))
        assert abs(float(got["induced_effective_energy"]) - float(base["induced_effective_energy"])) / denom < 1e-12


def test_soft_mode_growth_tracks_field_energy_exactly():
    b = [1.0, 0.0]
    e1 = diagonal_energy_scale([1.0, 2.0], b)
    e2 = diagonal_energy_scale([1.0e-9, 2.0], b)
    assert math.isclose(e2 / e1, 1.0e9, rel_tol=1e-12)


def test_exact_null_with_source_is_unstable():
    assert diagonal_null_mode_classification([0.0, 1.0], [1.0, 0.0]) == "UNSTABLE_NO_PASSIVE_EQUILIBRIUM"
    with pytest.raises(ValueError, match="UNSTABLE_NO_PASSIVE_EQUILIBRIUM"):
        diagonal_energy_scale([0.0, 1.0], [1.0, 0.0])


def test_exact_null_orthogonal_to_source_is_finite():
    assert diagonal_null_mode_classification([0.0, 2.0], [0.0, 3.0]) == "FINITE_POSITIVE_SUBSPACE"
    assert math.isclose(diagonal_energy_scale([0.0, 2.0], [0.0, 3.0]), 2.25, rel_tol=1e-15)


def test_negative_stiffness_is_unstable():
    assert diagonal_null_mode_classification([-1.0, 2.0], [0.0, 1.0]) == "UNSTABLE_NEGATIVE_STIFFNESS"


def test_single_mode_limit_matches_square_completion():
    out = equilibrium_energy_scales([[4.0]], [3.0])
    assert math.isclose(float(out["field_energy"]), 9.0 / 8.0, rel_tol=1e-15)
    assert math.isclose(float(out["induced_effective_energy"]), -9.0 / 8.0, rel_tol=1e-15)
