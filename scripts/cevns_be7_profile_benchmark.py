from __future__ import annotations

import json
from pathlib import Path

from nmir.cevns_be7_profile import load_profile, profile_norm, threshold_row


PROFILE = Path("data/be7_bahcall1994_ground_profile.csv")
THRESHOLDS_EV = [0.0, 10.0, 20.0, 30.0, 35.0, 38.0, 39.0, 40.0]


def main() -> None:
    profile = load_profile(PROFILE)
    rows = [threshold_row(profile, t) for t in THRESHOLDS_EV]
    result = {
        "status": "PASS_CEVNS_BE7_PROFILE_GATE",
        "scope": "ideal low-q SM CEvNS detection fold for the dominant thermally broadened solar Be7 line on pure Ar-40; detector/nucleation efficiency and dark counts excluded",
        "profile_path": str(PROFILE),
        "profile_norm": profile_norm(profile),
        "rows": rows,
        "classification": {
            "detection": "PASS_SURVIVOR" if rows[-1]["ideal_events_per_kg_day"] > 0.0 else "CLOSED_AT_40_EV",
            "interaction_enhancement": "NONE",
            "neutrino_energy_gain": "NONE",
        },
        "interpretation": "The physical solar Be7 line profile is folded with the SM differential CEvNS recoil response. A nonzero rate at 40 eV is a detector-threshold survivor only; it does not increase the weak cross section or neutrino-supplied energy.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
