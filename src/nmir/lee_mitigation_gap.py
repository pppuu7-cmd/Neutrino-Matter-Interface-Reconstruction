from __future__ import annotations

import math

G0053_5SIGMA_DELTA30 = 4.1485517170734453e9


def residual_gap(required_improvement: float, reduction_factor: float) -> float:
    if required_improvement <= 0 or reduction_factor <= 0:
        raise ValueError("required improvement and reduction factor must be positive")
    value = required_improvement / reduction_factor
    if not math.isfinite(value) or value <= 0:
        raise ValueError("invalid residual gap")
    return value


def projected_residuals() -> dict[int, float]:
    return {factor: residual_gap(G0053_5SIGMA_DELTA30, factor) for factor in (10, 100)}


def classify_public_evidence(*, demonstrated_mechanism: bool, comparable_measured_factor: bool) -> str:
    if comparable_measured_factor:
        return "PASS_MEASURED_LEE_MITIGATION_FACTOR"
    if demonstrated_mechanism:
        return "MECHANISM_SURVIVOR_QUANTITATIVE_GAP_OPEN"
    return "FAIL_NO_LEE_MITIGATION_HANDLE"
