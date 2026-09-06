"""Bahcall et al. (1996) 37Cl electron-neutrino capture response."""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

CL37_THRESHOLD_MEV = 0.814

@dataclass(frozen=True)
class Cl37ResponsePoint:
    energy_mev: float
    improved_cm2: float
    bahcall_ulrich_cm2: float


def default_response_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "cl37_bahcall1996_response.csv"


def load_cl37_response(path: str | Path | None = None) -> tuple[Cl37ResponsePoint, ...]:
    p = Path(path) if path is not None else default_response_path()
    out: list[Cl37ResponsePoint] = []
    with p.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            out.append(Cl37ResponsePoint(
                energy_mev=float(row["energy_mev"]),
                improved_cm2=float(row["improved_1e46_cm2"]) * 1e-46,
                bahcall_ulrich_cm2=float(row["bahcall_ulrich_1e46_cm2"]) * 1e-46,
            ))
    if len(out) != 19:
        raise ValueError("frozen Cl-37 response must contain exactly 19 points")
    if any(b.energy_mev <= a.energy_mev for a, b in zip(out, out[1:])):
        raise ValueError("Cl-37 response energies must be strictly increasing")
    if any(p.improved_cm2 <= 0 or p.bahcall_ulrich_cm2 <= 0 for p in out):
        raise ValueError("Cl-37 response cross sections must be positive")
    return tuple(out)


def _linear(x: float, x0: float, y0: float, x1: float, y1: float) -> float:
    return y0 + (y1-y0)*(x-x0)/(x1-x0)


def cl37_sigma_cm2(
    energy_mev: float,
    *,
    branch: str = "improved",
    low_energy_mode: str = "threshold_linear",
    response: Sequence[Cl37ResponsePoint] | None = None,
) -> float:
    """Piecewise-linear interpolation of the published Cl-37 response.

    Published numerical authority starts at 1 MeV. Two explicit sub-1-MeV
    conventions are supported solely for sensitivity accounting:
    ``threshold_linear`` (default) anchors sigma=0 at the physical 0.814-MeV
    threshold and connects linearly to the 1-MeV table point; ``zero_to_1``
    sets the unresolved interval to zero. Above 30 MeV the routine fails closed.
    """
    if energy_mev < 0:
        raise ValueError("energy must be non-negative")
    if low_energy_mode not in {"threshold_linear", "zero_to_1"}:
        raise ValueError("low_energy_mode must be threshold_linear or zero_to_1")
    if energy_mev <= CL37_THRESHOLD_MEV:
        return 0.0
    pts = tuple(response) if response is not None else load_cl37_response()
    field = {"improved":"improved_cm2", "bahcall_ulrich":"bahcall_ulrich_cm2"}.get(branch)
    if field is None:
        raise ValueError("branch must be improved or bahcall_ulrich")
    first = pts[0]
    if energy_mev < first.energy_mev:
        if low_energy_mode == "zero_to_1":
            return 0.0
        return _linear(energy_mev, CL37_THRESHOLD_MEV, 0.0, first.energy_mev, getattr(first, field))
    if energy_mev > pts[-1].energy_mev:
        raise ValueError("energy exceeds frozen Cl-37 response range")
    for left, right in zip(pts, pts[1:]):
        if left.energy_mev <= energy_mev <= right.energy_mev:
            return _linear(energy_mev, left.energy_mev, getattr(left, field), right.energy_mev, getattr(right, field))
    return getattr(pts[-1], field)
