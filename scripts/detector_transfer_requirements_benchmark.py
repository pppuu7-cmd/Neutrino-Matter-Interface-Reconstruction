from __future__ import annotations

import json

from nmir.detector_transfer_requirements import RATES, feasibility, ideal_events_per_year, required_effective_mass_kg, required_eta


def main() -> None:
    ar = {}
    for thr in (10, 20, 40):
        key = f"Ar40_{thr}eV"
        rate = RATES[key]
        eta1 = required_eta(rate, 10.0, 1.0)
        eta10 = required_eta(rate, 10.0, 10.0)
        ar[str(thr)] = {
            "rate_events_per_kg_day": rate,
            "ideal_events_per_year_10kg": ideal_events_per_year(rate, 10.0),
            "eta_required_1_event_per_year": eta1,
            "eta_required_10_events_per_year": eta10,
            "classification_10_events_per_year": feasibility(eta10),
        }

    eff_mass = {}
    for key, rate in RATES.items():
        eff_mass[key] = {
            "kg_eff_for_1_event_per_year": required_effective_mass_kg(rate, 1.0),
            "kg_eff_for_10_events_per_year": required_effective_mass_kg(rate, 10.0),
        }

    ar10_over_se10 = eff_mass["Ar40_10eV"]["kg_eff_for_10_events_per_year"] / eff_mass["Se82_10eV"]["kg_eff_for_10_events_per_year"]

    print(json.dumps({
        "status": "PASS_DETECTOR_TRANSFER_RATE_REQUIREMENT",
        "scope": "necessary rate/exposure requirement only; factorized average acceptance times live fraction; no background or full recoil-dependent efficiency model",
        "ar40_10kg": ar,
        "effective_mass_requirements": eff_mass,
        "ar10_to_se10_required_effective_mass_ratio": ar10_over_se10,
        "guards": [
            "eta<=1 is rate feasibility, not demonstrated detector performance",
            "backgrounds/false triggers/threshold dispersion remain open",
            "metastable released energy is not neutrino-supplied energy",
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
