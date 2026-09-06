import math

import pytest

from nmir.long_range_budget import (
    all_to_all_pair_budget,
    finite_n_per_particle_gain,
    first_moment_pair_bound,
    kac_normalized_factor,
    pair_count,
    per_particle,
    power_law_budget_factor,
)


def test_pair_count_and_guards():
    assert pair_count(1) == 0
    assert pair_count(4) == 6
    with pytest.raises(ValueError):
        pair_count(0)


def test_first_moment_bound_identity():
    budget = 123.456
    o0 = 0.5
    assert first_moment_pair_bound(budget, o0) == 8.0 * o0**2 * budget


def test_kac_per_particle_budget_is_asymptotically_constant():
    n1, n2 = 1_000, 1_000_000
    b1 = per_particle(all_to_all_pair_budget(n1, 1.0, 1.0), n1)
    b2 = per_particle(all_to_all_pair_budget(n2, 1.0, 1.0), n2)
    assert abs(b2 / b1 - 1.0) < 2e-3


@pytest.mark.parametrize("kappa", [0.0, 0.5, 1.0])
def test_response_and_budget_per_particle_gains_match(kappa):
    n1, n2 = 1_000, 1_000_000
    b1 = all_to_all_pair_budget(n1, 2.0, kappa)
    b2 = all_to_all_pair_budget(n2, 2.0, kappa)
    m1 = first_moment_pair_bound(b1, 0.5)
    m2 = first_moment_pair_bound(b2, 0.5)
    budget_gain = per_particle(b2, n2) / per_particle(b1, n1)
    response_gain = per_particle(m2, n2) / per_particle(m1, n1)
    assert abs(response_gain / budget_gain - 1.0) <= 1e-12
    assert abs(budget_gain / finite_n_per_particle_gain(n1, n2, kappa) - 1.0) <= 1e-12


def test_power_law_scaling_and_kac_diagnostic():
    n = 1e6
    assert power_law_budget_factor(n, 0.0, 3.0) == n
    assert math.isclose(power_law_budget_factor(n, 3.0, 3.0), math.log(n))
    assert power_law_budget_factor(n, 4.0, 3.0) == 1.0
    assert kac_normalized_factor(n, 1.0, 3.0) == 1.0
