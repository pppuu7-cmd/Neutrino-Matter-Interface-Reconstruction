"""Neutrino-supplied energy ceiling for oscillated solar 71Ga capture.

The quantity here is deliberately an upper bound: each successful capture is
credited with at most the incident neutrino energy E_nu.  Daughter decay,
nuclear-mass release, and any other energy not carried by the incident
neutrino are excluded by construction.
"""
from __future__ import annotations

from pathlib import Path

from .capture_metrics import target_atoms_per_kg, JOULE_PER_EV
from .ga71_response import ga71_sigma_cm2, parse_two_column_spectrum, trapz
from .ga71_solar_fold import _download_matter, _pee_function
from .solar_flux import load_b16_fluxes
from .solar_spectra import load_spectrum_manifest, materialize_all_spectra

SNU = 1.0e-36
GA71_MOLAR_MASS_G_MOL = 70.9247


def _continuum_moments(component: str, flux: float, table, spectrum_path: Path) -> tuple[float, float]:
    e, f = parse_two_column_spectrum(spectrum_path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    pee = _pee_function(table, component)
    rate_integrand = []
    energy_integrand = []
    for x, w in zip(e, f):
        sigma = ga71_sigma_cm2(x)
        if sigma == 0.0 or w == 0.0:
            r = 0.0
        else:
            r = w * pee(x) * sigma
        rate_integrand.append(r)
        energy_integrand.append(r * x)
    rate_snu = flux * trapz(e, rate_integrand) / norm / SNU
    energy_snu_mev = flux * trapz(e, energy_integrand) / norm / SNU
    return rate_snu, energy_snu_mev


def _profile_moments(flux: float, table, spectrum_path: Path, branch_weight: float) -> tuple[float, float]:
    rate, moment = _continuum_moments("Be7", flux * branch_weight, table, spectrum_path)
    return rate, moment


def oscillated_ga71_neutrino_energy_ceiling(model: str, workdir: str | Path) -> dict[str, dict[str, float] | float]:
    key = model.upper()
    if key not in {"GS98", "AGSS09MET"}:
        raise ValueError("model must be GS98 or AGSS09met")
    model_key = "B16_GS98" if key == "GS98" else "B16_AGSS09met"
    table = _download_matter(model_key)
    fluxes = load_b16_fluxes(model)
    paths = materialize_all_spectra(workdir)
    rows: dict[str, dict[str, float]] = {}

    for comp in ("pp", "hep", "B8", "N13", "O15", "F17"):
        rate, moment = _continuum_moments(comp, fluxes[comp].flux_cm2_s, table, paths[comp])
        rows[comp] = {"rate_snu": rate, "energy_snu_mev": moment, "mean_captured_enu_mev": moment / rate if rate else 0.0}

    pep_e = load_spectrum_manifest()["pep"].line_energy_mev
    assert pep_e is not None
    pep_pee = _pee_function(table, "pep")
    pep_rate = fluxes["pep"].flux_cm2_s * pep_pee(pep_e) * ga71_sigma_cm2(pep_e) / SNU
    rows["pep"] = {"rate_snu": pep_rate, "energy_snu_mev": pep_rate * pep_e, "mean_captured_enu_mev": pep_e}

    b1 = _profile_moments(fluxes["Be7"].flux_cm2_s, table, paths["Be7_ground"], 0.897)
    b2 = _profile_moments(fluxes["Be7"].flux_cm2_s, table, paths["Be7_excited"], 0.103)
    be_rate = b1[0] + b2[0]
    be_moment = b1[1] + b2[1]
    rows["Be7"] = {"rate_snu": be_rate, "energy_snu_mev": be_moment, "mean_captured_enu_mev": be_moment / be_rate}

    total_rate = sum(v["rate_snu"] for v in rows.values())
    total_moment = sum(v["energy_snu_mev"] for v in rows.values())
    atoms_kg = target_atoms_per_kg(GA71_MOLAR_MASS_G_MOL)
    power = total_moment * SNU * atoms_kg * 1.0e6 * JOULE_PER_EV
    return {
        "components": rows,
        "total_rate_snu": total_rate,
        "total_energy_snu_mev": total_moment,
        "mean_captured_enu_mev": total_moment / total_rate,
        "pure_ga71_neutrino_energy_ceiling_w_per_kg": power,
    }
