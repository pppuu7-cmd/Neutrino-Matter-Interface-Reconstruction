"""Adaptive target/threshold phase diagram for full-solar ideal CEvNS.

This module consumes the exact-mass/full-solar machinery frozen in iteration
0045.  It maps *which* target wins at fixed kg as the nuclear-recoil threshold
changes; it does not model a detector transfer function.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .cevns_solar_optimize import Target, total_rate_row


COARSE_THRESHOLDS_EV = tuple(
    [0.5 * i for i in range(1, 31)]
    + [16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 45.0, 50.0, 60.0, 80.0, 100.0]
)


@dataclass(frozen=True)
class WinnerState:
    threshold_ev: float
    winner: str
    runner_up: str
    winner_rate: float
    runner_up_rate: float
    margin_fraction: float
    dominant_component: str


class PhaseEvaluator:
    """Cache full target rankings by threshold during an adaptive scan."""

    def __init__(self, targets, fluxes, manifest, spectra, *, use_helm: bool = True):
        self.targets = list(targets)
        self.target_by_name = {target.name: target for target in self.targets}
        self.fluxes = fluxes
        self.manifest = manifest
        self.spectra = spectra
        self.use_helm = use_helm
        self._cache: dict[float, list[dict[str, object]]] = {}

    @staticmethod
    def _key(threshold_ev: float) -> float:
        return round(float(threshold_ev), 10)

    def ranking(self, threshold_ev: float) -> list[dict[str, object]]:
        key = self._key(threshold_ev)
        if key not in self._cache:
            rows = [
                total_rate_row(
                    target,
                    threshold_ev,
                    self.fluxes,
                    self.manifest,
                    self.spectra,
                    use_helm=self.use_helm,
                )
                for target in self.targets
            ]
            rows.sort(key=lambda row: float(row["total_events_per_kg_day"]), reverse=True)
            self._cache[key] = rows
        return self._cache[key]

    def state(self, threshold_ev: float) -> WinnerState:
        rows = self.ranking(threshold_ev)
        first, second = rows[0], rows[1]
        r1 = float(first["total_events_per_kg_day"])
        r2 = float(second["total_events_per_kg_day"])
        margin = (r1 - r2) / r1 if r1 > 0.0 else 0.0
        return WinnerState(
            threshold_ev=float(threshold_ev),
            winner=str(first["target"]),
            runner_up=str(second["target"]),
            winner_rate=r1,
            runner_up_rate=r2,
            margin_fraction=margin,
            dominant_component=str(first["dominant_component"]),
        )

    def rate(self, target_name: str, threshold_ev: float) -> float:
        for row in self.ranking(threshold_ev):
            if row["target"] == target_name:
                return float(row["total_events_per_kg_day"])
        raise KeyError(target_name)


def compress_states(states: list[WinnerState]) -> list[dict[str, object]]:
    """Compress a sorted threshold grid into winner/source phase intervals."""
    if not states:
        return []
    ordered = sorted(states, key=lambda s: s.threshold_ev)
    phases: list[dict[str, object]] = []
    start = ordered[0]
    previous = ordered[0]
    for state in ordered[1:]:
        if state.winner != previous.winner or state.dominant_component != previous.dominant_component:
            phases.append(
                {
                    "threshold_start_ev": start.threshold_ev,
                    "threshold_end_ev": previous.threshold_ev,
                    "winner": previous.winner,
                    "dominant_component": previous.dominant_component,
                }
            )
            start = state
        previous = state
    phases.append(
        {
            "threshold_start_ev": start.threshold_ev,
            "threshold_end_ev": previous.threshold_ev,
            "winner": previous.winner,
            "dominant_component": previous.dominant_component,
        }
    )
    return phases


def transition_brackets(states: list[WinnerState]) -> list[tuple[WinnerState, WinnerState]]:
    ordered = sorted(states, key=lambda s: s.threshold_ev)
    return [(left, right) for left, right in zip(ordered[:-1], ordered[1:]) if left.winner != right.winner]


def refine_transition(
    evaluator: PhaseEvaluator,
    left_ev: float,
    right_ev: float,
    left_winner: str,
    right_winner: str,
    *,
    tolerance_ev: float = 0.02,
    max_depth: int = 32,
) -> list[dict[str, object]]:
    """Resolve one coarse winner-change bracket, allowing an intermediate winner.

    The midpoint *full ranking* is inspected, rather than only the endpoint pair,
    so an intermediate target discovered during refinement is preserved and the
    bracket is split recursively.
    """
    if right_ev <= left_ev:
        raise ValueError("transition bracket must have positive width")
    if left_winner == right_winner:
        return []

    def rec(lo, hi, wl, wr, depth):
        if depth > max_depth:
            raise RuntimeError("transition refinement exceeded max_depth")
        if hi - lo <= tolerance_ev:
            return [
                {
                    "from": wl,
                    "to": wr,
                    "bracket_low_ev": lo,
                    "bracket_high_ev": hi,
                    "crossover_ev": 0.5 * (lo + hi),
                    "bracket_width_ev": hi - lo,
                }
            ]
        mid = 0.5 * (lo + hi)
        wm = evaluator.state(mid).winner
        if wm == wl:
            return rec(mid, hi, wm, wr, depth + 1)
        if wm == wr:
            return rec(lo, mid, wl, wm, depth + 1)
        return rec(lo, mid, wl, wm, depth + 1) + rec(mid, hi, wm, wr, depth + 1)

    return rec(float(left_ev), float(right_ev), left_winner, right_winner, 0)


def fine_grid_transition_identity(
    evaluator: PhaseEvaluator,
    left_ev: float,
    right_ev: float,
    *,
    subdivisions: int = 8,
) -> list[tuple[str, str, float, float]]:
    """Independent local grid used to check adjacent-winner topology."""
    if subdivisions < 2:
        raise ValueError("subdivisions must be >=2")
    step = (right_ev - left_ev) / subdivisions
    states = [evaluator.state(left_ev + i * step) for i in range(subdivisions + 1)]
    out: list[tuple[str, str, float, float]] = []
    for left, right in zip(states[:-1], states[1:]):
        if left.winner != right.winner:
            out.append((left.winner, right.winner, left.threshold_ev, right.threshold_ev))
    return out


def refine_all_transitions(
    evaluator: PhaseEvaluator,
    coarse_states: list[WinnerState],
    *,
    tolerance_ev: float = 0.02,
) -> list[dict[str, object]]:
    transitions: list[dict[str, object]] = []
    for left, right in transition_brackets(coarse_states):
        transitions.extend(
            refine_transition(
                evaluator,
                left.threshold_ev,
                right.threshold_ev,
                left.winner,
                right.winner,
                tolerance_ev=tolerance_ev,
            )
        )
    transitions.sort(key=lambda row: float(row["crossover_ev"]))
    return transitions


def phase_topology(transitions: list[dict[str, object]]) -> list[tuple[str, str]]:
    return [(str(row["from"]), str(row["to"])) for row in transitions]
