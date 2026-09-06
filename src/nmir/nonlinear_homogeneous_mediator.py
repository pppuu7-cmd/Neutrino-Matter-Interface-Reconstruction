"""Convex p-homogeneous nonlinear mediator accounting for NMIR G2."""

from __future__ import annotations

import math


def scalar_equilibrium(*, p: float, kappa: float, source: float) -> dict[str, float]:
    """Equilibrium of V=kappa*|x|^p/p - source*x for p>1, kappa>0."""
    if p <= 1.0:
        raise ValueError("p must exceed one")
    if kappa <= 0.0:
        raise ValueError("kappa must be positive")
    if source == 0.0:
        x = 0.0
    else:
        x = math.copysign((abs(source) / kappa) ** (1.0 / (p - 1.0)), source)
    stored = kappa * abs(x) ** p / p
    source_work = source * x
    total = stored - source_work
    induced_magnitude = -total
    stationarity = kappa * (abs(x) ** (p - 1.0) if x >= 0.0 else -abs(x) ** (p - 1.0)) - source
    return {
        "x_star": x,
        "stored_free_energy": stored,
        "source_work": source_work,
        "total_minimum_energy": total,
        "induced_energy_magnitude": induced_magnitude,
        "stationarity_residual": stationarity,
        "induced_to_stored_ratio": induced_magnitude / stored if stored else 0.0,
        "work_to_stored_ratio": source_work / stored if stored else 0.0,
    }


def collective_scaling_energy(
    *,
    n: float,
    p: float,
    gamma: float,
    g0: float = 1.0,
    o0: float = 1.0,
    kappa: float = 1.0,
) -> dict[str, float]:
    """Evaluate scalar homogeneous medium with source b_N=g0*N^(1-gamma)*o0."""
    if n <= 0.0:
        raise ValueError("n must be positive")
    source = g0 * o0 * n ** (1.0 - gamma)
    out = scalar_equilibrium(p=p, kappa=kappa, source=source)
    return {
        **out,
        "n": n,
        "gamma": gamma,
        "stored_per_particle": out["stored_free_energy"] / n,
        "induced_per_particle": out["induced_energy_magnitude"] / n,
    }


def analytic_per_particle_gain(*, n1: float, n2: float, p: float, gamma: float) -> float:
    """Analytic E/N gain between N2 and N1."""
    if n1 <= 0 or n2 <= 0 or p <= 1:
        raise ValueError("invalid inputs")
    exponent = p * (1.0 - gamma) / (p - 1.0) - 1.0
    return (n2 / n1) ** exponent


def extensive_gamma(p: float) -> float:
    if p <= 1.0:
        raise ValueError("p must exceed one")
    return 1.0 / p
