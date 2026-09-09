#!/usr/bin/env python3
"""Pin the DeepCore B4RITM Dataverse metadata inventory for NMIR v2 gate 0105a4.

Metadata/provenance only. This gate does not download event files or evaluate
an observed residual.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import socket
import time
import urllib.error
import urllib.parse
import urllib.request

EXPECTED_DOI = "10.7910/DVN/B4RITM"
FORBIDDEN_STERILE_DOI = "10.7910/DVN/QKL28Z"
API_URL = (
    "https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId="
    + urllib.parse.quote(f"doi:{EXPECTED_DOI}", safe="")
)
TRANSIENT_HTTP = {429, 500, 502, 503, 504}


def fetch_bytes(url: str, attempts: int = 4) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 NMIR/0105a4 authority-inventory",
            "Accept": "application/json,text/plain;q=0.9,*/*;q=0.8",
        },
    )
    last = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in TRANSIENT_HTTP:
                raise RuntimeError(f"BLOCKED_0105A4_HTTP_{exc.code}") from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last = exc
        if attempt < attempts:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"BLOCKED_0105A4_TRANSPORT attempts={attempts}") from last


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_dataverse(raw: bytes) -> dict:
    obj = json.loads(raw.decode("utf-8"))
    if not isinstance(obj, dict):
        raise ValueError("Dataverse metadata root must be a JSON object")
    data = obj.get("data") or {}
    latest = data.get("latestVersion") or {}
    files = []
    for item in latest.get("files") or []:
        df = item.get("dataFile") or {}
        checksum = df.get("checksum") or {}
        files.append(
            {
                "id": df.get("id"),
                "filename": df.get("filename"),
                "content_type": df.get("contentType"),
                "size_bytes": df.get("filesize"),
                "persistent_id": df.get("persistentId"),
                "checksum_type": checksum.get("type"),
                "checksum_value": checksum.get("value"),
                "description": item.get("description"),
                "categories": item.get("categories") or [],
            }
        )
    return {
        "api_status": obj.get("status"),
        "dataset_id": data.get("id"),
        "persistent_url": data.get("persistentUrl"),
        "identifier": data.get("identifier"),
        "protocol": data.get("protocol"),
        "authority": data.get("authority"),
        "version_number": latest.get("versionNumber"),
        "version_minor_number": latest.get("versionMinorNumber"),
        "version_state": latest.get("versionState"),
        "release_time": latest.get("releaseTime"),
        "file_count": len(files),
        "files": files,
    }


def _identity_text(summary: dict) -> str:
    return " ".join(
        str(summary.get(k) or "")
        for k in ("persistent_url", "identifier", "protocol", "authority")
    ).lower()


def build_result(raw: bytes, git_sha: str | None = None) -> dict:
    summary = normalize_dataverse(raw)
    identity = _identity_text(summary)
    files = summary["files"]
    file_fields_valid = all(
        bool(f.get("filename"))
        and isinstance(f.get("size_bytes"), int)
        and f["size_bytes"] > 0
        and bool(f.get("checksum_type"))
        and bool(f.get("checksum_value"))
        for f in files
    )
    expected_identity = (
        "b4ritm" in identity or EXPECTED_DOI.lower() in identity
    )
    forbidden_identity = (
        "qkl28z" in identity or FORBIDDEN_STERILE_DOI.lower() in identity
    )
    gates = {
        "dataverse_api_ok": summary.get("api_status") == "OK",
        "b4ritm_identity_ok": expected_identity,
        "qkl28z_sterile_identity_absent": not forbidden_identity,
        "version_released": summary.get("version_state") == "RELEASED",
        "inventory_nonempty": summary.get("file_count", 0) > 0,
        "all_files_have_name_size_checksum": file_fields_valid,
        "observed_residual_execution_remains_locked": True,
    }
    return {
        "benchmark": "NMIR-V2-0105A4",
        "status": (
            "PASS_0105A4_DEEPCORE_B4RITM_AUTHORITY_INVENTORY_NONTERMINAL"
            if all(gates.values())
            else "BLOCKED_0105A4_DEEPCORE_B4RITM_AUTHORITY_INVENTORY_INCOMPLETE"
        ),
        "expected_doi": EXPECTED_DOI,
        "forbidden_sterile_doi": FORBIDDEN_STERILE_DOI,
        "metadata_url": API_URL,
        "raw_metadata_sha256": sha256_bytes(raw),
        "inventory": summary,
        "gates": gates,
        "deepcore_consumed_byte_lock_complete": False,
        "observed_residual_execution_allowed": False,
        "git_sha": git_sha,
    }


def normalized_result(result: dict) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/0105a4"))
    parser.add_argument("--dataverse-json", type=Path)
    parser.add_argument("--git-sha")
    args = parser.parse_args()

    raw = args.dataverse_json.read_bytes() if args.dataverse_json else fetch_bytes(API_URL)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "deepcore_b4ritm_dataverse_metadata.json").write_bytes(raw)
    result = build_result(raw, args.git_sha)
    normalized = normalized_result(result)
    (args.output_dir / "deepcore_b4ritm_authority_inventory.json").write_text(normalized, encoding="utf-8")
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    (args.output_dir / "normalized_inventory_sha256.txt").write_text(digest + "\n", encoding="utf-8")
    print(normalized, end="")
    print(f"normalized_inventory_sha256={digest}")
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
