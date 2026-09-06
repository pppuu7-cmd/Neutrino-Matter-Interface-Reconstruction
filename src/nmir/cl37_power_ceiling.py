"""Neutrino-supplied energy ceiling for oscillated solar 37Cl capture.

Each successful capture is credited with at most the incident neutrino energy.
Daughter-decay energy, target nuclear-mass release, and other target-internal
energy reservoirs are excluded by construction.  The authoritative Be7 source-
average rate is retained and assigned the capture-active 0.862-MeV line energy.
The unresolved 0.814--1.0 MeV continuum response is propagated as an explicit
envelope using the two frozen Cl response conventions.
"""
from __future__ import annotations

from pathlib import Path

from .capture_metrics import JOULE_PER_EV, target_atoms_per_kg
from .cl37_response import cl37_sigma_cm2
from .cl37_source_average import be7_authority_oscillated_snu
from .cl37_solar_fold import _download_matter, _pee_function
from .ga71_response import parse_two_column_spectrum, trapz
from .solar_flux import load_b16_fluxes
from .solar_spectra import load_spectrum_manifest, materialize_all_spectra

SNU = 1.0e-36
CL37_MOLAR_MASS_G_MOL = 36.9659026
BE7_CAPTURE_LINE_MEV = 0.862


def _continuum_moments(component: str, flux: float, table, spectrum_path: Path, low_energy_mode: str) -> tuple[float, float]:
    e, f = parse_two_column_spectrum(spectrum_path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    pee = _pee_function(table, component)
    rate_integrand: list[float] = []
    energy_integrand: list[float] = []
    for x, w in zip(e, f):
        sigma = cl37_sigma_cm2(x, low_energy_mode=low_energy_mode)
        if sigma == 0.0 or w == 0.0:
            r = 0.0
        else:
            r = w * pee(x) * sigma
        rate_integrand.append(r)
        energy_integrand.append(r * x)
    rate = flux * trapz(e, rate_integrand) / norm / SNU
    moment = flux * trapz(e, energy_integrand) / norm / SNU
    return rate, moment


def oscillated_cl37_neutrino_energy_ceiling(model: str, workdir: str | Path, *, low_energy_mode: str = "threshold_linear") -> dict[str, dict[str, float] | float | str]:
    key = model.upper()
    if key not in {"GS98", "AGSS09MET"}:
        raise ValueError("model must be GS98 or AGSS09met")
    if low_energy_mode not in {"threshold_linear", "zero_to_1"}:
        raise ValueError("low_energy_mode must be threshold_linear or zero_to_1")
    model_key = "B16_GS98" if key == "GS98" else "B16_AGSS09met"
    table = _download_matter(model_key)
    fluxes = load_b16_fluxes(model)
    paths = materialize_all_spectra(workdir)
    rows: dict[str, dict[str, float]] = {}

    for comp in ("pp", "hep", "B8", "N13", "O15", "F17"):
        rate, moment = _continuum_moments(comp, fluxes[comp].flux_cm2_s, table, paths[comp], low_energy_mode)
        rows[comp] = {"rate_snu": rate, "energy_snu_mev": moment, "mean_captured_enu_mev": moment / rate if rate else 0.0}

    pep_e = load_spectrum_manifest()["pep"].line_energy_mev
    assert pep_e is not None
    pep_rate = fluxes["pep"].flux_cm2_s * _pee_function(table, "pep")(pep_e) * cl37_sigma_cm2(pep_e, low_energy_mode=low_energy_mode) / SNU
    rows["pep"] = {"rate_snu": pep_rate, "energy_snu_mev": pep_rate * pep_e, "mean_captured_enu_mev": pep_e}

    be7_rate = be7_authority_oscillated_snu(fluxes["Be7"].flux_cm2_s, _pee_function(table, "Be7")(BE7_CAPTURE_LINE_MEV))
    rows["Be7"] = {
        "rate_snu": be7_rate,
        "energy_snu_mev": be7_rate * BE7_CAPTURE_LINE_MEV,
        "mean_captured_enu_mev": BE7_CAPTURE_LINE_MEV,
    }

    total_rate = sum(v["rate_snu"] for v in rows.values())
    total_moment = sum(v["energy_snu_mev"] for v in rows.values())
    atoms_kg = target_atoms_per_kg(CL37_MOLAR_MASS_G_MOL)
    power = total_moment * SNU * atoms_kg * 1.0e6 * JOULE_PER_EV
    return {
        "low_energy_mode": low_energy_mode,
        "components": rows,
        "total_rate_snu": total_rate,
        "total_energy_snu_mev": total_moment,
        "mean_captured_enu_mev": total_moment / total_rate,
        "pure_cl37_neutrino_energy_ceiling_w_per_kg": power,
    }


def cl37_power_envelope(model: str, workdir: str | Path) -> dict[str, object]:
    high = oscillated_cl37_neutrino_energy_ceiling(model, workdir, low_energy_mode="threshold_linear")
    low = oscillated_cl37_neutrino_energy_ceiling(model, workdir, low_energy_mode="zero_to_1")
    p_hi = float(high["pure_cl37_neutrino_energy_ceiling_w_per_kg"])
    p_lo = float(low["pure_cl37_neutrino_energy_ceiling_w_per_kg"])
    return {
        "model": model,
        "threshold_linear": high,
        "zero_to_1": low,
        "power_min_w_per_kg": min(p_hi, p_lo),
        "power_max_w_per_kg": max(p_hi, p_lo),
        "relative_power_span": abs(p_hi - p_lo) / max(p_hi, p_lo),
    }
