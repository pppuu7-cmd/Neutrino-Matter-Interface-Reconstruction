"""Provisional 115In solar-neutrino capture response for cross-target screening.

This module is deliberately a *screening* response, not precision authority.
It uses the experimentally motivated dominant transition

    115In(9/2+) + nu_e -> 115Sn*(612.8 keV, 7/2+) + e-

with threshold Q_nu ~= 0.114 MeV and B(GT) ~= 0.17 reported from the
115In(p,n) charge-exchange programme (Rapaport et al., PRL 54, 2325, 1985;
LENS design literature).  The charged-current allowed-GT cross section is
computed with a point-Coulomb Fermi/Sommerfeld factor.  Finite-size,
screening, radiative, recoil, forbidden and additional excited-state
corrections are intentionally not promoted into authority here.

The purpose is to decide whether 115In deserves a full matched-response
reconstruction in NMIR G3, not to publish a final 115In cross section.
"""
from __future__ import annotations

import math

GF_GEV_M2 = 1.1663787e-5
VUD = 0.97420
G_A = 1.2754
ALPHA = 1.0 / 137.035999084
M_E_MEV = 0.510998950
GEV_M2_TO_CM2 = 0.389379338e-27

IN115_THRESHOLD_MEV = 0.114
IN115_DAUGHTER_Z = 50
IN115_BGT_DOMINANT = 0.17


def point_coulomb_fermi_factor(z_daughter: int, electron_total_energy_mev: float, electron_momentum_mev: float) -> float:
    """Attractive point-Coulomb Fermi/Sommerfeld factor for emitted e-.

    F = x/(1-exp(-x)), x=2*pi*alpha*Z*E/p.
    This is a controlled screening approximation, not the final heavy-nucleus
    finite-size Fermi function.
    """
    if z_daughter <= 0:
        raise ValueError("z_daughter must be positive")
    if electron_total_energy_mev <= M_E_MEV or electron_momentum_mev <= 0.0:
        raise ValueError("electron must have positive kinetic energy")
    eta = ALPHA * z_daughter * electron_total_energy_mev / electron_momentum_mev
    x = 2.0 * math.pi * eta
    return x / (1.0 - math.exp(-x))


def in115_dominant_sigma_cm2(
    enu_mev: float,
    *,
    threshold_mev: float = IN115_THRESHOLD_MEV,
    bgt: float = IN115_BGT_DOMINANT,
    z_daughter: int = IN115_DAUGHTER_Z,
    g_a: float = G_A,
) -> float:
    """Allowed-GT screening cross section for the tagged 612.8-keV state.

    sigma = (G_F^2 |Vud|^2 / pi) g_A^2 B(GT) p_e E_e F(Z,E)

    with p_e and E_e in GeV.  ``E_e`` is total electron energy and
    T_e = E_nu - threshold.  Returns zero at/below threshold.
    """
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
