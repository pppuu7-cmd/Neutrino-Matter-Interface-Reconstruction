import pytest

from nmir.cevns_mass_optimum import (
    analytic_a_star,
    benchmark_row,
    exact_closure_a,
    fixed_mass_objective,
)

BENCHMARKS = [
    (0.86258, 40.0),
    (0.86258, 20.0),
    (0.86258, 10.0),
    (0.420, 10.0),
    (1.44, 40.0),
]


def test_frozen_analytic_reference_values():
    expected = [13.3127387221, 26.6254774441, 53.2509548883, 12.6248786433, 37.1016841762]
    for (energy, threshold), ref in zip(BENCHMARKS, expected):
        assert analytic_a_star(energy, threshold) == pytest.approx(ref, rel=1e-10)


@pytest.mark.parametrize("energy,threshold", BENCHMARKS)
def test_exact_numeric_optimum_matches_analytic_envelope(energy, threshold):
    row = benchmark_row(energy, threshold)
    assert abs(row["relative_a_star_residual"]) < 0.01
    assert abs(row["exact_tmax_over_threshold_at_numeric_optimum"] / 3.0 - 1.0) < 0.01


@pytest.mark.parametrize("energy,threshold", BENCHMARKS)
def test_objective_is_positive_below_and_zero_at_closure(energy, threshold):
    closure = exact_closure_a(energy, threshold)
    assert fixed_mass_objective(energy, threshold, closure * 0.5) > 0.0
    assert fixed_mass_objective(energy, threshold, closure) == 0.0
    assert fixed_mass_objective(energy, threshold, closure * 1.01) == 0.0


def test_invalid_arguments_fail_closed():
    with pytest.raises(ValueError):
        analytic_a_star(0.0, 10.0)
    with pytest.raises(ValueError):
        analytic_a_star(1.0, 0.0)
