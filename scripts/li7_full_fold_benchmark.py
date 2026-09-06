from __future__ import annotations

import json
from pathlib import Path

from nmir.li7_full_response import li7_two_state_sigma_cm2
from nmir.li7_full_solar_fold import li7_two_state_b16_fold


def main() -> None:
    outdir = Path("artifacts/li7_full_fold")
    outdir.mkdir(parents=True, exist_ok=True)
    result = {
        "response_validation_authority_run": 34037499594,
        "response_validation_total_b8_cm2": 3.813646693502232e-42,
        "response_validation_published_total_b8_cm2": 3.759e-42,
        "fixed_energy_cross_sections_cm2": {
            "pep_1.442_MeV": li7_two_state_sigma_cm2(1.442),
            "5_MeV": li7_two_state_sigma_cm2(5.0),
            "10_MeV": li7_two_state_sigma_cm2(10.0),
        },
        "GS98_MSW": li7_two_state_b16_fold("GS98", outdir / "gs98", oscillated=True),
        "AGSS09met_MSW": li7_two_state_b16_fold("AGSS09met", outdir / "agss09", oscillated=True),
        "GS98_no_osc": li7_two_state_b16_fold("GS98", outdir / "gs98_noosc", oscillated=False),
    }
    path = outdir / "results.json"
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
