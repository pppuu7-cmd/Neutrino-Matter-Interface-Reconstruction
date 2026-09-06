import math

import pytest

from nmir.duality import (
    K_B_EV_PER_K,
    deposited_fraction,
    detailed_balance_ratio,
    lorentzian_peak,
    normalized_lorentzian,
)


def test_deposited_fraction_reference_scales():
    assert deposited_fraction(1.0e-3, 1.0e6) == pytest.approx(1.0e-9)
    assert deposited_fraction(1.0, 1.0e6) == pytest.approx(1.0e-6)
    assert deposited_fraction(1.0e3, 1.0e6) == pytest.approx(1.0e-3)


def test_detailed_balance_kT_point():
    t = 300.0
    omega = K_B_EV_PER_K * t
    assert detailed_balance_ratio(omega, t) == pytest.approx(math.e ** -1, rel=1e-12)


def test_lorentzian_peak_inverse_width_scaling():
    p1 = lorentzian_peak(1.0)
    p2 = lorentzian_peak(0.1)
    assert p2 / p1 == pytest.approx(10.0, rel=1e-12)


def test_lorentzian_peak_matches_formula():
    width = 2.0
    assert normalized_lorentzian(0.0, 0.0, width) == pytest.approx(1.0 / math.pi)


def test_invalid_inputs():
    with pytest.raises(ValueError):
        deposited_fraction(1.0, 0.0)
    with pytest.raises(ValueError):
        detailed_balance_ratio(1.0, 0.0)
    with pytest.raises(ValueError):
        normalized_lorentzian(0.0, 0.0, 0.0)
