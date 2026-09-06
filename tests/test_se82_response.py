import pytest

from nmir.se82_response import (
    SE82_DOMINANT_BGT,
    SE82_DOMINANT_THRESHOLD_MEV,
    se82_dominant_sigma_cm2,
)


def test_se82_dominant_threshold():
    assert SE82_DOMINANT_THRESHOLD_MEV == pytest.approx(0.1716, rel=1e-12)
    assert se82_dominant_sigma_cm2(0.0) == 0.0
    assert se82_dominant_sigma_cm2(SE82_DOMINANT_THRESHOLD_MEV) == 0.0


def test_se82_response_positive_and_increasing_over_low_solar_range():
    vals = [se82_dominant_sigma_cm2(e) for e in (0.2, 0.3, 0.42, 0.862, 1.442)]
    assert all(v > 0.0 for v in vals)
    assert all(b > a for a, b in zip(vals, vals[1:]))


def test_se82_bgt_scaling_is_linear():
    e = 0.3
    s0 = se82_dominant_sigma_cm2(e)
    s1 = se82_dominant_sigma_cm2(e, bgt=2.0 * SE82_DOMINANT_BGT)
    assert s1 / s0 == pytest.approx(2.0, rel=1e-12)
