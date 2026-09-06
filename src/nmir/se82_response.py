"""Measured-GT dominant 82Se solar-neutrino capture response.

Primary physics input: Frekers et al., Phys. Rev. C 94, 014614 (2016),
high-resolution 82Se(3He,t)82Br charge-exchange measurement.

The dominant low-energy transition is the 75-keV 1+ state in 82Br with
B(GT)=0.338(31). The 82Se-82Br ground-state mass difference is about
96.6 keV, giving a neutrino-capture threshold near 171.6 keV for this state.

Iteration 0020/0021 history:
- a simple point-Coulomb/Sommerfeld treatment underpredicted the published
  pp source-average cross section by 32.6% and is retained as a negative
  approximation result;
- the next prospective repair is the standard relativistic finite-size Fermi
  function for the emitted electron. The scientific validation tolerance is
  unchanged (15%).
"""
from __future__ import annotations

import cmath
import math

GF_GEV_M2 = 1.1663787e-5
VUD = 0.97420
G_A = 1.2754
ALPHA = 1.0 / 137.035999084
M_E_MEV = 0.510998950
GEV_M2_TO_CM2 = 0.389379338e-27
HBARC_MEV_FM = 197.3269804

SE82_A = 82
SE82_GS_MASS_DIFFERENCE_MEV = 0.0966
SE82_DOMINANT_EXCITATION_MEV = 0.0750
SE82_DOMINANT_THRESHOLD_MEV = SE82_GS_MASS_DIFFERENCE_MEV + SE82_DOMINANT_EXCITATION_MEV
SE82_DOMINANT_BGT = 0.338
SE82_DAUGHTER_Z = 35

# Lanczos coefficients, g=7, adequate for the gamma arguments used below.
_LANCZOS = (
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.32342877765313,
    -176.61502916214059,
    12.507343278686905,
    -0.13857109526572012,
    9.9843695780195716e-6,
    1.5056327351493116e-7,
)


def _complex_gamma(z: complex) -> complex:
    """Complex gamma from a compact Lanczos approximation."""
    if z.real < 0.5:
        return math.pi / (cmath.sin(math.pi * z) * _complex_gamma(1.0 - z))
    zz = z - 1.0
    x = complex(_LANCZOS[0])
    for i, coeff in enumerate(_LANCZOS[1:], start=1):
        x += coeff / (zz + i)
    t = zz + 7.5
    return math.sqrt(2.0 * math.pi) * (t ** (zz + 0.5)) * cmath.exp(-t) * x


def point_coulomb_fermi_factor(z_daughter: int, electron_total_energy_mev: float, electron_momentum_mev: float) -> float:
    """Attractive point-Coulomb Fermi/Sommerfeld factor (negative baseline)."""
    if z_daughter <= 0:
        raise ValueError("z_daughter must be positive")
    if electron_total_energy_mev <= M_E_MEV or electron_momentum_mev <= 0.0:
        raise ValueError("electron must have positive kinetic energy")
    eta = ALPHA * z_daughter * electron_total_energy_mev / electron_momentum_mev
    x = 2.0 * math.pi * eta
    return x / (1.0 - math.exp(-x))


def relativistic_finite_size_fermi_factor(
    z_daughter: int,
    mass_number: int,
    electron_total_energy_mev: float,
    electron_momentum_mev: float,
    *,
    nuclear_radius_coefficient_fm: float = 1.2,
) -> float:
    """Relativistic finite-size Fermi function F_0(Z,W).

    Uses

      F_0 = 2(1+gamma) (2 p R)^{2(gamma-1)} exp(pi y)
            |Gamma(gamma+i y)|^2 / Gamma(2 gamma + 1)^2,

    with dimensionless W=E/m_e, p=p_e/m_e, y=alpha Z W/p and
    R = r0 A^(1/3) / (hbar/(m_e c)). This is a physically motivated
    improvement over the point Sommerfeld factor, while atomic screening and
    higher-order shape/radiative corrections remain outside this first gate.
    """
    if z_daughter <= 0 or mass_number <= 0:
        raise ValueError("Z and A must be positive")
    if electron_total_energy_mev <= M_E_MEV or electron_momentum_mev <= 0.0:
        raise ValueError("electron must have positive kinetic energy")
    if nuclear_radius_coefficient_fm <= 0.0:
        raise ValueError("nuclear radius coefficient must be positive")

    az = ALPHA * z_daughter
    gamma_rel = math.sqrt(1.0 - az * az)
    w = electron_total_energy_mev / M_E_MEV
    p = electron_momentum_mev / M_E_MEV
    y = az * w / p
    nuclear_radius_fm = nuclear_radius_coefficient_fm * (mass_number ** (1.0 / 3.0))
    electron_reduced_compton_fm = HBARC_MEV_FM / M_E_MEV
    radius = nuclear_radius_fm / electron_reduced_compton_fm

    gamma_abs_sq = abs(_complex_gamma(complex(gamma_rel, y))) ** 2
    denominator = math.gamma(2.0 * gamma_rel + 1.0) ** 2
    return (
        2.0
        * (1.0 + gamma_rel)
        * ((2.0 * p * radius) ** (2.0 * (gamma_rel - 1.0)))
        * math.exp(math.pi * y)
        * gamma_abs_sq
        / denominator
    )


def _allowed_gt_sigma_cm2(
    enu_mev: float,
    *,
    threshold_mev: float,
    bgt: float,
    z_daughter: int,
    g_a: float,
    fermi_model: str,
) -> float:
    if enu_mev < 0.0:
        raise ValueError("neutrino energy must be non-negative")
    if threshold_mev <= 0.0 or bgt <= 0.0 or g_a <= 0.0:
        raise ValueError("threshold, B(GT), and g_A must be positive")
    if enu_mev <= threshold_mev:
        return 0.0
    kinetic_mev = enu_mev - threshold_mev
    total_mev = M_E_MEV + kinetic_mev
    momentum_mev = math.sqrt(total_mev * total_mev - M_E_MEV * M_E_MEV)
    if fermi_model == "point":
        fermi = point_coulomb_fermi_factor(z_daughter, total_mev, momentum_mev)
    elif fermi_model == "relativistic_finite_size":
        fermi = relativistic_finite_size_fermi_factor(z_daughter, SE82_A, total_mev, momentum_mev)
    else:
        raise ValueError("fermi_model must be 'point' or 'relativistic_finite_size'")
    p_gev = momentum_mev * 1.0e-3
    e_gev = total_mev * 1.0e-3
    prefactor = GF_GEV_M2**2 * VUD**2 / math.pi
    return prefactor * (g_a**2 * bgt) * p_gev * e_gev * fermi * GEV_M2_TO_CM2


def se82_dominant_sigma_cm2(
    enu_mev: float,
    *,
    threshold_mev: float = SE82_DOMINANT_THRESHOLD_MEV,
    bgt: float = SE82_DOMINANT_BGT,
    z_daughter: int = SE82_DAUGHTER_Z,
    g_a: float = G_A,
    fermi_model: str = "relativistic_finite_size",
) -> float:
    """Allowed-GT cross section to the dominant 75-keV 1+ state."""
    return _allowed_gt_sigma_cm2(
        enu_mev,
        threshold_mev=threshold_mev,
        bgt=bgt,
        z_daughter=z_daughter,
        g_a=g_a,
        fermi_model=fermi_model,
    )
