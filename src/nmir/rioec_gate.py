"""Source/flavor and integrated-area guards for resonant induced orbital EC (RIOEC)."""

from __future__ import annotations

import math


def lorentzian(E: float, E_R: float, gamma: float) -> float:
    """Unit-area Lorentzian, with FWHM ``gamma``."""
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    return (gamma / (2.0 * math.pi)) / ((E - E_R) ** 2 + (gamma / 2.0) ** 2)


def rioec_cross_section_density(E: float, E_R: float, gamma: float, B0: float) -> float:
    """Breit-Wigner cross-section density with integrated strength B0."""
    if B0 < 0.0:
        raise ValueError("B0 must be non-negative")
    return B0 * lorentzian(E, E_R, gamma)


def source_flavor_factor(source_particle: str) -> float:
    """RIOEC requires an electron antineutrino entrance state.

    Standard oscillations among active neutrino flavors do not convert nu to anti-nu,
    so ordinary thermonuclear solar nu_e sources have factor zero here.
    """
    normalized = source_particle.strip().lower().replace("ν", "nu")
    allowed = {"anti-nu_e", "antinu_e", "nubar_e", "anti_nu_e"}
    neutrinos = {"nu_e", "nu_mu", "nu_tau"}
    if normalized in allowed:
        return 1.0
    if normalized in neutrinos:
        return 0.0
    raise ValueError(f"unknown source particle class: {source_particle}")


def trapezoid_integral(func, lo: float, hi: float, n: int = 200_000) -> float:
    if n < 2 or hi <= lo:
        raise ValueError("invalid integration grid")
    h = (hi - lo) / n
    total = 0.5 * (func(lo) + func(hi))
    for i in range(1, n):
        total += func(lo + i * h)
    return total * h


def resonance_area_numeric(E_R: float, gamma: float, B0: float, half_widths: float = 5000.0) -> float:
    """Numerically integrate a resonance over +/- half_widths*gamma.

    A dimensionless transformed variable is used so resolution does not degrade for
    extremely narrow physical widths.
    """
    if half_widths <= 0.0:
        raise ValueError("half_widths must be positive")
    # x=(E-E_R)/gamma; sigma(E)dE = B0 * [1/(2pi)]/[x^2+1/4] dx
    integrand = lambda x: B0 * (1.0 / (2.0 * math.pi)) / (x * x + 0.25)
    return trapezoid_integral(integrand, -half_widths, half_widths, n=200_000)


def gaussian_profile(E: float, E_R: float, sigma_E: float, amplitude_at_resonance: float = 1.0) -> float:
    if sigma_E <= 0.0 or amplitude_at_resonance < 0.0:
        raise ValueError("invalid Gaussian source profile")
    return amplitude_at_resonance * math.exp(-0.5 * ((E - E_R) / sigma_E) ** 2)


def smooth_profile_overlap_ratio(gamma_over_sigma: float, half_widths: float = 100.0) -> float:
    """Return convolution / [B0*phi(E_R)] for a Gaussian source.

    The ratio is independent of E_R and B0 after scaling.  Width is expressed as
    gamma/sigma_source.
    """
    if gamma_over_sigma <= 0.0:
        raise ValueError("gamma_over_sigma must be positive")
    r = gamma_over_sigma
    integrand = lambda x: (
        (1.0 / (2.0 * math.pi)) / (x * x + 0.25)
        * math.exp(-0.5 * (r * x) ** 2)
    )
    return trapezoid_integral(integrand, -half_widths, half_widths, n=200_000)
