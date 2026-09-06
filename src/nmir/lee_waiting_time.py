from __future__ import annotations

import math

G0053 = 4.1485517170734453e9
DAYS_PER_YEAR = 365.25
PROJECTION_DECADE_DAYS = 450.0
TAU_FAST_DAYS = 10.2
TAU_FAST_UNC_DAYS = 1.1


def projected_reduction(time_days: float) -> float:
    if time_days < 0:
        raise ValueError("time must be non-negative")
    return 10.0 ** (time_days / PROJECTION_DECADE_DAYS)


def exponential_reduction(time_days: float, tau_days: float) -> float:
    if time_days < 0 or tau_days <= 0:
        raise ValueError("time must be non-negative and tau positive")
    return math.exp(time_days / tau_days)


def residual_gap(required_improvement: float, reduction: float) -> float:
    if required_improvement <= 0 or reduction <= 0:
        raise ValueError("inputs must be positive")
    value = required_improvement / reduction
    if not math.isfinite(value) or value <= 0:
        raise ValueError("invalid residual gap")
    return value


def projection_time_to_reduction(reduction: float) -> float:
    if reduction <= 0:
        raise ValueError("reduction must be positive")
    return PROJECTION_DECADE_DAYS * math.log10(reduction)


def exponential_time_to_reduction(reduction: float, tau_days: float) -> float:
    if reduction <= 0 or tau_days <= 0:
        raise ValueError("reduction and tau must be positive")
    return tau_days * math.log(reduction)


def first_integer_year_reaching(required_improvement: float = G0053) -> int:
    if required_improvement <= 1:
        return 0
    years = 0
    while projected_reduction(years * DAYS_PER_YEAR) < required_improvement:
        years += 1
        if years > 1000:
            raise RuntimeError("failed to find finite year")
    return years
