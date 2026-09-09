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


def range_information_kernel(mediator_mass_gev: float, q_gev: float) -> float:
    """Return the common fixed-absolute-covariance range-information kernel."""
    mass = _positive("mediator_mass_gev", mediator_mass_gev)
    q = _positive("q_gev", q_gev)
    return range_information_kernel_from_f(finite_q_ratio(mass, q))


def range_information_kernel_mass_ratio(mass_over_q: float) -> float:
    """Dimensionless convenience form K_eta(x), x=mX/q>0."""
    x = _positive("mass_over_q", mass_over_q)
    # Setting q=1 keeps this exactly tied to the authoritative 0105b bridge.
    return range_information_kernel(x, 1.0)


def composition_information_amplitude_factor(mediator_mass_gev: float, q_gev: float) -> float:
    """Return f^2, the common fixed-absolute-covariance amplitude factor for rho."""
    mass = _positive("mediator_mass_gev", mediator_mass_gev)
    q = _positive("q_gev", q_gev)
    f = finite_q_ratio(mass, q)
    return f * f
