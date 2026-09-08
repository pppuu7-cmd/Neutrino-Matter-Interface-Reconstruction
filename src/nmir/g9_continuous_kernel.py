"""Monotone-branch radial-kernel primitives for NMIR iteration 0089d.

This module never discovers turning points. Callers must supply the certified
branch boundaries from iteration 0089c. The authoritative signed map remains
scalar; dense-array evaluators are validation replicas only.
"""
from __future__ import annotations

import math
from typing import Callable, Iterable


class KernelBlocked(RuntimeError):
    pass


class KernelScientificFail(RuntimeError):
    pass


def bisect_monotone_target(
    yfn: Callable[[float], float],
    lo: float,
    hi: float,
    target: float,
    *,
    width: float = 1e-12,
    residual_tol: float | None = None,
) -> float:
    """Solve y(x)=target on a certified monotone branch by deterministic bisection.

    When ``residual_tol`` is supplied, both the frozen width requirement and the
    frozen map-residual requirement must be met. This is a numerical-conformance
    condition, not a relaxed scientific criterion.
    """
    yl = yfn(lo) - target
    yr = yfn(hi) - target
    if not (math.isfinite(yl) and math.isfinite(yr)):
        raise KernelBlocked("non-finite branch endpoint value")
    if yl == 0.0:
        return lo
    if yr == 0.0:
        return hi
    if yl * yr > 0.0:
        raise KernelBlocked("target is not bracketed by certified monotone branch")
    for _ in range(256):
        mid = 0.5 * (lo + hi)
        ym = yfn(mid) - target
        if not math.isfinite(ym):
            raise KernelBlocked("non-finite target bisection value")
        width_ok = (hi - lo) <= width
        residual_ok = residual_tol is None or abs(ym) <= residual_tol
        if ym == 0.0 or (width_ok and residual_ok):
            return mid
        if yl * ym <= 0.0:
            hi, yr = mid, ym
        else:
            lo, yl = mid, ym
        if mid == lo or mid == hi:
            break
    candidate = lo if abs(yl) <= abs(yr) else hi
    residual = abs(yfn(candidate) - target)
    if (hi - lo) <= width and (residual_tol is None or residual <= residual_tol):
        return candidate
    raise KernelBlocked("bisection cannot satisfy frozen width/residual requirements")


def branch_crossings(
    yfn: Callable[[float], float], lo: float, hi: float, radius: float
) -> dict[float, float]:
    """Solve the preregistered targets 0,+r,-r when endpoint-bracketed."""
    ylo, yhi = yfn(lo), yfn(hi)
    if not (math.isfinite(ylo) and math.isfinite(yhi)):
        raise KernelBlocked("non-finite branch endpoint map")
    low, high = min(ylo, yhi), max(ylo, yhi)
    roots: dict[float, float] = {}
    residual_tol = max(1e-4, 2e-10 * float(radius))
    for target in (0.0, float(radius), -float(radius)):
        if low <= target <= high:
            roots[target] = bisect_monotone_target(
                yfn, lo, hi, target, residual_tol=residual_tol
            )
    return roots


def accepted_branch_interval(
    yfn: Callable[[float], float],
    lo: float,
    hi: float,
    radius: float,
    roots: dict[float, float],
) -> tuple[float, float] | None:
    """Return the unique |y|<=r subset of a certified monotone branch."""
    ylo, yhi = yfn(lo), yfn(hi)
    increasing = yhi > ylo
    if yhi == ylo:
        raise KernelBlocked("certified monotone branch has equal endpoint values")
    low_y, high_y = (ylo, yhi) if increasing else (yhi, ylo)
    keep_low = max(low_y, -radius)
    keep_high = min(high_y, radius)
    if keep_low > keep_high:
        return None

    def x_for(value: float) -> float:
        if value == ylo:
            return lo
        if value == yhi:
            return hi
        if value in roots:
            return roots[value]
        return bisect_monotone_target(
            yfn,
            lo,
            hi,
            value,
            residual_tol=max(1e-4, 2e-10 * float(radius)),
        )

    x_a = x_for(keep_low)
    x_b = x_for(keep_high)
    return (min(x_a, x_b), max(x_a, x_b))


def merge_adjacent_with_parents(
    intervals: Iterable[tuple[float, float, int]], *, tol: float = 2e-11
) -> list[dict]:
    """Merge only adjacent/tolerance-equivalent intervals; reject overlap."""
    rows = sorted((float(a), float(b), int(p)) for a, b, p in intervals)
    out: list[dict] = []
    for lo, hi, parent in rows:
        if hi < lo:
            raise KernelScientificFail("negative-width accepted interval")
        if not out:
            out.append({"lo": lo, "hi": hi, "parents": [parent]})
            continue
        prev = out[-1]
        if lo < prev["hi"] - tol:
            raise KernelScientificFail("positive-width accepted intervals overlap")
        if abs(lo - prev["hi"]) <= tol:
            prev["hi"] = max(prev["hi"], hi)
            prev["parents"].append(parent)
        else:
            out.append({"lo": lo, "hi": hi, "parents": [parent]})
    return out


def annular_area_cm2(intervals: Iterable[dict], radius_sun_cm: float) -> float:
    terms = [row["hi"] ** 2 - row["lo"] ** 2 for row in intervals]
    return math.pi * radius_sun_cm**2 * math.fsum(terms)


def indicator_midpoint_area_cm2(
    xs,
    accepted,
    *,
    dx: float,
    radius_sun_cm: float,
) -> float:
    """Composite midpoint replica of integral 2*pi*R^2*x*1[accepted] dx."""
    total = math.fsum(float(x) for x, ok in zip(xs, accepted) if bool(ok))
    return 2.0 * math.pi * radius_sun_cm**2 * dx * total


__all__ = [
    "KernelBlocked",
    "KernelScientificFail",
    "bisect_monotone_target",
    "branch_crossings",
    "accepted_branch_interval",
    "merge_adjacent_with_parents",
    "annular_area_cm2",
    "indicator_midpoint_area_cm2",
]
