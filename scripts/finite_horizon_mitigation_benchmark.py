#!/usr/bin/env python3
from __future__ import annotations

import json

from nmir.finite_horizon_mitigation import G0053, build_budget


def main() -> None:
    budget = build_budget()
    scenarios = budget["time_scenarios"]
    authority = scenarios["authority_cap_100x"]
    stress = scenarios["stress_extrapolation_3y"]

    assert abs(budget["bmax_s10_5sigma_delta30"] - 1.0806120114381677) < 1e-11
    assert stress["time_reduction"] > authority["time_reduction"]
    assert stress["residual_requirement_full_acceptance"] < authority["residual_requirement_full_acceptance"]
    assert abs(authority["residual_requirement_full_acceptance"] - G0053 / 100.0) / (G0053 / 100.0) < 1e-12

    payload = {
        "status": "PASS_FINITE_HORIZON_MITIGATION_BUDGET",
        "scope": "3-year factorized LEE requirements map with authority-capped and stress-extrapolated time branches; signal acceptance explicitly charged",
        "guards": [
            "100x authority-cap and 272.27x stress-extrapolation are alternative time branches and are never multiplied",
            "stress continuation beyond 900d is not a CRESST forecast",
            "DoubleTES topology has no frozen comparable numeric rejection*acceptance factor in the 0053 window",
            "equal-factor diagnostics assume no experimental independence and are scale diagnostics only",
        ],
        **budget,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
