import math

import pytest

from nmir.b_minus_l_contour_convert import (
    G_PER_SQRT_ALPHA,
    alpha_tilde_from_g_bl,
    convert_yukawa_point,
    g_bl_from_alpha_tilde,
    mass_ev_from_range_m,
    range_m_from_mass_ev,
)


def test_mass_range_roundtrip():
    m_ev = 1.0e-6
    lam = range_m_from_mass_ev(m_ev)
    assert lam == pytest.approx(0.1973269804, rel=1e-12)
    assert mass_ev_from_range_m(lam) == pytest.approx(m_ev, rel=1e-12)


def test_wagner_alpha_coupling_roundtrip():
    alpha = 3.559085604069644e-6
    g = g_bl_from_alpha_tilde(alpha)
    assert g == pytest.approx(5.10309948748322e-22, rel=5e-6)
    assert alpha_tilde_from_g_bl(g) == pytest.approx(alpha, rel=1e-12)


def test_secondary_regression_locator_only():
    # AxionLimits EotwashEP point used ONLY as a numerical regression target,
    # never as primary scientific authority for iteration 0072.
    m_ev = 1.073903817077052e-6
    g_bl = 5.10309948748322e-22
    lam = range_m_from_mass_ev(m_ev)
    alpha = alpha_tilde_from_g_bl(g_bl)
    m2, g2 = convert_yukawa_point(lam, alpha)
    assert m2 == pytest.approx(m_ev, rel=1e-12)
    assert g2 == pytest.approx(g_bl, rel=1e-12)


def test_conversion_constant():
    assert G_PER_SQRT_ALPHA == pytest.approx(2.70463357586823e-19, rel=1e-12)


def test_invalid_ranges_rejected():
    with pytest.raises(ValueError):
        range_m_from_mass_ev(0.0)
    with pytest.raises(ValueError):
        mass_ev_from_range_m(-1.0)
