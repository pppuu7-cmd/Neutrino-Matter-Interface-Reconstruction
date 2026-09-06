"""Full B16 solar-neutrino folding for 71Ga capture."""
from __future__ import annotations

from pathlib import Path

from .ga71_response import ga71_sigma_cm2, parse_two_column_spectrum, trapz
from .solar_flux import load_b16_fluxes
from .solar_oscillation import production_averaged_day_pee
from .solar_spectra import load_spectrum_manifest, materialize_all_spectra
from .solar_matter import load_solar_matter_manifest, parse_solar_matter_bytes, raw_pinned_url


def _download_matter(model_key: str):
    import urllib.request
    manifest = load_solar_matter_manifest()
    with urllib.request.urlopen(raw_pinned_url(model_key, manifest), timeout=60) as r:
        data = r.read()
    return parse_solar_matter_bytes(model_key, data, manifest)


def _continuum_snu(component: str, flux: float, table, spectrum_path: Path) -> float:
    e, f = parse_two_column_spectrum(spectrum_path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    integrand = [w * production_averaged_day_pee(x, table, component) * ga71_sigma_cm2(x) for x, w in zip(e, f)]
    return flux * trapz(e, integrand) / norm / 1e-36


def _profile_snu(component: str, flux: float, table, spectrum_path: Path, branch_weight: float) -> float:
    e, f = parse_two_column_spectrum(spectrum_path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    integrand = [w * production_averaged_day_pee(x, table, "Be7") * ga71_sigma_cm2(x) for x, w in zip(e, f)]
    return flux * branch_weight * trapz(e, integrand) / norm / 1e-36


def oscillated_ga71_snu(model: str, workdir: str | Path) -> dict[str, float]:
    model_key = "B16_GS98" if model.upper() == "GS98" else "B16_AGSS09met"
    table = _download_matter(model_key)
    fluxes = load_b16_fluxes(model)
    paths = materialize_all_spectra(workdir)
    out: dict[str, float] = {}
    for comp in ("pp", "hep", "B8", "N13", "O15", "F17"):
        out[comp] = _continuum_snu(comp, fluxes[comp].flux_cm2_s, table, paths[comp])
    pep_e = load_spectrum_manifest()["pep"].line_energy_mev
    assert pep_e is not None
    out["pep"] = fluxes["pep"].flux_cm2_s * production_averaged_day_pee(pep_e, table, "pep") * ga71_sigma_cm2(pep_e) / 1e-36
    out["Be7"] = _profile_snu("Be7", fluxes["Be7"].flux_cm2_s, table, paths["Be7_ground"], 0.897) + _profile_snu("Be7", fluxes["Be7"].flux_cm2_s, table, paths["Be7_excited"], 0.103)
    out["total"] = sum(out.values())
    return out
