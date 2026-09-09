#!/usr/bin/env python3
"""Discover exact Zenodo file metadata for the preregistered 0100c coherent control.

This step deliberately avoids downloading the multi-GB stellar archive. It records
immutable record/file metadata first so a later heavy pinning run can be frozen
prospectively.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

EMISSION_RECORD_ID = 20618971
EMISSION_DOI = "10.5281/zenodo.20618971"
EMISSION_API = f"https://zenodo.org/api/records/{EMISSION_RECORD_ID}"
STELLAR_RECORD_ID = 20822085
STELLAR_DOI = "10.5281/zenodo.20822085"
STELLAR_API = f"https://zenodo.org/api/records/{STELLAR_RECORD_ID}"
STELLAR_25_NAME = "25msun.tar.gz"
STELLAR_25_MD5 = "b34c9573c929638afac89cec43ae7203"


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "NMIR-authority-pinner/0100c"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_checksum(value):
    if value is None:
        return None, None
    text = str(value)
    if ":" in text:
        kind, digest = text.split(":", 1)
        return kind.lower(), digest.lower()
    return None, text.lower()


def inventory(record: dict) -> list[dict]:
    out = []
    for f in record.get("files", []):
        ctype, cvalue = normalize_checksum(f.get("checksum"))
        out.append(
            {
                "key": f.get("key"),
                "size": f.get("size"),
                "checksum_type": ctype,
                "checksum_value": cvalue,
                "download_url": (f.get("links") or {}).get("content") or (f.get("links") or {}).get("self"),
            }
        )
    return out


def record_summary(record: dict) -> dict:
    md = record.get("metadata", {})
    return {
        "id": record.get("id"),
        "doi": md.get("doi") or record.get("doi"),
        "title": md.get("title"),
        "version": md.get("version"),
        "publication_date": md.get("publication_date"),
        "files": inventory(record),
    }


def is_mesa25_name(name: str | None) -> bool:
    if not name:
        return False
    low = name.lower().replace("-", "").replace("_", "")
    return "mesa" in low and any(tok in low for tok in ("25msun", "25m", "m25", "25solar"))


def build_result(emission_raw: bytes, stellar_raw: bytes, git_sha: str | None = None) -> dict:
    emission = json.loads(emission_raw)
    stellar = json.loads(stellar_raw)
    es = record_summary(emission)
    ss = record_summary(stellar)

    emission_candidates = [f for f in es["files"] if is_mesa25_name(f.get("key"))]
    stellar_exact = [f for f in ss["files"] if f.get("key") == STELLAR_25_NAME]
    stellar_hash_ok = bool(stellar_exact) and stellar_exact[0].get("checksum_type") == "md5" and stellar_exact[0].get("checksum_value") == STELLAR_25_MD5

    gates = {
        "emission_record_identity": es["id"] == EMISSION_RECORD_ID,
        "emission_file_inventory_nonempty": len(es["files"]) > 0,
        "stellar_record_identity": ss["id"] == STELLAR_RECORD_ID,
        "stellar_25_exact_file_present": len(stellar_exact) == 1,
        "stellar_25_published_md5_matches_prereg": stellar_hash_ok,
    }

    return {
        "benchmark": "NMIR-BENCHMARK-0100C",
        "status": (
            "PASS_0100C_ZENODO_METADATA_DISCOVERED_NONTERMINAL"
            if all(gates.values())
            else "BLOCKED_0100C_ZENODO_METADATA_DISCOVERY_INCOMPLETE"
        ),
        "emission": {
            "doi": EMISSION_DOI,
            "api_url": EMISSION_API,
            "metadata_sha256": sha256_bytes(emission_raw),
            "record": es,
            "mesa25_filename_candidates": emission_candidates,
            "mesa25_candidate_count": len(emission_candidates),
        },
        "stellar": {
            "doi": STELLAR_DOI,
            "api_url": STELLAR_API,
            "metadata_sha256": sha256_bytes(stellar_raw),
            "record": ss,
            "frozen_25msun_file": stellar_exact[0] if len(stellar_exact) == 1 else None,
        },
        "gates": gates,
        "terminal_physics_execution_allowed": False,
        "heavy_archive_download_allowed": all(gates.values()),
        "snapshot_mapping_authority_closed": False,
        "git_sha": git_sha,
        "terminal_next_step": (
            "freeze the exact emission asset(s) identified from this inventory; then run a separate heavy parser to prove 25 Msun spectrum/lightcurve-to-stellar-profile snapshot correspondence before any MSW terminal calculation"
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", type=Path, default=Path("artifacts/0100c"))
    p.add_argument("--emission-json", type=Path)
    p.add_argument("--stellar-json", type=Path)
    p.add_argument("--git-sha")
    args = p.parse_args()
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)

    emission_raw = args.emission_json.read_bytes() if args.emission_json else fetch_bytes(EMISSION_API)
    stellar_raw = args.stellar_json.read_bytes() if args.stellar_json else fetch_bytes(STELLAR_API)
    (out / "emission_zenodo_metadata.json").write_bytes(emission_raw)
    (out / "stellar_zenodo_metadata.json").write_bytes(stellar_raw)
    result = build_result(emission_raw, stellar_raw, args.git_sha)
    (out / "zenodo_metadata_lock_discovery.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
