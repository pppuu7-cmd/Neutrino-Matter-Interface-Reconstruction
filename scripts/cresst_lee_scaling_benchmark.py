from __future__ import annotations

import json

from nmir.cresst_lee_scaling import (
    BLIND_EXPOSURE_KG_DAY,
    BMAX,
    DAYS_PER_YEAR,
    M10_KG,
    accepted_lee_rate_per_kg_day,
    corrected_lee_rate_per_kg_day,
    rejection_factor,
)


def main() -> None:
    accepted_20k = accepted_lee_rate_per_kg_day(intervals=20_000)
    accepted_40k = accepted_lee_rate_per_kg_day(intervals=40_000)
    corrected = corrected_lee_rate_per_kg_day(intervals=40_000)
    convergence = abs(accepted_40k / accepted_20k - 1.0)

    accepted_blind = accepted_40k * BLIND_EXPOSURE_KG_DAY
    accepted_per_kg_year = accepted_40k * DAYS_PER_YEAR
    accepted_scaled_year = accepted_per_kg_year * M10_KG

    requirements = {}
    all_need_rejection = True
    for key, bmax in BMAX.items():
        factor = rejection_factor(accepted_scaled_year, bmax)
        all_need_rejection &= factor > 1.0
        requirements[key] = {
            "bmax_events_per_year": bmax,
            "required_rejection_factor": factor,
            "required_surviving_fraction": 1.0 / factor,
        }

    passed = (
        corrected > accepted_40k > 0.0
        and convergence <= 1e-5
        and all_need_rejection
    )
    status = "PASS_LEE_SCALING_GAP_STRESS" if passed else "FAIL_LEE_SCALING_GAP_STRESS"

    print(json.dumps({
        "status": status,
        "scope": "central published CRESST Si LEE fit, 10-300 eV, folded through the 0052 factorized transfer surrogate and stress-scaled linearly per kg to the 0052 M10 target",
        "integration": {
            "efficiency_corrected_lee_rate_events_per_kg_day": corrected,
            "accepted_lee_rate_events_per_kg_day": accepted_40k,
            "accepted_over_corrected": accepted_40k / corrected,
            "point_doubling_relative_change": convergence,
        },
        "published_blind_exposure_kg_day": BLIND_EXPOSURE_KG_DAY,
        "central_fit_expected_accepted_events_in_blind_exposure": accepted_blind,
        "accepted_lee_events_per_kg_year": accepted_per_kg_year,
        "scaled_mass_for_10_solar_cevns_per_year_kg": M10_KG,
        "stress_scaled_accepted_lee_events_per_year": accepted_scaled_year,
        "discovery_requirements": requirements,
        "guards": [
            "LEE fit is empirical and has no assigned physical origin",
            "linear per-kg scaling to 9.77 kg is a stress extrapolation, not a prediction",
            "required rejection can be supplied by intrinsic LEE suppression, discrimination, statistical separation, or their combination",
            "do not call every LEE event a known physical background; it is a competing accepted low-energy event population",
            "no weak-interaction or neutrino-energy enhancement is implied",
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
