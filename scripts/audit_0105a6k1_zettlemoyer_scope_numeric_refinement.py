#!/usr/bin/env python3
"""0105a6k1 numeric-only refinement of verified 0105a6k page-score evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

PARENT_JSON_SHA256 = "5d12e129e0fcdcea63ae7329e86310e7339162713d62ace7bffab01e5c37ad30"
THESIS_SHA256 = "6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9"
PARENT_CLASS = "BLOCKED_0105A6K_ANALYSISA_SCOPE_NOT_UNIQUELY_MAPPED"
PREREG_COMMIT = "83dd52043e91229fd41c73711cf802eda71fdc2a"
WINDOW = 24
PAD = 3


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def refine(parent: dict) -> dict:
    if parent.get("classification") != PARENT_CLASS:
        raise ValueError("unexpected parent classification")
    if parent.get("source_sha256_observed") != THESIS_SHA256:
        raise ValueError("unexpected thesis identity")
    scores = parent.get("page_scores")
    selected = (parent.get("scope_map") or {}).get("selected")
    if not isinstance(scores, list) or not isinstance(selected, dict):
        raise ValueError("parent numeric evidence incomplete")
    first = int(selected["first_core"])
    last = int(selected["last_core"])
    span = last - first + 1
    if not (span > 30 and span >= WINDOW):
        raise ValueError("parent span does not require frozen refinement")

    by_page = {int(r["page"]): r for r in scores}
    parent_core = [p for p in range(first, last + 1) if by_page[p].get("core_hit") is True]
    parent_support = [p for p in range(first, last + 1) if by_page[p].get("support_hit") is True]
    core_need = math.ceil(2 * len(parent_core) / 3)
    support_need = math.ceil(2 * len(parent_support) / 3)

    windows = []
    for start in range(first, last - WINDOW + 2):
        end = start + WINDOW - 1
        core = [p for p in parent_core if start <= p <= end]
        support = [p for p in parent_support if start <= p <= end]
        score_sum = sum(int(by_page[p]["A"]) + int(by_page[p]["S"]) + int(by_page[p]["Y"]) for p in range(start, end + 1))
        rank = [len(core), len(support), score_sum, -start]
        windows.append({
            "start": start,
            "end": end,
            "core_pages": core,
            "support_pages": support,
            "anchor_score_sum": score_sum,
            "rank_tuple": rank,
        })
    windows.sort(key=lambda x: tuple(x["rank_tuple"]), reverse=True)
    if not windows:
        raise ValueError("no candidate windows")
    winner = windows[0]
    future_first = max(1, winner["start"] - PAD)
    n_pages = int(parent["pdf_pages"])
    future_last = min(n_pages, winner["end"] + PAD)
    future_width = future_last - future_first + 1
    representative = len(winner["core_pages"]) >= core_need and len(winner["support_pages"]) >= support_need

    return {
        "parent_core_span": [first, last],
        "parent_core_hit_count": len(parent_core),
        "parent_support_hit_count": len(parent_support),
        "required_core_hits": core_need,
        "required_support_hits": support_need,
        "candidate_window_count": len(windows),
        "winning_core_window": winner,
        "future_semantic_interval": [future_first, future_last],
        "future_semantic_interval_width": future_width,
        "representativeness_pass": representative,
        "rank_tie_at_top": len(windows) > 1 and windows[0]["rank_tuple"] == windows[1]["rank_tuple"],
        "pass_gate": representative and future_width <= 30,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent-json", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", default="unknown")
    ns = ap.parse_args()
    p = Path(ns.parent_json)
    out = {
        "benchmark": "NMIR-V2-0105A6K1",
        "git_sha": ns.git_sha,
        "preregistration_commit": PREREG_COMMIT,
        "parent_result_sha256_expected": PARENT_JSON_SHA256,
        "sm_null_reproduction_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "pdf_or_thesis_text_accessed": False,
    }
    try:
        got = sha256_file(p)
        out["parent_result_sha256_observed"] = got
        if got != PARENT_JSON_SHA256:
            raise ValueError("parent result SHA256 mismatch")
        parent = json.loads(p.read_text(encoding="utf-8"))
        result = refine(parent)
        out.update(result)
        if result["pass_gate"]:
            out["classification"] = "PASS_0105A6K1_ZETTLEMOYER_SCOPE_NUMERIC_REFINEMENT_NONDISCOVERY"
            out["thesis_semantic_audit_permission_percent"] = 100
        else:
            out["classification"] = "BLOCKED_0105A6K1_SCOPE_REFINEMENT_NOT_REPRESENTATIVE_OR_NONUNIQUE"
            out["thesis_semantic_audit_permission_percent"] = 0
    except Exception as exc:
        out.update({
            "classification": "BLOCKED_0105A6K1_PARENT_EVIDENCE_TRANSPORT_OR_IDENTITY",
            "error": f"{type(exc).__name__}: {exc}",
            "thesis_semantic_audit_permission_percent": 0,
        })
    Path(ns.output).parent.mkdir(parents=True, exist_ok=True)
    Path(ns.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
