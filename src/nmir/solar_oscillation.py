"""Frozen baseline solar-neutrino oscillation convention and adiabatic MSW kernel."""

from __future__ import annotations

import csv
import math
from pathlib import Path

from .solar_matter import SolarMatterTable, normalized_production_weights

# sqrt(2) G_F n_e expressed for n_e/N_A in mol cm^-3:
# V_e = 7.63247e-14 eV * (n_e / (N_A cm^-3)).
# Therefore 2 E V_e = 1.526494e-7 eV^2 * E[MeV] * n_e[mol cm^-3].
_TWO_E_V_COEFF_EV2_PER_MEV_MOLCM3 = 1.526494e-7


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


def vacuum_averaged_pee(sin2_theta12: float, sin2_theta13: float) -> float:
    """Phase-averaged three-flavour vacuum survival probability."""
    s12, s13 = sin2_theta12, sin2_theta13
    c13 = 1.0 - s13
    sin2_2theta12 = 4.0 * s12 * (1.0 - s12)
    return c13**2 * (1.0 - 0.5 * sin2_2theta12) + s13**2


def high_density_adiabatic_pee(sin2_theta12: float, sin2_theta13: float) -> float:
    """Normal-ordering high-density 1-2 adiabatic limit with small 1-3 matter effects neglected."""
    s12, s13 = sin2_theta12, sin2_theta13
    c13 = 1.0 - s13
    return c13**2 * s12 + s13**2


def adiabatic_day_pee_at_density(
    energy_mev: float,
    electron_density_mol_cm3: float,
    sin2_theta12: float | None = None,
    sin2_theta13: float | None = None,
    delta_m21_sq_ev2: float | None = None,
) -> float:
    """Day-side adiabatic three-flavour P_ee at one production density.

    Uses the standard decoupled 1-2 solar approximation
      P_ee = c13^4 [1 + cos(2theta12) cos(2theta12^m)]/2 + s13^4,
    with A -> A*c13^2 in the effective 1-2 matter Hamiltonian.
    Earth regeneration and nonadiabatic hopping are excluded by the frozen first benchmark.
    """
    if energy_mev <= 0.0 or electron_density_mol_cm3 < 0.0:
        raise ValueError("energy must be positive and electron density non-negative")
    if sin2_theta12 is None or sin2_theta13 is None or delta_m21_sq_ev2 is None:
        p12, p13, dm21 = numerical_solar_parameters()
        sin2_theta12 = p12 if sin2_theta12 is None else sin2_theta12
        sin2_theta13 = p13 if sin2_theta13 is None else sin2_theta13
        delta_m21_sq_ev2 = dm21 if delta_m21_sq_ev2 is None else delta_m21_sq_ev2
    s12 = float(sin2_theta12)
    s13 = float(sin2_theta13)
    dm21 = float(delta_m21_sq_ev2)
    if not (0.0 < s12 < 1.0 and 0.0 <= s13 < 1.0 and dm21 > 0.0):
        raise ValueError("invalid solar mixing parameters")
    cos2 = 1.0 - 2.0 * s12
    sin2sq = 4.0 * s12 * (1.0 - s12)
    c13 = 1.0 - s13
    a_eff = (
        _TWO_E_V_COEFF_EV2_PER_MEV_MOLCM3
        * energy_mev
        * electron_density_mol_cm3
        * c13
        / dm21
    )
    denom = math.sqrt((cos2 - a_eff) ** 2 + sin2sq)
    cos2_m = (cos2 - a_eff) / denom
    pee = c13**2 * 0.5 * (1.0 + cos2 * cos2_m) + s13**2
    if not (0.0 <= pee <= 1.0) or not math.isfinite(pee):
        raise ValueError("non-physical survival probability")
    return pee


def production_averaged_day_pee(
    energy_mev: float,
    table: SolarMatterTable,
    component: str,
) -> float:
    """Production-average P_ee on the native B16 radial grid."""
    weights = normalized_production_weights(table, component)
    return sum(
        w * adiabatic_day_pee_at_density(energy_mev, ne)
        for w, ne in zip(weights, table.electron_density_mol_cm3)
    )
