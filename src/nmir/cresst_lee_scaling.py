from __future__ import annotations

import math
from collections.abc import Callable

A_LEE = 7.6e-2
ALPHA_LEE = 5.02
B_LEE = 7.2e2
BETA_LEE = 2.22
E_MIN_KEV = 0.010
E_MAX_KEV = 0.300
ALL_CUTS_PLATEAU = 0.6591
E50_EV = 10.0
SIGMA_EV = 1.36
DAYS_PER_YEAR = 365.25
BLIND_EXPOSURE_KG_DAY = 0.05506
M10_KG = 9.766089763088724

BMAX = {
    "3sigma_delta30": 4.274968302863348,
    "5sigma_delta30": 1.0806120114381677,
    "5sigma_delta50": 0.692094879071742,
}


def lee_fit_rate_density(energy_kev: float) -> float:
    """Central published CRESST LEE fit in counts/(keV kg day)."""
    if energy_kev <= 0:
        raise ValueError("energy must be positive")
    return A_LEE * energy_kev ** (-ALPHA_LEE) + B_LEE * energy_kev ** (-BETA_LEE)


def surrogate_efficiency(energy_kev: float) -> float:
    if energy_kev < 0:
        raise ValueError("energy must be non-negative")
    energy_ev = 1000.0 * energy_kev
    return ALL_CUTS_PLATEAU * 0.5 * (
        1.0 + math.erf((energy_ev - E50_EV) / (math.sqrt(2.0) * SIGMA_EV))
    )


def integrate_log_trapezoid(
    integrand: Callable[[float], float],
    e_min_kev: float = E_MIN_KEV,
    e_max_kev: float = E_MAX_KEV,
    *,
    intervals: int = 20_000,
) -> float:
    """Integrate dE using uniform trapezoids in log(E)."""
    if not (0 < e_min_kev < e_max_kev) or intervals < 100:
        raise ValueError("invalid integration domain")
    x0 = math.log(e_min_kev)
    x1 = math.log(e_max_kev)
    h = (x1 - x0) / intervals

    def transformed(x: float) -> float:
        energy = math.exp(x)
        value = integrand(energy) * energy
        if not math.isfinite(value):
            raise ValueError("non-finite integrand")
        return value

    total = 0.5 * (transformed(x0) + transformed(x1))
    for i in range(1, intervals):
        total += transformed(x0 + i * h)
    return total * h


def corrected_lee_rate_per_kg_day(*, intervals: int = 20_000) -> float:
    return integrate_log_trapezoid(lee_fit_rate_density, intervals=intervals)


def accepted_lee_rate_per_kg_day(*, intervals: int = 20_000) -> float:
    return integrate_log_trapezoid(
        lambda e: lee_fit_rate_density(e) * surrogate_efficiency(e),
        intervals=intervals,
    )


def rejection_factor(accepted_lee_events_per_year: float, bmax_events_per_year: float) -> float:
    if accepted_lee_events_per_year <= 0 or bmax_events_per_year <= 0:
        raise ValueError("event counts must be positive")
    return accepted_lee_events_per_year / bmax_events_per_year
