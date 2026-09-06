"""Exact CEvNS recoil/source-opening kinematics.

This module intentionally contains kinematics only. It does not infer a CEvNS
rate, cross-section enhancement, or neutrino-energy gain from detector threshold.
"""

from __future__ import annotations

from math import sqrt

U_TO_MEV = 931.49410242


def nuclear_mass_mev(atomic_mass_u: float) -> float:
    if atomic_mass_u <= 0.0:
        raise ValueError("atomic_mass_u must be positive")
    return atomic_mass_u * U_TO_MEV


def recoil_max_mev(neutrino_energy_mev: float, nuclear_mass_mev_value: float) -> float:
    if neutrino_energy_mev < 0.0:
        raise ValueError("neutrino energy must be non-negative")
    if nuclear_mass_mev_value <= 0.0:
        raise ValueError("nuclear mass must be positive")
    e = neutrino_energy_mev
    m = nuclear_mass_mev_value
    return 2.0 * e * e / (m + 2.0 * e)


def source_min_energy_mev(recoil_threshold_mev: float, nuclear_mass_mev_value: float) -> float:
    if recoil_threshold_mev < 0.0:
        raise ValueError("recoil threshold must be non-negative")
    if nuclear_mass_mev_value <= 0.0:
        raise ValueError("nuclear mass must be positive")
    t = recoil_threshold_mev
    m = nuclear_mass_mev_value
    return 0.5 * (t + sqrt(t * t + 2.0 * m * t))


def line_is_open(neutrino_energy_mev: float, recoil_threshold_mev: float, nuclear_mass_mev_value: float) -> bool:
    return recoil_threshold_mev <= recoil_max_mev(neutrino_energy_mev, nuclear_mass_mev_value)


def continuum_is_open(endpoint_mev: float, recoil_threshold_mev: float, nuclear_mass_mev_value: float) -> bool:
    if endpoint_mev < 0.0:
        raise ValueError("endpoint must be non-negative")
    return endpoint_mev >= source_min_energy_mev(recoil_threshold_mev, nuclear_mass_mev_value)


AR40_ATOMIC_MASS_U = 39.9623831237
SOLAR_REFERENCE_ENERGIES_MEV = {
    "pp_endpoint": 0.420,
    "be7_line": 0.8618,
    "pep_line": 1.44,
    "b8_endpoint": 16.36,
}


def ar40_reference_map(threshold_ev: float = 40.0) -> dict[str, object]:
    if threshold_ev < 0.0:
        raise ValueError("threshold_ev must be non-negative")
    mass = nuclear_mass_mev(AR40_ATOMIC_MASS_U)
    threshold_mev = threshold_ev * 1.0e-6
    endpoints_ev = {
        name: recoil_max_mev(energy, mass) * 1.0e6
        for name, energy in SOLAR_REFERENCE_ENERGIES_MEV.items()
    }
    open_flags = {
        name: threshold_ev <= endpoint_ev
        for name, endpoint_ev in endpoints_ev.items()
    }
    return {
        "threshold_ev": threshold_ev,
        "ar40_mass_mev": mass,
        "source_min_energy_mev": source_min_energy_mev(threshold_mev, mass),
        "recoil_endpoints_ev": endpoints_ev,
        "open": open_flags,
    }
