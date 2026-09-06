import math

import pytest

from nmir.higher_body_strength import (
    P_LEADING_W_PER_KG,
    R_EMPIRICAL_EXTRA,
    R_ONE_BODY,
    classify,
    required_extra_amplitude_for_power,
    stress_ladder,
    stressed_power_w_per_kg,
)


def test_zero_two_body_recovers_one_body_stress():
    expected = P_LEADING_W_PER_KG * (1.0 + R_ONE_BODY) ** 2
    assert math.isclose(stressed_power_w_per_kg(0.0), expected, rel_tol=1e-15)


def test_required_bridge_is_exact():
    r = required_extra_amplitude_for_power(1.0)
    assert math.isclose(stressed_power_w_per_kg(r), 1.0, rel_tol=1e-12)


def test_frozen_ladder_is_monotonic():
    points = stress_ladder()
    assert [p.safety_factor for p in points] == [1.0, 3.0, 10.0, 100.0, 1000.0]
    assert all(a.power_w_per_kg < b.power_w_per_kg for a, b in zip(points, points[1:]))
    assert all(math.isclose(p.r_two_body, p.safety_factor * R_EMPIRICAL_EXTRA) for p in points)


def test_preregistered_classification():
    points = {p.safety_factor: p for p in stress_ladder()}
    bridge_ratio = required_extra_amplitude_for_power(1.0) / R_EMPIRICAL_EXTRA
    assert points[100.0].power_w_per_kg < 1e-3
    assert bridge_ratio > 1e4
    assert classify() == "PASS_EMPIRICAL_STRENGTH_STRONG_NEGATIVE"


def test_invalid_inputs_fail_closed():
    with pytest.raises(ValueError):
        stressed_power_w_per_kg(-1e-6)
    with pytest.raises(ValueError):
        required_extra_amplitude_for_power(0.0)
