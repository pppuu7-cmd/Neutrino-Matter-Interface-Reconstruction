#!/usr/bin/env python3
"""0105a6q systematic-excursion semantics preflight.

No pseudo-data and no likelihood are evaluated.  The auditor verifies exact
parent artifacts, extracts only physical thesis PDF pages 154--158, records
bounded semantic windows, and measures structural properties of the eight
exact official excursion files.
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

import numpy as np

BENCHMARK = "NMIR-V2-0105A6Q"
PREREG_COMMIT = "5fe9c78d674d8eacf42d834d69ebb3ed19866e31"
THESIS_URL = "https://scholarworks.iu.edu/dspace/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/download"
THESIS_SIZE = 34641327
THESIS_SHA256 = "6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9"
A6P_MANIFEST_SHA256 = "5b1df47a50dd4dbb2a7fbd5ee64346c2854bdbad0540bfa6f16637eb10b6bada"
A6M_EVIDENCE_SHA256 = "672b8e5ec68e01395250e97fbafcbda956f8ffc51b52773d6379588b1fb87364"
PAGE_FIRST = 154
PAGE_LAST = 158
MAX_WINDOW = 700

CENTRAL = {
    "prompt_brn": "brnpdf.txt",
    "cevns": "cevnspdf.txt",
}
EXCURSIONS = {
    "brnpdf+1sigBRNTimingMean.txt": "prompt_brn",
    "brnpdf-1sigBRNTimingMean.txt": "prompt_brn",
    "brnpdf+1sigEnergy.txt": "prompt_brn",
    "brnpdf-1sigEnergy.txt": "prompt_brn",
    "brnpdfBRNTimingWidthSyst.txt": "prompt_brn",
    "cevnspdf+1sigF90.txt": "cevns",
    "cevnspdf-1sigF90.txt": "cevns",
    "cevnspdfCEvNSTimingMeanSyst.txt": "cevns",
}
PAIRING = {
    "brn_timing_mean": ["brnpdf+1sigBRNTimingMean.txt", "brnpdf-1sigBRNTimingMean.txt"],
    "brn_energy": ["brnpdf+1sigEnergy.txt", "brnpdf-1sigEnergy.txt"],
    "cevns_f90": ["cevnspdf+1sigF90.txt", "cevnspdf-1sigF90.txt"],
    "brn_timing_width": ["brnpdfBRNTimingWidthSyst.txt"],
    "cevns_timing_mean": ["cevnspdfCEvNSTimingMeanSyst.txt"],
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def bounded_window(text: str, terms: list[str]) -> str | None:
    positions = [text.find(term) for term in terms if text.find(term) >= 0]
    if not positions:
        return None
    center = min(positions)
    half = MAX_WINDOW // 2
    start = max(0, center - half)
    end = min(len(text), start + MAX_WINDOW)
    start = max(0, end - MAX_WINDOW)
    return text[start:end]


def extract_scoped_pages(pdf: Path) -> dict[int, str]:
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "scope.txt"
        subprocess.run(
            ["pdftotext", "-f", str(PAGE_FIRST), "-l", str(PAGE_LAST), "-layout", str(pdf), str(out)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
        raw = out.read_text(encoding="utf-8", errors="replace")
    chunks = raw.split("\f")
    if chunks and not chunks[-1].strip():
        chunks.pop()
    if len(chunks) != PAGE_LAST - PAGE_FIRST + 1:
        raise RuntimeError(f"expected 5 extracted pages, observed {len(chunks)}")
    return {PAGE_FIRST + i: normalize(chunk) for i, chunk in enumerate(chunks)}


def parse_template(path: Path):
    arr = np.loadtxt(path, dtype=float)
    if arr.shape != (960, 4):
        raise ValueError(f"{path.name}: expected 960x4, got {arr.shape}")
    return arr[:, :3], arr[:, 3]


def structural_metrics(files_dir: Path):
    central = {}
    for family, name in CENTRAL.items():
        coords, vals = parse_template(files_dir / name)
        central[family] = (coords, vals)
    result = {}
    for name, family in EXCURSIONS.items():
        coords, vals = parse_template(files_dir / name)
        ccoords, cvals = central[family]
        if not np.array_equal(coords, ccoords):
            raise ValueError(f"coordinate mismatch for {name}")
        raw_total = float(vals.sum())
        central_total = float(cvals.sum())
        if raw_total <= 0 or central_total <= 0:
            raise ValueError(f"nonpositive template total for {name}")
        unit = vals / raw_total
        cunit = cvals / central_total
        result[name] = {
            "component_family": family,
            "raw_total": raw_total,
            "central_total": central_total,
            "raw_total_ratio": raw_total / central_total,
            "raw_total_diff_events": raw_total - central_total,
            "raw_total_diff_gt_0p05": abs(raw_total - central_total) > 0.05,
            "unit_shape_l1_distance": float(np.abs(unit - cunit).sum()),
            "literal_sign_token": "+1sig" if "+1sig" in name else ("-1sig" if "-1sig" in name else "none"),
        }
    return result


def field_evidence(pages: dict[int, str]):
    joined = " ".join(pages.values())
    per_page = {}
    terms = {
        "Q1": ["10000 pseudo", "10 000 pseudo", "10,000 pseudo"],
        "Q2": ["generated using the excursion", "fit with the central value", "central value pdf"],
        "Q3": ["poisson", "extended", "number of events", "event count", "fluctuat", "fixed"],
        "Q4": ["average difference", "pair of excursion", "absolute", "half difference", "magnitude"],
        "Q5": ["timing width", "timing mean", "one sided", "one-sided"],
        "Q6": ["normalization", "renormal", "rate", "acceptance"],
        "Q7": ["uncorrelated systematic", "added in quadrature", "quadrature"],
        "Q8": ["159", "43", "14", "3.5"],
        "Q9": ["f90", "timing mean", "timing width", "energy"],
    }
    for page, text in pages.items():
        windows = {}
        for field, field_terms in terms.items():
            w = bounded_window(text, field_terms)
            if w:
                windows[field] = w
        per_page[str(page)] = {
            "text_sha256": sha256_bytes(text.encode("utf-8")),
            "windows": windows,
        }

    q1 = bool(re.search(r"(?:10000|10[ ,]000) pseudo(?: data)? sets?", joined))
    q2 = ("generated using the excursion" in joined and "fit with the central value" in joined)

    # Q3 is intentionally conservative. 'extended' likelihood alone is not a generation law.
    q3_poisson = bool(re.search(r"pseudo.{0,220}(?:poisson|poissonian)|(?:poisson|poissonian).{0,220}pseudo", joined))
    q3_fixed = bool(re.search(r"pseudo.{0,220}(?:fixed number|fixed event|fixed count)|(?:fixed number|fixed event|fixed count).{0,220}pseudo", joined))
    q3_explicit_other = bool(re.search(r"pseudo.{0,220}(?:multinomial|bootstrap|resampl)", joined))
    q3 = q3_poisson or q3_fixed or q3_explicit_other

    # Q4 requires an operation that uniquely resolves sign/absolute-value handling.
    q4 = bool(re.search(r"(?:absolute|magnitude|half[- ]?difference|divide.{0,40}two|mean absolute|average absolute).{0,260}(?:excursion|\+1|\-1)|(?:excursion|\+1|\-1).{0,260}(?:absolute|magnitude|half[- ]?difference|divide.{0,40}two|mean absolute|average absolute)", joined))

    # Q5 requires explicit one-sided treatment; source names alone are insufficient.
    q5 = bool(re.search(r"(?:one[- ]sided|single excursion|only one excursion|single alternative).{0,320}(?:timing|systematic)|(?:timing|systematic).{0,320}(?:one[- ]sided|single excursion|only one excursion|single alternative)", joined))

    # Q6 requires an explicit instruction about retaining or removing excursion rate changes.
    q6_keep = bool(re.search(r"(?:retain|preserve|include|use).{0,180}(?:excursion|alternative).{0,180}(?:normalization|rate|event total)", joined))
    q6_renorm = bool(re.search(r"(?:renormal|normalize).{0,180}(?:excursion|alternative).{0,180}(?:central|same total|normalization)", joined))
    q6 = q6_keep or q6_renorm

    q7 = ("uncorrelated systematic" in joined and ("quadrature" in joined or "added in quadrature" in joined))
    q8 = bool(re.search(r"159.{0,50}43.{0,50}14", joined))

    inventory_markers = {
        "brn_timing_mean": ("brn" in joined and "timing mean" in joined),
        "brn_energy": ("brn" in joined and "energy" in joined),
        "brn_timing_width": ("brn" in joined and "timing width" in joined),
        "cevns_f90": ("cevns" in joined and "f90" in joined),
        "cevns_timing_mean": ("cevns" in joined and "timing mean" in joined),
    }
    q9 = all(inventory_markers.values())

    statuses = {
        "Q1": "COMPLETE" if q1 else "MISSING_OR_PARTIAL",
        "Q2": "COMPLETE" if q2 else "MISSING_OR_PARTIAL",
        "Q3": "COMPLETE" if q3 else "MISSING_OR_PARTIAL",
        "Q4": "COMPLETE" if q4 else "MISSING_OR_PARTIAL",
        "Q5": "COMPLETE" if q5 else "MISSING_OR_PARTIAL",
        "Q6": "COMPLETE" if q6 else "MISSING_OR_PARTIAL",
        "Q7": "COMPLETE" if q7 else "MISSING_OR_PARTIAL",
        "Q8": "COMPLETE" if q8 else "MISSING_OR_PARTIAL",
        "Q9": "COMPLETE" if q9 else "MISSING_OR_PARTIAL",
    }
    details = {
        "Q3_generation_law_markers": {"poisson": q3_poisson, "fixed": q3_fixed, "other": q3_explicit_other},
        "Q6_normalization_rule_markers": {"keep_raw_rate": q6_keep, "renormalize": q6_renorm},
        "Q9_inventory_markers": inventory_markers,
    }
    return statuses, details, per_page


def download_thesis(path: Path):
    req = urllib.request.Request(THESIS_URL, headers={"User-Agent": "NMIR-0105a6q-authority-audit/1.0"})
    with urllib.request.urlopen(req, timeout=120) as response:
        data = response.read()
    if len(data) != THESIS_SIZE or sha256_bytes(data) != THESIS_SHA256:
        raise RuntimeError("institutional thesis byte identity mismatch")
    path.write_bytes(data)


def run(files_dir: Path, a6p_manifest: Path, a6m_evidence: Path, thesis_path: Path):
    if sha256_file(a6p_manifest) != A6P_MANIFEST_SHA256:
        raise ValueError("0105a6p manifest SHA mismatch")
    if sha256_file(a6m_evidence) != A6M_EVIDENCE_SHA256:
        raise ValueError("0105a6m evidence SHA mismatch")
    a6p = json.loads(a6p_manifest.read_text(encoding="utf-8"))
    a6m = json.loads(a6m_evidence.read_text(encoding="utf-8"))
    if not a6p.get("systematics_ready") or a6p.get("accepted_count") != 14:
        raise ValueError("0105a6p systematic bytes not ready")
    if a6m.get("classification") != "PASS_0105A6M_BOUNDED_SECONDARY_EVIDENCE_EXTRACTION_NONDISCOVERY":
        # The extraction artifact's classification is distinct from later manual adjudication.
        raise ValueError("unexpected 0105a6m bounded evidence extraction classification")

    for item in a6p["files"]:
        expected = item["official_expected"]["sha256"]
        p = files_dir / item["filename"]
        if not p.exists() or sha256_file(p) != expected:
            raise ValueError(f"exact official byte mismatch for {item['filename']}")

    if not thesis_path.exists():
        download_thesis(thesis_path)
    if thesis_path.stat().st_size != THESIS_SIZE or sha256_file(thesis_path) != THESIS_SHA256:
        raise ValueError("thesis identity mismatch before scoped extraction")

    pages = extract_scoped_pages(thesis_path)
    statuses, details, page_receipts = field_evidence(pages)
    structural = structural_metrics(files_dir)
    all_complete = all(v == "COMPLETE" for v in statuses.values())
    critical_missing = [q for q in ("Q3", "Q4", "Q5", "Q6", "Q9") if statuses[q] != "COMPLETE"]
    classification = (
        "PASS_0105A6Q_SYSTEMATIC_EXCURSION_SEMANTICS_PREFLIGHT_NONDISCOVERY"
        if all_complete
        else "BLOCKED_0105A6Q_SYSTEMATIC_EXCURSION_SEMANTICS_INCOMPLETE"
    )
    return {
        "benchmark": BENCHMARK,
        "preregistration_commit": PREREG_COMMIT,
        "source_identity": {"thesis_size": THESIS_SIZE, "thesis_sha256": THESIS_SHA256, "physical_pages": [PAGE_FIRST, PAGE_LAST]},
        "parent_artifacts": {"a6p_manifest_sha256": A6P_MANIFEST_SHA256, "a6m_evidence_sha256": A6M_EVIDENCE_SHA256},
        "field_status": statuses,
        "field_details": details,
        "critical_unresolved_fields": critical_missing,
        "page_receipts": page_receipts,
        "excursion_structural_metrics": structural,
        "literal_release_pairing_from_filenames": PAIRING,
        "classification": classification,
        "pseudo_data_generated": False,
        "likelihood_evaluated": False,
        "visual_pdf_verification_performed": False,
        "tierA_exact_collaboration_internal_likelihood": "BLOCKED",
        "observed_bsm_residual_permission_percent": 0,
        "observed_bsm_residual_inspected": False,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--files-dir", required=True)
    ap.add_argument("--a6p-manifest", required=True)
    ap.add_argument("--a6m-evidence", required=True)
    ap.add_argument("--thesis", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()
    try:
        result = run(Path(args.files_dir), Path(args.a6p_manifest), Path(args.a6m_evidence), Path(args.thesis))
        result["git_sha"] = args.git_sha
    except Exception as exc:
        result = {
            "benchmark": BENCHMARK,
            "preregistration_commit": PREREG_COMMIT,
            "git_sha": args.git_sha,
            "classification": "BLOCKED_0105A6Q_SOURCE_TRANSPORT_OR_EXTRACTION",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "pseudo_data_generated": False,
            "likelihood_evaluated": False,
            "visual_pdf_verification_performed": False,
            "tierA_exact_collaboration_internal_likelihood": "BLOCKED",
            "observed_bsm_residual_permission_percent": 0,
            "observed_bsm_residual_inspected": False,
        }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
