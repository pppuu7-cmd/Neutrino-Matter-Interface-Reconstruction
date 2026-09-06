from dataclasses import replace

import pytest

from nmir.cevns_phase_diagram import (
    COARSE_THRESHOLDS_EV,
    WinnerState,
    compress_states,
    fine_grid_transition_identity,
    phase_topology,
    refine_transition,
    transition_brackets,
)


def state(t, winner, source="Be7_ground", runner="X"):
    return WinnerState(t, winner, runner, 1.0, 0.8, 0.2, source)


def test_frozen_coarse_threshold_grid_matches_prereg():
    assert COARSE_THRESHOLDS_EV[0] == 0.5
    assert 15.0 in COARSE_THRESHOLDS_EV
    assert 16.0 in COARSE_THRESHOLDS_EV
    assert 20.0 in COARSE_THRESHOLDS_EV
    assert 40.0 in COARSE_THRESHOLDS_EV
    assert COARSE_THRESHOLDS_EV[-1] == 100.0
    assert all(b > a for a, b in zip(COARSE_THRESHOLDS_EV[:-1], COARSE_THRESHOLDS_EV[1:]))


def test_transition_brackets_detect_only_winner_changes():
    states = [state(1, "Pb"), state(2, "Pb"), state(3, "Xe"), state(4, "Xe"), state(5, "Se")]
    brackets = transition_brackets(states)
    assert [(a.winner, b.winner) for a, b in brackets] == [("Pb", "Xe"), ("Xe", "Se")]


def test_compress_states_splits_on_winner_or_source():
    states = [
        state(1, "Pb", "Be7_ground"),
        state(2, "Pb", "Be7_ground"),
        state(3, "Pb", "B8"),
        state(4, "Xe", "B8"),
    ]
    phases = compress_states(states)
    assert [(p["winner"], p["dominant_component"]) for p in phases] == [
        ("Pb", "Be7_ground"),
        ("Pb", "B8"),
        ("Xe", "B8"),
    ]


class ThreePhaseEvaluator:
    def state(self, threshold):
        if threshold < 1.0:
            return state(threshold, "Pb")
        if threshold < 2.0:
            return state(threshold, "Xe")
        return state(threshold, "Se", "B8")


def test_refinement_preserves_intermediate_winner():
    ev = ThreePhaseEvaluator()
    transitions = refine_transition(ev, 0.5, 2.5, "Pb", "Se", tolerance_ev=0.02)
    assert phase_topology(transitions) == [("Pb", "Xe"), ("Xe", "Se")]
    assert transitions[0]["bracket_width_ev"] <= 0.02
    assert transitions[1]["bracket_width_ev"] <= 0.02
    assert transitions[0]["crossover_ev"] == pytest.approx(1.0, abs=0.02)
    assert transitions[1]["crossover_ev"] == pytest.approx(2.0, abs=0.02)


def test_fine_grid_identity_recovers_adjacent_topology():
    ev = ThreePhaseEvaluator()
    identities = fine_grid_transition_identity(ev, 0.5, 2.5, subdivisions=16)
    assert [(a, b) for a, b, _, _ in identities] == [("Pb", "Xe"), ("Xe", "Se")]


def test_refine_rejects_nonpositive_bracket():
    ev = ThreePhaseEvaluator()
    with pytest.raises(ValueError):
        refine_transition(ev, 1.0, 1.0, "Pb", "Xe")
