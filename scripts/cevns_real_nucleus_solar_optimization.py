from __future__ import annotations

import json
from pathlib import Path

from nmir.cevns_solar_optimize import (
    load_all_spectra,
    read_fluxes,
    read_manifest,
    read_targets,
    total_rate_row,
)

TARGETS = Path("data/cevns_target_candidates.csv")
FLUXES = Path("data/solar_flux_b16.csv")
MANIFEST = Path("data/solar_spectrum_manifest.csv")
BE7_GROUND = Path("data/be7_bahcall1994_ground_profile.csv")
THRESHOLDS = [1.0, 3.0, 5.0, 10.0, 20.0, 40.0]


def main() -> None:
    targets = read_targets(TARGETS)
    fluxes = read_fluxes(FLUXES)
    manifest = read_manifest(MANIFEST)
    spectra = load_all_spectra(manifest, BE7_GROUND)

    threshold_results = []
    for threshold in THRESHOLDS:
        rows = [total_rate_row(t, threshold, fluxes, manifest, spectra, use_helm=True) for t in targets]
        rows.sort(key=lambda r: r["total_events_per_kg_day"], reverse=True)
        winner = rows[0]
        runner_up = rows[1]
        winner_target = next(t for t in targets if t.name == winner["target"])
        no_helm = total_rate_row(winner_target, threshold, fluxes, manifest, spectra, use_helm=False)
        suppression = winner["total_events_per_kg_day"] / no_helm["total_events_per_kg_day"] if no_helm["total_events_per_kg_day"] else 1.0
        threshold_results.append({
            "threshold_ev": threshold,
            "winner": winner,
            "runner_up": runner_up,
            "winner_no_helm_total_events_per_kg_day": no_helm["total_events_per_kg_day"],
            "winner_helm_suppression_ratio": suppression,
            "all_targets": rows,
        })

    print(json.dumps({
        "status": "PASS_REAL_NUCLEUS_SOLAR_OPTIMIZATION",
        "scope": "pure-isotope physics-only B16-GS98 full-solar ideal CEvNS events/kg/day; actual Z/N and Helm form factor; detector efficiency/chemistry/abundance excluded",
        "thresholds_ev": THRESHOLDS,
        "results": threshold_results,
        "interpretation": "Ranks the frozen real-nucleus candidate set by full-source solar CEvNS counts per kg. A target win is a detector-physics design result, not microscopic interaction enhancement and not neutrino-energy gain.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
