from __future__ import annotations

import json
from pathlib import Path

from nmir.cevns_phase_diagram import (
    COARSE_THRESHOLDS_EV,
    PhaseEvaluator,
    compress_states,
    fine_grid_transition_identity,
    phase_topology,
    refine_transition,
    transition_brackets,
)
from nmir.cevns_solar_optimize import (
    load_all_spectra,
    read_fluxes,
    read_manifest,
    read_targets,
    total_rate_row,
)

TARGETS = Path("data/cevns_target_candidates_exact_mass.csv")
FLUXES = Path("data/solar_flux_b16.csv")
MANIFEST = Path("data/solar_spectrum_manifest.csv")
BE7_GROUND = Path("data/be7_bahcall1994_ground_profile.csv")
REFINE_TOL_EV = 0.02
STABILITY_SUBDIVISIONS = 8


def state_dict(state):
    return {
        "threshold_ev": state.threshold_ev,
        "winner": state.winner,
        "runner_up": state.runner_up,
        "winner_rate_events_per_kg_day": state.winner_rate,
        "runner_up_rate_events_per_kg_day": state.runner_up_rate,
        "winner_margin_fraction": state.margin_fraction,
        "dominant_component": state.dominant_component,
    }


def main() -> None:
    targets = read_targets(TARGETS)
    target_by_name = {target.name: target for target in targets}
    fluxes = read_fluxes(FLUXES)
    manifest = read_manifest(MANIFEST)
    spectra = load_all_spectra(manifest, BE7_GROUND)
    evaluator = PhaseEvaluator(targets, fluxes, manifest, spectra, use_helm=True)

    coarse_states = [evaluator.state(t) for t in COARSE_THRESHOLDS_EV]

    coarse_rows = []
    for state in coarse_states:
        winner_target = target_by_name[state.winner]
        with_helm = state.winner_rate
        no_helm_row = total_rate_row(
            winner_target,
            state.threshold_ev,
            fluxes,
            manifest,
            spectra,
            use_helm=False,
        )
        no_helm = float(no_helm_row["total_events_per_kg_day"])
        row = state_dict(state)
        row["winner_helm_nohelm_ratio"] = with_helm / no_helm if no_helm > 0.0 else 1.0
        row["winner_components_events_per_kg_day"] = evaluator.ranking(state.threshold_ev)[0][
            "components_events_per_kg_day"
        ]
        coarse_rows.append(row)

    all_transitions = []
    stability_rows = []
    for left, right in transition_brackets(coarse_states):
        primary = refine_transition(
            evaluator,
            left.threshold_ev,
            right.threshold_ev,
            left.winner,
            right.winner,
            tolerance_ev=REFINE_TOL_EV,
        )
        all_transitions.extend(primary)

        fine_brackets = fine_grid_transition_identity(
            evaluator,
            left.threshold_ev,
            right.threshold_ev,
            subdivisions=STABILITY_SUBDIVISIONS,
        )
        independent = []
        for wl, wr, lo, hi in fine_brackets:
            independent.extend(
                refine_transition(
                    evaluator,
                    lo,
                    hi,
                    wl,
                    wr,
                    tolerance_ev=REFINE_TOL_EV,
                )
            )

        topology_match = phase_topology(primary) == phase_topology(independent)
        location_diffs = []
        locations_pass = topology_match and len(primary) == len(independent)
        if locations_pass:
            for a, b in zip(primary, independent):
                diff = abs(float(a["crossover_ev"]) - float(b["crossover_ev"]))
                allowed = max(0.05, 0.02 * abs(float(a["crossover_ev"])))
                location_diffs.append({"difference_ev": diff, "allowed_ev": allowed, "pass": diff <= allowed})
                locations_pass = locations_pass and diff <= allowed

        stability_rows.append(
            {
                "coarse_bracket_ev": [left.threshold_ev, right.threshold_ev],
                "endpoint_winners": [left.winner, right.winner],
                "primary_transitions": primary,
                "independent_fine_transitions": independent,
                "topology_match": topology_match,
                "location_checks": location_diffs,
                "pass": bool(topology_match and locations_pass),
            }
        )

    all_transitions.sort(key=lambda row: float(row["crossover_ev"]))
    all_stable = all(row["pass"] for row in stability_rows)
    status = "PASS_PHASE_DIAGRAM" if all_stable else "PARTIAL_PHASE_DIAGRAM"

    # Phase labels on the prospectively frozen grid. Exact target crossovers are
    # separately recorded above; source-dominance changes are intentionally not
    # overfit beyond the frozen threshold sampling in this gate.
    phases = compress_states(coarse_states)

    result = {
        "status": status,
        "scope": (
            "pure-isotope physics-only B16-GS98 full-solar ideal CEvNS target/threshold phase diagram; "
            "same exact masses, actual Z/N, pinned spectra and Helm form factor as iteration 0045; "
            "detector transfer function/chemistry/abundance excluded"
        ),
        "coarse_thresholds_ev": list(COARSE_THRESHOLDS_EV),
        "refinement_tolerance_ev": REFINE_TOL_EV,
        "stability_subdivisions": STABILITY_SUBDIVISIONS,
        "coarse_states": coarse_rows,
        "phase_intervals_on_frozen_grid": phases,
        "refined_target_crossovers": all_transitions,
        "stability_checks": stability_rows,
        "interpretation_guard": (
            "A phase winner is source/threshold matching, not weak-interaction enhancement, practical detector ranking, "
            "or neutrino-energy amplification."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))

    if status != "PASS_PHASE_DIAGRAM":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
