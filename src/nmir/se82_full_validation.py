"""Source-average validation matrix for the full measured-GT 82Se response."""
from __future__ import annotations

from pathlib import Path

from .ga71_response import parse_two_column_spectrum, trapz
from .se82_full_response import se82_full_sigma_cm2
from .solar_spectra import materialize_all_spectra

PUBLISHED_1E46 = {
    "pp": 76.2,
    "pep": 775.0,
    "hep": 126000.0,
    "Be7_862": 350.0,
    "Be7_384": 117.0,
    "B8": 47000.0,
    "N13": 277.0,
    "O15": 464.0,
    "F17": 462.0,
}


def _continuum_average(path: str | Path) -> float:
    e, f = parse_two_column_spectrum(Path(path).read_text(encoding="utf-8"))
    norm = trapz(e, f)
    return trapz(e, [w * se82_full_sigma_cm2(x) for x, w in zip(e, f)]) / norm


def validate_source_averages(workdir: str | Path) -> dict[str, dict[str, float]]:
    paths = materialize_all_spectra(workdir)
    calculated = {
        "pp": _continuum_average(paths["pp"]),
        "pep": se82_full_sigma_cm2(1.442),
        "hep": _continuum_average(paths["hep"]),
        "Be7_862": se82_full_sigma_cm2(0.862),
        "Be7_384": se82_full_sigma_cm2(0.384),
        "B8": _continuum_average(paths["B8"]),
        "N13": _continuum_average(paths["N13"]),
        "O15": _continuum_average(paths["O15"]),
        "F17": _continuum_average(paths["F17"]),
    }
    out: dict[str, dict[str, float]] = {}
    for key, calc in calculated.items():
        pub = PUBLISHED_1E46[key] * 1.0e-46
        rel = calc / pub - 1.0
        out[key] = {
            "calculated_cm2": calc,
            "published_cm2": pub,
            "relative_residual": rel,
            "absolute_relative_residual": abs(rel),
        }
    return out
