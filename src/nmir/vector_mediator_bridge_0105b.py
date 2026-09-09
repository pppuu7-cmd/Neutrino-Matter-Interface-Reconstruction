"""NMIR v2 gate 0105b: analytic vector-mediator forward/finite-q bridge.

Scientific scope is frozen by
research/prereg/0105b_vector_mediator_cross_regime_bridge.md.

This module contains coefficient-level identities only.  It deliberately does
not calculate detector event rates, likelihoods, confidence levels or discovery
statistics.
"""
from __future__ import annotations

import math

KEV_TO_GEV = 1.0e-6


def _require_positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and > 0")
    return value


def _require_nonnegative(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value < 0.0:
        raise ValueError(f"{name} must be finite and >= 0")
    return value


def _require_finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def forward_coefficient_gev2(gprod: float, mediator_mass_gev: float) -> float:
    """Return C(0)=gprod/mX^2 in GeV^-2 for dimensionless ``gprod``."""
    gprod = _require_finite("gprod", gprod)
    mass = _require_positive("mediator_mass_gev", mediator_mass_gev)
    return gprod / (mass * mass)


def finite_q_coefficient_gev2(
    gprod: float,
    mediator_mass_gev: float,
    q_gev: float,
) -> float:
    """Return C(q)=gprod/(mX^2+q^2) in GeV^-2."""
    gprod = _require_finite("gprod", gprod)
    mass = _require_positive("mediator_mass_gev", mediator_mass_gev)
    q = _require_nonnegative("q_gev", q_gev)
    return gprod / (mass * mass + q * q)


def finite_q_ratio(mediator_mass_gev: float, q_gev: float) -> float:
    """Return C(q)/C(0)=mX^2/(mX^2+q^2), independent of coupling."""
    mass = _require_positive("mediator_mass_gev", mediator_mass_gev)
    q = _require_nonnegative("q_gev", q_gev)
    if q == 0.0:
        return 1.0
    ratio_sq = q / mass
    # This form is stable in the heavy/contact regime without subtracting two
    # nearly equal coefficients.  Very large q/m may overflow when squared;
    # the mathematically correct limiting ratio is then zero.
    if ratio_sq > math.sqrt(float.fromhex("0x1.fffffffffffffp+1023")):
        return 0.0
    return 1.0 / (1.0 + ratio_sq * ratio_sq)


def mediator_mass_from_ratio_gev(ratio: float, q_gev: float) -> float:
    """Invert r=mX^2/(mX^2+q^2) for 0<r<1 and q>0."""
    ratio = _require_finite("ratio", ratio)
    q = _require_positive("q_gev", q_gev)
    if not 0.0 < ratio < 1.0:
        raise ValueError("ratio must satisfy 0 < ratio < 1")
    return q * math.sqrt(ratio / (1.0 - ratio))


def cevns_momentum_transfer_gev(nucleus_mass_gev: float, recoil_gev: float) -> float:
    """Nonrelativistic CEvNS momentum transfer q=sqrt(2 M T), in GeV."""
    mass = _require_positive("nucleus_mass_gev", nucleus_mass_gev)
    recoil = _require_nonnegative("recoil_gev", recoil_gev)
    return math.sqrt(2.0 * mass * recoil)


def cevns_momentum_transfer_from_kev_gev(
    nucleus_mass_gev: float,
    recoil_kev: float,
) -> float:
    """Explicit keV-recoil convenience wrapper returning q in GeV."""
    recoil_kev = _require_nonnegative("recoil_kev", recoil_kev)
    return cevns_momentum_transfer_gev(nucleus_mass_gev, recoil_kev * KEV_TO_GEV)


def nuclear_vector_charge(z: int, n: int, g_proton: float, g_neutron: float) -> float:
    """Return the coherent benchmark charge QX=Z gp + N gn."""
    if not isinstance(z, int) or isinstance(z, bool) or z < 0:
        raise ValueError("z must be a nonnegative integer")
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    gp = _require_finite("g_proton", g_proton)
    gn = _require_finite("g_neutron", g_neutron)
    return z * gp + n * gn
