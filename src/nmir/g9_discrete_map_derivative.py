"""Exact open-interval derivative of the frozen G9 trapezoidal projected-mass map.

This module differentiates the *actual* finite trapezoidal algorithm used by
``gravity_extended.projected_mass_g``.  It performs no quadrature and defines
no derivative at fixed Model-S radial knots, where the augmented-grid topology
changes.
"""
from __future__ import annotations

from bisect import bisect_right
import math

from .gravity_extended import RadialDensityProfile


class DiscreteMapDerivativeBoundary(ValueError):
    """Raised when a derivative is requested exactly at a fixed radial knot."""


def _sym_shell_fraction(x: float, u: float) -> float:
    if u == 0.0 or u <= x:
        return 1.0
    ratio = x / u
    return 1.0 - math.sqrt(max(0.0, 1.0 - ratio * ratio))


def _shell_fraction_dx(x: float, u: float) -> float:
    """d/dx [1-sqrt(1-(x/u)^2)] for fixed u>x."""
    if not 0.0 < x < u:
        raise ValueError("shell derivative requires 0 < x < u")
    rad = 1.0 - (x / u) ** 2
    if rad <= 0.0:
        raise ValueError("shell derivative is singular at/above fixed knot")
    return x / (u * u * math.sqrt(rad))


def _interval_index(profile: RadialDensityProfile, x: float) -> int:
    rs = profile.radius_fraction
    if not rs[0] <= x <= rs[-1]:
        raise ValueError("x outside parsed profile support")
    if x in rs:
        raise DiscreteMapDerivativeBoundary("derivative undefined at fixed radial knot")
    k = bisect_right(rs, x) - 1
    if k < 0 or k >= len(rs) - 1:
        raise ValueError("x not inside an open radial-knot interval")
    return k


def _rho_inside(profile: RadialDensityProfile, k: int, x: float) -> tuple[float, float]:
    rs = profile.radius_fraction
    ys = profile.density_g_cm3
    a, b = rs[k], rs[k + 1]
    slope = (ys[k + 1] - ys[k]) / (b - a)
    rho = ys[k] + slope * (x - a)
    return rho, slope


def finite_sum_projected_mass_g(
    profile: RadialDensityProfile,
    x: float,
    radius_cm: float,
) -> float:
    """Independent dimensionless finite-sum form of frozen ``projected_mass_g``."""
    if not 0.0 < x <= 1.0:
        raise ValueError("x must lie in (0,1]")
    if radius_cm <= 0.0:
        raise ValueError("radius_cm must be positive")

    rs = profile.radius_fraction
    ys = profile.density_g_cm3
    points = list(zip(rs, ys))
    if x < rs[-1] and x not in rs:
        k = bisect_right(rs, x) - 1
        rho_x, _ = _rho_inside(profile, k, x)
        points.append((x, rho_x))
        points.sort(key=lambda p: p[0])

    total = 0.0
    for (u0, rho0), (u1, rho1) in zip(points, points[1:]):
        g0 = u0 * u0 * rho0 * _sym_shell_fraction(x, u0)
        g1 = u1 * u1 * rho1 * _sym_shell_fraction(x, u1)
        total += (u1 - u0) * (g0 + g1)
    return 2.0 * math.pi * radius_cm**3 * total


def projected_mass_derivative_g_per_x(
    profile: RadialDensityProfile,
    x: float,
    radius_cm: float,
) -> float:
    """Exact derivative d(projected_mass_g)/dx on one open fixed-knot interval."""
    if not 0.0 < x < 1.0:
        raise ValueError("derivative authority domain is 0 < x < 1")
    if radius_cm <= 0.0:
        raise ValueError("radius_cm must be positive")

    k = _interval_index(profile, x)
    rs = profile.radius_fraction
    ys = profile.density_g_cm3
    a, b = rs[k], rs[k + 1]
    rho_a, rho_b = ys[k], ys[k + 1]
    rho_x, slope = _rho_inside(profile, k, x)

    def g(u: float, rho: float) -> float:
        return u * u * rho

    g_a = g(a, rho_a)
    g_b = g(b, rho_b)
    gprime_x = 2.0 * x * rho_x + x * x * slope

    f_b = _sym_shell_fraction(x, b)
    fp_b = _shell_fraction_dx(x, b)

    # Derivative of the two trapezoids [a,x] and [x,b].
    hprime = (
        g_a
        - g_b * f_b
        + (b - a) * gprime_x
        + (b - x) * g_b * fp_b
    )

    # Every fully external fixed interval remains topologically fixed.
    for j in range(k + 1, len(rs) - 1):
        u0, u1 = rs[j], rs[j + 1]
        g0 = g(u0, ys[j])
        g1 = g(u1, ys[j + 1])
        fp0 = _shell_fraction_dx(x, u0)
        fp1 = _shell_fraction_dx(x, u1)
        hprime += (u1 - u0) * (g0 * fp0 + g1 * fp1)

    result = 2.0 * math.pi * radius_cm**3 * hprime
    if not math.isfinite(result):
        raise ValueError("nonfinite frozen-map derivative")
    return result


__all__ = [
    "DiscreteMapDerivativeBoundary",
    "finite_sum_projected_mass_g",
    "projected_mass_derivative_g_per_x",
]
