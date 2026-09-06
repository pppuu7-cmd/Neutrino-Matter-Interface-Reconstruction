#!/usr/bin/env python3
from __future__ import annotations

import json

from nmir.cevns_threshold import AR40_ATOMIC_MASS_U, ar40_reference_map, nuclear_mass_mev, recoil_max_mev


def main() -> None:
    result = ar40_reference_map(40.0)
    mass = nuclear_mass_mev(AR40_ATOMIC_MASS_U)
    result["be7_margin_ev"] = recoil_max_mev(0.8618, mass) * 1.0e6 - 40.0
    result["classification"] = "F3_KINEMATIC_SOURCE_OPENING_ONLY"
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
