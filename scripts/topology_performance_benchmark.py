#!/usr/bin/env python3
from __future__ import annotations

import json
import math

from nmir.topology_performance import ACCEPTANCES, BRANCHES, required_topology_envelope

FROZEN_0057 = {
    "authority_capped_900d": 17757030.4169906,
    "stress_3y": 14440370.654436817,
}


def main() -> None:
    fine = required_topology_envelope(n=8192)
    coarse = required_topology_envelope(n=4096)

    for branch in BRANCHES:
        frow = fine["branches"][branch]
        crow = coarse["branches"][branch]
        assert math.isclose(
            frow["base_rejection_full_acceptance"], FROZEN_0057[branch], rel_tol=1e-8
        )
        previous_fixed = 0.0
        previous_restored = 0.0
        for eps in ACCEPTANCES:
            key = str(eps)
            row = frow["acceptance_budget"][key]
            c = crow["acceptance_budget"][key]
            assert row["fixed_exposure"] >= previous_fixed
            assert row["signal_restored_exposure"] >= previous_restored
            previous_fixed = row["fixed_exposure"]
            previous_restored = row["signal_restored_exposure"]
            assert row["fixed_exposure"] > 1e6
            assert row["signal_restored_exposure"] > 1e6
            assert math.isclose(
                row["signal_restored_exposure"],
                frow["base_rejection_full_acceptance"] / eps,
                rel_tol=2e-14,
            )
            if eps < 1.0:
                assert row["fixed_exposure"] >= row["signal_restored_exposure"]
            if eps in (1.0, 0.5, 0.3):
                assert math.isclose(
                    row["fixed_exposure"], c["fixed_exposure"], rel_tol=1e-8
                )

    payload = {
        "status": "PASS_REQUIRED_TOPOLOGY_PERFORMANCE_ENVELOPE",
        "classification": "PUBLIC_ACHIEVEMENT_ANCHOR_OPEN",
        "scope": "required measured detector/topology rejection versus CEvNS-like bulk-event acceptance using the exact frozen 0057 three-year time likelihood",
        "guards": [
            "requirements are not claimed achieved DoubleTES performance",
            "time-aware rejection requirement already includes temporal discrimination and is not multiplied by 0056/0057 factors",
            "fixed exposure charges lost signal directly",
            "signal-restored exposure charges the corresponding increase in pre-cut background",
            "known background normalization and time shape remain an optimistic 0057 assumption",
        ],
        **fine,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
