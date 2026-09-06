"""Frozen B16 standard-solar-model neutrino flux inputs."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SolarFluxComponent:
    component: str
    flux_cm2_s: float
    relative_uncertainty: float


def default_flux_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "solar_flux_b16.csv"


def load_b16_fluxes(model: str = "GS98", path: str | Path | None = None) -> dict[str, SolarFluxComponent]:
    """Load one of the two B16 solar-model flux vectors.

    Parameters
    ----------
    model:
        ``GS98`` (high metallicity) or ``AGSS09met`` (low metallicity).
    path:
        Optional CSV override for reproducibility tests.
    """
    key = model.strip().lower()
    if key == "gs98":
        flux_col = "b16_gs98_flux_cm2_s"
        unc_col = "b16_gs98_rel_unc"
    elif key in {"agss09met", "agss09"}:
        flux_col = "b16_agss09met_flux_cm2_s"
        unc_col = "b16_agss09met_rel_unc"
    else:
        raise ValueError("model must be 'GS98' or 'AGSS09met'")

    csv_path = Path(path) if path is not None else default_flux_path()
    out: dict[str, SolarFluxComponent] = {}
    with csv_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            component = row["component"]
            out[component] = SolarFluxComponent(
                component=component,
                flux_cm2_s=float(row[flux_col]),
                relative_uncertainty=float(row[unc_col]),
            )
    return out


def cno_total_flux_cm2_s(model: str = "GS98", path: str | Path | None = None) -> float:
    """Return N13+O15+F17 flux, avoiding double counting a derived CNO row."""
    fluxes = load_b16_fluxes(model=model, path=path)
    return sum(fluxes[name].flux_cm2_s for name in ("N13", "O15", "F17"))


def total_component_flux_cm2_s(model: str = "GS98", path: str | Path | None = None) -> float:
    """Sum tabulated component number fluxes.

    This is a bookkeeping diagnostic, not an energy-weighted solar-neutrino
    observable and not an oscillated electron-neutrino flux.
    """
    return sum(item.flux_cm2_s for item in load_b16_fluxes(model=model, path=path).values())
