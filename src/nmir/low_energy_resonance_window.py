"""Kinematic design windows for low-energy neutrino resonances.

This module does not introduce a new particle or target.  It maps source energy
onto the on-shell mass required for a hypothetical stationary-electron s-channel
state and records the distinct RIOEC atomic+nuclear resonance condition.
"""

from __future__ import annotations

import math

M_E_MEV = 0.51099895
M_W_GEV = 80.4
SOLAR_CEILING_MEV = 20.0
THERMAL_MAX_KEV = 5.0
IBD_THRESHOLD_MEV = 1.8

SOURCE_CONTROLS_MEV = {
    "thermal_10_eV": 10.0e-6,
    "thermal_1_keV": 1.0e-3,
    "pp_endpoint_0p420": 0.420,
    "Be7_0p8618": 0.8618,
    "pep_1p442": 1.442,
    "solar_ceiling_20": SOLAR_CEILING_MEV,
}


def stationary_electron_s_mev2(enu_mev: float) -> float:
    if enu_mev < 0:
        raise ValueError("enu_mev must be non-negative")
    return M_E_MEV**2 + 2.0 * M_E_MEV * enu_mev


def stationary_electron_resonance_mass_mev(enu_mev: float) -> float:
    return math.sqrt(stationary_electron_s_mev2(enu_mev))


def stationary_electron_resonance_energy_mev(mass_mev: float) -> float:
    if mass_mev < M_E_MEV:
        raise ValueError("s-channel mass must be at least the electron mass")
    return (mass_mev**2 - M_E_MEV**2) / (2.0 * M_E_MEV)


def glashow_calibration_pev() -> float:
    m_w_mev = M_W_GEV * 1.0e3
    return stationary_electron_resonance_energy_mev(m_w_mev) / 1.0e9


def stationary_electron_window() -> dict[str, object]:
    rows: dict[str, dict[str, float]] = {}
    for name, enu in SOURCE_CONTROLS_MEV.items():
        mass = stationary_electron_resonance_mass_mev(enu)
        rows[name] = {
            "enu_mev": enu,
            "required_mass_mev": mass,
            "mass_excess_over_electron_mev": mass - M_E_MEV,
            "mass_excess_over_electron_kev": (mass - M_E_MEV) * 1.0e3,
        }

    thermal_low_mev = 10.0e-6
    thermal_high_mev = THERMAL_MAX_KEV * 1.0e-3
    m_thermal_low = stationary_electron_resonance_mass_mev(thermal_low_mev)
    m_thermal_high = stationary_electron_resonance_mass_mev(thermal_high_mev)
    m_solar_high = stationary_electron_resonance_mass_mev(SOLAR_CEILING_MEV)

    return {
        "electron_mass_mev": M_E_MEV,
        "source_rows": rows,
        "solar_stationary_electron_mass_window_mev": [M_E_MEV, m_solar_high],
        "solar_stationary_electron_mass_excess_window_mev": [0.0, m_solar_high - M_E_MEV],
        "thermal_10eV_to_5keV_mass_window_mev": [m_thermal_low, m_thermal_high],
        "thermal_10eV_to_5keV_mass_excess_window_kev": [
            (m_thermal_low - M_E_MEV) * 1.0e3,
            (m_thermal_high - M_E_MEV) * 1.0e3,
        ],
        "glashow_calibration_pev": glashow_calibration_pev(),
        "glashow_relative_error_to_6p3": abs(glashow_calibration_pev() / 6.3 - 1.0),
        "scope": (
            "Pure stationary-electron s-channel kinematics. This does not assert that a state "
            "exists or has the required quantum numbers/coupling; BSM remains locked."
        ),
    }


def rioec_resonance_energy_mev(q_ec_mev: float, excitation_mev: float, binding_mev: float) -> float:
    """Primary-paper RIOEC condition E_R=-Q_epsilon+E_x+E_b."""
    return -q_ec_mev + excitation_mev + binding_mev


def rioec_relative_tuning(
    q_ec_mev: float,
    excitation_mev: float,
    binding_mev: float,
) -> dict[str, float | bool]:
    er = rioec_resonance_energy_mev(q_ec_mev, excitation_mev, binding_mev)
    scale = max(abs(q_ec_mev), abs(excitation_mev), abs(binding_mev), 1.0)
    return {
        "resonance_energy_mev": er,
        "resonance_energy_kev": er * 1.0e3,
        "representative_scale_mev": scale,
        "relative_cancellation": abs(er) / scale,
        "in_thermal_below_5keV_window": 0.0 < er <= THERMAL_MAX_KEV * 1.0e-3,
        "below_ibd_threshold": 0.0 < er < IBD_THRESHOLD_MEV,
    }


def low_energy_resonance_design_gate() -> dict[str, object]:
    stationary = stationary_electron_window()
    # Generic cancellation-scale examples only; they are not target candidates.
    generic_relative_requirements = {
        "1_keV_resonance_vs_1_MeV_terms": 1.0e-3,
        "5_keV_resonance_vs_1_MeV_terms": 5.0e-3,
        "10_eV_resonance_vs_1_MeV_terms": 1.0e-5,
    }
    return {
        "stationary_electron_s_channel": stationary,
        "rioec": {
            "condition": "E_R=-Q_epsilon+E_x+E_b",
            "thermal_solar_design_window_kev": [0.0, THERMAL_MAX_KEV],
            "generic_below_ibd_design_window_mev": [0.0, IBD_THRESHOLD_MEV],
            "generic_relative_cancellation_requirements": generic_relative_requirements,
            "scope": (
                "Kinematic tuning requirement only. Candidate-specific rates require evaluated entrance "
                "strength B0 and primary thermal-solar anti-nu_e spectral density at E_R."
            ),
        },
        "classification": "G8_LOW_ENERGY_RESONANCE_WINDOW_PASS",
        "bsM_status": "LOCKED",
    }
