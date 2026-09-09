import math

import pytest

from nmir.composition_range_identifiability_0105d import (
    composition_determinant,
    normalized_scattering_to_forward_ratio,
    recover_equal_q_parameters,
    recover_mass_from_target_ratio_equal_q_gev,
    recover_rho_from_two_targets_equal_q,
)

AR40 = (18, 22)
CS133 = (55, 78)
I127 = (53, 74)
MEDIUM = (1.0, 1.2)


def forward_ratios(rho, mass, q, target1=AR40, target2=CS133):
    yp, yn = MEDIUM
    r1 = normalized_scattering_to_forward_ratio(rho, mass, q, *target1, yp, yn)
    r2 = normalized_scattering_to_forward_ratio(rho, mass, q, *target2, yp, yn)
    return r1, r2


def test_real_composition_controls_are_nonparallel():
    assert composition_determinant(*AR40, *CS133) == 194
    assert composition_determinant(*AR40, *I127) == 166


def test_equal_q_roundtrip_signed_rho_values():
    q = 0.04
    mass = 0.03
    for rho in (-0.5, -0.1, 0.0, 0.7, 2.0):
        r1, r2 = forward_ratios(rho, mass, q)
        recovered = recover_equal_q_parameters(r1, r2, q, *AR40, *CS133, *MEDIUM)
        assert math.isclose(recovered.rho_gp_over_gn, rho, rel_tol=2e-12, abs_tol=2e-12)
        assert math.isclose(recovered.mediator_mass_gev, mass, rel_tol=2e-12)


def test_mass_roundtrip_spans_four_decades_for_both_real_target_pairs():
    rho = 0.35
    q = 0.04
    for target2 in (CS133, I127):
        for mass_over_q in (1e-2, 1e-1, 1.0, 1e1, 1e2):
            mass = mass_over_q * q
            # Generate and invert the same explicitly named target pair.  This
            # prevents a silent fixture mismatch from masquerading as a
            # light-mediator conditioning failure.
            r1, r2 = forward_ratios(rho, mass, q, target1=AR40, target2=target2)
            recovered = recover_equal_q_parameters(r1, r2, q, *AR40, *target2, *MEDIUM)
            assert math.isclose(recovered.rho_gp_over_gn, rho, rel_tol=2e-11, abs_tol=2e-11)
            assert math.isclose(recovered.mediator_mass_gev, mass, rel_tol=2e-9)


def test_proportional_targets_fail_rho_identification():
    # (Z,N)=(2,4) and (3,6) are exactly parallel.
    with pytest.raises(ValueError):
        recover_rho_from_two_targets_equal_q(1.0, 2.0, 2, 4, 3, 6)


def test_mass_inversion_requires_nonzero_finite_q():
    with pytest.raises(ValueError):
        recover_mass_from_target_ratio_equal_q_gev(1.0, 0.5, 0.0, *AR40, *MEDIUM)
    with pytest.raises(ValueError):
        recover_mass_from_target_ratio_equal_q_gev(1.0, 0.5, -0.01, *AR40, *MEDIUM)


def test_unphysical_finite_q_factor_fails_closed():
    rho = 0.4
    yp, yn = MEDIUM
    z, n = AR40
    a_medium = yp * rho + yn
    a_target = z * rho + n
    for f in (0.0, -0.2, 1.0, 1.2):
        ratio = f * a_target / a_medium
        with pytest.raises(ValueError):
            recover_mass_from_target_ratio_equal_q_gev(ratio, rho, 0.04, z, n, yp, yn)


def test_swapping_target_order_preserves_solution():
    rho, mass, q = -0.25, 0.06, 0.035
    r_ar, r_cs = forward_ratios(rho, mass, q)
    a = recover_equal_q_parameters(r_ar, r_cs, q, *AR40, *CS133, *MEDIUM)
    b = recover_equal_q_parameters(r_cs, r_ar, q, *CS133, *AR40, *MEDIUM)
    assert math.isclose(a.rho_gp_over_gn, b.rho_gp_over_gn, rel_tol=1e-12, abs_tol=1e-12)
    assert math.isclose(a.mediator_mass_gev, b.mediator_mass_gev, rel_tol=1e-12)


def test_common_unknown_scale_preserves_composition_but_not_mass():
    rho, mass, q = 0.6, 0.05, 0.04
    r1, r2 = forward_ratios(rho, mass, q)
    recovered_rho = recover_rho_from_two_targets_equal_q(r1, r2, *AR40, *CS133)
    scaled_rho = recover_rho_from_two_targets_equal_q(0.5 * r1, 0.5 * r2, *AR40, *CS133)
    assert math.isclose(recovered_rho, scaled_rho, rel_tol=1e-13)

    true_mass, _ = recover_mass_from_target_ratio_equal_q_gev(r1, rho, q, *AR40, *MEDIUM)
    scaled_mass, _ = recover_mass_from_target_ratio_equal_q_gev(0.5 * r1, rho, q, *AR40, *MEDIUM)
    assert math.isclose(true_mass, mass, rel_tol=1e-12)
    assert not math.isclose(scaled_mass, mass, rel_tol=1e-3)


def test_forward_medium_charge_zero_is_singular():
    # MEDIUM=(1,1.2) vanishes at rho=-1.2.
    with pytest.raises(ValueError):
        normalized_scattering_to_forward_ratio(-1.2, 0.03, 0.04, *AR40, *MEDIUM)
