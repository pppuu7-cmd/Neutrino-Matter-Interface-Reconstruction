"""Published source-averaged 37Cl solar-neutrino capture anchors."""
from __future__ import annotations

import csv
from pathlib import Path


def default_source_average_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "cl37_bahcall_ulrich1988_source_average.csv"


def load_cl37_source_averages(path: str | Path | None = None) -> dict[str, float]:
    p = Path(path) if path is not None else default_source_average_path()
    out: dict[str, float] = {}
    with p.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            unit = row["source_average_unit"]
            scale = {"1e-46_cm2": 1e-46, "1e-42_cm2": 1e-42}.get(unit)
            if scale is None:
                raise ValueError(f"unknown source-average unit {unit}")
            comp = row["component"]
            if comp in out:
                raise ValueError(f"duplicate component {comp}")
            out[comp] = float(row["source_average_cm2"]) * scale
    expected = {"pp", "pep", "hep", "Be7", "B8", "N13", "O15", "F17"}
    if set(out) != expected:
        raise ValueError("frozen Cl-37 source-average table has wrong component set")
    return out


def be7_authority_oscillated_snu(flux_cm2_s: float, pee_862: float) -> float:
    """Use the published standard-spectrum Be7 average as the Cl-37 low-energy authority.

    The 0.384-MeV Be7 branch is below the 0.814-MeV Cl threshold, so the
    published source-average cross section is effectively the thermally
    averaged 0.862-MeV branch strength times its branching fraction.  For an
    oscillated solar fold we therefore multiply that source-average by the
    production-averaged survival probability of the capture-active line.
    """
    if flux_cm2_s < 0:
        raise ValueError("flux must be non-negative")
    if not 0.0 <= pee_862 <= 1.0:
        raise ValueError("Pee must lie in [0,1]")
    sigma_avg = load_cl37_source_averages()["Be7"]
    return flux_cm2_s * pee_862 * sigma_avg / 1e-36
