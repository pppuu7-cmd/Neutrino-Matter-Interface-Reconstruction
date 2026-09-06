import math

import pytest

from nmir.cresst_lee_scaling import (
    BMAX,
    M10_KG,
    accepted_lee_rate_per_kg_day,
    corrected_lee_rate_per_kg_day,
    lee_fit_rate_density,
    rejection_factor,
    surrogate_efficiency,
)


def test_published_central_fit_is_positive():
    for energy in (0.010, 0.014, 0.1, 0.3):
        assert lee_fit_rate_density(energy) > 0.0


def test_surrogate_efficiency_is_bounded_and_turns_on():
    vals = [surrogate_efficiency(e) for e in (0.010, 0.011, 0.014, 0.1)]
    assert all(0.0 < v <= 0.6591 for v in vals)
    assert all(a < b for a, b in zip(vals, vals[1:]))


def test_dense_log_quadrature_converges():
    coarse = accepted_lee_rate_per_kg_day(intervals=20_000)
    fine = accepted_lee_rate_per_kg_day(intervals=40_000)
    assert abs(fine / coarse - 1.0) <= 1e-5


def test_accepted_rate_is_below_efficiency_corrected_rate():
    corrected = corrected_lee_rate_per_kg_day(intervals=20_000)
    accepted = accepted_lee_rate_per_kg_day(intervals=20_000)
    assert 0.0 < accepted < corrected


def test_scaled_discovery_targets_need_rejection():
    accepted_per_year = accepted_lee_rate_per_kg_day(intervals=20_000) * 365.25 * M10_KG
    for bmax in BMAX.values():
        factor = rejection_factor(accepted_per_year, bmax)
        assert factor > 1.0
        assert math.isfinite(factor)


def test_invalid_inputs_fail_closed():
    with pytest.raises(ValueError):
        lee_fit_rate_density(0.0)
    with pytest.raises(ValueError):
        surrogate_efficiency(-1.0)
    with pytest.raises(ValueError):
        rejection_factor(0.0, 1.0)
    with pytest.raises(ValueError):
        rejection_factor(1.0, 0.0)
