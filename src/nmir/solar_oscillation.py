"""Frozen baseline solar-neutrino oscillation convention for NMIR."""

from __future__ import annotations

import csv
from pathlib import Path


def _path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "solar_oscillation_convention.csv"


def load_oscillation_convention(path: str | Path | None = None) -> dict[str, str]:
    p = Path(path) if path is not None else _path()
    out: dict[str, str] = {}
    with p.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = row["parameter"].strip()
            if not key or key in out:
                raise ValueError(f"duplicate/empty oscillation parameter: {key!r}")
            out[key] = row["value"].strip()
    required = {
        "sin2_theta12",
        "sin2_theta13",
        "delta_m21_sq",
        "mass_ordering",
        "propagation",
        "earth_regeneration",
    }
    if set(out) != required:
        raise ValueError(f"oscillation convention keys differ from frozen schema: {set(out)!r}")
    return out


def numerical_solar_parameters() -> tuple[float, float, float]:
    c = load_oscillation_convention()
    return float(c["sin2_theta12"]), float(c["sin2_theta13"]), float(c["delta_m21_sq"])
