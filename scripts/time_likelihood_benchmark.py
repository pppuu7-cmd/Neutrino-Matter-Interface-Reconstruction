#!/usr/bin/env python3
from __future__ import annotations

import json
import math

from nmir.time_likelihood import build_time_likelihood_map, evaluate_branch


def main() -> None:
    result = build_time_likelihood_map(n=8192)
    branches = result["branches"]

    auth = branches["authority_capped_900d"]
    stress = branches["stress_3y"]

    assert math.isclose(auth["end_reduction"], 100.0, rel_tol=1e-13)
    assert stress["end_reduction"] > 100.0

    for name in ("authority_capped_900d", "stress_3y"):
        row = branches[name]
        assert row["rejection_time_5sigma"] < row["rejection_count_5sigma"]
        assert row["rejection_time_5sigma"] > 1e6
        assert row["unsuppressed_time_z"] < 0.01
        coarse = evaluate_branch(name, n=4096)
        assert math.isclose(
            coarse["rejection_time_5sigma"], row["rejection_time_5sigma"], rel_tol=1e-8
        )
        assert math.isclose(
            coarse["rejection_count_5sigma"], row["rejection_count_5sigma"], rel_tol=1e-8
        )

    payload = {
        "status": "PASS_TIME_LIKELIHOOD_BOUND",
        "classification": "TIME_SHAPE_USEFUL_BUT_INSUFFICIENT",
        "scope": "3-year exact extended-Poisson Asimov event-time discrimination under perfectly known single-component stress backgrounds",
        "guards": [
            "known time shape and normalization are deliberately optimistic",
            "stress_3y continuation beyond 900d is not a CRESST forecast",
            "authority_capped_900d stops additional waiting benefit at 100x",
            "weak-signal Fisher information is local diagnostic only and is not extrapolated to 5 sigma",
            "multi-component LEE, floors, resets and decay-parameter nuisance are not assigned guessed penalties",
        ],
        **result,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
