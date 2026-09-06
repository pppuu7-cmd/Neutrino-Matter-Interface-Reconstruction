"""B16+MSW fold for the directly crossed 7Li ground-state capture only."""
from __future__ import annotations

from pathlib import Path

from .capture_metrics import JOULE_PER_EV, target_atoms_per_kg
from .ga71_response import parse_two_column_spectrum, trapz
from .ga71_solar_fold import _download_matter, _pee_function
from .li7_ground_response import li7_ground_sigma_cm2
from .solar_flux import load_b16_fluxes
from .solar_spectra import load_spectrum_manifest, materialize_all_spectra

SNU = 1.0e-36
LI7_MOLAR_MASS_G_MOL = 7.016003434
NATURAL_LI_MOLAR_MASS_G_MOL = 6.94
LI7_NATURAL_FRACTION = 0.9241


def _continuum(component: str, flux: float, table, spectrum_path: Path, *, oscillated: bool) -> tuple[float, float]:
    e, f = parse_two_column_spectrum(spectrum_path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    pee = _pee_function(table, component) if oscillated else (lambda _e: 1.0)
    rate_y: list[float] = []
    energy_y: list[float] = []
    for x, w in zip(e, f):
        sigma = li7_ground_sigma_cm2(x)
        if w == 0.0 or sigma == 0.0:
            value = 0.0
        else:
            value = w * pee(x) * sigma
        rate_y.append(value)
        energy_y.append(value * x)
    return flux * trapz(e, rate_y) / norm / SNU, flux * trapz(e, energy_y) / norm / SNU


def li7_ground_b16_fold(model: str, workdir: str | Path, *, oscillated: bool = True) -> dict[str, object]:
    key = model.upper()
    if key not in {"GS98", "AGSS09MET"}:
        raise ValueError("model must be GS98 or AGSS09met")
    model_key = "B16_GS98" if key == "GS98" else "B16_AGSS09met"
    table = _download_matter(model_key)
    fluxes = load_b16_fluxes(model)
    paths = materialize_all_spectra(workdir)
    rows: dict[str, dict[str, float]] = {}

    for comp in ("pp", "hep", "B8", "N13", "O15", "F17"):
        rate, moment = _continuum(comp, fluxes[comp].flux_cm2_s, table, paths[comp], oscillated=oscillated)
        rows[comp] = {"rate_snu": rate, "energy_snu_mev": moment, "mean_captured_enu_mev": moment / rate if rate else 0.0}

    manifest = load_spectrum_manifest()
    pep_e = manifest["pep"].line_energy_mev
    assert pep_e is not None
    pep_pee = _pee_function(table, "pep")(pep_e) if oscillated else 1.0
    pep_rate = fluxes["pep"].flux_cm2_s * pep_pee * li7_ground_sigma_cm2(pep_e) / SNU
    rows["pep"] = {"rate_snu": pep_rate, "energy_snu_mev": pep_rate * pep_e, "mean_captured_enu_mev": pep_e}

    # Only the thermally broadened ~862-keV line can cross the gs threshold.
    be_rate, be_moment = _continuum("Be7", fluxes["Be7"].flux_cm2_s * 0.897, table, paths["Be7_ground"], oscillated=oscillated)
    rows["Be7"] = {"rate_snu": be_rate, "energy_snu_mev": be_moment, "mean_captured_enu_mev": be_moment / be_rate if be_rate else 0.0}

    total_rate = sum(v["rate_snu"] for v in rows.values())
    total_moment = sum(v["energy_snu_mev"] for v in rows.values())
    mev_to_j = 1.0e6 * JOULE_PER_EV
    pure_power = total_moment * SNU * target_atoms_per_kg(LI7_MOLAR_MASS_G_MOL) * mev_to_j
    natural_power = total_moment * SNU * target_atoms_per_kg(NATURAL_LI_MOLAR_MASS_G_MOL, LI7_NATURAL_FRACTION) * mev_to_j
    return {
        "status": "GROUND_STATE_DIRECT_CROSSING_SCREEN_ONLY",
        "oscillated": oscillated,
        "components": rows,
        "total_rate_snu": total_rate,
        "total_energy_snu_mev": total_moment,
        "mean_captured_enu_mev": total_moment / total_rate if total_rate else 0.0,
        "pure_li7_neutrino_energy_ceiling_w_per_kg": pure_power,
        "natural_li_neutrino_energy_ceiling_w_per_kg": natural_power,
        "scope_guard": "Not a complete Li-7 nuclear response; no promotion to G3 authority without external full-response validation.",
    }
