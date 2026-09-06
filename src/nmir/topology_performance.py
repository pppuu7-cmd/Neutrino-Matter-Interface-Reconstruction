from __future__ import annotations

import math
from collections.abc import Callable

from .time_likelihood import (
    AUTHORITY_CAP_DAY,
    HORIZON_DAYS,
    SIGNAL_TOTAL,
    background_rate_day,
    simpson_integral,
    stable_h,
)

ACCEPTANCES = (1.0, 0.9, 0.8, 0.7, 0.5, 0.3)
BRANCHES = ("authority_capped_900d", "stress_3y")


def _segments(branch: str) -> tuple[tuple[float, float], ...]:
    if branch == "authority_capped_900d":
        return ((0.0, AUTHORITY_CAP_DAY), (AUTHORITY_CAP_DAY, HORIZON_DAYS))
    if branch == "stress_3y":
        return ((0.0, HORIZON_DAYS),)
    raise ValueError(f"unknown branch: {branch}")


def _segment_grid(total_n: int, a: float, b: float) -> int:
    n = max(2, int(round(total_n * (b - a) / HORIZON_DAYS)))
    if n % 2:
        n += 1
    return n


def time_q_with_signal(
    branch: str,
    rejection: float,
    signal_total: float,
    *,
    n: int = 8192,
) -> float:
    if rejection <= 0:
        raise ValueError("rejection must be positive")
    if signal_total <= 0:
        raise ValueError("signal_total must be positive")
    s = signal_total / HORIZON_DAYS

    def integrand(t: float) -> float:
        b = background_rate_day(t, branch) / rejection
        return 2.0 * b * stable_h(s / b)

    q = sum(
        simpson_integral(
            integrand, a, b, _segment_grid(n, a, b)
        )
        for a, b in _segments(branch)
    )
    if q <= 0 or not math.isfinite(q):
        raise RuntimeError("invalid time-domain q")
    return q


def solve_rejection(
    branch: str,
    signal_total: float,
    *,
    target_q: float = 25.0,
    n: int = 8192,
    rtol: float = 1e-11,
) -> float:
    def qfunc(r: float) -> float:
        return time_q_with_signal(branch, r, signal_total, n=n)

    lo, hi = 1.0, 10.0
    while qfunc(hi) < target_q:
        hi *= 10.0
        if hi > 1e16:
            raise RuntimeError("failed to bracket topology rejection")
    for _ in range(256):
        mid = math.sqrt(lo * hi)
        if qfunc(mid) < target_q:
            lo = mid
        else:
            hi = mid
        if hi / lo - 1.0 <= rtol:
            break
    return math.sqrt(lo * hi)


def required_topology_envelope(*, n: int = 8192) -> dict[str, object]:
    branches: dict[str, object] = {}
    for branch in BRANCHES:
        base = solve_rejection(branch, SIGNAL_TOTAL, n=n)
        rows: dict[str, object] = {}
        for eps in ACCEPTANCES:
            fixed = solve_rejection(branch, SIGNAL_TOTAL * eps, n=n)
            restored = base / eps
            rows[str(eps)] = {
                "fixed_exposure": fixed,
                "signal_restored_exposure": restored,
                "fixed_penalty_vs_full_acceptance": fixed / base,
                "restored_penalty_vs_full_acceptance": 1.0 / eps,
            }
        branches[branch] = {
            "base_rejection_full_acceptance": base,
            "acceptance_budget": rows,
        }
    return {
        "horizon_days": HORIZON_DAYS,
        "preselection_signal_total": SIGNAL_TOTAL,
        "branches": branches,
    }
