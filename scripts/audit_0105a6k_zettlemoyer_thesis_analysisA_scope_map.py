#!/usr/bin/env python3
"""0105a6k deterministic page-scope mapper for the exact byte-locked thesis.

NONDICOVERY. Emits page numbers/scores only, never thesis page text.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path

PDF_URL = "https://scholarworks.iu.edu/dspace/bitstreams/a56e81c4-990a-4f54-b98d-6276a3c7c80a/download"
PDF_SHA256 = "6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9"
PDF_BYTES = 34641327
PREREG_COMMIT = "b0dfb320210ec10654de600819bcf9a6e1c3d4d6"

ANALYSIS_ANCHORS_RAW = [
    "analysis a", "cenns-10", "cenns10", "f90", "beam-related neutron", "beam related neutron",
]
STAT_ANCHORS_RAW = [
    "extended maximum likelihood", "maximum likelihood", "likelihood", "roofit", "profile likelihood", "gaussian constraint",
]
SYST_ANCHORS_RAW = [
    "systematic uncertainty", "systematic uncertainties", "quenching factor", "energy resolution", "acceptance efficiency",
]


def normalize(text: str) -> str:
    text = text.lower().replace("\u00ad", "")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalized_unique(items: list[str]) -> list[str]:
    return list(dict.fromkeys(normalize(x) for x in items))


ANALYSIS_ANCHORS = normalized_unique(ANALYSIS_ANCHORS_RAW)
STAT_ANCHORS = normalized_unique(STAT_ANCHORS_RAW)
SYST_ANCHORS = normalized_unique(SYST_ANCHORS_RAW)


def fetch(url: str, attempts: int = 4) -> bytes:
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-authority-audit/0105a6k"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception as exc:
            last = exc
            if i + 1 < attempts:
                time.sleep(2 ** i)
    raise RuntimeError(f"fetch failed: {type(last).__name__}: {last}")


def page_scores(pages: list[str]) -> list[dict]:
    out = []
    for idx, raw in enumerate(pages, start=1):
        t = normalize(raw)
        ah = [a for a in ANALYSIS_ANCHORS if a in t]
        sh = [a for a in STAT_ANCHORS if a in t]
        yh = [a for a in SYST_ANCHORS if a in t]
        A, S, Y = len(ah), len(sh), len(yh)
        out.append({
            "page": idx,
            "A": A,
            "S": S,
            "Y": Y,
            "core_hit": A >= 2 and S >= 1,
            "support_hit": (A >= 2 and Y >= 1) or (S >= 2 and Y >= 1),
        })
    return out


def select_scope(scores: list[dict]) -> dict:
    core = [x["page"] for x in scores if x["core_hit"]]
    support = [x["page"] for x in scores if x["support_hit"]]
    if not core:
        return {"core_pages": [], "support_pages": support, "clusters": [], "selected": None}

    clusters: list[list[int]] = [[core[0]]]
    for p in core[1:]:
        if p - clusters[-1][-1] <= 8:
            clusters[-1].append(p)
        else:
            clusters.append([p])

    by_page = {x["page"]: x for x in scores}
    ranked = []
    for c in clusters:
        lo, hi = c[0], c[-1]
        support_in_span = sum(1 for p in support if lo <= p <= hi)
        score_sum = sum(by_page[p]["A"] + by_page[p]["S"] + by_page[p]["Y"] for p in range(lo, hi + 1))
        width = hi - lo + 1
        rank_tuple = [len(c), support_in_span, score_sum, -width, -lo]
        ranked.append({
            "core_pages": c,
            "first_core": lo,
            "last_core": hi,
            "support_hits_in_core_span": support_in_span,
            "anchor_score_sum_in_core_span": score_sum,
            "core_span_width": width,
            "rank_tuple": rank_tuple,
        })
    ranked.sort(key=lambda x: tuple(x["rank_tuple"]), reverse=True)
    winner = ranked[0]
    n = len(scores)
    future_lo = max(1, winner["first_core"] - 3)
    future_hi = min(n, winner["last_core"] + 3)
    selected = dict(winner)
    selected.update({
        "future_interval_first_page": future_lo,
        "future_interval_last_page": future_hi,
        "future_interval_width": future_hi - future_lo + 1,
    })
    return {"core_pages": core, "support_pages": support, "clusters": ranked, "selected": selected}


def split_pdftotext(raw: str, n_pages: int) -> list[str]:
    pages = raw.split("\f")
    if pages and pages[-1] == "":
        pages = pages[:-1]
    if len(pages) != n_pages:
        raise ValueError(f"pdftotext page split mismatch: got {len(pages)}, expected {n_pages}")
    return pages


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", default="unknown")
    ns = ap.parse_args()
    out = {
        "benchmark": "NMIR-V2-0105A6K",
        "git_sha": ns.git_sha,
        "preregistration_commit": PREREG_COMMIT,
        "source_sha256_expected": PDF_SHA256,
        "source_bytes_expected": PDF_BYTES,
        "sm_null_reproduction_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
    }
    try:
        pdf = fetch(PDF_URL)
        got_sha = hashlib.sha256(pdf).hexdigest()
        got_bytes = len(pdf)
        out["source_sha256_observed"] = got_sha
        out["source_bytes_observed"] = got_bytes
        if got_sha != PDF_SHA256 or got_bytes != PDF_BYTES:
            out.update({
                "classification": "BLOCKED_0105A6K_THESIS_BYTE_IDENTITY_MISMATCH",
                "thesis_semantic_audit_permission_percent": 0,
            })
        else:
            with tempfile.TemporaryDirectory() as td:
                pdf_path = Path(td) / "thesis.pdf"
                txt_path = Path(td) / "thesis.txt"
                pdf_path.write_bytes(pdf)
                info = subprocess.run(["pdfinfo", str(pdf_path)], check=True, text=True, capture_output=True).stdout
                m = re.search(r"^Pages:\s+(\d+)\s*$", info, flags=re.M)
                if not m:
                    raise ValueError("pdfinfo did not report page count")
                n_pages = int(m.group(1))
                subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(pdf_path), str(txt_path)], check=True, capture_output=True)
                pages = split_pdftotext(txt_path.read_text(encoding="utf-8", errors="replace"), n_pages)
                scores = page_scores(pages)
                mapping = select_scope(scores)
                selected = mapping["selected"]
                pass_gate = (
                    n_pages >= 50
                    and len(mapping["core_pages"]) >= 2
                    and selected is not None
                    and len(selected["core_pages"]) >= 2
                    and selected["future_interval_width"] <= 30
                )
                out.update({
                    "pdf_pages": n_pages,
                    "anchor_vocabulary_normalized": {
                        "analysis": ANALYSIS_ANCHORS,
                        "statistical": STAT_ANCHORS,
                        "systematics": SYST_ANCHORS,
                    },
                    "page_scores": scores,
                    "scope_map": mapping,
                    "classification": (
                        "PASS_0105A6K_ZETTLEMOYER_ANALYSISA_SCOPE_MAP_NONDISCOVERY"
                        if pass_gate else
                        "BLOCKED_0105A6K_ANALYSISA_SCOPE_NOT_UNIQUELY_MAPPED"
                    ),
                    "thesis_semantic_audit_permission_percent": 100 if pass_gate else 0,
                    "authority_ceiling": {
                        "collaboration_release_authority": False,
                        "secondary_collaboration_author_source": True,
                    },
                })
    except Exception as exc:
        out.update({
            "classification": "BLOCKED_0105A6K_SOURCE_TRANSPORT_OR_PDF_EXTRACTION",
            "error": f"{type(exc).__name__}: {exc}",
            "thesis_semantic_audit_permission_percent": 0,
        })
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    # Deliberately do not print page text.
    print(json.dumps({k: v for k, v in out.items() if k != "page_scores"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
