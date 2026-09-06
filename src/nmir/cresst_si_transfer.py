from __future__ import annotations

import math
from collections.abc import Callable

from .baseline import G_F_GEV2, GEV2_TO_CM2, weak_charge
from .cevns_solar_optimize import (
    SIN2_THETA_W,
    Target,
    SpectrumSpec,
    helm_form_factor_sq,
    nuclei_per_kg,
    normalized,
    recoil_tmax_gev,
    trapz,
)

SECONDS_PER_DAY = 86400.0
E50_EV = 10.0
SIGMA_EV = 1.36
TRIGGER_PLATEAU = 0.8053
ALL_CUTS_PLATEAU = 0.6591
ANALYSIS_FLOOR_EV = 10.0


def cresst_trigger_efficiency(recoil_ev: float) -> float:
    if recoil_ev < 0:
        raise ValueError("recoil energy must be non-negative")
    turn_on = 0.5 * (1.0 + math.erf((recoil_ev - E50_EV) / (math.sqrt(2.0) * SIGMA_EV)))
    return TRIGGER_PLATEAU * turn_on


def cresst_factorized_surrogate_efficiency(recoil_ev: float) -> float:
    if recoil_ev < 0:
        raise ValueError("recoil energy must be non-negative")
    return cresst_trigger_efficiency(recoil_ev) * (ALL_CUTS_PLATEAU / TRIGGER_PLATEAU)


def hard_step_efficiency(recoil_ev: float) -> float:
    if recoil_ev < 0:
        raise ValueError("recoil energy must be non-negative")
    return 1.0


def cevns_sigma_with_efficiency_cm2(
    e_nu_mev: float,
    target: Target,
    efficiency: Callable[[float], float],
    *,
    analysis_floor_ev: float = ANALYSIS_FLOOR_EV,
    use_helm: bool = True,
    recoil_steps: int = 160,
) -> float:
    if e_nu_mev < 0 or analysis_floor_ev < 0 or recoil_steps < 8:
        raise ValueError("invalid CEvNS fold input")
    if e_nu_mev == 0:
        return 0.0

    e_gev = e_nu_mev * 1.0e-3
    m_gev = target.mass_mev * 1.0e-3
    t0 = analysis_floor_ev * 1.0e-9
    t1 = recoil_tmax_gev(e_nu_mev, target)
    if t0 >= t1:
        return 0.0

    q_w = weak_charge(target.z, target.n, SIN2_THETA_W)
    pref = G_F_GEV2**2 * q_w**2 * m_gev / (4.0 * math.pi)
    nstep = recoil_steps + recoil_steps % 2
    h = (t1 - t0) / nstep

    def kernel(t_gev: float) -> float:
        recoil_shape = max(0.0, 1.0 - m_gev * t_gev / (2.0 * e_gev * e_gev))
        recoil_ev = t_gev * 1.0e9
        eps = efficiency(recoil_ev)
        if not math.isfinite(eps) or eps < 0 or eps > 1:
            raise ValueError("efficiency must be finite and within [0,1]")
        if not use_helm:
            return recoil_shape * eps
        q_mev = math.sqrt(max(0.0, 2.0 * (m_gev * 1.0e3) * (t_gev * 1.0e3)))
        return recoil_shape * helm_form_factor_sq(target.a, q_mev) * eps

    total = kernel(t0) + kernel(t1)
    for i in range(1, nstep):
        total += (4.0 if i % 2 else 2.0) * kernel(t0 + i * h)
    integral = h * total / 3.0
    return pref * integral * GEV2_TO_CM2


def spectrum_average_sigma_with_efficiency_cm2(
    spectrum: list[tuple[float, float]],
    target: Target,
    efficiency: Callable[[float], float],
    *,
    analysis_floor_ev: float = ANALYSIS_FLOOR_EV,
    use_helm: bool = True,
) -> float:
    points = normalized(spectrum)
    weighted = [
        (
            energy,
            weight
            * cevns_sigma_with_efficiency_cm2(
                energy,
                target,
                efficiency,
                analysis_floor_ev=analysis_floor_ev,
                use_helm=use_helm,
            ),
        )
        for energy, weight in points
    ]
    return trapz(weighted)


def rate_per_kg_day(flux_cm2_s: float, sigma_cm2: float, target: Target) -> float:
    return flux_cm2_s * sigma_cm2 * nuclei_per_kg(target) * SECONDS_PER_DAY


def component_rate_with_efficiency(
    component: str,
    target: Target,
    efficiency: Callable[[float], float],
    fluxes: dict[str, float],
    manifest: dict[str, SpectrumSpec],
    spectra: dict[str, list[tuple[float, float]]],
    *,
    analysis_floor_ev: float = ANALYSIS_FLOOR_EV,
    use_helm: bool = True,
) -> float:
    if component == "pep":
        sigma = cevns_sigma_with_efficiency_cm2(
            manifest["pep"].line_energy_mev or 1.442,
            target,
            efficiency,
            analysis_floor_ev=analysis_floor_ev,
            use_helm=use_helm,
        )
        return rate_per_kg_day(fluxes["pep"], sigma, target)

    source_key = component
    if component == "Be7_ground":
        flux = fluxes["Be7"] * 0.897
    elif component == "Be7_excited":
        flux = fluxes["Be7"] * 0.103
    else:
        flux = fluxes[component]

    sigma = spectrum_average_sigma_with_efficiency_cm2(
        spectra[source_key],
        target,
        efficiency,
        analysis_floor_ev=analysis_floor_ev,
        use_helm=use_helm,
    )
    return rate_per_kg_day(flux, sigma, target)


def total_rate_with_efficiency(
    target: Target,
    efficiency: Callable[[float], float],
    fluxes: dict[str, float],
    manifest: dict[str, SpectrumSpec],
    spectra: dict[str, list[tuple[float, float]]],
    *,
    analysis_floor_ev: float = ANALYSIS_FLOOR_EV,
    use_helm: bool = True,
) -> dict[str, object]:
    components = ["pp", "Be7_ground", "Be7_excited", "pep", "N13", "O15", "F17", "B8", "hep"]
    rates = {
        c: component_rate_with_efficiency(
            c,
            target,
            efficiency,
            fluxes,
            manifest,
            spectra,
            analysis_floor_ev=analysis_floor_ev,
            use_helm=use_helm,
        )
        for c in components
    }
    return {
        "target": target.name,
        "analysis_floor_ev": analysis_floor_ev,
        "components_events_per_kg_day": rates,
        "total_events_per_kg_day": sum(rates.values()),
        "dominant_component": max(rates, key=rates.get),
    }
