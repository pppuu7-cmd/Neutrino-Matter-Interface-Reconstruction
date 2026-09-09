"""NMIR v2 gate 0105e: pre-data finite-range information kernels.

These are coefficient-level information-geometry controls only.  They do not
consume observed events or calculate a likelihood, p-value, confidence level,
or BSM significance.
"""
from __future__ import annotations

import math

from nmir.vector_mediator_bridge_0105b import finite_q_ratio


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and > 0")
    return value


def range_information_kernel_from_f(finite_q_factor: float) -> float:
    """Return K_eta=4 f^2 (1-f)^2 for eta=ln(mX), 0<=f<=1."""
    f = float(finite_q_factor)
    if not math.isfinite(f) or not 0.0 <= f <= 1.0:
        raise ValueError("finite_q_factor must be finite and satisfy 0 <= f <= 1")
    return 4.0 * f * f * (1.0 - f) * (1.0 - f)


def range_information_kernel_mass_ratio(mass_over_q: float) -> float:
    """Return reciprocal-stable K_eta(x), x=mX/q>0.

    Analytically K=4*x^4/(1+x^2)^4.  For x>1 evaluate the exactly
    reciprocal form at y=1/x, avoiding loss of precision from 1-f as f->1.
    """
    x = _positive("mass_over_q", mass_over_q)
    y = x if x <= 1.0 else 1.0 / x
    y2 = y * y
    return 4.0 * y2 * y2 / ((1.0 + y2) ** 4)


def range_information_kernel(mediator_mass_gev: float, q_gev: float) -> float:
    """Return the common fixed-absolute-covariance range-information kernel."""
    mass = _positive("mediator_mass_gev", mediator_mass_gev)
    q = _positive("q_gev", q_gev)
    return range_information_kernel_mass_ratio(mass / q)


def composition_information_amplitude_factor(mediator_mass_gev: float, q_gev: float) -> float:
    """Return f^2, the common fixed-absolute-covariance amplitude factor for rho."""
    mass = _positive("mediator_mass_gev", mediator_mass_gev)
    q = _positive("q_gev", q_gev)
    f = finite_q_ratio(mass, q)
    return f * f
