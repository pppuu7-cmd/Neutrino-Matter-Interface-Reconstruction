"""Validation helpers for the measured-GT 82Se dominant capture response."""
from __future__ import annotations

from pathlib import Path

from .ga71_response import parse_two_column_spectrum, trapz
from .se82_response import se82_dominant_sigma_cm2
from .solar_spectra import materialize_all_spectra

# Frekers et al., PRC 94, 014614 (2016), Table V.
# Source-averaged cross section for pp neutrinos, full measured response.
# Because pp neutrinos cannot reach the higher low-lying 82Br states, this is
# effectively a clean validation of the 75-keV dominant transition.
PUBLISHED_PP_SOURCE_AVG_CM2 = 76.2e-46


def source_average_sigma_cm2(spectrum_path: str | Path) -> float:
    e, f = parse_two_column_spectrum(Path(spectrum_path).read_text(encoding="utf-8"))
    norm = trapz(e, f)
    weighted = [w * se82_dominant_sigma_cm2(x) for x, w in zip(e, f)]
    return trapz(e, weighted) / norm


def validate_pp_source_average(workdir: str | Path) -> dict[str, float]:
    paths = materialize_all_spectra(workdir)
    calc = source_average_sigma_cm2(paths["pp"])
    rel = (calc / PUBLISHED_PP_SOURCE_AVG_CM2) - 1.0
    return {
        "calculated_cm2": calc,
        "published_cm2": PUBLISHED_PP_SOURCE_AVG_CM2,
        "relative_residual": rel,
        "absolute_relative_residual": abs(rel),
    }
