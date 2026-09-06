from __future__ import annotations

import json

from nmir.higher_body_strength import (
    R_EMPIRICAL_EXTRA,
    classify,
    required_extra_amplitude_for_power,
    stress_ladder,
)


def main() -> None:
    bridge = required_extra_amplitude_for_power(1.0)
    points = [
        {
            "safety_factor": p.safety_factor,
            "r_two_body": p.r_two_body,
            "power_w_per_kg": p.power_w_per_kg,
            "deficit_to_1w": p.deficit_to_1w,
        }
        for p in stress_ladder()
    ]
    print(json.dumps({
        "status": classify(),
        "scope": "empirical/EFT-anchored stress envelope for finite-range genuine higher-body SM nuclear-current amplitudes; not a universal coefficient theorem",
        "largest_empirical_extra_amplitude_anchor": R_EMPIRICAL_EXTRA,
        "required_extra_amplitude_to_1w": bridge,
        "bridge_over_empirical_anchor": bridge / R_EMPIRICAL_EXTRA,
        "stress_points": points,
        "guards": [
            "no resonance/gravity/metastable/structure/BSM gain multiplied",
            "stored/daughter/external energy excluded",
            "unknown universal contact/operator coefficient residual remains outside scope",
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
