#!/usr/bin/env python3
"""Discover and pin metadata for the preregistered 0101a factorized authority route.

This is a provenance-discovery step only. It does not create a terminal 0101
parameter lock and it must never combine MicroBooNE and IceCube confidence levels.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import urllib.parse
import urllib.request

HEPDATA_DOI = "10.17182/hepdata.166435.v1"
HEPDATA_INSPIRE = "3088922"
HEPDATA_JSON_URL = f"https://www.hepdata.net/record/ins{HEPDATA_INSPIRE}?format=json"
ICECUBE_DOI = "10.7910/DVN/QKL28Z"
ICECUBE_API_URL = (
    "https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId="
    + urllib.parse.quote(f"doi:{ICECUBE_DOI}", safe="")
)


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "NMIR-authority-pinner/0101a"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json_bytes(data: bytes) -> dict:
    return json.loads(data.decode("utf-8"))


def _walk(obj, path="$"):
    if isinstance(obj, dict):
        for k, v in obj.items():
            child = f"{path}.{k}"
            yield child, k, v
            yield from _walk(v, child)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            child = f"{path}[{i}]"
            yield child, str(i), v
            yield from _walk(v, child)


def summarize_hepdata(obj: dict) -> dict:
    title = obj.get("record", {}).get("title") or obj.get("title") or ""
    tables = obj.get("data_tables") or obj.get("tables") or []
    if isinstance(tables, dict):
        tables = list(tables.values())

    strings = []
    for path, key, value in _walk(obj):
        if isinstance(value, str):
            strings.append((path, key, value))

    resource_candidates = []
    for path, key, value in strings:
        low = value.lower()
        if any(token in low for token in ("chi", "grid", "sterile", "resource", "download")):
            resource_candidates.append({"path": path, "key": key, "value": value})

    doi_strings = sorted({v for _, _, v in strings if "10.17182/hepdata.166435" in v.lower()})
    return {
        "title": title,
        "table_count": len(tables),
        "table_names": [
            (t.get("name") or t.get("title") or t.get("processed_name") or str(i))
            if isinstance(t, dict) else str(t)
            for i, t in enumerate(tables)
        ],
        "record_doi_mentions": doi_strings,
        "resource_candidates": resource_candidates,
    }


def summarize_dataverse(obj: dict) -> dict:
    status = obj.get("status")
    data = obj.get("data", {})
    latest = data.get("latestVersion", {})
    files = latest.get("files", [])
    inventory = []
    for item in files:
        df = item.get("dataFile", {})
        checksum = df.get("checksum") or {}
        inventory.append(
            {
                "id": df.get("id"),
                "filename": df.get("filename"),
                "content_type": df.get("contentType"),
                "filesize": df.get("filesize"),
                "checksum_type": checksum.get("type"),
                "checksum_value": checksum.get("value"),
                "persistent_id": df.get("persistentId"),
                "description": item.get("description"),
                "categories": item.get("categories", []),
            }
        )
    return {
        "api_status": status,
        "dataset_id": data.get("id"),
        "persistent_url": data.get("persistentUrl"),
        "version_number": latest.get("versionNumber"),
        "version_minor_number": latest.get("versionMinorNumber"),
        "version_state": latest.get("versionState"),
        "release_time": latest.get("releaseTime"),
        "file_count": len(inventory),
        "files": inventory,
    }


def build_result(hepdata_raw: bytes, icecube_raw: bytes, git_sha: str | None = None) -> dict:
    hep = load_json_bytes(hepdata_raw)
    ice = load_json_bytes(icecube_raw)
    hep_summary = summarize_hepdata(hep)
    ice_summary = summarize_dataverse(ice)

    gates = {
        "hepdata_title_mentions_microboone": "microboone" in hep_summary["title"].lower(),
        "hepdata_has_expected_three_or_more_tables": hep_summary["table_count"] >= 3,
        "icecube_dataverse_api_ok": ice_summary["api_status"] == "OK",
        "icecube_file_inventory_nonempty": ice_summary["file_count"] > 0,
        "no_joint_likelihood_claim": True,
    }

    return {
        "benchmark": "NMIR-BENCHMARK-0101A",
        "status": (
            "PASS_0101A_AUTHORITY_METADATA_DISCOVERED_NONTERMINAL"
            if all(gates.values())
            else "BLOCKED_0101A_AUTHORITY_METADATA_DISCOVERY_INCOMPLETE"
        ),
        "microboone": {
            "doi": HEPDATA_DOI,
            "inspire_id": HEPDATA_INSPIRE,
            "metadata_url": HEPDATA_JSON_URL,
            "metadata_sha256": sha256_bytes(hepdata_raw),
            "summary": hep_summary,
        },
        "icecube": {
            "doi": ICECUBE_DOI,
            "metadata_url": ICECUBE_API_URL,
            "metadata_sha256": sha256_bytes(icecube_raw),
            "summary": ice_summary,
        },
        "gates": gates,
        "joint_global_likelihood_claim_allowed": False,
        "terminal_physics_execution_allowed": False,
        "git_sha": git_sha,
        "terminal_next_step": (
            "inspect the discovered official file/resource inventory, then prospectively freeze exact consumed assets, hashes, parameter domains and statistic conventions in 0101b before terminal execution"
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", type=Path, default=Path("artifacts/0101a"))
    p.add_argument("--hepdata-json", type=Path)
    p.add_argument("--icecube-json", type=Path)
    p.add_argument("--git-sha")
    args = p.parse_args()
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)

    hep_raw = args.hepdata_json.read_bytes() if args.hepdata_json else fetch_bytes(HEPDATA_JSON_URL)
    ice_raw = args.icecube_json.read_bytes() if args.icecube_json else fetch_bytes(ICECUBE_API_URL)

    (out / "microboone_hepdata_metadata.json").write_bytes(hep_raw)
    (out / "icecube_dataverse_metadata.json").write_bytes(ice_raw)
    result = build_result(hep_raw, ice_raw, args.git_sha)
    (out / "authority_metadata_lock_discovery.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
