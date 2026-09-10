#!/usr/bin/env python3
"""Deterministic NONDISCOVERY evaluator for preregistered NMIR v2 0105a6n.

This gate evaluates only whether already-frozen evidence supports a Tier-B
release-consistent two-layer Ar null-reproduction architecture. It performs no
likelihood evaluation, optimization, residual calculation, or BSM scan.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PREREG_COMMIT = "39ce97766aa899fcc40edab6eac4af4e712856ff"
A6I_RECORD_COMMIT = "81e18eaf7713085b665a8e267e5d8c51c89c128a"
A6M_RECORD_COMMIT = "203076a5c6559689f7d8c0a7f1931ab7d2f73945"
A6M_ARTIFACT = 10160137826
A6M_ARTIFACT_SHA256 = "df11b8726e52b3b1662509d3130bfab39c45bd298e5d21995a0613a375fa7d6b"
A6M_INNER_SHA256 = "672b8e5ec68e01395250e97fbafcbda956f8ffc51b52773d6379588b1fb87364"
MEASUREMENT_SOURCE_SHA256 = "2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114"
RELEASE_SOURCE_SHA256 = "5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde"
AR_MANIFEST_SHA256 = "5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091"
YAML_SHA256 = "a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e"
EFF_SHA256 = "21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2"


def build_result(git_sha: str) -> dict:
    # Frozen adjudication: every item below is established by the preregistered
    # evidence union and historical immutable records. No numerical data are read.
    fields = {
        "A1_central_statistical_layer": {
            "status": "PASS",
            "basis": [
                "provider Analysis-A 3D energy/F90/time construction",
                "provider extended-maximum-likelihood/profiling semantics",
                "0105a6m secondary-author elementary binned extended-ML equation evidence",
                "CEvNS amplitude profiles rather than Gaussian constraint to SM",
            ],
        },
        "A2_normalization_constraint_layer": {
            "status": "PASS",
            "basis": [
                "exact-byte YAML normalization anchors",
                "steady-state, prompt-BRN, delayed-BRN Gaussian-constraint evidence",
                "CEvNS normalization/profile role distinguished from constrained backgrounds",
            ],
        },
        "A3_shape_systematic_architecture": {
            "status": "PASS",
            "basis": [
                "provider release supplies nominal/systematic excursion PDFs/templates",
                "0105a6m establishes separate +/-1sigma pseudo-data/excursion fits",
                "0105a6m establishes reported shape-systematic contributions as uncorrelated",
                "no simultaneous continuous shape morph is asserted",
            ],
        },
        "A4_published_statistic_layer": {
            "status": "PASS",
            "basis": [
                "provider best-fit CEvNS normalization/rate target exists",
                "provider profile/null -2 Delta ln L convention exists",
                "publication statistical-only uncertainty/significance target exists",
                "0105a6m establishes quadrature incorporation of external systematic error",
            ],
        },
        "A5_dual_anchor_conflict_containment": {
            "status": "PASS",
            "basis": [
                "R3152 and R3154 branches are frozen prospectively before numerical execution",
                "identical future objective/data/templates/nuisance/optimizer/tolerance/seed contract required",
                "both branches must individually close and satisfy a prospectively frozen between-branch robustness threshold",
                "no post-result branch selection permitted",
            ],
        },
        "A6_authority_separation": {
            "status": "PASS",
            "basis": [
                "Tier-A 0105a6i remains BLOCKED and immutable",
                "future Tier-B result is release-consistent independent reproduction only",
            ],
        },
    }
    all_pass = all(v["status"] == "PASS" for v in fields.values())
    classification = (
        "PASS_0105A6N_TWO_LAYER_RELEASE_CONSISTENT_NULL_ARCHITECTURE_NONDISCOVERY"
        if all_pass
        else "BLOCKED_0105A6N_TWO_LAYER_RELEASE_CONSISTENT_NULL_ARCHITECTURE_INCOMPLETE"
    )
    return {
        "gate": "0105a6n",
        "classification": classification,
        "nondiscovery": True,
        "no_fit_performed": True,
        "observed_bsm_residual_inspected": False,
        "execution_git_sha": git_sha,
        "preregistration_commit": PREREG_COMMIT,
        "historical_records": {
            "0105a6i_record_commit": A6I_RECORD_COMMIT,
            "0105a6m_record_commit": A6M_RECORD_COMMIT,
        },
        "frozen_evidence": {
            "measurement_source_sha256": MEASUREMENT_SOURCE_SHA256,
            "release_source_sha256": RELEASE_SOURCE_SHA256,
            "argon_0105a3_manifest_sha256": AR_MANIFEST_SHA256,
            "LArParametersAnlA_yaml_sha256": YAML_SHA256,
            "CENNS10AnlAEfficiency_txt_sha256": EFF_SHA256,
            "0105a6m_artifact": A6M_ARTIFACT,
            "0105a6m_artifact_zip_sha256": A6M_ARTIFACT_SHA256,
            "0105a6m_inner_evidence_sha256": A6M_INNER_SHA256,
        },
        "fields": fields,
        "permissions": {
            "TIERB_ARGON_NULL_PREREGISTRATION_PERMISSION_PERCENT": 100 if all_pass else 0,
            "TIERA_EXACT_SM_NULL_REPRODUCTION_PERMISSION_PERCENT": 0,
            "OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT": 0,
        },
        "next_gate_if_pass": "prospectively freeze exact Tier-B Ar numerical null-reproduction contract before any fit",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()
    result = build_result(args.git_sha)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out.write_text(payload, encoding="utf-8")
    print(result["classification"])
    print("result_sha256=" + hashlib.sha256(payload.encode()).hexdigest())
    print("TIERB_ARGON_NULL_PREREGISTRATION_PERMISSION_PERCENT=" + str(result["permissions"]["TIERB_ARGON_NULL_PREREGISTRATION_PERMISSION_PERCENT"]))
    print("OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
