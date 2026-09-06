from __future__ import annotations

import math
from collections.abc import Callable

B0_YEAR = 4.482974815542e9
DAYS_PER_YEAR = 365.25
HORIZON_DAYS = 3.0 * DAYS_PER_YEAR
SIGNAL_TOTAL = 30.0
SIGNAL_RATE = SIGNAL_TOTAL / HORIZON_DAYS
B0_RATE_DAY = B0_YEAR / DAYS_PER_YEAR
K_LOG10_450 = math.log(10.0) / 450.0
AUTHORITY_CAP_DAY = 900.0


def stable_h(x: float) -> float:
    """Return (1+x) log(1+x) - x with cancellation-safe small-x series."""
    if x < 0:
        raise ValueError("x must be non-negative")
    if x < 1e-4:
        # sum_{n=2}^inf (-1)^n x^n/[n(n-1)]
        xpow = x * x
        total = 0.5 * xpow
        for n in range(3, 12):
            xpow *= x
            total += ((-1.0) ** n) * xpow / (n * (n - 1))
        return total
    return (1.0 + x) * math.log1p(x) - x


def background_rate_day(t_day: float, branch: str) -> float:
    if t_day < 0 or t_day > HORIZON_DAYS:
        raise ValueError("t_day outside frozen horizon")
    if branch == "stress_3y":
        return B0_RATE_DAY * math.exp(-K_LOG10_450 * t_day)
    if branch == "authority_capped_900d":
        if t_day <= AUTHORITY_CAP_DAY:
            return B0_RATE_DAY * math.exp(-K_LOG10_450 * t_day)
        return B0_RATE_DAY / 100.0
    raise ValueError(f"unknown branch: {branch}")


def simpson_integral(func: Callable[[float], float], a: float, b: float, n: int) -> float:
    if n <= 0 or n % 2:
        raise ValueError("n must be a positive even integer")
    h = (b - a) / n
    total = func(a) + func(b)
    total += 4.0 * sum(func(a + i * h) for i in range(1, n, 2))
    total += 2.0 * sum(func(a + i * h) for i in range(2, n, 2))
    return total * h / 3.0


def _segments(branch: str) -> tuple[tuple[float, float], ...]:
    if branch == "authority_capped_900d":
        return ((0.0, AUTHORITY_CAP_DAY), (AUTHORITY_CAP_DAY, HORIZON_DAYS))
    if branch == "stress_3y":
        return ((0.0, HORIZON_DAYS),)
    raise ValueError(f"unknown branch: {branch}")


def _segment_grid(total_n: int, segment: tuple[float, float]) -> int:
    a, b = segment
    fraction = (b - a) / HORIZON_DAYS
    n = max(2, int(round(total_n * fraction)))
    if n % 2:
        n += 1
    return n


def integrated_background(branch: str, *, n: int = 8192) -> float:
    return sum(
        simpson_integral(
            lambda t: background_rate_day(t, branch), a, b, _segment_grid(n, (a, b))
        )
        for a, b in _segments(branch)
    )


def time_asimov_q(branch: str, rejection: float = 1.0, *, n: int = 8192) -> float:
    if rejection <= 0:
        raise ValueError("rejection must be positive")

    def integrand(t: float) -> float:
        b = background_rate_day(t, branch) / rejection
        x = SIGNAL_RATE / b
        return 2.0 * b * stable_h(x)

    q = sum(
        simpson_integral(integrand, a, b, _segment_grid(n, (a, b)))
        for a, b in _segments(branch)
    )
    if q <= 0 or not math.isfinite(q):
        raise RuntimeError("invalid time Asimov q")
    return q


def count_asimov_q(branch: str, rejection: float = 1.0, *, n: int = 8192) -> float:
    if rejection <= 0:
        raise ValueError("rejection must be positive")
    b = integrated_background(branch, n=n) / rejection
    x = SIGNAL_TOTAL / b
    q = 2.0 * b * stable_h(x)
    if q <= 0 or not math.isfinite(q):
        raise RuntimeError("invalid count Asimov q")
    return q


def solve_rejection_for_q(
    qfunc: Callable[[float], float], target_q: float = 25.0, *, rtol: float = 1e-11
) -> float:
    if target_q <= 0 or rtol <= 0:
        raise ValueError("target_q and rtol must be positive")
    lo = 1.0
    hi = 10.0
    while qfunc(hi) < target_q:
        hi *= 10.0
        if hi > 1e16:
            raise RuntimeError("failed to bracket rejection")
    for _ in range(256):
        mid = math.sqrt(lo * hi)
        if qfunc(mid) < target_q:
            lo = mid
        else:
            hi = mid
        if hi / lo - 1.0 <= rtol:
            break
    return math.sqrt(lo * hi)


def fisher_local_q(branch: str, *, n: int = 8192) -> float:
    # Local weak-signal information diagnostic at mu=0; never extrapolate it to 5 sigma.
    return sum(
        simpson_integral(
            lambda t: (SIGNAL_RATE * SIGNAL_RATE) / background_rate_day(t, branch),
            a,
            b,
            _segment_grid(n, (a, b)),
        )
        for a, b in _segments(branch)
    )


def evaluate_branch(branch: str, *, n: int = 8192) -> dict[str, float]:
    q0 = time_asimov_q(branch, n=n)
    bint = integrated_background(branch, n=n)
    r_time = solve_rejection_for_q(lambda r: time_asimov_q(branch, r, n=n))
    r_count = solve_rejection_for_q(lambda r: count_asimov_q(branch, r, n=n))
    return {
        "integrated_background": bint,
        "unsuppressed_time_q": q0,
        "unsuppressed_time_z": math.sqrt(q0),
        "fisher_local_q": fisher_local_q(branch, n=n),
        "rejection_time_5sigma": r_time,
        "rejection_count_5sigma": r_count,
        "time_shape_rejection_advantage": r_count / r_time,
        "end_reduction": B0_RATE_DAY / background_rate_day(HORIZON_DAYS, branch),
    }


def build_time_likelihood_map(*, n: int = 8192) -> dict[str, object]:
    return {
        "horizon_days": HORIZON_DAYS,
        "signal_total": SIGNAL_TOTAL,
        "branches": {
            branch: evaluate_branch(branch, n=n)
            for branch in ("authority_capped_900d", "stress_3y")
        },
    }
