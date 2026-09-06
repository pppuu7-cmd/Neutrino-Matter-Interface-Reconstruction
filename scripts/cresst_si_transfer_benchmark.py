from __future__ import annotations

import json
import math
from pathlib import Path

from nmir.cevns_solar_optimize import load_all_spectra, read_fluxes, read_manifest, read_targets
from nmir.cresst_si_transfer import (
    ALL_CUTS_PLATEAU,
    TRIGGER_PLATEAU,
    cresst_factorized_surrogate_efficiency,
    cresst_trigger_efficiency,
    hard_step_efficiency,
    total_rate_with_efficiency,
)

TARGETS = Path("data/cevns_target_candidates_exact_mass.csv")
FLUXES = Path("data/solar_flux_b16.csv")
MANIFEST = Path("data/solar_spectrum_manifest.csv")
BE7_GROUND = Path("data/be7_bahcall1994_ground_profile.csv")
FROZEN_IDEAL_RATE = 4.3476963498860904e-3
DAYS_PER_YEAR = 365.25
ACTUAL_CRESST_MASS_KG = 0.00035
GOAL_EVENTS_PER_YEAR = 10.0


def main() -> None:
    targets = read_targets(TARGETS)
    si = next(t for t in targets if t.name == "Si28")
    fluxes = read_fluxes(FLUXES)
    manifest = read_manifest(MANIFEST)
    spectra = load_all_spectra(manifest, BE7_GROUND)

    ideal = total_rate_with_efficiency(si, hard_step_efficiency, fluxes, manifest, spectra)
    trigger = total_rate_with_efficiency(si, cresst_trigger_efficiency, fluxes, manifest, spectra)
    surrogate = total_rate_with_efficiency(si, cresst_factorized_surrogate_efficiency, fluxes, manifest, spectra)

    r_ideal = float(ideal["total_events_per_kg_day"])
    r_trigger = float(trigger["total_events_per_kg_day"])
    r_surrogate = float(surrogate["total_events_per_kg_day"])

    hard_rel_error = abs(r_ideal / FROZEN_IDEAL_RATE - 1.0)
    plateau_ratio = ALL_CUTS_PLATEAU / TRIGGER_PLATEAU
    surrogate_trigger_ratio = r_surrogate / r_trigger
    ratio_rel_error = abs(surrogate_trigger_ratio / plateau_ratio - 1.0)

    ordering_ok = 0.0 < r_surrogate < r_trigger < r_ideal
    trigger_bound_ok = r_trigger <= TRIGGER_PLATEAU * r_ideal * (1.0 + 1e-12)
    finite_positive = all(math.isfinite(x) and x > 0.0 for x in (r_ideal, r_trigger, r_surrogate))

    def kg_for_10(rate: float) -> float:
        return GOAL_EVENTS_PER_YEAR / (rate * DAYS_PER_YEAR)

    def events_for_actual_mass(rate: float) -> float:
        return rate * ACTUAL_CRESST_MASS_KG * DAYS_PER_YEAR

    passed = (
        hard_rel_error <= 5e-3
        and ordering_ok
        and trigger_bound_ok
        and ratio_rel_error <= 1e-10
        and finite_positive
    )
    status = "PASS_CRESST_SI_TRANSFER_FOLD" if passed else "FAIL_CRESST_SI_TRANSFER_FOLD"

    print(json.dumps({
        "status": status,
        "scope": "Si28 B16-GS98 full-solar CEvNS above a 10-eV analysis floor folded through published CRESST trigger anchors and an explicitly factorized all-cuts surrogate",
        "frozen_0049_ideal_rate_events_per_kg_day": FROZEN_IDEAL_RATE,
        "hard_step": {
            "rate_events_per_kg_day": r_ideal,
            "relative_error_vs_0049": hard_rel_error,
            "effective_kg_for_10_events_per_year": kg_for_10(r_ideal),
            "events_per_year_at_0p35g": events_for_actual_mass(r_ideal),
            "components_events_per_kg_day": ideal["components_events_per_kg_day"],
        },
        "published_trigger_turnon": {
            "rate_events_per_kg_day": r_trigger,
            "retained_fraction_of_ideal": r_trigger / r_ideal,
            "effective_kg_for_10_events_per_year": kg_for_10(r_trigger),
            "events_per_year_at_0p35g": events_for_actual_mass(r_trigger),
            "components_events_per_kg_day": trigger["components_events_per_kg_day"],
        },
        "factorized_all_cuts_surrogate": {
            "rate_events_per_kg_day": r_surrogate,
            "retained_fraction_of_ideal": r_surrogate / r_ideal,
            "effective_kg_for_10_events_per_year": kg_for_10(r_surrogate),
            "events_per_year_at_0p35g": events_for_actual_mass(r_surrogate),
            "components_events_per_kg_day": surrogate["components_events_per_kg_day"],
        },
        "plateau_ratio_allcuts_over_trigger": plateau_ratio,
        "rate_ratio_surrogate_over_trigger": surrogate_trigger_ratio,
        "rate_ratio_relative_error": ratio_rel_error,
        "ordering_ok": ordering_ok,
        "trigger_plateau_bound_ok": trigger_bound_ok,
        "guards": [
            "full green efficiency below 14 eV is not analytically published in the paper text",
            "factorized all-cuts curve is a labelled surrogate, not a measured full transfer function",
            "actual CRESST low-energy excess/background is not included in this rate-only fold",
            "this is detector acceptance, not weak-interaction enhancement or neutrino-energy gain",
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
