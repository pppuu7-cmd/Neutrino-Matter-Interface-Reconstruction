"""Matched B16+MSW screening fold for the dominant 115In capture branch.

This module deliberately inherits the same frozen solar flux/spectrum/matter/
oscillation authority used by the validated Ga-71 and Cl-37 folds.  The nuclear
response is still provisional (see :mod:`nmir.in115_response`), so outputs are
screening results until a stronger primary response/uncertainty treatment is
frozen.
"""
from __future__ import annotations

from pathlib import Path

from .capture_metrics import JOULE_PER_EV, target_atoms_per_kg
from .ga71_response import parse_two_column_spectrum, trapz
from .ga71_solar_fold import _download_matter, _pee_function
from .in115_response import in115_dominant_sigma_cm2
from .solar_flux import load_b16_fluxes
from .solar_spectra import load_spectrum_manifest, materialize_all_spectra

SNU = 1.0e-36
IN115_MOLAR_MASS_G_MOL = 114.9038788
NATURAL_IN_MOLAR_MASS_G_MOL = 114.818
IN115_NATURAL_FRACTION = 0.9571


def _continuum_moments(component: str, flux: float, table, spectrum_path: Path, *, oscillated: bool) -> tuple[float, float]:
    e, f = parse_two_column_spectrum(spectrum_path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    pee = _pee_function(table, component) if oscillated else (lambda _e: 1.0)
    rate_integrand: list[float] = []
    energy_integrand: list[float] = []
    for x, w in zip(e, f):
        sigma = in115_dominant_sigma_cm2(x)
        r = 0.0 if sigma == 0.0 or w == 0.0 else w * pee(x) * sigma
        rate_integrand.append(r)
        energy_integrand.append(r * x)
    rate = flux * trapz(e, rate_integrand) / norm / SNU
    moment = flux * trapz(e, energy_integrand) / norm / SNU
    return rate, moment


def _profile_moments(flux: float, table, spectrum_path: Path, branch_weight: float, *, oscillated: bool) -> tuple[float, float]:
    return _continuum_moments("Be7", flux * branch_weight, table, spectrum_path, oscillated=oscillated)


def in115_b16_screen(model: str, workdir: str | Path, *, oscillated: bool = True) -> dict[str, object]:
    key = model.upper()
    if key not in {"GS98", "AGSS09MET"}:
        raise ValueError("model must be GS98 or AGSS09met")
    model_key = "B16_GS98" if key == "GS98" else "B16_AGSS09met"
    table = _download_matter(model_key)
    fluxes = load_b16_fluxes(model)
    paths = materialize_all_spectra(workdir)
    rows: dict[str, dict[str, float]] = {}

    for comp in ("pp", "hep", "B8", "N13", "O15", "F17"):
        rate, moment = _continuum_moments(comp, fluxes[comp].flux_cm2_s, table, paths[comp], oscillated=oscillated)
        rows[comp] = {
            "rate_snu": rate,
            "energy_snu_mev": moment,
            "mean_captured_enu_mev": moment / rate if rate else 0.0,
        }

    manifest = load_spectrum_manifest()
    pep_e = manifest["pep"].line_energy_mev
    assert pep_e is not None
    pep_pee = _pee_function(table, "pep")(pep_e) if oscillated else 1.0
    pep_rate = fluxes["pep"].flux_cm2_s * pep_pee * in115_dominant_sigma_cm2(pep_e) / SNU
    rows["pep"] = {"rate_snu": pep_rate, "energy_snu_mev": pep_rate * pep_e, "mean_captured_enu_mev": pep_e}

    b1 = _profile_moments(fluxes["Be7"].flux_cm2_s, table, paths["Be7_ground"], 0.897, oscillated=oscillated)
    b2 = _profile_moments(fluxes["Be7"].flux_cm2_s, table, paths["Be7_excited"], 0.103, oscillated=oscillated)
    be_rate = b1[0] + b2[0]
    be_moment = b1[1] + b2[1]
    rows["Be7"] = {"rate_snu": be_rate, "energy_snu_mev": be_moment, "mean_captured_enu_mev": be_moment / be_rate if be_rate else 0.0}

    total_rate = sum(v["rate_snu"] for v in rows.values())
    total_moment = sum(v["energy_snu_mev"] for v in rows.values())
    pure_atoms = target_atoms_per_kg(IN115_MOLAR_MASS_G_MOL)
    natural_atoms = target_atoms_per_kg(NATURAL_IN_MOLAR_MASS_G_MOL, IN115_NATURAL_FRACTION)
    mev_to_j = 1.0e6 * JOULE_PER_EV
    return {
        "status": "PROVISIONAL_SCREENING_RESPONSE",
        "oscillated": oscillated,
        "nuclear_response": {
            "transition": "115In(9/2+) -> 115Sn*(612.8 keV, 7/2+)",
            "threshold_mev": 0.114,
            "bgt": 0.17,
            "response_caveat": "point-Coulomb allowed-GT screen; requires precision primary-response upgrade before G3 authority",
        },
        "components": rows,
        "total_rate_snu": total_rate,
        "total_energy_snu_mev": total_moment,
        "mean_captured_enu_mev": total_moment / total_rate if total_rate else 0.0,
        "pure_in115_neutrino_energy_ceiling_w_per_kg": total_moment * SNU * pure_atoms * mev_to_j,
        "natural_indium_neutrino_energy_ceiling_w_per_kg": total_moment * SNU * natural_atoms * mev_to_j,
        "pure_in115_captures_per_year_per_10_t": total_rate * SNU * pure_atoms * 10000.0 * (365.25 * 86400.0),
    }
