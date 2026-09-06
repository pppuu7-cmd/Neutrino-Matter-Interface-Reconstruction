from __future__ import annotations

import json

from nmir.lee_waiting_time import (
    DAYS_PER_YEAR,
    G0053,
    TAU_FAST_DAYS,
    TAU_FAST_UNC_DAYS,
    exponential_time_to_reduction,
    first_integer_year_reaching,
    projected_reduction,
    projection_time_to_reduction,
    residual_gap,
)


def main() -> None:
    horizons = {
        "450d": 450.0,
        "900d": 900.0,
        "1y": DAYS_PER_YEAR,
        "3y": 3.0 * DAYS_PER_YEAR,
        "5y": 5.0 * DAYS_PER_YEAR,
        "10y": 10.0 * DAYS_PER_YEAR,
    }
    rows = {}
    previous = None
    monotonic = True
    for name, days in horizons.items():
        reduction = projected_reduction(days)
        gap = residual_gap(G0053, reduction)
        if previous is not None and days > previous[0]:
            monotonic &= gap < previous[1]
        previous = (days, gap)
        rows[name] = {
            "days": days,
            "projection_reduction": reduction,
            "residual_required_improvement": gap,
        }

    t_req = projection_time_to_reduction(G0053)
    fast = {
        "tau_minus_1sigma": exponential_time_to_reduction(G0053, TAU_FAST_DAYS - TAU_FAST_UNC_DAYS),
        "tau_central": exponential_time_to_reduction(G0053, TAU_FAST_DAYS),
        "tau_plus_1sigma": exponential_time_to_reduction(G0053, TAU_FAST_DAYS + TAU_FAST_UNC_DAYS),
    }
    first_year = first_integer_year_reaching(G0053)

    passed = (
        abs(projected_reduction(450.0) / 10.0 - 1.0) <= 1e-14
        and abs(projected_reduction(900.0) / 100.0 - 1.0) <= 1e-14
        and t_req > 900.0
        and monotonic
        and all(value > 0 for value in fast.values())
    )
    status = "PASS_WAITING_TIME_REQUIREMENT_MAP" if passed else "FAIL_WAITING_TIME_REQUIREMENT_MAP"

    print(json.dumps({
        "status": status,
        "scope": "requirements-only stress map: log-linear continuation of the published 10x/450d and 100x/900d CRESST projection benchmarks; fast 10.2d component reported counterfactually and not promoted to whole LEE",
        "frozen_0053_gap_5sigma_delta30": G0053,
        "projection_horizons": rows,
        "projection_time_to_close_gap_days": t_req,
        "projection_time_to_close_gap_years": t_req / DAYS_PER_YEAR,
        "first_integer_year_reaching_gap": first_year,
        "counterfactual_fast_component_time_to_close_days": fast,
        "guards": [
            "R_proj beyond 900d is an NMIR stress extrapolation, not a CRESST forecast",
            "10.2±1.1d is measured for one absorber-band fast component, not the full LEE",
            "waiting changes background in time but does not enhance the neutrino interaction",
            "thermal resets/multiple slow components can invalidate indefinite exponential continuation",
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
