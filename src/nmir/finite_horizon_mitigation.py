from __future__ import annotations

import math

from .background_nuisance import max_background_for_significance_with_uncertainty

G0053 = 4.1485517170734453e9
B0053 = 4.482974815542e9
S0 = 10.0
TARGET_Z = 5.0
DELTA_B = 0.30
DAYS_PER_YEAR = 365.25


def projection_reduction(days: float) -> float:
    if days < 0:
        raise ValueError("days must be non-negative")
    return 10.0 ** (days / 450.0)


def background_ceiling(signal: float) -> float:
    return max_background_for_significance_with_uncertainty(
        signal, TARGET_Z, DELTA_B
    )


def required_other_rejection(
    time_reduction: float,
    signal_acceptance: float,
    *,
    restore_signal_with_exposure: bool,
) -> float:
    if time_reduction <= 0:
        raise ValueError("time_reduction must be positive")
    if not (0.0 < signal_acceptance <= 1.0):
        raise ValueError("signal_acceptance must be in (0,1]")

    background_after_time = B0053 / time_reduction
    if restore_signal_with_exposure:
        background_before_remaining_cut = background_after_time / signal_acceptance
        ceiling = background_ceiling(S0)
    else:
        background_before_remaining_cut = background_after_time
        ceiling = background_ceiling(S0 * signal_acceptance)

    result = background_before_remaining_cut / ceiling
    if result <= 0 or not math.isfinite(result):
        raise RuntimeError("invalid rejection requirement")
    return result


def equal_factor(requirement: float, n_handles: int) -> float:
    if requirement <= 0:
        raise ValueError("requirement must be positive")
    if n_handles < 1:
        raise ValueError("n_handles must be >=1")
    return requirement ** (1.0 / n_handles)


def build_budget() -> dict:
    time_scenarios = {
        "authority_cap_100x": 100.0,
        "stress_extrapolation_3y": projection_reduction(3.0 * DAYS_PER_YEAR),
    }
    acceptances = (1.0, 0.9, 0.8, 0.7, 0.5, 0.3)
    out: dict[str, object] = {
        "bmax_s10_5sigma_delta30": background_ceiling(S0),
        "time_scenarios": {},
    }
    scenario_out = out["time_scenarios"]
    assert isinstance(scenario_out, dict)

    for name, time_factor in time_scenarios.items():
        req_full_acceptance = G0053 / time_factor
        rows = {}
        for eps in acceptances:
            rows[str(eps)] = {
                "fixed_exposure": required_other_rejection(
                    time_factor, eps, restore_signal_with_exposure=False
                ),
                "signal_restored_exposure": required_other_rejection(
                    time_factor, eps, restore_signal_with_exposure=True
                ),
            }
        scenario_out[name] = {
            "time_reduction": time_factor,
            "residual_requirement_full_acceptance": req_full_acceptance,
            "residual_decades_full_acceptance": math.log10(req_full_acceptance),
            "equal_independent_factor_diagnostic": {
                str(n): equal_factor(req_full_acceptance, n) for n in (2, 3, 4, 5)
            },
            "acceptance_budget": rows,
        }
    return out
