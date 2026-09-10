#!/usr/bin/env python3
"""0105a6l: machine-text semantic-evidence preflight for frozen thesis pages 129-158.

NONDICOVERY / NO FIT. This gate verifies the exact institutional PDF and records
only page-level hashes and boolean/token evidence. It never emits page text.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
import urllib.request
from pathlib import Path

BENCHMARK = "NMIR-V2-0105A6L"
PREREG_COMMIT = "24c0ea26f5c861f5a2c5fe41609dd631af4370c2"
PDF_URL = "https://scholarworks.iu.edu/iuswrrest/api/core/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/content"
EXPECTED_SHA256 = "6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9"
EXPECTED_BYTES = 34641327
FIRST_PAGE = 129
LAST_PAGE = 158

L0_IMPL = ("likelihood", "roofit", "fit", "systematic", "background")
F1_CONSTRUCTION = (
    "poisson",
    "unbinned",
    "binned likelihood",
    "extended likelihood",
    "extended maximum likelihood",
    "product of probabilities",
    "probability density function",
)
F3_NUISANCE = ("nuisance", "gaussian constraint", "constraint", "prior", "float", "profile")
F3_COMPONENTS = (
    "cevns",
    "steady state",
    "beam related neutron",
    "prompt",
    "delayed",
    "quenching factor",
    "energy resolution",
    "acceptance efficiency",
)
F4_TEMPLATE = ("template", "pdf", "systematic")
F4_COUPLING = (
    "interpolat",
    "morph",
    "vertical morph",
    "horizontal morph",
    "template variation",
    "shape variation",
    "vary the shape",
    "varied shape",
)
F6_COMBINATION = (
    "simultaneous",
    "correlat",
    "covariance",
    "combined",
    "quadrature",
    "independent nuisance",
    "one at a time",
    "alternative fit",
)
F7_CONTEXT = ("steady state", "background", "prediction", "normalization", "table", "analysis a", "fit")
F7_PRECEDENCE = (
    "typo",
    "erratum",
    "corrected",
    "should be",
    "instead of",
    "supersede",
    "use 3152",
    "use 3154",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def contains_marker(norm: str, marker: str) -> bool:
    """Substring semantics are deliberate for frozen stems such as interpolat/correlat."""
    return marker in norm


def exact_decimal_token(norm: str, token: str) -> bool:
    return re.search(rf"(?<!\d){re.escape(token)}(?!\d)", norm) is not None


def classify_page(norm: str) -> dict:
    l0_hits = [m for m in L0_IMPL if contains_marker(norm, m)]
    l0 = contains_marker(norm, "analysis a") and bool(l0_hits)

    f1_hits = [m for m in F1_CONSTRUCTION if contains_marker(norm, m)]
    f1 = contains_marker(norm, "likelihood") and bool(f1_hits)

    nuisance_hits = [m for m in F3_NUISANCE if contains_marker(norm, m)]
    component_hits = [m for m in F3_COMPONENTS if contains_marker(norm, m)]
    f3 = bool(nuisance_hits) and len(component_hits) >= 2

    template_hits = [m for m in F4_TEMPLATE if contains_marker(norm, m)]
    coupling_hits = [m for m in F4_COUPLING if contains_marker(norm, m)]
    f4 = bool(template_hits) and bool(coupling_hits)

    combination_hits = [m for m in F6_COMBINATION if contains_marker(norm, m)]
    f6 = contains_marker(norm, "systematic") and bool(combination_hits)

    has_3152 = exact_decimal_token(norm, "3152")
    has_3154 = exact_decimal_token(norm, "3154")
    f7_context_hits = [m for m in F7_CONTEXT if contains_marker(norm, m)] if (has_3152 or has_3154) else []
    precedence_hits = [m for m in F7_PRECEDENCE if contains_marker(norm, m)] if (has_3152 or has_3154) else []
    f7_resolution = (has_3152 or has_3154) and bool(precedence_hits)

    return {
        "L0": {"candidate": l0, "implementation_markers": l0_hits},
        "F1": {"candidate": f1, "construction_markers": f1_hits},
        "F3": {"candidate": f3, "nuisance_markers": nuisance_hits, "component_markers": component_hits},
        "F4": {"candidate": f4, "template_markers": template_hits, "coupling_markers": coupling_hits},
        "F6": {"candidate": f6, "combination_markers": combination_hits},
        "F7": {
            "candidate_discrepancy_resolution": f7_resolution,
            "has_3152": has_3152,
            "has_3154": has_3154,
            "context_markers": f7_context_hits,
            "precedence_markers": precedence_hits,
        },
    }


def extract_page(pdf_path: Path, page: int) -> str:
    proc = subprocess.run(
        ["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(pdf_path), "-"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.stdout.decode("utf-8", errors="replace")


def audit(pdf_bytes: bytes, git_sha: str) -> dict:
    observed_sha = sha256_bytes(pdf_bytes)
    identity_ok = len(pdf_bytes) == EXPECTED_BYTES and observed_sha == EXPECTED_SHA256
    if not identity_ok:
        return {
            "benchmark": BENCHMARK,
            "classification": "BLOCKED_0105A6L_SOURCE_TRANSPORT_OR_SCOPE_EXTRACTION",
            "git_sha": git_sha,
            "preregistration_commit": PREREG_COMMIT,
            "source_identity": {
                "expected_bytes": EXPECTED_BYTES,
                "observed_bytes": len(pdf_bytes),
                "expected_sha256": EXPECTED_SHA256,
                "observed_sha256": observed_sha,
                "verified": False,
            },
            "terminal_semantic_authority_pass": False,
            "sm_null_reproduction_permission_percent": 0,
            "observed_bsm_residual_permission_percent": 0,
        }

    page_records = []
    family_pages = {k: [] for k in ("L0", "F1", "F3", "F4", "F6", "F7")}
    with tempfile.TemporaryDirectory() as td:
        pdf_path = Path(td) / "thesis.pdf"
        pdf_path.write_bytes(pdf_bytes)
        try:
            for page in range(FIRST_PAGE, LAST_PAGE + 1):
                raw = extract_page(pdf_path, page)
                norm = normalize(raw)
                evidence = classify_page(norm)
                page_records.append({
                    "physical_pdf_page": page,
                    "normalized_text_sha256": sha256_bytes(norm.encode("utf-8")),
                    "normalized_character_count": len(norm),
                    "evidence": evidence,
                })
                for fam in ("L0", "F1", "F3", "F4", "F6"):
                    if evidence[fam]["candidate"]:
                        family_pages[fam].append(page)
                if evidence["F7"]["candidate_discrepancy_resolution"]:
                    family_pages["F7"].append(page)
        except (subprocess.CalledProcessError, OSError, UnicodeError) as exc:
            return {
                "benchmark": BENCHMARK,
                "classification": "BLOCKED_0105A6L_SOURCE_TRANSPORT_OR_SCOPE_EXTRACTION",
                "git_sha": git_sha,
                "preregistration_commit": PREREG_COMMIT,
                "source_identity": {
                    "expected_bytes": EXPECTED_BYTES,
                    "observed_bytes": len(pdf_bytes),
                    "expected_sha256": EXPECTED_SHA256,
                    "observed_sha256": observed_sha,
                    "verified": True,
                },
                "scope_extraction_error_type": type(exc).__name__,
                "terminal_semantic_authority_pass": False,
                "sm_null_reproduction_permission_percent": 0,
                "observed_bsm_residual_permission_percent": 0,
            }

    l0_exists = bool(family_pages["L0"])
    any_field = any(family_pages[f] for f in ("F1", "F3", "F4", "F6", "F7"))
    passed = l0_exists and any_field
    classification = (
        "PASS_0105A6L_MACHINE_TEXT_EVIDENCE_PREFLIGHT_NONDISCOVERY"
        if passed
        else "BLOCKED_0105A6L_NO_SCOPED_IMPLEMENTATION_EVIDENCE"
    )

    f7_number_pages = {
        "3152": [r["physical_pdf_page"] for r in page_records if r["evidence"]["F7"]["has_3152"]],
        "3154": [r["physical_pdf_page"] for r in page_records if r["evidence"]["F7"]["has_3154"]],
    }

    return {
        "benchmark": BENCHMARK,
        "classification": classification,
        "git_sha": git_sha,
        "preregistration_commit": PREREG_COMMIT,
        "source_identity": {
            "url": PDF_URL,
            "expected_bytes": EXPECTED_BYTES,
            "observed_bytes": len(pdf_bytes),
            "expected_sha256": EXPECTED_SHA256,
            "observed_sha256": observed_sha,
            "verified": True,
        },
        "scope": {
            "first_physical_pdf_page": FIRST_PAGE,
            "last_physical_pdf_page": LAST_PAGE,
            "page_count": LAST_PAGE - FIRST_PAGE + 1,
            "outside_scope_pages_accessed": False,
        },
        "candidate_evidence_pages": family_pages,
        "f7_exact_number_pages": f7_number_pages,
        "pages": page_records,
        "authority_ceiling": {
            "collaboration_release_authority": False,
            "secondary_collaboration_author_source": True,
            "terminal_semantic_authority_pass": False,
        },
        "thesis_evidence_verification_gate_permission_percent": 100 if passed else 0,
        "sm_null_reproduction_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "full_page_text_emitted": False,
        "likelihood_numerical_evaluation_performed": False,
    }


def fetch_pdf() -> bytes:
    req = urllib.request.Request(PDF_URL, headers={"User-Agent": "NMIR-authority-audit/0105a6l"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return resp.read()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()
    try:
        pdf_bytes = fetch_pdf()
        result = audit(pdf_bytes, args.git_sha)
    except Exception as exc:  # transport failure must be classified, not crash away evidence
        result = {
            "benchmark": BENCHMARK,
            "classification": "BLOCKED_0105A6L_SOURCE_TRANSPORT_OR_SCOPE_EXTRACTION",
            "git_sha": args.git_sha,
            "preregistration_commit": PREREG_COMMIT,
            "transport_error_type": type(exc).__name__,
            "terminal_semantic_authority_pass": False,
            "sm_null_reproduction_permission_percent": 0,
            "observed_bsm_residual_permission_percent": 0,
        }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
