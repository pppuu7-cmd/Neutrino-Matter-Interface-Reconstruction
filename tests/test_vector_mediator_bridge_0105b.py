import math

import pytest

from nmir.vector_mediator_bridge_0105b import (
    cevns_momentum_transfer_from_kev_gev,
    cevns_momentum_transfer_gev,
    finite_q_coefficient_gev2,
    finite_q_ratio,
    forward_coefficient_gev2,
    mediator_mass_from_ratio_gev,
    nuclear_vector_charge,
)


def test_q_zero_is_exact_forward_limit():
    assert finite_q_ratio(0.03, 0.0) == 1.0
    assert finite_q_coefficient_gev2(2.5e-7, 0.03, 0.0) == forward_coefficient_gev2(2.5e-7, 0.03)


def test_finite_q_ratio_bounds_and_contact_light_limits():
    assert 0.0 < finite_q_ratio(0.03, 0.05) < 1.0
    assert math.isclose(finite_q_ratio(1.0e3, 1.0e-3), 1.0, rel_tol=0.0, abs_tol=2e-12)
    assert finite_q_ratio(1.0e-6, 1.0) < 1.1e-12


def test_ratio_inverse_roundtrip_over_six_decades():
    q = 0.04
    for mass_over_q in (1e-3, 1e-2, 1e-1, 1.0, 1e1, 1e2, 1e3):
        mass = mass_over_q * q
        ratio = finite_q_ratio(mass, q)
        recovered = mediator_mass_from_ratio_gev(ratio, q)
        assert math.isclose(recovered, mass, rel_tol=5e-10)


def test_inverse_rejects_singular_or_unphysical_domain():
    for ratio in (-1.0, 0.0, 1.0, 2.0):
        with pytest.raises(ValueError):
            mediator_mass_from_ratio_gev(ratio, 0.04)
    with pytest.raises(ValueError):
        mediator_mass_from_ratio_gev(0.5, 0.0)


def test_mass_and_momentum_domain_guards():
    for mass in (0.0, -1.0):
        with pytest.raises(ValueError):
            finite_q_ratio(mass, 0.01)
        with pytest.raises(ValueError):
            forward_coefficient_gev2(1.0, mass)
    with pytest.raises(ValueError):
        finite_q_ratio(0.01, -1.0)
    with pytest.raises(ValueError):
        finite_q_coefficient_gev2(1.0, 0.01, -1.0)


def test_finite_q_coefficient_sign_and_magnitude():
    for gprod in (3.0e-8, -3.0e-8):
        c0 = forward_coefficient_gev2(gprod, 0.02)
        cq = finite_q_coefficient_gev2(gprod, 0.02, 0.05)
        assert math.copysign(1.0, cq) == math.copysign(1.0, gprod)
        assert abs(cq) <= abs(c0)


def test_ratio_is_coupling_independent_identity():
    mass, q = 0.025, 0.04
    expected = finite_q_ratio(mass, q)
    for gprod in (1e-12, 1e-7, -1e-9):
        c0 = forward_coefficient_gev2(gprod, mass)
        cq = finite_q_coefficient_gev2(gprod, mass, q)
        assert math.isclose(cq / c0, expected, rel_tol=2e-15)


def test_cevns_momentum_transfer_scaling_and_units():
    mass = 39.9623831237 * 0.93149410242
    assert cevns_momentum_transfer_gev(mass, 0.0) == 0.0
    q10 = cevns_momentum_transfer_from_kev_gev(mass, 10.0)
    q40 = cevns_momentum_transfer_from_kev_gev(mass, 40.0)
    assert math.isclose(q40 / q10, 2.0, rel_tol=2e-15)
    assert 0.02 < q10 < 0.04
    assert 0.04 < q40 < 0.07


def test_nuclear_vector_charge_exact_limits():
    assert nuclear_vector_charge(18, 0, 2.0, 7.0) == 36.0
    assert nuclear_vector_charge(0, 22, 2.0, 7.0) == 154.0
    assert nuclear_vector_charge(18, 22, 1.0, 1.0) == 40.0
    assert nuclear_vector_charge(18, 22, 1.0, -1.0) == -4.0
