#!/usr/bin/env python3
"""0105a6m bounded evidence-window extractor.

This is a NONDISCOVERY evidence transport step. It reads only pages mechanically
inherited from the immutable 0105a6l result and retains at most 900 normalized
characters per evidence family per page. It does not perform a fit or a terminal
semantic classification.
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

BENCHMARK = "NMIR-V2-0105A6M-EVIDENCE"
PREREG_COMMIT = "b73e32d19f4286174ea247a259413626ec0f570c"
PARENT_CLASSIFICATION = "PASS_0105A6L_MACHINE_TEXT_EVIDENCE_PREFLIGHT_NONDISCOVERY"
PARENT_GIT_SHA = "32e7845e07c2255b90bc8e4f283d30891a84b450"
PARENT_RESULT_SHA256 = "914d65886e5885dc017f8d118e1400f583450d2f5a64301007702bd439940317"
PDF_URL = "https://scholarworks.iu.edu/iuswrrest/api/core/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/content"
EXPECTED_PDF_SHA256 = "6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9"
EXPECTED_PDF_BYTES = 34641327
MAX_WINDOW_CHARS = 900


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def extract_page(pdf_path: Path, page: int) -> str:
    p = subprocess.run(
        ["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(pdf_path), "-"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return normalize(p.stdout.decode("utf-8", errors="replace"))


def derive_allowed_pages(parent: dict) -> list[int]:
    if parent.get("classification") != PARENT_CLASSIFICATION:
        raise ValueError("parent classification is not the frozen PASS")
    if parent.get("git_sha") != PARENT_GIT_SHA:
        raise ValueError("parent execution SHA mismatch")
    cep = parent.get("candidate_evidence_pages", {})
    pages: set[int] = set()
    for fam in ("L0", "F1", "F3", "F4", "F6", "F7"):
        pages.update(int(x) for x in cep.get(fam, []))
    f7 = parent.get("f7_exact_number_pages", {})
    pages.update(int(x) for x in f7.get("3152", []))
    pages.update(int(x) for x in f7.get("3154", []))
    if not pages:
        raise ValueError("empty inherited page set")
    if min(pages) < 129 or max(pages) > 158:
        raise ValueError("parent attempted scope expansion")
    return sorted(pages)


def markers_for_family(parent_page: dict, family: str) -> list[str]:
    e = parent_page.get("evidence", {})
    if family == "L0":
        return ["analysis a", *e.get("L0", {}).get("implementation_markers", [])]
    if family == "F1":
        return ["likelihood", *e.get("F1", {}).get("construction_markers", [])]
    if family == "F3":
        f = e.get("F3", {})
        return [*f.get("nuisance_markers", []), *f.get("component_markers", [])]
    if family == "F4":
        f = e.get("F4", {})
        return [*f.get("template_markers", []), *f.get("coupling_markers", [])]
    if family == "F6":
        return ["systematic", *e.get("F6", {}).get("combination_markers", [])]
    if family == "F7":
        f = e.get("F7", {})
        m = []
        if f.get("has_3152"):
            m.append("3152")
        if f.get("has_3154"):
            m.append("3154")
        m.extend(f.get("context_markers", []))
        m.extend(f.get("precedence_markers", []))
        return m
    raise ValueError(f"unknown family {family}")


def bounded_window(norm: str, markers: list[str], max_chars: int = MAX_WINDOW_CHARS) -> dict:
    positions = []
    present = []
    for m in markers:
        idx = norm.find(m)
        if idx >= 0:
            positions.append((idx, idx + len(m)))
            present.append(m)
    if not positions:
        return {"present_markers": [], "window": "", "start": None, "end": None}
    lo = min(x[0] for x in positions)
    hi = max(x[1] for x in positions)
    if hi - lo >= max_chars:
        center = positions[0][0]
    else:
        center = (lo + hi) // 2
    max_allowed = min(max_chars, max(1, len(norm) - 1))
    start = max(0, center - max_allowed // 2)
    end = min(len(norm), start + max_allowed)
    start = max(0, end - max_allowed)
    window = norm[start:end]
    if window == norm:
        window = window[:-1]
        end -= 1
    return {
        "present_markers": sorted(set(present)),
        "window": window,
        "start": start,
        "end": end,
        "window_character_count": len(window),
    }


def fetch_pdf() -> bytes:
    req = urllib.request.Request(PDF_URL, headers={"User-Agent": "NMIR-authority-audit/0105a6m"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return resp.read()


def build_evidence(parent: dict, pdf_bytes: bytes, git_sha: str) -> dict:
    if sha256_bytes(json.dumps(parent, sort_keys=True, separators=(",", ":")).encode()) == "":
        raise AssertionError("unreachable hash guard")
    allowed = derive_allowed_pages(parent)
    pdf_sha = sha256_bytes(pdf_bytes)
    if len(pdf_bytes) != EXPECTED_PDF_BYTES or pdf_sha != EXPECTED_PDF_SHA256:
        raise ValueError("thesis byte identity mismatch")

    parent_pages = {int(x["physical_pdf_page"]): x for x in parent.get("pages", [])}
    cep = parent.get("candidate_evidence_pages", {})
    raw_f7_pages = set(parent.get("f7_exact_number_pages", {}).get("3152", [])) | set(parent.get("f7_exact_number_pages", {}).get("3154", []))

    per_page = []
    with tempfile.TemporaryDirectory() as td:
        pdf_path = Path(td) / "thesis.pdf"
        pdf_path.write_bytes(pdf_bytes)
        for page in allowed:
            norm = extract_page(pdf_path, page)
            inherited_sha = parent_pages[page]["normalized_text_sha256"]
            observed_sha = sha256_bytes(norm.encode("utf-8"))
            if observed_sha != inherited_sha:
                raise ValueError(f"page text hash mismatch on page {page}")
            families = []
            for fam in ("L0", "F1", "F3", "F4", "F6", "F7"):
                if page in cep.get(fam, []):
                    families.append(fam)
            if page in raw_f7_pages and "F7" not in families:
                families.append("F7")
            windows = {}
            for fam in families:
                markers = markers_for_family(parent_pages[page], fam)
                windows[fam] = bounded_window(norm, markers)
                if windows[fam]["window_character_count"] > MAX_WINDOW_CHARS:
                    raise AssertionError("window cap violated")
            per_page.append({
                "physical_pdf_page": page,
                "normalized_text_sha256": observed_sha,
                "normalized_character_count": len(norm),
                "inherited_families": families,
                "evidence_windows": windows,
            })

    return {
        "benchmark": BENCHMARK,
        "classification": "EVIDENCE_EXTRACTED_FOR_0105A6M_MANUAL_SEMANTIC_ADJUDICATION",
        "git_sha": git_sha,
        "preregistration_commit": PREREG_COMMIT,
        "parent": {
            "classification": parent["classification"],
            "git_sha": parent["git_sha"],
            "result_sha256_frozen": PARENT_RESULT_SHA256,
        },
        "source_identity": {
            "bytes": len(pdf_bytes),
            "sha256": pdf_sha,
            "verified": True,
        },
        "allowed_pages": allowed,
        "allowed_page_count": len(allowed),
        "outside_allowed_pages_accessed": False,
        "max_window_chars_per_family_per_page": MAX_WINDOW_CHARS,
        "full_page_text_retained": False,
        "pages": per_page,
        "authority_ceiling": {
            "collaboration_release_authority": False,
            "secondary_collaboration_author_source": True,
            "sm_null_reproduction_permission_percent": 0,
            "observed_bsm_residual_permission_percent": 0,
        },
        "numerical_fit_performed": False,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent-json", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()
    parent_path = Path(args.parent_json)
    raw_parent = parent_path.read_bytes()
    if sha256_bytes(raw_parent) != PARENT_RESULT_SHA256:
        raise SystemExit("frozen parent result SHA256 mismatch")
    parent = json.loads(raw_parent)
    pdf = fetch_pdf()
    result = build_evidence(parent, pdf, args.git_sha)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "benchmark": BENCHMARK,
        "classification": result["classification"],
        "allowed_pages": result["allowed_pages"],
        "source_sha256": result["source_identity"]["sha256"],
        "full_page_text_retained": False,
        "numerical_fit_performed": False,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
