import math

from nmir.low_energy_resonance_window import (
    M_E_MEV,
    glashow_calibration_pev,
    low_energy_resonance_design_gate,
    rioec_relative_tuning,
    stationary_electron_resonance_energy_mev,
    stationary_electron_resonance_mass_mev,
)


def test_stationary_electron_inverse_map():
    for enu in (1.0e-5, 1.0e-3, 0.420, 0.8618, 1.442, 20.0):
        mass = stationary_electron_resonance_mass_mev(enu)
        back = stationary_electron_resonance_energy_mev(mass)
        assert math.isclose(back, enu, rel_tol=1e-12, abs_tol=1e-15)


def test_glashow_calibration():
    assert abs(glashow_calibration_pev() / 6.3 - 1.0) < 0.02


def test_solar_window_is_low_mev_mass_window():
    out = low_energy_resonance_design_gate()["stationary_electron_s_channel"]
    low, high = out["solar_stationary_electron_mass_window_mev"]
    assert math.isclose(low, M_E_MEV, rel_tol=0, abs_tol=0)
    assert 4.5 < high < 4.6


def test_thermal_window_is_only_ev_to_kev_above_electron_mass():
    out = low_energy_resonance_design_gate()["stationary_electron_s_channel"]
    low, high = out["thermal_10eV_to_5keV_mass_excess_window_kev"]
    assert 0.009 < low < 0.011
    assert 4.9 < high < 5.0


def test_known_source_rows_are_reproduced():
    rows = low_energy_resonance_design_gate()["stationary_electron_s_channel"]["source_rows"]
    assert math.isclose(rows["Be7_0p8618"]["required_mass_mev"], 1.068586785020806, rel_tol=1e-12)
    assert math.isclose(rows["pep_1p442"]["required_mass_mev"], 1.3171335918201699, rel_tol=1e-12)
    assert math.isclose(rows["solar_ceiling_20"]["required_mass_mev"], 4.549843725547186, rel_tol=1e-12)


def test_rioec_condition_and_windows():
    # Generic synthetic tuning example: 1.000 MeV Q, 0.999 MeV excitation, 2 keV binding -> 1 keV resonance.
    row = rioec_relative_tuning(1.000, 0.999, 0.002)
    assert math.isclose(row["resonance_energy_kev"], 1.0, rel_tol=1e-12)
    assert row["in_thermal_below_5keV_window"]
    assert row["below_ibd_threshold"]
    assert math.isclose(row["relative_cancellation"], 1.0e-3, rel_tol=1e-12)


def test_gate_keeps_bsm_locked():
    out = low_energy_resonance_design_gate()
    assert out["classification"] == "G8_LOW_ENERGY_RESONANCE_WINDOW_PASS"
    assert out["bsM_status"] == "LOCKED"
