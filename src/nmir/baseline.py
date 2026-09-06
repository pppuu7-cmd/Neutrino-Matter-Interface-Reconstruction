"""Trusted low-energy normalization benchmarks for NMIR.

These formulas are deliberately simple limiting expressions. They establish units,
scaling and orders of magnitude before higher-precision nuclear/material response
calculations are added.
"""

from __future__ import annotations

import math

# CODATA/PDG-style constants used only for baseline normalization.
G_F_GEV2 = 1.1663787e-5  # GeV^-2
GEV2_TO_CM2 = 0.3893793721e-27  # 1 GeV^-2 in cm^2
N_A = 6.02214076e23  # mol^-1
HBAR_C_EV_M = 1.973269804e-7  # eV m
MU_B_EV_T = 5.7883818060e-5  # eV/T


def weak_charge(z: int, n: int, sin2_theta_w: float = 0.23857) -> float:
    """Return the tree-level low-q weak charge Q_W.

    Q_W = N - (1 - 4 sin^2 theta_W) Z.
    """
    return n - (1.0 - 4.0 * sin2_theta_w) * z


def cevns_sigma_lowq_cm2(
    e_nu_mev: float,
    z: int,
    n: int,
    sin2_theta_w: float = 0.23857,
) -> float:
    """Ideal coherent low-energy CEvNS total cross section in cm^2.

    Uses sigma ~= G_F^2 Q_W^2 E_nu^2 / (4 pi), with E_nu in GeV.
    Recoil corrections, nuclear form factors and radiative corrections are omitted.
    This is a normalization benchmark, not a precision CEvNS prediction.
    """
    if e_nu_mev <= 0:
        raise ValueError("e_nu_mev must be positive")
    q_w = weak_charge(z, n, sin2_theta_w)
    e_gev = e_nu_mev * 1e-3
    sigma_gev2 = G_F_GEV2**2 * q_w**2 * e_gev**2 / (4.0 * math.pi)
    return sigma_gev2 * GEV2_TO_CM2


def number_density_cm3(density_g_cm3: float, molar_mass_g_mol: float) -> float:
    """Number density of target atoms/molecules in cm^-3."""
    if density_g_cm3 <= 0 or molar_mass_g_mol <= 0:
        raise ValueError("density and molar mass must be positive")
    return density_g_cm3 / molar_mass_g_mol * N_A


def mean_free_path_m(sigma_cm2: float, number_density_cm3_value: float) -> float:
    """Mean free path in metres for independent scatterers."""
    if sigma_cm2 <= 0 or number_density_cm3_value <= 0:
        raise ValueError("sigma and number density must be positive")
    lambda_cm = 1.0 / (sigma_cm2 * number_density_cm3_value)
    return lambda_cm / 100.0


def column_density_tau_one_g_cm2(sigma_cm2: float, molar_mass_g_mol: float) -> float:
    """Mass column density required for optical depth tau=1.

    Assumes one scattering center per atom/molecule with cross section sigma.
    """
    if sigma_cm2 <= 0 or molar_mass_g_mol <= 0:
        raise ValueError("sigma and molar mass must be positive")
    return molar_mass_g_mol / (N_A * sigma_cm2)


def magnetic_phase(mu_nu_in_mu_b: float, b_tesla: float, length_m: float) -> float:
    """Dimensionless magnetic spin-precession phase mu B L/(hbar c)."""
    if mu_nu_in_mu_b < 0 or b_tesla < 0 or length_m < 0:
        raise ValueError("magnitudes must be non-negative")
    return mu_nu_in_mu_b * MU_B_EV_T * b_tesla * length_m / HBAR_C_EV_M


def field_for_first_magnetic_maximum_t(mu_nu_in_mu_b: float, length_m: float) -> float:
    """Field B such that mu B L/(hbar c) = pi/2."""
    if mu_nu_in_mu_b <= 0 or length_m <= 0:
        raise ValueError("mu_nu and length must be positive")
    return (0.5 * math.pi * HBAR_C_EV_M) / (mu_nu_in_mu_b * MU_B_EV_T * length_m)


def minimal_dirac_magnetic_moment_mu_b(m_nu_ev: float) -> float:
    """Minimal-SM-extension Dirac neutrino magnetic moment benchmark.

    mu_nu ~= 3.2e-19 (m_nu/eV) mu_B.
    """
    if m_nu_ev < 0:
        raise ValueError("m_nu_ev must be non-negative")
    return 3.2e-19 * m_nu_ev


def xenon132_reference(e_nu_mev: float = 1.0) -> dict[str, float]:
    """Convenience benchmark for Xe-132-like target in liquid-xenon density."""
    z, n = 54, 78
    molar_mass = 131.293
    density = 2.94
    sigma = cevns_sigma_lowq_cm2(e_nu_mev, z, n)
    nd = number_density_cm3(density, molar_mass)
    return {
        "weak_charge": weak_charge(z, n),
        "sigma_cm2": sigma,
        "number_density_cm3": nd,
        "mean_free_path_m": mean_free_path_m(sigma, nd),
        "tau_one_column_g_cm2": column_density_tau_one_g_cm2(sigma, molar_mass),
    }


if __name__ == "__main__":
    for energy in (0.3, 0.862, 1.0, 5.0, 10.0, 15.0):
        ref = xenon132_reference(energy)
        print(
            f"E={energy:6.3f} MeV  "
            f"sigma={ref['sigma_cm2']:.6e} cm^2  "
            f"lambda={ref['mean_free_path_m']:.6e} m  "
            f"Sigma_tau1={ref['tau_one_column_g_cm2']:.6e} g/cm^2"
        )

    mu = minimal_dirac_magnetic_moment_mu_b(0.05)
    print(f"minimal Dirac benchmark mu_nu(m=0.05 eV)={mu:.6e} mu_B")
    print(
        "B(first maximum, L=1 m)="
        f"{field_for_first_magnetic_maximum_t(mu, 1.0):.6e} T"
    )
