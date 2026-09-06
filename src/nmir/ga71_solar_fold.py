"""Full B16 solar-neutrino folding for 71Ga capture."""
from __future__ import annotations

from pathlib import Path

from .ga71_response import ga71_sigma_cm2, parse_two_column_spectrum, trapz
from .solar_flux import load_b16_fluxes
from .solar_oscillation import adiabatic_day_pee_at_density, numerical_solar_parameters
from .solar_spectra import load_spectrum_manifest, materialize_all_spectra
from .solar_matter import (
    load_solar_matter_manifest,
    normalized_production_weights,
    parse_solar_matter_bytes,
    raw_pinned_url,
)


def _download_matter(model_key: str):
    import urllib.request
    manifest = load_solar_matter_manifest()
    with urllib.request.urlopen(raw_pinned_url(model_key, manifest), timeout=60) as r:
        data = r.read()
    return parse_solar_matter_bytes(model_key, data, manifest)


def _pee_function(table, component: str):
    """Cache immutable radial weights and oscillation constants for one component."""
    weights = normalized_production_weights(table, component)
    p12, p13, dm21 = numerical_solar_parameters()
    density = table.electron_density_mol_cm3

    def pee(energy_mev: float) -> float:
        if energy_mev <= 0.0:
            raise ValueError("Pee is undefined at non-positive energy")
        return sum(
            w * adiabatic_day_pee_at_density(energy_mev, ne, p12, p13, dm21)
            for w, ne in zip(weights, density)
        )

    return pee


def _weighted_capture_integrand(energy_mev: float, shape: float, pee) -> float:
    """Return f(E) Pee(E) sigma(E), with the E=0 endpoint contributing exactly zero."""
    sigma = ga71_sigma_cm2(energy_mev)
    if sigma == 0.0 or shape == 0.0:
        return 0.0
    return shape * pee(energy_mev) * sigma


def _continuum_snu(component: str, flux: float, table, spectrum_path: Path) -> float:
    e, f = parse_two_column_spectrum(spectrum_path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    pee = _pee_function(table, component)
    integrand = [_weighted_capture_integrand(x, w, pee) for x, w in zip(e, f)]
    return flux * trapz(e, integrand) / norm / 1e-36


def _profile_snu(flux: float, table, spectrum_path: Path, branch_weight: float) -> float:
    e, f = parse_two_column_spectrum(spectrum_path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    pee = _pee_function(table, "Be7")
    integrand = [_weighted_capture_integrand(x, w, pee) for x, w in zip(e, f)]
    return flux * branch_weight * trapz(e, integrand) / norm / 1e-36


def oscillated_ga71_snu(model: str, workdir: str | Path) -> dict[str, float]:
    key = model.upper()
    if key not in {"GS98", "AGSS09MET"}:
        raise ValueError("model must be GS98 or AGSS09met")
    model_key = "B16_GS98" if key == "GS98" else "B16_AGSS09met"
    table = _download_matter(model_key)
    fluxes = load_b16_fluxes(model)
    paths = materialize_all_spectra(workdir)
    out: dict[str, float] = {}
    for comp in ("pp", "hep", "B8", "N13", "O15", "F17"):
        out[comp] = _continuum_snu(comp, fluxes[comp].flux_cm2_s, table, paths[comp])
    pep_e = load_spectrum_manifest()["pep"].line_energy_mev
    assert pep_e is not None
    pep_pee = _pee_function(table, "pep")
    out["pep"] = fluxes["pep"].flux_cm2_s * pep_pee(pep_e) * ga71_sigma_cm2(pep_e) / 1e-36
    out["Be7"] = _profile_snu(fluxes["Be7"].flux_cm2_s, table, paths["Be7_ground"], 0.897) + _profile_snu(fluxes["Be7"].flux_cm2_s, table, paths["Be7_excited"], 0.103)
    out["total"] = sum(out.values())
    return out
