#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

from nmir.cevns_solar_optimize import (
    git_blob_sha,
    load_all_spectra,
    normalized,
    read_fluxes,
    read_manifest,
)
from nmir.contact_unitarity_ceiling import (
    continuum_power_w_per_kg,
    line_power_w_per_kg,
    nuclei_per_kg_class,
    partial_wave_lmax,
    power_kernel_w_per_target,
    refine_linear_spectrum,
    sigma_unitarity_cm2,
    trapz_values,
)

FLUX_PATH = Path("data/solar_flux_b16.csv")
MANIFEST_PATH = Path("data/solar_spectrum_manifest.csv")
BE7_GROUND_PATH = Path("data/be7_bahcall1994_ground_profile.csv")
EXPECTED_LOCAL_BLOBS = {
    "data/solar_flux_b16.csv": "4c190992fed3dad60dbdc09af114fd28be8b29a9",
    "data/solar_spectrum_manifest.csv": "06ea4fe761eccbc2a5faa075feaa66c52a75fb2e",
    "data/be7_bahcall1994_ground_profile.csv": "f68370cf99f3d272631931f138b514739b6f394a",
}
COMPONENTS = ["pp", "Be7_ground", "Be7_excited", "pep", "N13", "O15", "F17", "B8", "hep"]
R0_VALUES = (1.2, 1.4, 1.6)
SUBDIVISIONS_SWEEP = 8
SUBDIVISIONS_CONVERGENCE = (16, 32, 64)
CONVERGENCE_REL_TOL = 5.0e-3  # frozen before hosted scientific result
A_COARSE_STEP = 1.0
A_FINE_STEP = 0.25
A_GRID_REL_TOL = 5.0e-3  # frozen before hosted scientific result


def verify_local_provenance() -> dict[str, str]:
    out: dict[str, str] = {}
    for name, expected in EXPECTED_LOCAL_BLOBS.items():
        data = Path(name).read_bytes()
        actual = git_blob_sha(data)
        if actual != expected:
            raise RuntimeError(f"local Git blob mismatch for {name}: {actual} != {expected}")
        out[name] = actual
    return out


def component_flux(component: str, fluxes: dict[str, float]) -> float:
    if component == "Be7_ground":
        return fluxes["Be7"] * 0.897
    if component == "Be7_excited":
        return fluxes["Be7"] * 0.103
    return fluxes[component]


def component_power(
    component: str,
    a: float,
    r0_fm: float,
    mode: str,
    subdivisions: int,
    fluxes: dict[str, float],
    manifest,
    spectra,
) -> float:
    flux = component_flux(component, fluxes)
    if component == "pep":
        energy = manifest["pep"].line_energy_mev
        if energy is None:
            raise RuntimeError("pep line energy missing")
        return line_power_w_per_kg(energy, flux, a, r0_fm=r0_fm, mode=mode)
    return continuum_power_w_per_kg(
        spectra[component], flux, a, r0_fm=r0_fm, mode=mode, subdivisions=subdivisions
    )


def total_power_row(a, r0_fm, mode, subdivisions, fluxes, manifest, spectra):
    parts = {
        component: component_power(component, a, r0_fm, mode, subdivisions, fluxes, manifest, spectra)
        for component in COMPONENTS
    }
    return {
        "A": a,
        "r0_fm": r0_fm,
        "lmax_mode": mode,
        "components_w_per_kg": parts,
        "total_w_per_kg": sum(parts.values()),
        "dominant_component": max(parts, key=parts.get),
    }


def a_grid(step: float) -> list[float]:
    n = int(round((250.0 - 1.0) / step))
    return [1.0 + i * step for i in range(n + 1)]


def sweep(step, r0_fm, mode, fluxes, manifest, spectra):
    best = None
    for a in a_grid(step):
        row = total_power_row(a, r0_fm, mode, SUBDIVISIONS_SWEEP, fluxes, manifest, spectra)
        if best is None or row["total_w_per_kg"] > best["total_w_per_kg"]:
            best = row
    assert best is not None
    return best


def pp_low_energy_power(a, r0_fm, mode, fluxes, spectra, upper_mev=0.1):
    points = refine_linear_spectrum(normalized(spectra["pp"]), 128)
    weighted = []
    for e, w in points:
        if e > upper_mev:
            break
        weighted.append((e, power_kernel_w_per_target(e, w, fluxes["pp"], a, r0_fm, mode)))
    if len(weighted) < 2:
        return 0.0
    return nuclei_per_kg_class(a) * trapz_values(weighted)


def main() -> None:
    local_blobs = verify_local_provenance()
    fluxes = read_fluxes(FLUX_PATH, "b16_gs98_flux_cm2_s")
    manifest = read_manifest(MANIFEST_PATH)
    spectra = load_all_spectra(manifest, BE7_GROUND_PATH)

    external_pins = {
        component: {
            "source_repo": manifest[component].source_repo,
            "source_commit": manifest[component].source_commit,
            "source_path": manifest[component].source_path,
            "source_blob_sha": manifest[component].source_blob_sha,
        }
        for component in ["pp", "hep", "B8", "N13", "O15", "F17", "Be7_excited"]
    }

    sweep_rows = []
    scientific_candidates = []
    for r0 in R0_VALUES:
        coarse = sweep(A_COARSE_STEP, r0, "ceil", fluxes, manifest, spectra)
        fine = sweep(A_FINE_STEP, r0, "ceil", fluxes, manifest, spectra)
        floor_control = sweep(A_FINE_STEP, r0, "floor", fluxes, manifest, spectra)
        rel_grid = abs(fine["total_w_per_kg"] - coarse["total_w_per_kg"]) / fine["total_w_per_kg"]
        sweep_rows.append({"r0_fm": r0, "coarse": coarse, "fine": fine, "floor_control": floor_control, "a_grid_max_relative_change": rel_grid})
        scientific_candidates.append(fine)

    winner = max(scientific_candidates, key=lambda row: row["total_w_per_kg"])
    a_win = winner["A"]
    r0_win = winner["r0_fm"]

    convergence = []
    for subdivisions in SUBDIVISIONS_CONVERGENCE:
        convergence.append(total_power_row(a_win, r0_win, "ceil", subdivisions, fluxes, manifest, spectra))
    max_conv_rel = abs(convergence[-1]["total_w_per_kg"] - convergence[-2]["total_w_per_kg"]) / convergence[-1]["total_w_per_kg"]

    physical_controls = [
        total_power_row(float(a), r0_win, "ceil", 32, fluxes, manifest, spectra)
        for a in (1, 4, 12, 16, 28, 40, 56, 82, 132, 184, 208, 238)
    ]
    # Algebra/unit controls included in the artifact as inspectable diagnostics.
    s_wave_1mev = sigma_unitarity_cm2(1.0, 1.0, r0_win, "floor")
    ceil_1mev = sigma_unitarity_cm2(1.0, 1.0, r0_win, "ceil")
    pp_low = pp_low_energy_power(a_win, r0_win, "ceil", fluxes, spectra)

    provenance_ok = bool(local_blobs) and all(pin["source_blob_sha"] for pin in external_pins.values())
    grid_ok = all(row["a_grid_max_relative_change"] <= A_GRID_REL_TOL for row in sweep_rows)
    convergence_ok = max_conv_rel <= CONVERGENCE_REL_TOL
    model_ok = (
        provenance_ok
        and grid_ok
        and convergence_ok
        and s_wave_1mev > 0.0
        and ceil_1mev >= s_wave_1mev
        and partial_wave_lmax(1.0, 1.0, r0_win, "floor") == 0
        and math.isfinite(winner["total_w_per_kg"])
        and winner["total_w_per_kg"] > 0.0
    )

    if not model_ok:
        status = "FAIL_UNITARITY_MODEL"
    elif winner["total_w_per_kg"] < 1.0:
        status = "PASS_CONTACT_RESIDUAL_BOUND_BELOW_1WKG"
    else:
        status = "PASS_UNITARITY_BOUND_VALID_BUT_TOO_WEAK / RESIDUAL_OPEN"

    result = {
        "status": status,
        "scientific_ceiling_w_per_kg": winner["total_w_per_kg"],
        "distance_to_1_w_per_kg_factor": winner["total_w_per_kg"],
        "winner": winner,
        "r0_and_grid_sweeps": sweep_rows,
        "energy_convergence_at_winner": convergence,
        "max_relative_32_to_64_change": max_conv_rel,
        "convergence_rel_tol": CONVERGENCE_REL_TOL,
        "a_grid_rel_tol": A_GRID_REL_TOL,
        "pp_below_0p1mev_w_per_kg_at_winner": pp_low,
        "s_wave_floor_sigma_1mev_A1_cm2": s_wave_1mev,
        "ceil_sigma_1mev_A1_cm2": ceil_1mev,
        "physical_A_controls": physical_controls,
        "local_source_git_blobs": local_blobs,
        "external_spectrum_pins": external_pins,
        "solar_flux_branch": "B16 GS98",
        "be7_branching": {"ground": 0.897, "excited": 0.103},
        "pep_line_energy_mev": manifest["pep"].line_energy_mev,
        "formula": "P=N_T integral Phi(E) [4*pi*(lmax+1)^2/k^2] E dE, k=E/(hbar*c), Edep=E, lmax=ceil(k*1.4fm*A^(1/3)); scientific max also scans r0=1.2,1.4,1.6fm",
        "scope": "coefficient-independent inclusive short-range/contact upper ceiling only; no detector/metastable/resonance/gravity/geometry gain multiplication",
        "model_ok": model_ok,
    }
    Path("contact_unitarity_ceiling_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not model_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
