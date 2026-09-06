"""Measured beta-decay ft -> low-energy neutrino capture benchmarks.

The normalization follows Cocco, Mangano & Messina (2007), Eq. (19), with
explicit restoration of hbar and c.  Electron momentum and total energy are
in MeV; ft is in seconds; the result is sigma*(v_nu/c) in cm^2.
"""

from __future__ import annotations

import math

ALPHA = 1.0 / 137.035999084
M_E_MEV = 0.51099895
HBAR_MEV_S = 6.582119569e-22
HBARC_MEV_CM = 1.973269804e-11


def point_fermi_function(z_daughter: int, electron_total_energy_mev: float) -> float:
    """Simple point-Coulomb beta-minus Fermi function.

    F = 2*pi*eta/(1-exp(-2*pi*eta)), eta=alpha*Z*E/p.
    This is a transparent low-Z benchmark, not a precision finite-size/
    screening treatment.
    """
    if z_daughter <= 0:
        raise ValueError("z_daughter must be positive")
    if electron_total_energy_mev <= M_E_MEV:
        raise ValueError("electron total energy must exceed the rest mass")
    p = math.sqrt(electron_total_energy_mev**2 - M_E_MEV**2)
    eta = ALPHA * z_daughter * electron_total_energy_mev / p
    x = 2.0 * math.pi * eta
    return x / (1.0 - math.exp(-x))


def sigma_v_over_c_from_ft_cm2(
    ft_s: float,
    electron_total_energy_mev: float,
    fermi_function: float,
) -> float:
    """Return sigma_NCB*(v_nu/c) in cm^2 from measured ft.

    Starting from Eq. (19) of Cocco, Mangano & Messina (2007),
        sigma v = 2*pi^2 ln2 * p_e E_e F / ft
    in their natural-unit convention. Restoring units gives
        sigma (v/c) [cm^2] = C_ft * p_e[MeV] E_e[MeV] F / ft[s],
    with
        C_ft = 2*pi^2 ln2 * hbar * (hbar c)^2 / m_e^5.
    """
    if ft_s <= 0:
        raise ValueError("ft_s must be positive")
    if electron_total_energy_mev <= M_E_MEV:
        raise ValueError("electron total energy must exceed the rest mass")
    if fermi_function <= 0:
        raise ValueError("fermi_function must be positive")
    p = math.sqrt(electron_total_energy_mev**2 - M_E_MEV**2)
    c_ft = (
        2.0
        * math.pi**2
        * math.log(2.0)
        * HBAR_MEV_S
        * HBARC_MEV_CM**2
        / M_E_MEV**5
    )
    return c_ft * p * electron_total_energy_mev * fermi_function / ft_s


def tritium_low_energy_reference_cm2() -> float:
    """Approximate H-3 low-p_nu capture benchmark from evaluated log(ft).

    Inputs:
      Q_beta = 18.5906 keV (ENSDF evaluation),
      log10(ft/s) = 3.0524,
      daughter charge Z=2.

    The simple point-Coulomb Fermi function reproduces the published
    7.84e-45 cm^2 result at the ~1% level; precision work must use the same
    finite-size/screening F(Z,E) convention as the source publication.
    """
    q_mev = 18.5906e-3
    e_total = M_E_MEV + q_mev
    ft_s = 10.0**3.0524
    f = point_fermi_function(2, e_total)
    return sigma_v_over_c_from_ft_cm2(ft_s, e_total, f)
