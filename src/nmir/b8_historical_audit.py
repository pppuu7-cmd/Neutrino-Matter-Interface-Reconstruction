"""Matched-convention audit helpers for historical 8B -> 37Cl source averages."""
from __future__ import annotations

import csv
from pathlib import Path
import numpy as np


def _root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_bahcall_lisi1996_spectrum(path: str | Path | None = None) -> tuple[np.ndarray, np.ndarray]:
    p = Path(path) if path is not None else _root() / "data" / "b8_bahcall_lisi1996_spectrum.csv"
    e, lam = [], []
    with p.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            e.append(float(row["energy_mev"]))
            lam.append(float(row["lambda_per_mev"]))
    E = np.asarray(e, dtype=float)
    L = np.asarray(lam, dtype=float)
    if len(E) != 160 or not np.all(np.diff(E) > 0):
        raise ValueError("unexpected Bahcall-Lisi 1996 spectrum grid")
    # Table I is a 0.1-MeV-bin probability density; normalization should be unity.
    norm = float(np.trapezoid(L, E))
    if abs(norm - 1.0) > 5e-4:
        raise ValueError(f"spectrum normalization mismatch: {norm}")
    return E, L


def load_cl37_tabulation(column: str = "improved_1e46_cm2") -> tuple[np.ndarray, np.ndarray]:
    p = _root() / "data" / "cl37_bahcall1996_response.csv"
    e, s = [], []
    with p.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            e.append(float(row["energy_mev"]))
            s.append(float(row[column]) * 1e-46)
    return np.asarray(e), np.asarray(s)


def source_average_from_sparse_table(column: str = "improved_1e46_cm2") -> float:
    """Fold Table-I 1996 spectrum with sparse Table-II Cl response.

    This reproduces only a *tabulated/interpolated* approximation to the paper's
    internal continuous response.  It is therefore a consistency check, not a
    replacement for the published source-average authority.
    """
    E, L = load_bahcall_lisi1996_spectrum()
    Er, Sr = load_cl37_tabulation(column)
    sigma = np.interp(E, Er, Sr)
    sigma[E < 0.814] = 0.0
    m = (E >= 0.814) & (E < 1.0)
    sigma[m] = Sr[0] * (E[m] - 0.814) / (1.0 - 0.814)
    return float(np.trapezoid(L * sigma, E))
