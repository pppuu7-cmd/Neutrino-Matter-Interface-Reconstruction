"""Matched-convention audit helpers for historical 8B -> 37Cl source averages."""
from __future__ import annotations

import bisect
import csv
from pathlib import Path


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def _trapezoid(y: list[float], x: list[float]) -> float:
    return sum(0.5 * (y[i] + y[i - 1]) * (x[i] - x[i - 1]) for i in range(1, len(x)))


def _interp(x: float, xp: list[float], fp: list[float]) -> float:
    if x <= xp[0]:
        return fp[0]
    if x >= xp[-1]:
        return fp[-1]
    j = bisect.bisect_right(xp, x)
    x0, x1 = xp[j - 1], xp[j]
    y0, y1 = fp[j - 1], fp[j]
    t = (x - x0) / (x1 - x0)
    return y0 + t * (y1 - y0)


def load_bahcall_lisi1996_spectrum(path: str | Path | None = None) -> tuple[list[float], list[float]]:
    p = Path(path) if path is not None else _root() / "data" / "b8_bahcall_lisi1996_spectrum.csv"
    energy: list[float] = []
    lam: list[float] = []
    with p.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            energy.append(float(row["energy_mev"]))
            lam.append(float(row["lambda_per_mev"]))
    if len(energy) != 160 or any(b <= a for a, b in zip(energy, energy[1:])):
        raise ValueError("unexpected Bahcall-Lisi 1996 spectrum grid")
    norm = _trapezoid(lam, energy)
    if abs(norm - 1.0) > 5e-4:
        raise ValueError(f"spectrum normalization mismatch: {norm}")
    return energy, lam


def load_cl37_tabulation(column: str = "improved_1e46_cm2") -> tuple[list[float], list[float]]:
    p = _root() / "data" / "cl37_bahcall1996_response.csv"
    energy: list[float] = []
    sigma: list[float] = []
    with p.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            energy.append(float(row["energy_mev"]))
            sigma.append(float(row[column]) * 1e-46)
    return energy, sigma


def source_average_from_sparse_table(column: str = "improved_1e46_cm2") -> float:
    """Fold Table-I 1996 spectrum with sparse Table-II Cl response.

    This reproduces only a tabulated/interpolated approximation to the paper's
    internal continuous response. It is a consistency check, not a replacement
    for the published source-average authority.
    """
    energy, lam = load_bahcall_lisi1996_spectrum()
    response_energy, response_sigma = load_cl37_tabulation(column)
    sigma: list[float] = []
    for e in energy:
        if e < 0.814:
            s = 0.0
        elif e < 1.0:
            s = response_sigma[0] * (e - 0.814) / (1.0 - 0.814)
        else:
            s = _interp(e, response_energy, response_sigma)
        sigma.append(s)
    integrand = [l * s for l, s in zip(lam, sigma)]
    return _trapezoid(integrand, energy)
