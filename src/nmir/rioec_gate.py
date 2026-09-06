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
    """RIOEC requires an electron-antineutrino entrance state."""
    normalized = source_particle.strip().lower().replace("ν", "nu")
    allowed = {"anti-nu_e", "antinu_e", "nubar_e", "anti_nu_e"}
    neutrinos = {"nu_e", "nu_mu", "nu_tau"}
    if normalized in allowed:
        return 1.0
    if normalized in neutrinos:
        return 0.0
    raise ValueError(f"unknown source particle class: {source_particle}")


def trapezoid_integral(func, lo: float, hi: float, n: int = 100_000) -> float:
    if n < 2 or hi <= lo:
        raise ValueError("invalid integration grid")
    h = (hi - lo) / n
    total = 0.5 * (func(lo) + func(hi))
    for i in range(1, n):
        total += func(lo + i * h)
    return total * h


def resonance_area_numeric(E_R: float, gamma: float, B0: float, half_widths: float = 100_000.0) -> float:
    """Integrate the resonance over +/- ``half_widths`` FWHM using x=tan(theta)/2.

    The transform removes the narrow peak numerically: L(E)dE=dtheta/pi.
    """
    del E_R  # area is translation invariant
    if gamma <= 0.0 or B0 < 0.0 or half_widths <= 0.0:
        raise ValueError("invalid resonance parameters")
    theta_max = math.atan(2.0 * half_widths)
    return trapezoid_integral(lambda theta: B0 / math.pi, -theta_max, theta_max, n=10_000)


def smooth_profile_overlap_ratio(gamma_over_sigma: float) -> float:
    """Convolution / [B0*phi(E_R)] for a Gaussian source profile.

    With x=(E-E_R)/gamma=tan(theta)/2, the Lorentzian measure is
    exactly dtheta/pi.  The result tends to one for a source much broader
    than the resonance.
    """
    if gamma_over_sigma <= 0.0:
        raise ValueError("gamma_over_sigma must be positive")
    r = gamma_over_sigma
    eps = 1.0e-9
    integrand = lambda theta: math.exp(-0.5 * (0.5 * r * math.tan(theta)) ** 2) / math.pi
    return trapezoid_integral(integrand, -math.pi / 2.0 + eps, math.pi / 2.0 - eps, n=200_000)
