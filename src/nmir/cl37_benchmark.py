"""Source-average validation helpers for the frozen 37Cl response."""
from __future__ import annotations

from pathlib import Path

from .cl37_response import cl37_sigma_cm2
from .ga71_response import parse_two_column_spectrum, trapz


def source_average_sigma_from_spectrum(path: str | Path, *, low_energy_mode: str = "threshold_linear") -> float:
    """Average the frozen energy-dependent Cl-37 response over a normalized source shape."""
    p = Path(path)
    e, f = parse_two_column_spectrum(p.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    if norm <= 0.0:
        raise ValueError("spectrum normalization must be positive")
    values = [w * cl37_sigma_cm2(x, low_energy_mode=low_energy_mode) for x, w in zip(e, f)]
    return trapz(e, values) / norm
