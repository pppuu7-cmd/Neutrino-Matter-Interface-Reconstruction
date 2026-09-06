import math

import pytest

from nmir.lee_waiting_time import (
    DAYS_PER_YEAR,
    G0053,
    TAU_FAST_DAYS,
    exponential_reduction,
    exponential_time_to_reduction,
    first_integer_year_reaching,
    projected_reduction,
    projection_time_to_reduction,
    residual_gap,
)


def test_projection_matches_frozen_benchmark_points():
    assert math.isclose(projected_reduction(450.0), 10.0, rel_tol=1e-15)
    assert math.isclose(projected_reduction(900.0), 100.0, rel_tol=1e-15)


def test_projection_inversion_closes_required_gap():
    t = projection_time_to_reduction(G0053)
    assert t > 900.0
    assert math.isclose(projected_reduction(t), G0053, rel_tol=1e-13)


def test_residual_gap_decreases_monotonically():
    times = [450.0, 900.0, 3 * DAYS_PER_YEAR, 5 * DAYS_PER_YEAR, 10 * DAYS_PER_YEAR]
    gaps = [residual_gap(G0053, projected_reduction(t)) for t in times]
    assert all(a > b for a, b in zip(gaps, gaps[1:]))


def test_counterfactual_fast_component_inversion():
    t = exponential_time_to_reduction(G0053, TAU_FAST_DAYS)
    assert math.isclose(exponential_reduction(t, TAU_FAST_DAYS), G0053, rel_tol=1e-13)
    assert t > 0.0


def test_integer_year_requirement_is_consistent():
    years = first_integer_year_reaching(G0053)
    assert projected_reduction((years - 1) * DAYS_PER_YEAR) < G0053
    assert projected_reduction(years * DAYS_PER_YEAR) >= G0053


def test_invalid_inputs_fail_closed():
    with pytest.raises(ValueError):
        projected_reduction(-1.0)
    with pytest.raises(ValueError):
        exponential_reduction(1.0, 0.0)
    with pytest.raises(ValueError):
        projection_time_to_reduction(0.0)
    with pytest.raises(ValueError):
        residual_gap(0.0, 1.0)
