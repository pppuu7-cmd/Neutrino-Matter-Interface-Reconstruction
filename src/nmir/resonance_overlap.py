"""G8 isolated-resonance integrated-strength and source-overlap guards.

The central result is deliberately simple: an arbitrarily high Breit-Wigner
peak does not imply an arbitrarily large flux-averaged reaction rate.  For a
genuine isolated resonance, its energy-integrated cross section is controlled
by the entrance partial width.

All functions here use a consistent abstract energy unit.  If k, E and widths
are supplied in MeV, sigma has MeV^-2 and its energy integral MeV^-1.  Unit
conversion is intentionally kept outside this formal gate.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Sequence


def _validate_resonance(
    *,
    k_res: float,
    statistical_factor: float,
    gamma_in: float,
    gamma_out: float,
    gamma_total: float,
) -> None:
    if k_res <= 0:
        raise ValueError("k_res must be positive")
    if statistical_factor <= 0:
        raise ValueError("statistical_factor must be positive")
    if gamma_in <= 0 or gamma_out <= 0 or gamma_total <= 0:
        raise ValueError("all widths must be positive")
    if gamma_in > gamma_total:
        raise ValueError("gamma_in cannot exceed gamma_total")
    if gamma_out > gamma_total:
        raise ValueError("gamma_out cannot exceed gamma_total")


def breit_wigner_sigma(
    energy: float,
    *,
    e_res: float,
    k_res: float,
    statistical_factor: float,
    gamma_in: float,
    gamma_out: float,
    gamma_total: float,
) -> float:
    """Single-level Breit-Wigner cross section in the frozen G8 convention."""
    if e_res <= 0 or energy < 0:
        raise ValueError("energies must be positive/non-negative")
    _validate_resonance(
        k_res=k_res,
        statistical_factor=statistical_factor,
        gamma_in=gamma_in,
        gamma_out=gamma_out,
        gamma_total=gamma_total,
    )
    denominator = (energy - e_res) ** 2 + (0.5 * gamma_total) ** 2
    return (
        math.pi
        / (k_res * k_res)
        * statistical_factor
        * gamma_in
        * gamma_out
        / denominator
    )


def breit_wigner_peak(
    *,
    k_res: float,
    statistical_factor: float,
    gamma_in: float,
    gamma_out: float,
    gamma_total: float,
) -> float:
    """Exact peak cross section at E=Er in the frozen convention."""
    _validate_resonance(
        k_res=k_res,
        statistical_factor=statistical_factor,
        gamma_in=gamma_in,
        gamma_out=gamma_out,
        gamma_total=gamma_total,
    )
    return (
        4.0
        * math.pi
        / (k_res * k_res)
        * statistical_factor
        * gamma_in
        * gamma_out
        / (gamma_total * gamma_total)
    )


def breit_wigner_area(
    *,
    k_res: float,
    statistical_factor: float,
    gamma_in: float,
    gamma_out: float,
    gamma_total: float,
) -> float:
    """Analytic integral of sigma(E)dE over an isolated narrow resonance."""
    _validate_resonance(
        k_res=k_res,
        statistical_factor=statistical_factor,
        gamma_in=gamma_in,
        gamma_out=gamma_out,
        gamma_total=gamma_total,
    )
    return (
        2.0
        * math.pi**2
        / (k_res * k_res)
        * statistical_factor
        * gamma_in
        * gamma_out
        / gamma_total
    )


def entrance_width_area_bound(
    *,
    k_res: float,
    statistical_factor: float,
    gamma_in: float,
) -> float:
    """Width-independent G8 area bound using Gamma_out/Gamma <= 1."""
    if k_res <= 0 or statistical_factor <= 0 or gamma_in <= 0:
        raise ValueError("k_res, statistical_factor and gamma_in must be positive")
    return 2.0 * math.pi**2 / (k_res * k_res) * statistical_factor * gamma_in


def dimensionless_numeric_area(
    *,
    k_res: float,
    statistical_factor: float,
    gamma_in: float,
    gamma_out: float,
    gamma_total: float,
    t_max: float = 1.0e4,
    steps: int = 200_000,
) -> float:
    """Numerically integrate in t=2(E-Er)/Gamma without tiny-width cancellation.

    The finite t-domain omits Lorentzian tails; t_max=1e4 leaves a relative
    tail fraction ~2/(pi*t_max)=6.4e-5, inside the preregistered 1e-4 test.
    """
    _validate_resonance(
        k_res=k_res,
        statistical_factor=statistical_factor,
        gamma_in=gamma_in,
        gamma_out=gamma_out,
        gamma_total=gamma_total,
    )
    if t_max <= 0 or steps < 2:
        raise ValueError("t_max must be positive and steps >= 2")
    h = 2.0 * t_max / steps
    prefactor = (
        2.0
        * math.pi
        / (k_res * k_res)
        * statistical_factor
        * gamma_in
        * gamma_out
        / gamma_total
    )
    total = 0.5 / (1.0 + t_max * t_max) + 0.5 / (1.0 + t_max * t_max)
    for i in range(1, steps):
        t = -t_max + i * h
        total += 1.0 / (1.0 + t * t)
    return prefactor * h * total


def gaussian_profile(energy: float, *, center: float, sigma: float) -> float:
    """Normalized Gaussian source energy PDF."""
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    return math.exp(-0.5 * ((energy - center) / sigma) ** 2) / (math.sqrt(2.0 * math.pi) * sigma)


def lorentzian_profile(energy: float, *, center: float, half_width: float) -> float:
    """Normalized Lorentzian source energy PDF with HWHM=half_width."""
    if half_width <= 0:
        raise ValueError("half_width must be positive")
    return half_width / (math.pi * ((energy - center) ** 2 + half_width * half_width))


def profile_supremum_bound(area: float, profile_max: float) -> float:
    """Return ||rho||_infinity * integral(sigma dE)."""
    if area < 0 or profile_max < 0:
        raise ValueError("area and profile_max must be non-negative")
    return area * profile_max


def validate_sampled_profile(energies: Sequence[float], values: Sequence[float]) -> None:
    """Fail closed on negative/non-finite source profile samples."""
    if len(energies) != len(values) or len(energies) < 2:
        raise ValueError("profile arrays must have equal length >= 2")
    if any(not math.isfinite(x) for x in energies) or any(not math.isfinite(y) for y in values):
        raise ValueError("profile samples must be finite")
    if any(b <= a for a, b in zip(energies, energies[1:])):
        raise ValueError("profile energies must be strictly increasing")
    if any(y < 0 for y in values):
        raise ValueError("profile values must be non-negative")
    norm = sum(
        0.5 * (y0 + y1) * (x1 - x0)
        for x0, x1, y0, y1 in zip(energies, energies[1:], values, values[1:])
    )
    if norm <= 0:
        raise ValueError("profile must have positive integral")
