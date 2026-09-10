#!/usr/bin/env python3
"""0105a6q1: bounded authority audit for the central pseudo-data count law.

Reads only physical pages 152--153 of the exact institutional dissertation.
No pseudo-data, likelihood, or residual is evaluated.
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

BENCHMARK = "NMIR-V2-0105A6Q1"
PREREG_COMMIT = "268d7acb9d42e70fc6fe1fbf5d299df3ce1d8f64"
PARENT_Q_RESULT_SHA256 = "a996df0b6f9d12f03d1fc57cc3d69f13d1b941e3771eb99be9877510d34e6884"
PARENT_Q_CLASSIFICATION = "BLOCKED_0105A6Q_SYSTEMATIC_EXCURSION_SEMANTICS_INCOMPLETE"
THESIS_URL = "https://scholarworks.iu.edu/dspace/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/download"
THESIS_SIZE = 34641327
THESIS_SHA256 = "6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9"
PAGE_FIRST = 152
PAGE_LAST = 153
MAX_WINDOW = 900


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def download_thesis(path: Path) -> None:
    req = urllib.request.Request(THESIS_URL, headers={"User-Agent": "NMIR-0105a6q1/1.0"})
    with urllib.request.urlopen(req, timeout=120) as response:
        data = response.read()
    if len(data) != THESIS_SIZE or sha256_bytes(data) != THESIS_SHA256:
        raise RuntimeError("institutional thesis byte identity mismatch")
    path.write_bytes(data)


def extract_pages(pdf: Path) -> dict[int, str]:
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
    if len(chunks) != 2:
        raise RuntimeError(f"expected exactly 2 scoped pages, observed {len(chunks)}")
    return {PAGE_FIRST + i: normalize(chunk) for i, chunk in enumerate(chunks)}


def bounded_window(text: str) -> str | None:
    terms = [
        "pseudo data", "pseudo-data", "poisson", "fixed number", "fixed event",
        "fixed count", "multinomial", "bootstrap", "resampl", "generated",
        "number of events", "event count",
    ]
    positions = [text.find(term) for term in terms if text.find(term) >= 0]
    if not positions:
        return None
    center = min(positions)
    start = max(0, center - MAX_WINDOW // 2)
    end = min(len(text), start + MAX_WINDOW)
    start = max(0, end - MAX_WINDOW)
    return text[start:end]


def classify_count_law(pages: dict[int, str]):
    joined = " ".join(pages[p] for p in sorted(pages))

    pseudo_near_poisson = bool(re.search(
        r"(?:pseudo(?:[- ]data)?|event(?:s| count)?|number of events).{0,260}(?:poisson|poissonian)"
        r"|(?:poisson|poissonian).{0,260}(?:pseudo(?:[- ]data)?|event(?:s| count)?|number of events)",
        joined,
    ))
    explicit_poisson_total = bool(re.search(
        r"(?:total|number).{0,120}(?:events|count).{0,160}(?:poisson|poissonian)"
        r"|(?:poisson|poissonian).{0,160}(?:total|number).{0,120}(?:events|count)",
        joined,
    ))
    extended_plus_poisson = bool(re.search(
        r"extended.{0,220}(?:poisson|poissonian).{0,220}(?:event|count|pseudo)"
        r"|(?:poisson|poissonian).{0,220}extended.{0,220}(?:event|count|pseudo)",
        joined,
    ))
    q3_p = pseudo_near_poisson or explicit_poisson_total or extended_plus_poisson

    fixed_total = bool(re.search(
        r"(?:pseudo(?:[- ]data)?|event|count).{0,260}(?:fixed number|fixed total|fixed event count|number of events is fixed)"
        r"|(?:fixed number|fixed total|fixed event count|number of events is fixed).{0,260}(?:pseudo(?:[- ]data)?|event|count)",
        joined,
    ))
    multinomial = bool(re.search(
        r"multinomial.{0,220}(?:pseudo|event|count)|(?:pseudo|event|count).{0,220}multinomial",
        joined,
    ))
    q3_f = fixed_total or multinomial

    other = bool(re.search(
        r"(?:bootstrap|resampl(?:e|ed|ing)?).{0,220}(?:pseudo|event|count)"
        r"|(?:pseudo|event|count).{0,220}(?:bootstrap|resampl(?:e|ed|ing)?)",
        joined,
    ))
    q3_o = other

    categories = []
    if q3_p:
        categories.append("Q3-P")
    if q3_f:
        categories.append("Q3-F")
    if q3_o:
        categories.append("Q3-O")

    if len(categories) == 0:
        detected = "NONE"
        classification = "BLOCKED_0105A6Q1_PSEUDODATA_COUNT_LAW_NOT_EXPLICIT"
    elif len(categories) > 1:
        detected = "CONFLICT"
        classification = "BLOCKED_0105A6Q1_CONFLICTING_PSEUDODATA_COUNT_LAW_AUTHORITY"
    else:
        detected = categories[0]
        classification = "PASS_0105A6Q1_EXPLICIT_PSEUDODATA_COUNT_LAW_SECONDARY_AUTHORITY_NONDISCOVERY"

    details = {
        "poisson_markers": {
            "pseudo_near_poisson": pseudo_near_poisson,
            "explicit_poisson_total": explicit_poisson_total,
            "extended_plus_poisson": extended_plus_poisson,
        },
        "fixed_total_markers": {"fixed_total": fixed_total, "multinomial": multinomial},
        "other_law_markers": {"bootstrap_or_resampling": other},
    }
    return detected, classification, details


def run(parent_q_result: Path, thesis: Path):
    if sha256_file(parent_q_result) != PARENT_Q_RESULT_SHA256:
        raise ValueError("0105a6q parent result SHA mismatch")
    parent = json.loads(parent_q_result.read_text(encoding="utf-8"))
    if parent.get("classification") != PARENT_Q_CLASSIFICATION:
        raise ValueError("unexpected 0105a6q parent classification")
    if parent.get("critical_unresolved_fields") != ["Q3"]:
        raise ValueError("0105a6q does not isolate Q3 as the sole critical unresolved field")
    if parent.get("pseudo_data_generated") is not False or parent.get("likelihood_evaluated") is not False:
        raise ValueError("0105a6q parent violated nondiscovery execution ceiling")

    if not thesis.exists():
        download_thesis(thesis)
    if thesis.stat().st_size != THESIS_SIZE or sha256_file(thesis) != THESIS_SHA256:
        raise ValueError("thesis identity mismatch before scoped extraction")

    pages = extract_pages(thesis)
    detected, classification, details = classify_count_law(pages)
    receipts = {}
    for page, text in pages.items():
        receipts[str(page)] = {
            "normalized_text_sha256": sha256_bytes(text.encode("utf-8")),
            "bounded_window": bounded_window(text),
        }

    pass_gate = classification.startswith("PASS_")
    return {
        "benchmark": BENCHMARK,
        "preregistration_commit": PREREG_COMMIT,
        "parent_q_result_sha256": PARENT_Q_RESULT_SHA256,
        "source_identity": {
            "thesis_size": THESIS_SIZE,
            "thesis_sha256": THESIS_SHA256,
            "physical_pages": [PAGE_FIRST, PAGE_LAST],
        },
        "detected_count_law_category": detected,
        "count_law_markers": details,
        "page_receipts": receipts,
        "full_page_text_retained": False,
        "outside_allowed_pages_accessed": False,
        "classification": classification,
        "systematic_monte_carlo_preregistration_permission_percent": 100 if pass_gate else 0,
        "systematic_monte_carlo_execution_permission_percent": 0,
        "pseudo_data_generated": False,
        "likelihood_evaluated": False,
        "tierA_exact_collaboration_internal_likelihood": "BLOCKED",
        "observed_bsm_residual_permission_percent": 0,
        "observed_bsm_residual_inspected": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent-q-result", required=True)
    parser.add_argument("--thesis", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--git-sha", required=True)
    args = parser.parse_args()
    try:
        result = run(Path(args.parent_q_result), Path(args.thesis))
        result["git_sha"] = args.git_sha
    except Exception as exc:
        result = {
            "benchmark": BENCHMARK,
            "preregistration_commit": PREREG_COMMIT,
            "git_sha": args.git_sha,
            "classification": "BLOCKED_0105A6Q1_SOURCE_TRANSPORT_OR_SCOPE_EXTRACTION",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "systematic_monte_carlo_preregistration_permission_percent": 0,
            "systematic_monte_carlo_execution_permission_percent": 0,
            "pseudo_data_generated": False,
            "likelihood_evaluated": False,
            "tierA_exact_collaboration_internal_likelihood": "BLOCKED",
            "observed_bsm_residual_permission_percent": 0,
            "observed_bsm_residual_inspected": False,
        }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
