#!/usr/bin/env python3
"""NMIR v2 0105a5b R1b: byte-first B4RITM machine-schema audit.

All nine Saved Original CSV payloads are fetched and SHA256-verified against
0105a4d *before any CSV is decoded or parsed*. After that barrier this script
records only schema/structural information needed to determine whether the
frozen standard-3nu/null likelihood can be reproduced. It never constructs an
oscillated expectation, chi-square, nuisance fit, observed-minus-null residual,
or BSM quantity.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import socket
import time
import urllib.error
import urllib.request

DATASET_DOI = "10.7910/DVN/B4RITM"
FORBIDDEN_STERILE_DOI = "10.7910/DVN/QKL28Z"
TRANSIENT_HTTP = {429, 500, 502, 503, 504}

FILES = {
    "data.csv": (11646859, "68bdc3db7404d497a0c439fb2d95ab0b7ed9942ac4ed6dde236e761413360cfd"),
    "hs_numu_cc.csv": (11646858, "115faa79d37e36da7a170f26003aa10fed8b4f74cc4f05c8bc80a14c4c66c80a"),
    "hs_nu_nc_nue_cc.csv": (11646854, "b0dad7154fd0f1ca0b76c04f47bcdfd56de5689ac882238a1b5e9e4033e248be"),
    "hs_nutau_cc.csv": (11646853, "811ee4547e60a8e1ebe9037f6b6c48a2c4720b20daa49298af888aa384479f11"),
    "mc_mu.csv": (11646851, "b4efdd740b85bbfe5a8365d5f82284946620af3d355de795bb5bf9606958f28c"),
    "mc_nue_cc.csv": (11646852, "a968f274726dc4b316c6eb9d93901dacda13dc92528d1081887fd473a958cf8b"),
    "mc_numu_cc.csv": (11646856, "a3bc53223d8e6f9b9e43e36d277550976631315f5a00771dff2c588120410724"),
    "mc_nu_nc.csv": (11646850, "aab94b5e0e285135471d5eb7b27db3f818f40c423ed95f27af6d3ba06becf355"),
    "mc_nutau_cc.csv": (11646855, "7e8596016ae4a9fca8e2d805c132f3b89ac9a6eacfb1ea828a7347f6c0184f07"),
}

DATA_REQUIRED = {"count", "pid", "reco_coszen", "reco_energy"}
MC_REQUIRED = {
    "reco_energy", "reco_coszen", "pid", "pdg", "true_energy", "true_coszen",
    "weight", "type", "interaction", "MaCCQE_linear", "MaCCQE_quad",
    "MaCCRES_linear", "MaCCRES_quad", "Q2", "W", "x", "y",
}
MU_REQUIRED = {"count", "abs_uncertainty", "pid", "reco_coszen", "reco_energy"}
HS_REQUIRED = {
    "reco_energy", "reco_coszen", "pid", "deltam31", "intercept",
    "dom_eff", "hole_ice_p0", "hole_ice_p1", "bulk_ice_abs", "bulk_ice_scatter",
}
RECO_KEYS = ("reco_energy", "reco_coszen", "pid")


def fetch(url: str, attempts: int = 4, timeout: int = 240) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 NMIR/0105a5b-r1b", "Accept": "text/csv,*/*;q=0.8"},
    )
    last = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in TRANSIENT_HTTP:
                raise RuntimeError(f"BLOCKED_0105A5B_R1B_HTTP_{exc.code} url={url}") from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last = exc
        if attempt < attempts:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"BLOCKED_0105A5B_R1B_TRANSPORT attempts={attempts} url={url}") from last


def file_url(file_id: int) -> str:
    return f"https://dataverse.harvard.edu/api/access/datafile/{file_id}?format=original"


def byte_barrier(fetcher=fetch) -> tuple[dict[str, bytes], list[dict]]:
    raw: dict[str, bytes] = {}
    checks = []
    # Fetch all opaque payloads first. Do not decode any CSV in this loop.
    for name, (file_id, expected_sha) in FILES.items():
        payload = fetcher(file_url(file_id))
        raw[name] = payload
        actual_sha = hashlib.sha256(payload).hexdigest()
        checks.append({
            "name": name,
            "file_id": file_id,
            "request_mode": "saved-original",
            "request_url": file_url(file_id),
            "byte_count": len(payload),
            "expected_sha256": expected_sha,
            "actual_sha256": actual_sha,
            "sha256_match": actual_sha == expected_sha,
        })
    return raw, checks


def parse_csv(payload: bytes) -> tuple[list[str], list[dict[str, str]]]:
    text = payload.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    cols = list(reader.fieldnames or [])
    rows = list(reader)
    return cols, rows


def fnum(v: str) -> float:
    return float(v)


def coord(row: dict[str, str]) -> tuple[float, float, float]:
    return tuple(fnum(row[k]) for k in RECO_KEYS)  # type: ignore[return-value]


def finite_nonnegative(values) -> bool:
    for value in values:
        x = float(value)
        if not math.isfinite(x) or x < 0:
            return False
    return True


def classify_nuisances(schema_ok: dict[str, bool]) -> dict[str, dict[str, str]]:
    detector_ok = all(schema_ok.get(k, False) for k in (
        "hs_numu_cc.csv", "hs_nu_nc_nue_cc.csv", "hs_nutau_cc.csv"
    ))
    mc_ok = all(schema_ok.get(k, False) for k in (
        "mc_nue_cc.csv", "mc_numu_cc.csv", "mc_nu_nc.csv", "mc_nutau_cc.csv"
    ))
    mu_ok = schema_ok.get("mc_mu.csv", False)

    out: dict[str, dict[str, str]] = {}
    for name in ("dom_eff", "hole_ice_p0", "hole_ice_p1", "bulk_ice_abs", "bulk_ice_scatter"):
        out[name] = {
            "class": "NATIVE_RELEASE_RESPONSE" if detector_ok else "MISSING_AUTHORITY_BLOCKER",
            "reason": "multiplicative detector hypersurface slope is byte-locked in all required flavor groups",
        }
    out["flux_spectral_index"] = {
        "class": "NATIVE_RELEASE_PRIMITIVE_EXTERNAL_FORMULA" if mc_ok else "MISSING_AUTHORITY_BLOCKER",
        "reason": "true energy/flavor/direction and generator weight are native; nominal flux and spectral response require separately pinned flux authority",
    }
    for name in ("barr_pi_plus", "barr_pi_minus", "barr_k_plus", "barr_k_minus", "barr_k0", "barr_other"):
        out[name] = {
            "class": "EXTERNAL_COMPUTATIONAL_AUTHORITY_REQUIRED" if mc_ok else "MISSING_AUTHORITY_BLOCKER",
            "reason": "event kinematics are native but six hadron-yield/MCEq-Barr response directions are not encoded as release columns",
        }
    for name, primitive in (("xsec_MaCCQE", "MaCCQE_linear/quadratic"), ("xsec_MaCCRES", "MaCCRES_linear/quadratic")):
        out[name] = {
            "class": "NATIVE_RELEASE_PRIMITIVE_EXTERNAL_FORMULA" if mc_ok else "MISSING_AUTHORITY_BLOCKER",
            "reason": f"release contains {primitive} event coefficients; publication formula/parameter convention still governs application",
        }
    out["xsec_NC_CC_ratio"] = {
        "class": "NATIVE_RELEASE_PRIMITIVE_EXTERNAL_FORMULA" if mc_ok else "MISSING_AUTHORITY_BLOCKER",
        "reason": "reaction type is encoded per event; exact nuisance convention/penalty comes from publication authority",
    }
    out["xsec_DIS_CSMS"] = {
        "class": "EXTERNAL_COMPUTATIONAL_AUTHORITY_REQUIRED" if mc_ok else "MISSING_AUTHORITY_BLOCKER",
        "reason": "Q2/W/x/y are native DIS primitives but no exact GENIE-to-CSMS event response is encoded in the CSV schema",
    }
    out["atmospheric_muon_scale"] = {
        "class": "NATIVE_RELEASE_RESPONSE" if mu_ok else "MISSING_AUTHORITY_BLOCKER",
        "reason": "per-bin atmospheric-muon template and absolute uncertainty are native; scalar normalization is explicit",
    }
    out["global_effective_area_scale"] = {
        "class": "NATIVE_RELEASE_RESPONSE" if mc_ok else "MISSING_AUTHORITY_BLOCKER",
        "reason": "global rate normalization acts directly on native predicted neutrino event weights",
    }
    assert len(out) == 18
    return out


def analyze(raw: dict[str, bytes], checks: list[dict]) -> dict:
    all_hashes = len(checks) == 9 and all(c["sha256_match"] for c in checks)
    common = {
        "benchmark": "NMIR-V2-0105A5B-R1B",
        "dataset_doi": DATASET_DOI,
        "forbidden_sterile_doi": FORBIDDEN_STERILE_DOI,
        "byte_checks": checks,
        "all_nine_sha256_match_0105a4d": all_hashes,
        "oscillated_expectation_computed": False,
        "chi2_computed": False,
        "nuisance_fit_executed": False,
        "observed_minus_null_residual_computed": False,
        "observed_residual_execution_allowed": False,
        "bsm_interpretation_allowed": False,
    }
    if not all_hashes:
        return {**common, "status": "BLOCKED_0105A5B_BYTE_AUTHORITY_MISMATCH", "files": {}}

    parsed = {name: parse_csv(payload) for name, payload in raw.items()}
    schema_ok: dict[str, bool] = {}
    files_out: dict[str, dict] = {}

    for name, (cols, rows) in parsed.items():
        if name == "data.csv": required = DATA_REQUIRED
        elif name == "mc_mu.csv": required = MU_REQUIRED
        elif name.startswith("hs_"): required = HS_REQUIRED
        else: required = MC_REQUIRED
        ok = required.issubset(set(cols))
        schema_ok[name] = ok
        files_out[name] = {
            "columns": cols,
            "column_count": len(cols),
            "row_count": len(rows),
            "required_columns_present": ok,
            "missing_required_columns": sorted(required - set(cols)),
        }

    # Structural data audit only.
    dcols, data = parsed["data.csv"]
    data_coords = [coord(r) for r in data]
    unique_coords = set(data_coords)
    energies = sorted({c[0] for c in unique_coords})
    coszens = sorted({c[1] for c in unique_coords})
    pids = sorted({c[2] for c in unique_coords})
    observed_total = sum(float(r["count"]) for r in data)
    data_structure = {
        "row_count": len(data),
        "unique_coordinate_count": len(unique_coords),
        "duplicate_coordinate_count": len(data_coords) - len(unique_coords),
        "unique_reco_energy_count": len(energies),
        "unique_reco_coszen_count": len(coszens),
        "unique_pid_count": len(pids),
        "reco_energy_midpoints": energies,
        "reco_coszen_midpoints": coszens,
        "pid_midpoints": pids,
        "count_sum": observed_total,
        "count_finite_nonnegative": finite_nonnegative(r["count"] for r in data),
        "exact_200_cells": len(data) == 200 and len(unique_coords) == 200,
        "exact_10x10x2_axis_counts": (len(energies), len(coszens), len(pids)) == (10, 10, 2),
        "observed_total_21914": math.isclose(observed_total, 21914.0, rel_tol=0.0, abs_tol=1e-9),
    }

    _, mu = parsed["mc_mu.csv"]
    mu_coords = {coord(r) for r in mu}
    mu_structure = {
        "row_count": len(mu),
        "unique_coordinate_count": len(mu_coords),
        "covers_all_200_data_coordinates": mu_coords == unique_coords,
        "count_finite_nonnegative": finite_nonnegative(r["count"] for r in mu),
        "abs_uncertainty_finite_nonnegative": finite_nonnegative(r["abs_uncertainty"] for r in mu),
    }

    mc_structure = {}
    for name in ("mc_nue_cc.csv", "mc_numu_cc.csv", "mc_nu_nc.csv", "mc_nutau_cc.csv"):
        _, rows = parsed[name]
        coords = {coord(r) for r in rows}
        mc_structure[name] = {
            "row_count": len(rows),
            "unique_analysis_coordinate_count": len(coords),
            "coordinates_subset_of_data_grid": coords.issubset(unique_coords),
            "all_reco_and_true_core_fields_parseable_finite": all(
                all(math.isfinite(float(r[k])) for k in ("reco_energy", "reco_coszen", "pid", "pdg", "true_energy", "true_coszen", "weight"))
                for r in rows
            ),
        }

    hs_structure = {}
    hs_all_full = True
    for name in ("hs_numu_cc.csv", "hs_nu_nc_nue_cc.csv", "hs_nutau_cc.csv"):
        _, rows = parsed[name]
        supports = sorted({float(r["deltam31"]) for r in rows})
        per_support = {}
        for dm in supports:
            coords = {coord(r) for r in rows if float(r["deltam31"]) == dm}
            per_support[repr(dm)] = {
                "unique_coordinate_count": len(coords),
                "matches_data_grid": coords == unique_coords,
            }
            hs_all_full &= coords == unique_coords
        hs_structure[name] = {
            "row_count": len(rows),
            "deltam31_support_count": len(supports),
            "deltam31_support": supports,
            "per_support": per_support,
            "machine_scattering_column": "bulk_ice_scatter" if "bulk_ice_scatter" in files_out[name]["columns"] else None,
            "readme_alias_bulk_ice_scat_recorded": True,
        }

    nuisances = classify_nuisances(schema_ok)
    classes = {v["class"] for v in nuisances.values()}
    classification_complete = len(nuisances) == 18 and all(v["class"] in {
        "NATIVE_RELEASE_RESPONSE", "NATIVE_RELEASE_PRIMITIVE_EXTERNAL_FORMULA",
        "EXTERNAL_COMPUTATIONAL_AUTHORITY_REQUIRED", "MISSING_AUTHORITY_BLOCKER",
    } for v in nuisances.values())

    gates = {
        "all_nine_sha256_match_0105a4d": all_hashes,
        "all_frozen_minimum_schemas_present": all(schema_ok.values()),
        "exact_200_observed_cells": data_structure["exact_200_cells"],
        "exact_10x10x2_observed_axes": data_structure["exact_10x10x2_axis_counts"],
        "observed_total_exact_21914": data_structure["observed_total_21914"],
        "observed_counts_finite_nonnegative": data_structure["count_finite_nonnegative"],
        "muon_template_full_grid_and_finite_nonnegative": (
            mu_structure["covers_all_200_data_coordinates"]
            and mu_structure["count_finite_nonnegative"]
            and mu_structure["abs_uncertainty_finite_nonnegative"]
        ),
        "mc_coordinates_within_observed_grid": all(v["coordinates_subset_of_data_grid"] for v in mc_structure.values()),
        "hypersurfaces_cover_full_grid_at_each_dm31_support": hs_all_full,
        "all_18_nuisances_classified": classification_complete,
        "observed_residual_execution_remains_locked": True,
        "bsm_interpretation_remains_locked": True,
    }
    required = [k for k in gates if k not in ()]
    passed = all(gates[k] for k in required)
    return {
        **common,
        "status": (
            "PASS_0105A5B_R1B_MACHINE_SCHEMA_AUDIT_NONDISCOVERY"
            if passed else "BLOCKED_0105A5B_R1B_MACHINE_SCHEMA_OR_STRUCTURE_INCOMPLETE"
        ),
        "files": files_out,
        "schema_ok": schema_ok,
        "data_structure": data_structure,
        "muon_structure": mu_structure,
        "mc_structure": mc_structure,
        "hypersurface_structure": hs_structure,
        "nuisance_authority": nuisances,
        "nuisance_classes_present": sorted(classes),
        "external_dependencies_still_required": any(
            v["class"] == "EXTERNAL_COMPUTATIONAL_AUTHORITY_REQUIRED" for v in nuisances.values()
        ),
        "missing_authority_blocker_present": any(
            v["class"] == "MISSING_AUTHORITY_BLOCKER" for v in nuisances.values()
        ),
        "standard_3nu_propagation_external_authority_required": True,
        "gates": gates,
    }


def build(fetcher=fetch) -> dict:
    raw, checks = byte_barrier(fetcher=fetcher)
    return analyze(raw, checks)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", type=Path, default=Path("artifacts/0105a5b_r1b"))
    args = p.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result = build()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out = args.output_dir / "deepcore_r1b_machine_schema_audit.json"
    out.write_text(text, encoding="utf-8")
    digest = hashlib.sha256(text.encode()).hexdigest()
    (args.output_dir / "manifest_sha256.txt").write_text(digest + "\n", encoding="utf-8")
    print(text, end="")
    print(f"manifest_sha256={digest}")
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
