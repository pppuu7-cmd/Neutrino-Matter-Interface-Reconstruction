"""Full B16 solar-neutrino folding for 37Cl capture."""
from __future__ import annotations

from pathlib import Path

from .cl37_response import cl37_sigma_cm2
from .cl37_source_average import be7_authority_oscillated_snu
from .ga71_response import parse_two_column_spectrum, trapz
from .solar_flux import load_b16_fluxes
from .solar_oscillation import adiabatic_day_pee_at_density, numerical_solar_parameters
from .solar_spectra import load_spectrum_manifest, materialize_all_spectra
from .solar_matter import load_solar_matter_manifest, normalized_production_weights, parse_solar_matter_bytes, raw_pinned_url


def _download_matter(model_key: str):
    import urllib.request
    manifest = load_solar_matter_manifest()
    with urllib.request.urlopen(raw_pinned_url(model_key, manifest), timeout=60) as r:
        data = r.read()
    return parse_solar_matter_bytes(model_key, data, manifest)


def _pee_function(table, component: str):
    weights = normalized_production_weights(table, component)
    p12, p13, dm21 = numerical_solar_parameters()
    density = table.electron_density_mol_cm3
    def pee(energy_mev: float) -> float:
        if energy_mev <= 0.0:
            raise ValueError("Pee is undefined at non-positive energy")
        return sum(w * adiabatic_day_pee_at_density(energy_mev, ne, p12, p13, dm21) for w, ne in zip(weights, density))
    return pee


def _integrand(energy_mev: float, shape: float, pee, low_energy_mode: str) -> float:
    sigma = cl37_sigma_cm2(energy_mev, low_energy_mode=low_energy_mode)
    if sigma == 0.0 or shape == 0.0:
        return 0.0
    return shape * pee(energy_mev) * sigma


def _continuum_snu(component: str, flux: float, table, path: Path, low_energy_mode: str) -> float:
    e, f = parse_two_column_spectrum(path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    pee = _pee_function(table, component)
    return flux * trapz(e, [_integrand(x, w, pee, low_energy_mode) for x, w in zip(e, f)]) / norm / 1e-36


def _profile_snu(flux: float, table, path: Path, branch_weight: float, low_energy_mode: str) -> float:
    e, f = parse_two_column_spectrum(path.read_text(encoding="utf-8"))
    norm = trapz(e, f)
    pee = _pee_function(table, "Be7")
    return flux * branch_weight * trapz(e, [_integrand(x, w, pee, low_energy_mode) for x, w in zip(e, f)]) / norm / 1e-36


def oscillated_cl37_snu(
    model: str,
    workdir: str | Path,
    *,
    low_energy_mode: str = "threshold_linear",
    be7_mode: str = "source_average",
) -> dict[str, float]:
    """Return component and total oscillated Cl-37 capture rates in SNU.

    ``be7_mode='source_average'`` is the authoritative default: it uses the
    published Bahcall-Ulrich standard-spectrum Be7 average cross section and
    the production-averaged Pee of the capture-active 0.862-MeV line.  The
    legacy ``profile`` mode retains the explicit sub-1-MeV interpolation only
    for sensitivity/history comparisons.
    """
    if be7_mode not in {"source_average", "profile"}:
        raise ValueError("be7_mode must be source_average or profile")
    key = model.upper()
    if key not in {"GS98", "AGSS09MET"}:
        raise ValueError("model must be GS98 or AGSS09met")
    model_key = "B16_GS98" if key == "GS98" else "B16_AGSS09met"
    table = _download_matter(model_key)
    fluxes = load_b16_fluxes(model)
    paths = materialize_all_spectra(workdir)
    out: dict[str, float] = {}
    for comp in ("pp", "hep", "B8", "N13", "O15", "F17"):
        out[comp] = _continuum_snu(comp, fluxes[comp].flux_cm2_s, table, paths[comp], low_energy_mode)
    pep_e = load_spectrum_manifest()["pep"].line_energy_mev
    assert pep_e is not None
    out["pep"] = fluxes["pep"].flux_cm2_s * _pee_function(table, "pep")(pep_e) * cl37_sigma_cm2(pep_e, low_energy_mode=low_energy_mode) / 1e-36
    if be7_mode == "source_average":
        out["Be7"] = be7_authority_oscillated_snu(fluxes["Be7"].flux_cm2_s, _pee_function(table, "Be7")(0.862))
    else:
        out["Be7"] = _profile_snu(fluxes["Be7"].flux_cm2_s, table, paths["Be7_ground"], 0.897, low_energy_mode) + _profile_snu(fluxes["Be7"].flux_cm2_s, table, paths["Be7_excited"], 0.103, low_energy_mode)
    out["total"] = sum(out.values())
    return out
