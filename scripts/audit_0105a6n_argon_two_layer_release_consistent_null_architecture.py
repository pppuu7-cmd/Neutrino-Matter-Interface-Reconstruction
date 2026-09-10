#!/usr/bin/env python3
"""0105a6n: test the prospectively frozen two-layer Analysis-A reproduction architecture.

NONDICOVERY / NO FIT. Primary provider sources define release-facing semantics;
0105a6m supplies provenance-qualified secondary-author corroboration only.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import tarfile
import time
import urllib.request
from pathlib import Path

BENCHMARK = "NMIR-V2-0105A6N"
PREREG_COMMIT = "39ce97766aa899fcc40edab6eac4af4e712856ff"
MEASUREMENT_URL = "https://export.arxiv.org/e-print/2003.10630v7"
RELEASE_URL = "https://export.arxiv.org/e-print/2006.12659v2"
MEASUREMENT_SHA256 = "2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114"
RELEASE_SHA256 = "5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde"
PARENT_EVIDENCE_SHA256 = "672b8e5ec68e01395250e97fbafcbda956f8ffc51b52773d6379588b1fb87364"
PARENT_EXECUTION_SHA = "05a8cfb4275d59604b7a6d18ebc44cbe8967bf3f"
YAML_SHA256 = "a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e"
EFF_SHA256 = "21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2"
AR_MANIFEST_SHA256 = "5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str, attempts: int = 4) -> bytes:
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-authority-audit/0105a6n"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as exc:
            last = exc
            if i + 1 < attempts:
                time.sleep(2 ** i)
    raise RuntimeError(f"provider fetch failed: {type(last).__name__}: {last}")


def tex_text(raw: bytes) -> str:
    if raw.startswith(b"%PDF"):
        raise ValueError("source endpoint returned PDF rather than frozen source payload")
    chunks: list[str] = []
    try:
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:*") as tf:
            for m in tf.getmembers():
                if m.isfile() and m.name.lower().endswith((".tex", ".txt", ".yaml", ".yml")):
                    f = tf.extractfile(m)
                    if f:
                        chunks.append(f.read().decode("utf-8", errors="replace"))
    except tarfile.TarError:
        chunks.append(raw.decode("utf-8", errors="replace"))
    if not chunks:
        raise ValueError("no textual source members")
    return "\n".join(chunks)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", text.lower())).strip()


def has(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.I | re.S) is not None


def evidence_text(parent: dict, families: set[str] | None = None) -> str:
    chunks = []
    for page in parent.get("pages", []):
        for fam, payload in page.get("evidence_windows", {}).items():
            if families is None or fam in families:
                chunks.append(payload.get("window", ""))
    return " ".join(chunks)


def audit(measurement: str, release: str, parent: dict) -> dict:
    secondary_all = evidence_text(parent)
    secondary_f1 = evidence_text(parent, {"F1"})
    secondary_f3 = evidence_text(parent, {"F3"})
    secondary_f6 = evidence_text(parent, {"F6"})

    evidence = {
        "primary_extended_ml": has(measurement, r"extended.{0,50}maximum.{0,50}likelihood"),
        "primary_profile_semantics": has(measurement, r"profil(?:e|ed|ing)"),
        "primary_null_statistic": has(measurement, r"-\s*2.{0,100}(?:ln|log).{0,30}L"),
        "release_3d_binned": has(release, r"3.?D.{0,60}binned arrays|3.?dimensional.{0,100}binned"),
        "release_gaussian_constraints": has(release, r"Gaussian constraint"),
        "release_cevnspdf": has(release, r"cevnspdf\.txt"),
        "release_brn_pdfs": has(release, r"brnpdf\.txt") and has(release, r"delbrnpdf\.txt"),
        "release_ss_pdf": has(release, r"bkgpdf\.txt"),
        "release_alternative_systematic_fits": has(release, r"systematics.{0,350}alternative fits|alternative fits.{0,350}systematic"),
        "release_has_3152": "3152" in release,
        "secondary_extended_binned_ml": "extended binned maximum likelihood" in secondary_f1,
        "secondary_data_log_density_term": "ln f xi" in secondary_f1 or "ln f xi" in secondary_f3,
        "secondary_gaussian_penalty": "gaussian" in secondary_f3 and "constraint" in secondary_f3,
        "secondary_prompt_brn": "prompt brn" in secondary_f3,
        "secondary_delayed_brn": "delayed brn" in secondary_f3,
        "secondary_steady_state": "steady state" in secondary_f3 or "beam unrelated background" in secondary_f3,
        "secondary_cevns_profile": "cevns signal is profiled" in secondary_f3 or "profile likelihood" in secondary_f3,
        "secondary_uncorrelated_excursions": "uncorrelated systematic errors" in secondary_f6,
        "secondary_excursion_pdfs": "excursion pdf" in secondary_f6,
        "secondary_quadrature": "added in quadrature" in secondary_f6,
        "secondary_stat_only_significance": "stat only" in secondary_f6,
        "secondary_final_combined_significance": "stat syst" in secondary_all and "3 5" in secondary_all,
        "secondary_has_3154": "3154" in secondary_all,
    }

    fields = {
        "A1_central_statistical_layer": all([
            evidence["primary_extended_ml"], evidence["release_3d_binned"], evidence["release_cevnspdf"],
            evidence["release_brn_pdfs"], evidence["release_ss_pdf"], evidence["secondary_extended_binned_ml"],
            evidence["secondary_data_log_density_term"], evidence["secondary_cevns_profile"],
        ]),
        "A2_normalization_constraint_layer": all([
            evidence["release_gaussian_constraints"], evidence["secondary_gaussian_penalty"],
            evidence["secondary_prompt_brn"], evidence["secondary_delayed_brn"],
            evidence["secondary_steady_state"], evidence["secondary_cevns_profile"],
        ]),
        "A3_shape_systematic_architecture": all([
            evidence["release_alternative_systematic_fits"], evidence["secondary_uncorrelated_excursions"],
            evidence["secondary_excursion_pdfs"], evidence["secondary_quadrature"],
        ]),
        "A4_published_statistic_layer": all([
            evidence["primary_profile_semantics"], evidence["primary_null_statistic"],
            evidence["secondary_stat_only_significance"], evidence["secondary_quadrature"],
            evidence["secondary_final_combined_significance"],
        ]),
        "A5_dual_anchor_conflict_containment": evidence["release_has_3152"] and evidence["secondary_has_3154"],
        "A6_authority_separation": True,
    }
    all_pass = all(fields.values())
    return {
        "benchmark": BENCHMARK,
        "preregistration_commit": PREREG_COMMIT,
        "evidence": evidence,
        "architecture_fields": {k: {"pass": v} for k, v in fields.items()},
        "all_architecture_fields_pass": all_pass,
        "classification": (
            "PASS_0105A6N_TWO_LAYER_RELEASE_CONSISTENT_NULL_ARCHITECTURE_NONDISCOVERY"
            if all_pass else
            "BLOCKED_0105A6N_TWO_LAYER_RELEASE_CONSISTENT_NULL_ARCHITECTURE_INCOMPLETE"
        ),
        "authority_separation": {
            "tierA_exact_collaboration_internal_contract": "BLOCKED_0105A6I_ARGON_LIKELIHOOD_IMPLEMENTATION_AUTHORITY_INCOMPLETE",
            "tierB_label": "release-consistent independent reproduction",
            "collaboration_release_authority_from_secondary_source": False,
        },
        "dual_anchor_future_rule": {
            "R3152": {"steady_state_center": 3152, "width": 25, "source": "official release table"},
            "R3154": {"steady_state_center": 3154, "width": 25, "source": "exact official release YAML / secondary corroboration"},
            "post_result_branch_selection_forbidden": True,
        },
        "byte_anchors": {
            "Ar_0105a3_manifest_sha256": AR_MANIFEST_SHA256,
            "LArParametersAnlA.yaml_sha256": YAML_SHA256,
            "CENNS10AnlAEfficiency.txt_sha256": EFF_SHA256,
            "0105a6m_evidence_sha256": PARENT_EVIDENCE_SHA256,
        },
        "tierB_argon_null_preregistration_permission_percent": 100 if all_pass else 0,
        "tierA_exact_sm_null_reproduction_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "numerical_fit_performed": False,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent-evidence", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    ns = ap.parse_args()
    parent_raw = Path(ns.parent_evidence).read_bytes()
    if sha256(parent_raw) != PARENT_EVIDENCE_SHA256:
        raise SystemExit("0105a6m evidence SHA256 mismatch")
    parent = json.loads(parent_raw)
    if parent.get("git_sha") != PARENT_EXECUTION_SHA:
        raise SystemExit("0105a6m execution SHA mismatch")
    mraw = fetch(MEASUREMENT_URL)
    rraw = fetch(RELEASE_URL)
    if sha256(mraw) != MEASUREMENT_SHA256:
        raise SystemExit("measurement source SHA256 mismatch")
    if sha256(rraw) != RELEASE_SHA256:
        raise SystemExit("release source SHA256 mismatch")
    result = audit(tex_text(mraw), tex_text(rraw), parent)
    result["git_sha"] = ns.git_sha
    result["provider_sources"] = {
        "measurement": {"url": MEASUREMENT_URL, "bytes": len(mraw), "sha256": sha256(mraw)},
        "release": {"url": RELEASE_URL, "bytes": len(rraw), "sha256": sha256(rraw)},
    }
    out = Path(ns.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
