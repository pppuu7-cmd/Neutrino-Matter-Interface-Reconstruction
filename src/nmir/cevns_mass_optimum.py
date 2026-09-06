"""Inverse-design envelope for CEvNS target mass versus recoil threshold.

This module deliberately uses a continuous mass number A and fixed weak charge
per nucleon.  It is a class-level design heuristic, not a real-isotope model.
"""

from __future__ import annotations

import math

M_U_MEV = 931.49410242


def analytic_a_star(e_nu_mev: float, threshold_ev: float) -> float:
    if e_nu_mev <= 0.0 or threshold_ev <= 0.0:
        raise ValueError("energy and threshold must be positive")
    t_mev = threshold_ev * 1.0e-6
    return 2.0 * e_nu_mev**2 / (3.0 * M_U_MEV * t_mev)


def exact_tmax_mev(e_nu_mev: float, a_mass: float) -> float:
    if e_nu_mev <= 0.0 or a_mass <= 0.0:
        raise ValueError("energy and A must be positive")
    m_mev = a_mass * M_U_MEV
    return 2.0 * e_nu_mev**2 / (m_mev + 2.0 * e_nu_mev)


def exact_closure_a(e_nu_mev: float, threshold_ev: float) -> float:
    if e_nu_mev <= 0.0 or threshold_ev <= 0.0:
        raise ValueError("energy and threshold must be positive")
    t_mev = threshold_ev * 1.0e-6
    return (2.0 * e_nu_mev**2 / t_mev - 2.0 * e_nu_mev) / M_U_MEV


def fixed_mass_objective(e_nu_mev: float, threshold_ev: float, a_mass: float) -> float:
    """Objective proportional to events per fixed detector mass.

    Q_W/A is held constant, so an irrelevant common proportionality constant is
    omitted.  The exact recoil endpoint is retained while the frozen low-q
    differential CEvNS shape is integrated analytically above threshold.
    """
    if a_mass <= 0.0:
        return 0.0
    t0 = threshold_ev * 1.0e-6
    if t0 < 0.0:
        raise ValueError("threshold must be non-negative")
    m_mev = a_mass * M_U_MEV
    tmax = exact_tmax_mev(e_nu_mev, a_mass)
    if t0 >= tmax:
        return 0.0
    recoil_integral = (tmax - t0) - m_mev * (tmax**2 - t0**2) / (4.0 * e_nu_mev**2)
    # Q^2 ~ A^2, differential prefactor ~ Q^2 M, targets/kg ~ 1/A.
    return a_mass * m_mev * recoil_integral


def numerical_a_star(e_nu_mev: float, threshold_ev: float, iterations: int = 160) -> float:
    """Golden-section maximum of the exact frozen objective over continuous A."""
    hi = exact_closure_a(e_nu_mev, threshold_ev)
    if hi <= 0.0:
        raise ValueError("threshold is above all positive-A kinematic support")
    lo = max(1.0e-9, hi * 1.0e-12)
    hi *= 1.0 - 1.0e-12
    phi = (math.sqrt(5.0) - 1.0) / 2.0
    c = hi - phi * (hi - lo)
    d = lo + phi * (hi - lo)
    fc = fixed_mass_objective(e_nu_mev, threshold_ev, c)
    fd = fixed_mass_objective(e_nu_mev, threshold_ev, d)
    for _ in range(iterations):
        if fc > fd:
            hi, d, fd = d, c, fc
            c = hi - phi * (hi - lo)
            fc = fixed_mass_objective(e_nu_mev, threshold_ev, c)
        else:
            lo, c, fc = c, d, fd
            d = lo + phi * (hi - lo)
            fd = fixed_mass_objective(e_nu_mev, threshold_ev, d)
    return 0.5 * (lo + hi)


def benchmark_row(e_nu_mev: float, threshold_ev: float) -> dict[str, float]:
    analytic = analytic_a_star(e_nu_mev, threshold_ev)
    numeric = numerical_a_star(e_nu_mev, threshold_ev)
    return {
        "e_nu_mev": e_nu_mev,
        "threshold_ev": threshold_ev,
        "analytic_a_star": analytic,
        "numerical_a_star": numeric,
        "relative_a_star_residual": numeric / analytic - 1.0,
        "exact_tmax_over_threshold_at_numeric_optimum": exact_tmax_mev(e_nu_mev, numeric) / (threshold_ev * 1.0e-6),
        "exact_closure_a": exact_closure_a(e_nu_mev, threshold_ev),
    }
