"""Frozen 71Ga neutrino-capture response and spectral-folding utilities.

The response table is John N. Bahcall, Phys. Rev. C 56, 3391 (1997),
Tables II-IV / associated numerical data. Cross sections are tabulated in
units of 1e-46 cm^2 and intended for interpolation when spectra are modified.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


GA71_THRESHOLD_MEV = 0.233


@dataclass(frozen=True)
class Ga71ResponsePoint:
    energy_mev: float
    best_cm2: float
    minus3sigma_cm2: float
    plus3sigma_cm2: float


def default_response_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "ga71_bahcall1997_response.csv"


def load_ga71_response(path: str | Path | None = None) -> tuple[Ga71ResponsePoint, ...]:
    p = Path(path) if path is not None else default_response_path()
    points: list[Ga71ResponsePoint] = []
    with p.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            points.append(
                Ga71ResponsePoint(
                    energy_mev=float(row["energy_mev"]),
                    best_cm2=float(row["best_1e46_cm2"]) * 1e-46,
                    minus3sigma_cm2=float(row["minus3sigma_1e46_cm2"]) * 1e-46,
                    plus3sigma_cm2=float(row["plus3sigma_1e46_cm2"]) * 1e-46,
                )
            )
    if len(points) < 2:
        raise ValueError("Ga-71 response table must contain at least two points")
    if any(b.energy_mev <= a.energy_mev for a, b in zip(points, points[1:])):
        raise ValueError("Ga-71 response energies must be strictly increasing")
    if any(p.best_cm2 <= 0 or p.minus3sigma_cm2 <= 0 or p.plus3sigma_cm2 <= 0 for p in points):
        raise ValueError("Ga-71 response cross sections must be positive")
    return tuple(points)


def _linear(x: float, x0: float, y0: float, x1: float, y1: float) -> float:
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)


def ga71_sigma_cm2(
    energy_mev: float,
    *,
    branch: str = "best",
    response: Sequence[Ga71ResponsePoint] | None = None,
) -> float:
    """Interpolate the frozen Ga-71 response.

    Below the physical threshold the cross section is zero. Between the
    threshold and the first tabulated point, interpolation is anchored to
    sigma(threshold)=0. Above the final 30-MeV tabulation the function fails
    closed instead of extrapolating.
    """
    if energy_mev < 0:
        raise ValueError("energy must be non-negative")
    if energy_mev <= GA71_THRESHOLD_MEV:
        return 0.0
    pts = tuple(response) if response is not None else load_ga71_response()
    field = {"best": "best_cm2", "minus3sigma": "minus3sigma_cm2", "plus3sigma": "plus3sigma_cm2"}.get(branch)
    if field is None:
        raise ValueError("branch must be best, minus3sigma, or plus3sigma")
    first = pts[0]
    if energy_mev < first.energy_mev:
        return _linear(energy_mev, GA71_THRESHOLD_MEV, 0.0, first.energy_mev, getattr(first, field))
    if energy_mev > pts[-1].energy_mev:
        raise ValueError("energy exceeds frozen Ga-71 response range")
    for left, right in zip(pts, pts[1:]):
        if left.energy_mev <= energy_mev <= right.energy_mev:
            return _linear(energy_mev, left.energy_mev, getattr(left, field), right.energy_mev, getattr(right, field))
    return getattr(pts[-1], field)


def parse_two_column_spectrum(text: str) -> tuple[list[float], list[float]]:
    """Parse comma/whitespace two-column E[MeV], shape[1/MeV] tables."""
    energies: list[float] = []
    weights: list[float] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        fields = [x.strip() for x in line.replace(";", ",").split(",")]
        if len(fields) < 2:
            fields = line.split()
        if len(fields) < 2:
            continue
        energies.append(float(fields[0]))
        weights.append(float(fields[1]))
    if len(energies) < 2 or any(b <= a for a, b in zip(energies, energies[1:])):
        raise ValueError("spectrum requires >=2 strictly increasing energy points")
    if any(w < 0 for w in weights):
        raise ValueError("spectrum weights must be non-negative")
    return energies, weights


def trapz(x: Sequence[float], y: Sequence[float]) -> float:
    if len(x) != len(y) or len(x) < 2:
        raise ValueError("x and y must have equal length >=2")
    return sum(0.5 * (y0 + y1) * (x1 - x0) for x0, x1, y0, y1 in zip(x, x[1:], y, y[1:]))


def normalized_spectral_average_sigma_cm2(
    energies_mev: Sequence[float],
    shape_per_mev: Sequence[float],
    *,
    branch: str = "best",
) -> float:
    """Return ∫f(E)sigma(E)dE / ∫f(E)dE using trapezoidal quadrature."""
    norm = trapz(energies_mev, shape_per_mev)
    if norm <= 0:
        raise ValueError("spectrum normalization must be positive")
    weighted = [w * ga71_sigma_cm2(e, branch=branch) for e, w in zip(energies_mev, shape_per_mev)]
    return trapz(energies_mev, weighted) / norm


def line_capture_snu(flux_cm2_s: float, energy_mev: float, survival_probability: float = 1.0) -> float:
    """Capture rate in SNU for a monoenergetic electron-neutrino line."""
    if flux_cm2_s < 0 or not 0 <= survival_probability <= 1:
        raise ValueError("invalid flux or survival probability")
    return flux_cm2_s * survival_probability * ga71_sigma_cm2(energy_mev) / 1e-36
