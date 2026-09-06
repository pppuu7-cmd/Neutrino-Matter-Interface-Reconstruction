import math

import pytest

from nmir.passive_allowed_bound import (
    DEFAULT_OMITTED_PHYSICS_STRESS,
    allowed_sigma_operator_norm_bound_cm2,
    allowed_strength_operator_norm_bound,
    known_nuclei_allowed_stress_envelope,
    passive_allowed_power_bound_w_per_kg,
    point_coulomb_pef_ratio_bound,
)


def test_point_coulomb_phase_bound_is_monotone_and_above_one():
    assert point_coulomb_pef_ratio_bound(1) > 1.0
    assert point_coulomb_pef_ratio_bound(119) > point_coulomb_pef_ratio_bound(1)


def test_strength_bound_scales_as_a_squared():
    s7 = allowed_strength_operator_norm_bound(7)
    s14 = allowed_strength_operator_norm_bound(14)
    assert math.isclose(s14 / s7, 4.0, rel_tol=1e-14)


def test_sigma_bound_monotone_in_energy_a_and_z():
    base = allowed_sigma_operator_norm_bound_cm2(5.0, 7, 4)
    assert allowed_sigma_operator_norm_bound_cm2(10.0, 7, 4) > base
    assert allowed_sigma_operator_norm_bound_cm2(5.0, 14, 4) > base
    assert allowed_sigma_operator_norm_bound_cm2(5.0, 7, 10) > base


def test_power_bound_exceeds_all_current_validated_target_powers():
    # Current authoritative GS98 leaders from research/sm_power_ledger.md.
    current = [
        1.06589117436e-21,  # Li7
        2.94006655e-22,     # Se82
        1.03091848e-22,     # Ga71
        5.91482818e-23,     # Cl37
    ]
    envelope = known_nuclei_allowed_stress_envelope()
    analytic = float(envelope["analytic_allowed_bound_w_per_kg"])
    assert all(analytic > value for value in current)


def test_preregistered_stress_classification_is_fail_closed():
    envelope = known_nuclei_allowed_stress_envelope()
    analytic = float(envelope["analytic_allowed_bound_w_per_kg"])
    stressed = float(envelope["stressed_bound_w_per_kg"])
    assert math.isclose(stressed, analytic * DEFAULT_OMITTED_PHYSICS_STRESS, rel_tol=1e-15)
    if stressed < 1.0e-3:
        assert envelope["classification"] == "STRONG_NEGATIVE_SCOPED"
    elif analytic < 1.0:
        assert envelope["classification"] == "NEGATIVE_SCOPED"
    else:
        assert envelope["classification"] == "NO_NEGATIVE_BOUND"


def test_input_guards():
    with pytest.raises(ValueError):
        point_coulomb_pef_ratio_bound(0)
    with pytest.raises(ValueError):
        allowed_strength_operator_norm_bound(0)
    with pytest.raises(ValueError):
        allowed_sigma_operator_norm_bound_cm2(-1.0, 7, 4)
    with pytest.raises(ValueError):
        passive_allowed_power_bound_w_per_kg(
            a_mass=7,
            z_daughter=4,
            enu_max_mev=20.0,
            neutrino_energy_flux_w_m2=-1.0,
        )
