"""Coefficient-independent inclusive unitarity ceiling for NMIR G3 iteration 0062.

This module deliberately computes a very loose physical ceiling.  It does not
assume EFT naturalness or any fitted short-range current coefficient.  Each
partial wave is allowed to saturate the total-cross-section unitarity limit,
and the deposited neutrino energy is set equal to the full incident energy.
"""

from __future__ import annotations

import math

HBARC_MEV_FM = 197.3269804
U_GRAM = 1.66053906660e-24
FM2_TO_CM2 = 1.0e-26
MEV_TO_J = 1.602176634e-13


def nuclear_radius_fm(a: float, r0_fm: float = 1.4) -> float:
    if a < 1.0 or r0_fm <= 0.0:
        raise ValueError("A must be >=1 and r0 positive")
    return r0_fm * a ** (1.0 / 3.0)


def wave_number_fm_inv(e_nu_mev: float) -> float:
    if e_nu_mev < 0.0:
        raise ValueError("neutrino energy must be non-negative")
    return e_nu_mev / HBARC_MEV_FM


def partial_wave_lmax(e_nu_mev: float, a: float, r0_fm: float = 1.4, mode: str = "ceil") -> int:
    if e_nu_mev < 0.0:
        raise ValueError("neutrino energy must be non-negative")
    kr = wave_number_fm_inv(e_nu_mev) * nuclear_radius_fm(a, r0_fm)
    if mode == "ceil":
        return int(math.ceil(kr))
    if mode == "floor":
        return max(0, int(math.floor(kr)))
    raise ValueError("mode must be 'ceil' or 'floor'")


def odd_sum_through_l(lmax: int) -> int:
    if lmax < 0:
        raise ValueError("lmax must be non-negative")
    return sum(2 * ell + 1 for ell in range(lmax + 1))


def sigma_unitarity_cm2(
    e_nu_mev: float,
    a: float,
    r0_fm: float = 1.4,
    mode: str = "ceil",
    coefficient: float = 4.0 * math.pi,
) -> float:
    """Conservative inclusive total-cross-section partial-wave ceiling.

    sigma <= coefficient/k^2 * sum_l(2l+1), with coefficient=4*pi frozen
    for the scientific 0062 result.  E=0 is singular and must be handled only
    inside a spectrum integral whose physical endpoint weight vanishes.
    """
    if e_nu_mev <= 0.0:
        raise ValueError("unitarity cross section requires E_nu > 0")
    if coefficient <= 0.0:
        raise ValueError("coefficient must be positive")
    k = wave_number_fm_inv(e_nu_mev)
    lmax = partial_wave_lmax(e_nu_mev, a, r0_fm, mode)
    return coefficient * odd_sum_through_l(lmax) / (k * k) * FM2_TO_CM2


def nuclei_per_kg_class(a: float) -> float:
    if a < 1.0:
        raise ValueError("A must be >=1")
    return 1000.0 / (a * U_GRAM)


def power_kernel_w_per_target(
    e_nu_mev: float,
    spectral_density_per_mev: float,
    flux_cm2_s: float,
    a: float,
    r0_fm: float = 1.4,
    mode: str = "ceil",
) -> float:
    """dP/dE per target nucleus for a normalized source spectral density.

    The E=0 endpoint is defined by the physical beta-spectrum limit only when
    the tabulated spectral density itself vanishes there.  A nonzero endpoint
    density would make this intentionally loose 1/k^2 ceiling non-integrable
    and is therefore rejected instead of silently regularized.
    """
    if spectral_density_per_mev < 0.0 or flux_cm2_s < 0.0:
        raise ValueError("spectrum and flux must be non-negative")
    if e_nu_mev == 0.0:
        if spectral_density_per_mev != 0.0:
            raise ValueError("nonzero spectral density at E=0 is incompatible with frozen unitarity ceiling")
        return 0.0
    sigma = sigma_unitarity_cm2(e_nu_mev, a, r0_fm, mode)
    return flux_cm2_s * spectral_density_per_mev * sigma * e_nu_mev * MEV_TO_J


def refine_linear_spectrum(points: list[tuple[float, float]], subdivisions: int) -> list[tuple[float, float]]:
    if subdivisions < 1:
        raise ValueError("subdivisions must be >=1")
    if len(points) < 2:
        raise ValueError("at least two points required")
    out: list[tuple[float, float]] = []
    for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
        if x1 <= x0:
            raise ValueError("energies must increase")
        for j in range(subdivisions):
            t = j / subdivisions
            out.append((x0 + t * (x1 - x0), y0 + t * (y1 - y0)))
    out.append(points[-1])
    return out


def trapz_values(points: list[tuple[float, float]]) -> float:
    return sum(0.5 * (y0 + y1) * (x1 - x0) for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]))


def continuum_power_w_per_kg(
    normalized_spectrum: list[tuple[float, float]],
    flux_cm2_s: float,
    a: float,
    *,
    r0_fm: float = 1.4,
    mode: str = "ceil",
    subdivisions: int = 1,
) -> float:
    refined = refine_linear_spectrum(normalized_spectrum, subdivisions)
    weighted = [
        (e, power_kernel_w_per_target(e, w, flux_cm2_s, a, r0_fm, mode))
        for e, w in refined
    ]
    return nuclei_per_kg_class(a) * trapz_values(weighted)


def line_power_w_per_kg(
    energy_mev: float,
    flux_cm2_s: float,
    a: float,
    *,
    r0_fm: float = 1.4,
    mode: str = "ceil",
) -> float:
    if energy_mev <= 0.0 or flux_cm2_s < 0.0:
        raise ValueError("invalid line source")
    sigma = sigma_unitarity_cm2(energy_mev, a, r0_fm, mode)
    return nuclei_per_kg_class(a) * flux_cm2_s * sigma * energy_mev * MEV_TO_J
