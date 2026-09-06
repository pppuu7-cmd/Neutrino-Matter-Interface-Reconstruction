"""Measured-GT dominant 82Se solar-neutrino capture response.

Primary physics input: Frekers et al., Phys. Rev. C 94, 014614 (2016),
high-resolution 82Se(3He,t)82Br charge-exchange measurement.

The dominant low-energy transition is the 75-keV 1+ state in 82Br with
B(GT)=0.338(31). The 82Se-82Br ground-state mass difference is about
96.6 keV, giving a neutrino-capture threshold near 171.6 keV for this state.

This module starts with the allowed-GT + point-Coulomb approximation. It is
not promoted to full 82Se response authority until the published source-
averaged cross sections (especially pp = 76.2e-46 cm^2) are reproduced.
"""
from __future__ import annotations

import math

GF_GEV_M2 = 1.1663787e-5
VUD = 0.97420
G_A = 1.2754
ALPHA = 1.0 / 137.035999084
M_E_MEV = 0.510998950
GEV_M2_TO_CM2 = 0.389379338e-27

SE82_GS_MASS_DIFFERENCE_MEV = 0.0966
SE82_DOMINANT_EXCITATION_MEV = 0.0750
SE82_DOMINANT_THRESHOLD_MEV = SE82_GS_MASS_DIFFERENCE_MEV + SE82_DOMINANT_EXCITATION_MEV
SE82_DOMINANT_BGT = 0.338
SE82_DAUGHTER_Z = 35


def point_coulomb_fermi_factor(z_daughter: int, electron_total_energy_mev: float, electron_momentum_mev: float) -> float:
    """Attractive point-Coulomb Fermi/Sommerfeld factor for emitted electrons."""
    if z_daughter <= 0:
        raise ValueError("z_daughter must be positive")
    if electron_total_energy_mev <= M_E_MEV or electron_momentum_mev <= 0.0:
        raise ValueError("electron must have positive kinetic energy")
    eta = ALPHA * z_daughter * electron_total_energy_mev / electron_momentum_mev
    x = 2.0 * math.pi * eta
    return x / (1.0 - math.exp(-x))


def se82_dominant_sigma_cm2(
    enu_mev: float,
    *,
    threshold_mev: float = SE82_DOMINANT_THRESHOLD_MEV,
    bgt: float = SE82_DOMINANT_BGT,
    z_daughter: int = SE82_DAUGHTER_Z,
    g_a: float = G_A,
) -> float:
    """Allowed-GT cross section to the dominant 75-keV 1+ state."""
    if enu_mev < 0.0:
        raise ValueError("neutrino energy must be non-negative")
    if threshold_mev <= 0.0 or bgt <= 0.0 or g_a <= 0.0:
        raise ValueError("threshold, B(GT), and g_A must be positive")
    if enu_mev <= threshold_mev:
        return 0.0
    kinetic_mev = enu_mev - threshold_mev
    total_mev = M_E_MEV + kinetic_mev
    momentum_mev = math.sqrt(total_mev * total_mev - M_E_MEV * M_E_MEV)
    fermi = point_coulomb_fermi_factor(z_daughter, total_mev, momentum_mev)
    p_gev = momentum_mev * 1.0e-3
    e_gev = total_mev * 1.0e-3
    prefactor = GF_GEV_M2**2 * VUD**2 / math.pi
    return prefactor * (g_a**2 * bgt) * p_gev * e_gev * fermi * GEV_M2_TO_CM2
