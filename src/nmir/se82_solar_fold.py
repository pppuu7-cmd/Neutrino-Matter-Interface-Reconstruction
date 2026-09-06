"""Full B16+MSW solar-neutrino fold for measured-GT 82Se response."""
from __future__ import annotations

from pathlib import Path

from .capture_metrics import JOULE_PER_EV, target_atoms_per_kg
from .ga71_response import parse_two_column_spectrum, trapz
from .ga71_solar_fold import _download_matter, _pee_function
from .se82_full_response import se82_full_sigma_cm2
from .solar_flux import load_b16_fluxes
from .solar_spectra import load_spectrum_manifest, materialize_all_spectra

SNU = 1.0e-36
SE82_MOLAR_MASS_G_MOL = 81.9167000
NATURAL_SE_MOLAR_MASS_G_MOL = 78.971
SE82_NATURAL_FRACTION = 0.0873
# Frekers et al. total response systematic: ±60 SNU on 668 SNU.
PUBLISHED_RESPONSE_RELATIVE_SYSTEMATIC = 60.0 / 668.0


def _continuum(component: str, flux: float, table, spectrum_path: Path, *, oscillated: bool) -> tuple[float, float]:
    e, f = parse_two_column_spectrum(spectrum_path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    pee = _pee_function(table, component) if oscillated else (lambda _e: 1.0)
    rate_y: list[float] = []
    energy_y: list[float] = []
    for x, w in zip(e, f):
        sigma = se82_full_sigma_cm2(x)
        # Some frozen source spectra include exact E=0 endpoints with zero
        # spectral weight. Pee is intentionally undefined at E<=0, so skip
        # mathematically zero contributions before evaluating oscillations.
        if w == 0.0 or sigma == 0.0:
            value = 0.0
        else:
            value = w * pee(x) * sigma
        rate_y.append(value)
        energy_y.append(value * x)
    return flux * trapz(e, rate_y) / norm / SNU, flux * trapz(e, energy_y) / norm / SNU


def _profile(flux: float, table, spectrum_path: Path, branch_weight: float, *, oscillated: bool) -> tuple[float, float]:
    return _continuum("Be7", flux * branch_weight, table, spectrum_path, oscillated=oscillated)


def se82_b16_fold(model: str, workdir: str | Path, *, oscillated: bool = True) -> dict[str, object]:
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
    pep_rate = fluxes["pep"].flux_cm2_s * pep_pee * se82_full_sigma_cm2(pep_e) / SNU
    rows["pep"] = {"rate_snu": pep_rate, "energy_snu_mev": pep_rate * pep_e, "mean_captured_enu_mev": pep_e}

    b1 = _profile(fluxes["Be7"].flux_cm2_s, table, paths["Be7_ground"], 0.897, oscillated=oscillated)
    b2 = _profile(fluxes["Be7"].flux_cm2_s, table, paths["Be7_excited"], 0.103, oscillated=oscillated)
    be_rate = b1[0] + b2[0]
    be_moment = b1[1] + b2[1]
    rows["Be7"] = {"rate_snu": be_rate, "energy_snu_mev": be_moment, "mean_captured_enu_mev": be_moment / be_rate if be_rate else 0.0}

    total_rate = sum(v["rate_snu"] for v in rows.values())
    total_moment = sum(v["energy_snu_mev"] for v in rows.values())
    pure_atoms = target_atoms_per_kg(SE82_MOLAR_MASS_G_MOL)
    natural_atoms = target_atoms_per_kg(NATURAL_SE_MOLAR_MASS_G_MOL, SE82_NATURAL_FRACTION)
    mev_to_j = 1.0e6 * JOULE_PER_EV
    pure_power = total_moment * SNU * pure_atoms * mev_to_j
    natural_power = total_moment * SNU * natural_atoms * mev_to_j
    sys = PUBLISHED_RESPONSE_RELATIVE_SYSTEMATIC
    return {
        "status": "MATCHED_MEASURED_GT_RESPONSE",
        "oscillated": oscillated,
        "components": rows,
        "total_rate_snu": total_rate,
        "total_energy_snu_mev": total_moment,
        "mean_captured_enu_mev": total_moment / total_rate if total_rate else 0.0,
        "pure_se82_neutrino_energy_ceiling_w_per_kg": pure_power,
        "natural_se_neutrino_energy_ceiling_w_per_kg": natural_power,
        "response_systematic_relative_from_published_total": sys,
        "pure_se82_power_systematic_envelope_w_per_kg": [pure_power * (1.0 - sys), pure_power * (1.0 + sys)],
        "natural_se_power_systematic_envelope_w_per_kg": [natural_power * (1.0 - sys), natural_power * (1.0 + sys)],
    }
