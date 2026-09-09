#!/usr/bin/env python3
"""Pin the official COHERENT/ORNL -> Zenodo CEvNS release route for 0105a2.

This is provenance metadata only. It does not download event-release bytes and
never authorizes an observed residual scan.
"""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import urllib.parse
import urllib.request

OFFICIAL_URL = "https://coherent.ornl.gov/data-releases/"
EXPECTED = {
    "csi_event_release": {"record_id": "1228631", "doi": "10.5281/zenodo.1228631"},
    "ar_event_release": {"record_id": "3903810", "doi": "10.5281/zenodo.3903810"},
}
CALIBRATION_AUXILIARY_DOI = "10.13139/OLCF/1969085"


class _LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.links.append(value)


def fetch_bytes(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 NMIR/0105a2 provenance-pin",
            "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        return response.read()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _zenodo_record_id(href: str) -> str | None:
    absolute = urllib.parse.urljoin(OFFICIAL_URL, href)
    parsed = urllib.parse.urlsplit(absolute)
    host = (parsed.hostname or "").lower()
    if host not in {"zenodo.org", "www.zenodo.org"}:
        return None
    match = re.search(r"/(?:record|records)/(\d+)(?:/|$)", parsed.path)
    return match.group(1) if match else None


def build_result(raw_html: bytes, git_sha: str | None = None) -> dict:
    text = raw_html.decode("utf-8", errors="replace")
    parser = _LinkParser()
    parser.feed(text)

    zenodo_links: list[dict] = []
    for href in parser.links:
        record_id = _zenodo_record_id(href)
        if record_id is not None:
            zenodo_links.append({"record_id": record_id, "href": href})

    found_ids = {item["record_id"] for item in zenodo_links}
    expected_ids = {item["record_id"] for item in EXPECTED.values()}
    gates = {
        "csi_event_record_linked": EXPECTED["csi_event_release"]["record_id"] in found_ids,
        "ar_event_record_linked": EXPECTED["ar_event_release"]["record_id"] in found_ids,
        "expected_event_records_distinct": len(expected_ids) == 2,
        "event_byte_lock_remains_incomplete": True,
        "observed_residual_execution_remains_locked": True,
        "calibration_auxiliary_not_substituted": CALIBRATION_AUXILIARY_DOI
        not in {item["doi"] for item in EXPECTED.values()},
    }

    return {
        "benchmark": "NMIR-V2-0105A2",
        "status": (
            "PASS_0105A2_COHERENT_OFFICIAL_RELEASE_ROUTE_PINNED_NONTERMINAL"
            if all(gates.values())
            else "BLOCKED_0105A2_COHERENT_OFFICIAL_RELEASE_ROUTE_UNRESOLVED"
        ),
        "official_anchor": {
            "url": OFFICIAL_URL,
            "raw_html_sha256": sha256_bytes(raw_html),
        },
        "expected_event_releases": EXPECTED,
        "observed_zenodo_links": zenodo_links,
        "observed_zenodo_record_ids": sorted(found_ids),
        "separate_auxiliary_authority": {
            "doi": CALIBRATION_AUXILIARY_DOI,
            "role": "CsI[Na] nuclear-recoil response/calibration; NOT CEvNS event-release substitute",
        },
        "gates": gates,
        "event_byte_lock_complete": False,
        "observed_residual_execution_allowed": False,
        "git_sha": git_sha,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/0105a2"))
    parser.add_argument("--html", type=Path)
    parser.add_argument("--git-sha")
    args = parser.parse_args()

    raw = args.html.read_bytes() if args.html else fetch_bytes(OFFICIAL_URL)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "coherent_official_data_releases.html").write_bytes(raw)
    result = build_result(raw, args.git_sha)
    normalized = json.dumps(result, indent=2, sort_keys=True) + "\n"
    (args.output_dir / "coherent_official_release_route.json").write_text(normalized, encoding="utf-8")
    print(normalized, end="")
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
