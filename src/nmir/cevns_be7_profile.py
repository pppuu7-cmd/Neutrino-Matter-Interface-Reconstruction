"""Physical Be7 solar-line fold for ideal low-q CEvNS on Ar-40.

This module scores detector observability only. It does not enhance the weak
cross section and it does not count metastable target energy as neutrino energy.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Callable, Iterable

from .baseline import G_F_GEV2, GEV2_TO_CM2, N_A, weak_charge
from .cevns_threshold import AR40_ATOMIC_MASS_U, U_TO_MEV, source_min_energy_mev

AR40_Z = 18
AR40_N = 22
SIN2_THETA_W = 0.23857
BE7_GS98_TOTAL_FLUX_CM2_S = 4.93e9
BE7_DOMINANT_BRANCH = 0.897


def load_profile(path: str | Path) -> list[tuple[float, float]]:
    rows: list[tuple[float, float]] = []
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        for raw in handle:
            raw = raw.strip()
            if not raw or raw.startswith("#"):
                continue
            e, w = next(csv.reader([raw]))
            rows.append((float(e), float(w)))
    if len(rows) < 2:
        raise ValueError("profile requires at least two points")
    if any(rows[i + 1][0] <= rows[i][0] for i in range(len(rows) - 1)):
        raise ValueError("profile energies must be strictly increasing")
    if any(weight < 0.0 for _, weight in rows):
        raise ValueError("profile weights must be non-negative")
    return rows


def trapz_xy(points: Iterable[tuple[float, float]]) -> float:
    pts = list(points)
    return sum(
        0.5 * (y0 + y1) * (x1 - x0)
        for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:])
    )


def profile_norm(profile: list[tuple[float, float]]) -> float:
    return trapz_xy(profile)


def _interp_weight(profile: list[tuple[float, float]], energy_mev: float) -> float:
    if energy_mev <= profile[0][0]:
        return profile[0][1]
    if energy_mev >= profile[-1][0]:
        return profile[-1][1]
    for (e0, w0), (e1, w1) in zip(profile[:-1], profile[1:]):
        if e0 <= energy_mev <= e1:
            f = (energy_mev - e0) / (e1 - e0)
            return w0 + f * (w1 - w0)
    raise RuntimeError("interpolation bracket not found")


def profile_fraction_above(profile: list[tuple[float, float]], energy_mev: float) -> float:
    norm = profile_norm(profile)
    if norm <= 0.0:
        raise ValueError("profile normalization must be positive")
    if energy_mev <= profile[0][0]:
        return 1.0
    if energy_mev >= profile[-1][0]:
        return 0.0
    tail = [(energy_mev, _interp_weight(profile, energy_mev))]
    tail.extend((e, w) for e, w in profile if e > energy_mev)
    return trapz_xy(tail) / norm


def _profile_average(profile: list[tuple[float, float]], fn: Callable[[float], float]) -> float:
    norm = profile_norm(profile)
    weighted = [(e, w * fn(e)) for e, w in profile]
    return trapz_xy(weighted) / norm


def cevns_sigma_above_threshold_cm2(
    e_nu_mev: float,
    threshold_ev: float,
    *,
    z: int = AR40_Z,
    n: int = AR40_N,
    atomic_mass_u: float = AR40_ATOMIC_MASS_U,
    sin2_theta_w: float = SIN2_THETA_W,
) -> float:
    """Integrate the frozen ideal low-q CEvNS recoil spectrum above threshold."""
    if e_nu_mev <= 0.0:
        raise ValueError("e_nu_mev must be positive")
    if threshold_ev < 0.0:
        raise ValueError("threshold_ev must be non-negative")
    e_gev = e_nu_mev * 1.0e-3
    m_gev = atomic_mass_u * U_TO_MEV * 1.0e-3
    t0_gev = threshold_ev * 1.0e-9
    tmax_gev = 2.0 * e_gev * e_gev / (m_gev + 2.0 * e_gev)
    if t0_gev >= tmax_gev:
        return 0.0
    q_w = weak_charge(z, n, sin2_theta_w)
    prefactor = G_F_GEV2**2 * q_w**2 * m_gev / (4.0 * math.pi)
    integral_gev = (tmax_gev - t0_gev) - m_gev * (tmax_gev**2 - t0_gev**2) / (4.0 * e_gev**2)
    return prefactor * integral_gev * GEV2_TO_CM2


def profile_average_sigma_cm2(profile: list[tuple[float, float]], threshold_ev: float) -> float:
    return _profile_average(profile, lambda energy: cevns_sigma_above_threshold_cm2(energy, threshold_ev))


def ar40_nuclei_per_kg() -> float:
    return 1000.0 / AR40_ATOMIC_MASS_U * N_A


def ideal_events_per_kg_day(
    profile: list[tuple[float, float]],
    threshold_ev: float,
    *,
    total_be7_flux_cm2_s: float = BE7_GS98_TOTAL_FLUX_CM2_S,
    line_branch: float = BE7_DOMINANT_BRANCH,
) -> float:
    if total_be7_flux_cm2_s < 0.0 or not (0.0 <= line_branch <= 1.0):
        raise ValueError("invalid source normalization")
    sigma = profile_average_sigma_cm2(profile, threshold_ev)
    return total_be7_flux_cm2_s * line_branch * sigma * ar40_nuclei_per_kg() * 86400.0


def threshold_row(profile: list[tuple[float, float]], threshold_ev: float) -> dict[str, float]:
    mass_mev = AR40_ATOMIC_MASS_U * U_TO_MEV
    e_min = source_min_energy_mev(threshold_ev * 1.0e-6, mass_mev) if threshold_ev > 0.0 else 0.0
    total_sigma = profile_average_sigma_cm2(profile, 0.0)
    above_sigma = profile_average_sigma_cm2(profile, threshold_ev)
    return {
        "threshold_ev": threshold_ev,
        "source_min_energy_mev": e_min,
        "profile_fraction_above_emin": profile_fraction_above(profile, e_min) if threshold_ev > 0.0 else 1.0,
        "profile_average_total_sigma_cm2": total_sigma,
        "profile_average_above_threshold_sigma_cm2": above_sigma,
        "retained_cross_section_fraction": above_sigma / total_sigma,
        "ideal_events_per_kg_day": ideal_events_per_kg_day(profile, threshold_ev),
    }
