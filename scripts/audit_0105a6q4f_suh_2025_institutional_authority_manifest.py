#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

BENCHMARK = "NMIR-V2-0105A6Q4F"
PREREG_COMMIT = "309aa7d389b541fb6818a56aec67f44cee65f50d"
CEEM_URL = "https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html"
TITLE = "TOWARDS AN IMPROVED MEASUREMENT OF THE CEVNS PROCESS WITH THE CENNS-10 LAR DETECTOR"
AUTHOR_TOKENS = ("benjamin", "suh")
YEAR = "2025"
SEARCH_URL = "https://scholarworks.iu.edu/dspace/discover?query=" + urllib.parse.quote('"' + TITLE + '"')
UA = "NMIR-0105a6q4f-institutional-manifest/1.0"


def h256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def norm(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<script\b.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("–", "-").replace("—", "-")
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


def fetch(url: str) -> tuple[bytes, str, int]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read(), r.geturl(), int(getattr(r, "status", r.getcode()))


def official_iu(url: str) -> bool:
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    return host.endswith(".iu.edu") or host == "iu.edu" or host.endswith(".indiana.edu") or host == "indiana.edu"


def exact_title_present(text: str) -> bool:
    return norm(TITLE) in norm(text)


def author_present(text: str) -> bool:
    n = norm(text)
    return all(tok in n for tok in AUTHOR_TOKENS)


def discover_item_urls(search_html: str, base: str) -> list[str]:
    hrefs = re.findall(r'''href=["']([^"']+)["']''', search_html, flags=re.I)
    out = []
    for href in hrefs:
        u = urllib.parse.urljoin(base, html.unescape(href))
        if not official_iu(u):
            continue
        if re.search(r"/dspace/items/[0-9a-fA-F-]{20,}", urllib.parse.urlparse(u).path):
            u = u.split("?", 1)[0].split("#", 1)[0]
            if u not in out:
                out.append(u)
    return out


def classify() -> dict:
    ceem_raw, ceem_final, ceem_status = fetch(CEEM_URL)
    ceem_text = ceem_raw.decode("utf-8", errors="replace")
    ceem_ok = (
        ceem_status == 200
        and ceem_final == CEEM_URL
        and exact_title_present(ceem_text)
        and author_present(ceem_text)
        and YEAR in norm(ceem_text)
    )
    if not ceem_ok:
        return {
            "classification": "BLOCKED_0105A6Q4F_INSTITUTIONAL_METADATA_IDENTITY_FAILURE",
            "ceem": {"url": ceem_final, "status": ceem_status, "sha256": h256(ceem_raw)},
        }

    search_raw, search_final, search_status = fetch(SEARCH_URL)
    search_text = search_raw.decode("utf-8", errors="replace")
    urls = discover_item_urls(search_text, search_final)

    matches = []
    checked = []
    for url in urls:
        raw, final, status = fetch(url)
        text = raw.decode("utf-8", errors="replace")
        rec = {
            "requested_url": url,
            "final_url": final,
            "status": status,
            "response_sha256": h256(raw),
            "official_iu_host": official_iu(final),
            "title_match": exact_title_present(text),
            "author_match": author_present(text),
            "year_match": YEAR in norm(text),
        }
        checked.append(rec)
        if status == 200 and rec["official_iu_host"] and rec["title_match"] and rec["author_match"] and rec["year_match"]:
            matches.append(rec)

    if len(matches) == 0:
        classification = "BLOCKED_0105A6Q4F_CANONICAL_DISSERTATION_RECORD_NOT_RESOLVED"
    elif len(matches) > 1:
        classification = "BLOCKED_0105A6Q4F_CANONICAL_RECORD_AMBIGUOUS"
    else:
        classification = "PASS_0105A6Q4F_INSTITUTIONAL_AUTHORITY_MANIFEST_NONDISCOVERY"

    return {
        "classification": classification,
        "ceem": {
            "url": ceem_final,
            "status": ceem_status,
            "sha256": h256(ceem_raw),
            "title_match": True,
            "author_match": True,
            "year_match": True,
        },
        "scholarworks_search": {
            "requested_url": SEARCH_URL,
            "final_url": search_final,
            "status": search_status,
            "response_sha256": h256(search_raw),
            "candidate_item_urls": urls,
        },
        "checked_records": checked,
        "matching_records": matches,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    args = ap.parse_args()
    base = {
        "benchmark": BENCHMARK,
        "preregistration_commit": PREREG_COMMIT,
        "git_sha": args.git_sha,
        "pdf_downloaded": False,
        "pdf_content_inspected": False,
        "pdftotext_executed": False,
        "pseudo_data_generated": False,
        "likelihood_evaluated": False,
        "systematic_monte_carlo_preregistration_permission_percent": 0,
        "systematic_monte_carlo_execution_permission_percent": 0,
        "observed_bsm_residual_permission_percent": 0,
        "observed_bsm_residual_inspected": False,
    }
    try:
        result = {**base, **classify()}
    except Exception as exc:
        result = {
            **base,
            "classification": "BLOCKED_0105A6Q4F_INSTITUTIONAL_METADATA_IDENTITY_FAILURE",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
        }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
