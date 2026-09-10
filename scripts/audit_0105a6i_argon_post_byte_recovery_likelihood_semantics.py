#!/usr/bin/env python3
"""0105a6i provider-source semantic audit. NONDISCOVERY: no fit or residual access."""
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

MEASUREMENT_URL = "https://export.arxiv.org/e-print/2003.10630v7"
RELEASE_URL = "https://export.arxiv.org/e-print/2006.12659v2"
PREREG_COMMIT = "12521b8ae88aea7889c200ee913920ab645448a6"
YAML_SHA256 = "a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e"
EFF_SHA256 = "21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2"


def fetch(url: str, attempts: int = 4) -> bytes:
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-authority-audit/0105a6i"})
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read()
        except Exception as exc:  # transport is classified, never converted to semantic failure
            last = exc
            if i + 1 < attempts:
                time.sleep(2 ** i)
    raise RuntimeError(f"provider fetch failed after {attempts} attempts: {type(last).__name__}: {last}")


def tex_text(raw: bytes) -> str:
    if raw.startswith(b"%PDF"):
        raise ValueError("provider endpoint returned PDF instead of TeX/source payload")
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
        raise ValueError("no textual source members recovered")
    return "\n".join(chunks)


def has(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.I | re.S) is not None


def audit(measurement: str, release: str) -> dict:
    joined = measurement + "\n" + release
    evidence = {
        "measurement_extended_maximum_likelihood": has(measurement, r"extended.{0,40}maximum.{0,40}likelihood"),
        "measurement_roofit": has(measurement, r"RooFit"),
        "measurement_three_observables": all(has(measurement, p) for p in [r"F.?90", r"t.?\\?_{?\\?rm\s*trig", r"energy"]),
        "measurement_profile_language": has(measurement, r"profil(?:e|ed|ing)"),
        "measurement_minus2_delta_log_l": has(measurement, r"-\s*2.{0,80}(?:ln|log).{0,20}L"),
        "release_3d_binned_arrays": has(release, r"3.?D.{0,40}binned arrays|3.?dimensional.{0,80}binned"),
        "release_appropriate_likelihood_procedure": has(release, r"appropriate likelihood procedure"),
        "release_gaussian_constraint": has(release, r"Gaussian constraint"),
        "release_systematic_alternative_fits": has(release, r"systematics.{0,300}alternative fits|alternative fits.{0,300}systematic"),
        "release_mentions_cevnspdf": has(release, r"cevnspdf\.txt"),
        "release_mentions_prompt_delayed_brn": has(release, r"brnpdf\.txt") and has(release, r"delbrnpdf\.txt"),
        "release_mentions_ss": has(release, r"bkgpdf\.txt"),
        "release_explicit_binned_poisson_law": has(release, r"binned\s+Poisson|Poisson\s+likelihood"),
        "provider_explicit_shape_morphing_rule": has(joined, r"morph(?:ing)?|interpolat(?:e|ion).{0,120}(?:systematic|template|PDF)"),
        "provider_explicit_systematic_correlation_rule": has(joined, r"correlat(?:ed|ion).{0,160}(?:systematic|nuisance|template)"),
        "release_has_3152": "3152" in release,
        "release_has_3154": "3154" in release,
    }

    # Frozen decision rule from preregistration: COMPLETE requires analyst-choice-free implementation authority.
    fields = {
        "F1_elementary_objective": {
            "status": "COMPLETE" if evidence["measurement_extended_maximum_likelihood"] and evidence["release_explicit_binned_poisson_law"] and not evidence["release_appropriate_likelihood_procedure"] else "PARTIAL_OR_MISSING",
            "reason": "Extended-ML naming alone is insufficient if the release delegates an appropriate likelihood procedure or omits the elementary count law."
        },
        "F2_observables_support_binning_templates": {
            "status": "COMPLETE" if all(evidence[k] for k in ["release_3d_binned_arrays", "release_mentions_cevnspdf", "release_mentions_prompt_delayed_brn", "release_mentions_ss"]) else "PARTIAL_OR_MISSING",
            "reason": "Requires provider-defined 3D binned data plus all signal/background template identities."
        },
        "F3_nuisance_inventory_constraints": {
            "status": "COMPLETE" if evidence["release_gaussian_constraint"] and evidence["measurement_extended_maximum_likelihood"] else "PARTIAL_OR_MISSING",
            "reason": "Exact-byte YAML supplies normalization anchors; provider text must establish constraint semantics. Full shape wiring is tested separately in F4/F6."
        },
        "F4_nuisance_template_coupling": {
            "status": "COMPLETE" if evidence["provider_explicit_shape_morphing_rule"] else "PARTIAL_OR_MISSING",
            "reason": "Nominal and ±1σ templates are not an implementation rule unless provider-backed interpolation/morphing is specified."
        },
        "F5_profile_and_null_statistic": {
            "status": "COMPLETE" if evidence["measurement_profile_language"] and evidence["measurement_minus2_delta_log_l"] else "PARTIAL_OR_MISSING",
            "reason": "Requires explicit provider-backed profiling and null statistic semantics."
        },
        "F6_systematic_combination_correlation": {
            "status": "COMPLETE" if evidence["provider_explicit_systematic_correlation_rule"] and evidence["release_systematic_alternative_fits"] else "PARTIAL_OR_MISSING",
            "reason": "One-at-a-time alternative fits do not by themselves define a simultaneous combination/correlation contract."
        },
        "F7_numerical_anchors_reproduction_target": {
            "status": "COMPLETE" if not (evidence["release_has_3152"] and YAML_SHA256) else "PARTIAL_OR_MISSING",
            "reason": "Frozen provider discrepancy 3152±25 (release table) versus 3154±25 (exact YAML) has no allowed analyst-side precedence rule."
        },
    }
    all_complete = all(v["status"] == "COMPLETE" for v in fields.values())
    return {
        "benchmark": "NMIR-V2-0105A6I",
        "preregistration_commit": PREREG_COMMIT,
        "authority_byte_anchors": {"LArParametersAnlA.yaml": YAML_SHA256, "CENNS10AnlAEfficiency.txt": EFF_SHA256},
        "evidence": evidence,
        "fields": fields,
        "all_fields_complete": all_complete,
        "classification": "PASS_0105A6I_ARGON_POST_BYTE_RECOVERY_LIKELIHOOD_SEMANTICS_NONDISCOVERY" if all_complete else "BLOCKED_0105A6I_ARGON_LIKELIHOOD_IMPLEMENTATION_AUTHORITY_INCOMPLETE",
        "sm_null_reproduction_permission_percent": 100 if all_complete else 0,
        "observed_bsm_residual_permission_percent": 0,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", default="unknown")
    ns = ap.parse_args()
    out = {"benchmark": "NMIR-V2-0105A6I", "git_sha": ns.git_sha, "observed_bsm_residual_permission_percent": 0}
    try:
        mraw = fetch(MEASUREMENT_URL)
        rraw = fetch(RELEASE_URL)
        mtxt, rtxt = tex_text(mraw), tex_text(rraw)
        out.update(audit(mtxt, rtxt))
        out["git_sha"] = ns.git_sha
        out["provider_sources"] = {
            "measurement": {"url": MEASUREMENT_URL, "sha256": hashlib.sha256(mraw).hexdigest(), "bytes": len(mraw)},
            "release": {"url": RELEASE_URL, "sha256": hashlib.sha256(rraw).hexdigest(), "bytes": len(rraw)},
        }
    except Exception as exc:
        out.update({
            "classification": "BLOCKED_0105A6I_PROVIDER_SOURCE_TRANSPORT_OR_FORMAT",
            "error": f"{type(exc).__name__}: {exc}",
            "all_fields_complete": False,
            "sm_null_reproduction_permission_percent": 0,
        })
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
