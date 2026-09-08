"""Analytic continuous projection of the frozen piecewise-linear Model-S density.

NMIR 0089b production evaluator.  No numerical quadrature is used here.
The source table retains the already-frozen linear density interpolation; this
module integrates that continuous interpolation in closed form instead of
inserting a moving point into a trapezoidal radial quadrature.
"""
from __future__ import annotations

import math

from .gravity_extended import AU_CM, C_CGS, G_CGS, RadialDensityProfile


def _coeff(lo: float, hi: float, rho_lo: float, rho_hi: float) -> tuple[float, float]:
    if not hi > lo:
        raise ValueError("source interval must have positive width")
    a = (rho_hi - rho_lo) / (hi - lo)
    b = rho_lo - a * lo
    return a, b


def _q(x: float, u: float) -> float:
    if u < x or x <= 0.0:
        raise ValueError("require 0 < x <= u")
    if u == x:
        return 0.0
    ratio = x / u
    return math.sqrt(max(0.0, (1.0 - ratio) * (1.0 + ratio)))


def _fa(u: float, x: float) -> float:
    """Stable antiderivative for u^3 [1-sqrt(1-(x/u)^2)]."""
    q = _q(x, u)
    return (
        (u * u * x * x / 8.0) * (2.0 / (1.0 + q) + q)
        + (x**4 / 8.0) * math.acosh(u / x)
    )


def _fb(u: float, x: float) -> float:
    """Stable antiderivative for u^2 [1-sqrt(1-(x/u)^2)]."""
    q = _q(x, u)
    return (u * x * x / 3.0) * (1.0 + q + q * q) / (1.0 + q)


def _ja(u: float, x: float) -> float:
    """Antiderivative for u^2/sqrt(u^2-x^2), retained for diagnostics/tests."""
    if u < x or x <= 0.0:
        raise ValueError("require 0 < x <= u")
    root = math.sqrt(max(0.0, (u - x) * (u + x)))
    return 0.5 * (u * root + x * x * math.acosh(u / x))


def _jb(u: float, x: float) -> float:
    """Antiderivative for u/sqrt(u^2-x^2), retained for diagnostics/tests."""
    if u < x or x <= 0.0:
        raise ValueError("require 0 < x <= u")
    return math.sqrt(max(0.0, (u - x) * (u + x)))


def _poly(a: float, b: float, lo: float, hi: float) -> float:
    return a * (hi**4 - lo**4) / 4.0 + b * (hi**3 - lo**3) / 3.0


def _derivative_shell_tspace(
    x: float,
    lo: float,
    hi: float,
    rho_lo: float,
    rho_hi: float,
) -> float:
    """Exact endpoint-centered shell integral for u*rho/sqrt(u^2-x^2).

    The lower integration endpoint is max(lo, x).  This is algebraically
    equivalent to a*DeltaJ_A+b*DeltaJ_B but avoids acosh(u/x) near unity and
    the associated large a/b cancellation (0089b stability amendment).
    """
    if not (0.0 < x < hi and lo < hi):
        raise ValueError("require 0 < x < hi and lo < hi")
    lower = max(lo, x)
    a = (rho_hi - rho_lo) / (hi - lo)
    rho_lower = math.fsum([rho_lo, a * (lower - lo)])
    t_lower = math.sqrt(max(0.0, (lower - x) * (lower + x)))
    t_hi = math.sqrt(max(0.0, (hi - x) * (hi + x)))
    dt = t_hi - t_lower
    delta_asinh = math.asinh(t_hi / x) - math.asinh(t_lower / x)
    delta_k = math.fsum(
        [
            0.5 * (hi * t_hi - lower * t_lower),
            0.5 * x * x * delta_asinh,
            -lower * dt,
        ]
    )
    return math.fsum([rho_lower * dt, a * delta_k])


def continuous_projected_mass_g(
    profile: RadialDensityProfile,
    x: float,
    radius_cm: float,
) -> float:
    """Exact closed-form cylinder mass for the linearly interpolated density."""
    if not 0.0 < x <= 1.0:
        raise ValueError("x must lie in (0,1]")
    if radius_cm <= 0.0:
        raise ValueError("radius_cm must be positive")
    rs = profile.radius_fraction
    ys = profile.density_g_cm3
    pieces: list[float] = []
    for lo, hi, rlo, rhi in zip(rs, rs[1:], ys, ys[1:]):
        if lo >= 1.0:
            break
        hi = min(hi, 1.0)
        if hi <= lo:
            continue
        a, b = _coeff(lo, hi, rlo, rhi)
        if hi <= x:
            pieces.append(_poly(a, b, lo, hi))
        elif lo >= x:
            pieces.append(a * (_fa(hi, x) - _fa(lo, x)) + b * (_fb(hi, x) - _fb(lo, x)))
        else:
            pieces.append(_poly(a, b, lo, x))
            pieces.append(a * (_fa(hi, x) - _fa(x, x)) + b * (_fb(hi, x) - _fb(x, x)))
    value = 4.0 * math.pi * radius_cm**3 * math.fsum(pieces)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError("non-finite/non-positive continuous projected mass")
    return value


def continuous_projected_mass_derivative_g_per_x(
    profile: RadialDensityProfile,
    x: float,
    radius_cm: float,
) -> float:
    """Exact dM_cyl/dx for the same continuous piecewise-linear density."""
    if not 0.0 < x <= 1.0:
        raise ValueError("x must lie in (0,1]")
    if radius_cm <= 0.0:
        raise ValueError("radius_cm must be positive")
    if x == 1.0:
        return 0.0
    rs = profile.radius_fraction
    ys = profile.density_g_cm3
    pieces: list[float] = []
    for lo, hi, rlo, rhi in zip(rs, rs[1:], ys, ys[1:]):
        if lo >= 1.0:
            break
        hi = min(hi, 1.0)
        if hi <= x or hi <= lo:
            continue
        pieces.append(_derivative_shell_tspace(x, lo, hi, rlo, rhi))
    value = 4.0 * math.pi * radius_cm**3 * x * math.fsum(pieces)
    if not math.isfinite(value) or value < 0.0:
        raise ValueError("non-finite/negative continuous projected-mass derivative")
    return value


def continuous_focal_distance_au(
    profile: RadialDensityProfile,
    x: float,
    radius_cm: float,
) -> float:
    mass = continuous_projected_mass_g(profile, x, radius_cm)
    b_cm = x * radius_cm
    value = b_cm * b_cm * C_CGS * C_CGS / (4.0 * G_CGS * mass) / AU_CM
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError("non-finite/non-positive continuous focal distance")
    return value


__all__ = [
    "continuous_projected_mass_g",
    "continuous_projected_mass_derivative_g_per_x",
    "continuous_focal_distance_au",
]
