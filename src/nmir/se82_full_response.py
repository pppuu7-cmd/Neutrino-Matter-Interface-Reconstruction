"""Full measured/binned GT response for 82Se solar-neutrino capture.

Response authority seed: Frekers et al., Phys. Rev. C 94, 014614 (2016),
Tables II and III. Individual states are used through 2.498 MeV; above that,
the 0.5-MeV GT-bin strengths are represented at the Table-IV energies used by
the paper for its solar-capture calculation.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from .se82_response import (
    G_A,
    SE82_DAUGHTER_Z,
    SE82_GS_MASS_DIFFERENCE_MEV,
    _allowed_gt_sigma_cm2,
)

_DATA = Path(__file__).resolve().parents[2] / "data" / "se82_frekers2016_gt_response.csv"


@dataclass(frozen=True)
class GTTransition:
    mode: str
    excitation_mev: float
    bgt: float
    bgt_uncertainty: float

    @property
    def threshold_mev(self) -> float:
        return SE82_GS_MASS_DIFFERENCE_MEV + self.excitation_mev


def load_gt_transitions(path: str | Path = _DATA) -> tuple[GTTransition, ...]:
    rows: list[GTTransition] = []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows.append(
                GTTransition(
                    mode=row["mode"],
                    excitation_mev=float(row["excitation_mev"]),
                    bgt=float(row["bgt"]),
                    bgt_uncertainty=float(row["bgt_uncertainty"]),
                )
            )
    if not rows:
        raise ValueError("empty Se-82 GT response table")
    return tuple(rows)


def se82_full_sigma_cm2(
    enu_mev: float,
    *,
    transitions: tuple[GTTransition, ...] | None = None,
    fermi_model: str = "relativistic_finite_size",
    g_a: float = G_A,
) -> float:
    """Inclusive allowed-GT capture cross section below neutron threshold."""
    active = load_gt_transitions() if transitions is None else transitions
    total = 0.0
    for tr in active:
        total += _allowed_gt_sigma_cm2(
            enu_mev,
            threshold_mev=tr.threshold_mev,
            bgt=tr.bgt,
            z_daughter=SE82_DAUGHTER_Z,
            g_a=g_a,
            fermi_model=fermi_model,
        )
    return total


def se82_dominant_fraction_of_bgt() -> float:
    rows = load_gt_transitions()
    return rows[0].bgt / sum(r.bgt for r in rows)
