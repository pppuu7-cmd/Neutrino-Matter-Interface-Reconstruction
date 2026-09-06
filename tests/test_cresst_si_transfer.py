import math

import pytest

from nmir.cevns_solar_optimize import Target, cevns_sigma_above_threshold_cm2
from nmir.cresst_si_transfer import (
    ALL_CUTS_PLATEAU,
    E50_EV,
    SIGMA_EV,
    TRIGGER_PLATEAU,
    cevns_sigma_with_efficiency_cm2,
    component_rate_with_efficiency,
    cresst_factorized_surrogate_efficiency,
    cresst_trigger_efficiency,
    hard_step_efficiency,
)

SI28 = Target("Si28", 14, 28, 27.97692653465)


def test_published_trigger_anchors():
    assert math.isclose(cresst_trigger_efficiency(E50_EV), 0.5 * TRIGGER_PLATEAU, rel_tol=1e-14)
    assert math.isclose(cresst_trigger_efficiency(30.0), TRIGGER_PLATEAU, rel_tol=1e-12)
    assert math.isclose(cresst_factorized_surrogate_efficiency(30.0), ALL_CUTS_PLATEAU, rel_tol=1e-12)
    assert math.isclose(SIGMA_EV, 1.36, rel_tol=0.0, abs_tol=0.0)


def test_factorized_surrogate_ratio_is_frozen_plateau_ratio():
    ratio = ALL_CUTS_PLATEAU / TRIGGER_PLATEAU
    for energy in (10.0, 11.0, 14.0, 30.0):
        assert math.isclose(
            cresst_factorized_surrogate_efficiency(energy) / cresst_trigger_efficiency(energy),
            ratio,
            rel_tol=1e-14,
        )


def test_hard_step_fold_matches_existing_threshold_integral_for_monoenergetic_case():
    for e_nu in (0.862, 1.442, 5.0):
        folded = cevns_sigma_with_efficiency_cm2(e_nu, SI28, hard_step_efficiency, analysis_floor_ev=10.0)
        reference = cevns_sigma_above_threshold_cm2(e_nu, 10.0, SI28)
        assert math.isclose(folded, reference, rel_tol=1e-12, abs_tol=0.0)


def test_detector_efficiencies_reduce_cross_section():
    e_nu = 1.442
    ideal = cevns_sigma_with_efficiency_cm2(e_nu, SI28, hard_step_efficiency, analysis_floor_ev=10.0)
    trigger = cevns_sigma_with_efficiency_cm2(e_nu, SI28, cresst_trigger_efficiency, analysis_floor_ev=10.0)
    surrogate = cevns_sigma_with_efficiency_cm2(
        e_nu, SI28, cresst_factorized_surrogate_efficiency, analysis_floor_ev=10.0
    )
    assert 0.0 < surrogate < trigger < ideal
    assert trigger <= TRIGGER_PLATEAU * ideal * (1.0 + 1e-12)


def test_be7_components_map_to_common_flux_key():
    fluxes = {"Be7": 4.93e9}
    spectra = {
        "Be7_ground": [(0.861, 1.0), (0.863, 1.0)],
        "Be7_excited": [(0.383, 1.0), (0.385, 1.0)],
    }
    ground = component_rate_with_efficiency(
        "Be7_ground", SI28, hard_step_efficiency, fluxes, {}, spectra
    )
    excited = component_rate_with_efficiency(
        "Be7_excited", SI28, hard_step_efficiency, fluxes, {}, spectra
    )
    assert ground >= 0.0
    assert excited >= 0.0


def test_invalid_efficiency_inputs_fail_closed():
    with pytest.raises(ValueError):
        cresst_trigger_efficiency(-1.0)
    with pytest.raises(ValueError):
        cresst_factorized_surrogate_efficiency(-1.0)

    def bad_efficiency(_: float) -> float:
        return 1.1

    with pytest.raises(ValueError):
        cevns_sigma_with_efficiency_cm2(1.442, SI28, bad_efficiency)
