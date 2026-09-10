#!/usr/bin/env python3
"""Pin exact DeepCore B4RITM payload bytes for NMIR 0105a4b.

The four Dataverse payloads are treated as opaque bytes only. Provider MD5 and
size are checked, SHA256 is recorded, and no pickle is deserialized or parsed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import socket
import time
import urllib.error
import urllib.request

DATASET_PID = "doi:10.7910/DVN/B4RITM"
FORBIDDEN_STERILE_PID = "doi:10.7910/DVN/QKL28Z"
FILES = [
    {
        "file_id": 6660756,
        "filename": "DNN_uncertainty_splines.pckl",
        "expected_size": 438500,
        "provider_md5": "cf76ce7b74baa183f54930c21918a3df",
        "persistent_id": "doi:10.7910/DVN/B4RITM/PRGLAR",
    },
    {
        "file_id": 6660758,
        "filename": "oscNext_data_IC86.11-18.pckl",
        "expected_size": 1445962,
        "provider_md5": "95e1236193931562959b8547312c74ed",
        "persistent_id": "doi:10.7910/DVN/B4RITM/DIOZGU",
    },
    {
        "file_id": 6660757,
        "filename": "oscNext_genie_level7_v02.00_pass2.120000.pckl",
        "expected_size": 25054422,
        "provider_md5": "b2dcbf606438088bdee3a8a7b8a1df4e",
        "persistent_id": "doi:10.7910/DVN/B4RITM/EEIBWL",
    },
    {
        "file_id": 6660755,
        "filename": "oscNext_muongun_level7_v02.00_pass2.140000.pckl",
        "expected_size": 12162293,
        "provider_md5": "9c25d2ff8c16ea944d58a9eaa56dc60a",
        "persistent_id": "doi:10.7910/DVN/B4RITM/I3XG5M",
    },
]
TRANSIENT_HTTP = {429, 500, 502, 503, 504}


def file_url(file_id: int) -> str:
    return f"https://dataverse.harvard.edu/api/access/datafile/{file_id}"


def hash_bytes(data: bytes) -> tuple[str, str]:
    return hashlib.md5(data).hexdigest(), hashlib.sha256(data).hexdigest()


def fetch_opaque_bytes(url: str, attempts: int = 4) -> tuple[bytes, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 NMIR/0105a4b opaque-byte-pin",
            "Accept": "application/octet-stream,*/*;q=0.8",
        },
    )
    last = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                return response.read(), response.geturl()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in TRANSIENT_HTTP:
                raise RuntimeError(f"BLOCKED_0105A4B_HTTP_{exc.code} url={url}") from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last = exc
        if attempt < attempts:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"BLOCKED_0105A4B_TRANSPORT attempts={attempts} url={url}") from last


def frozen_inventory_valid() -> bool:
    if DATASET_PID != "doi:10.7910/DVN/B4RITM":
        return False
    if FORBIDDEN_STERILE_PID == DATASET_PID:
        return False
    if len(FILES) != 4:
        return False
    expected_ids = {6660756, 6660758, 6660757, 6660755}
    if {x["file_id"] for x in FILES} != expected_ids:
        return False
    for item in FILES:
        if not item["filename"] or item["expected_size"] <= 0:
            return False
        md5 = item["provider_md5"]
        if len(md5) != 32:
            return False
        try:
            int(md5, 16)
        except ValueError:
            return False
        if "B4RITM" not in item["persistent_id"] or "QKL28Z" in item["persistent_id"]:
            return False
    return True


def build_manifest(fetcher=fetch_opaque_bytes, git_sha: str | None = None) -> dict:
    if not frozen_inventory_valid():
        raise RuntimeError("BLOCKED_0105A4B_FROZEN_INVENTORY_INVALID")

    out = []
    all_md5 = True
    all_sizes = True
    all_sha = True
    for item in FILES:
        url = file_url(item["file_id"])
        data, resolved_url = fetcher(url)
        actual_md5, sha256 = hash_bytes(data)
        md5_ok = actual_md5 == item["provider_md5"]
        size_ok = len(data) == item["expected_size"]
        sha_ok = len(sha256) == 64
        all_md5 &= md5_ok
        all_sizes &= size_ok
        all_sha &= sha_ok
        out.append(
            {
                **item,
                "request_url": url,
                "resolved_url": resolved_url,
                "actual_size": len(data),
                "actual_md5": actual_md5,
                "provider_md5_match": md5_ok,
                "size_match": size_ok,
                "sha256": sha256,
            }
        )
        del data

    gates = {
        "frozen_inventory_valid": True,
        "exact_file_count_4": len(out) == 4,
        "all_provider_md5_match": all_md5,
        "all_provider_sizes_match": all_sizes,
        "all_sha256_recorded": all_sha,
        "dataset_identity_b4ritm": DATASET_PID.endswith("B4RITM"),
        "sterile_authority_substitution_detected": False,
        "binary_content_parsed": False,
        "observed_residual_execution_remains_locked": True,
        "bsm_interpretation_remains_locked": True,
    }
    pass_keys = (
        "frozen_inventory_valid",
        "exact_file_count_4",
        "all_provider_md5_match",
        "all_provider_sizes_match",
        "all_sha256_recorded",
        "dataset_identity_b4ritm",
        "observed_residual_execution_remains_locked",
        "bsm_interpretation_remains_locked",
    )
    passed = all(gates[k] for k in pass_keys) and not gates["sterile_authority_substitution_detected"] and not gates["binary_content_parsed"]
    return {
        "benchmark": "NMIR-V2-0105A4B",
        "status": (
            "PASS_0105A4B_DEEPCORE_B4RITM_DIRECT_BYTE_LOCK_NONTERMINAL_NONDISCOVERY"
            if passed
            else "BLOCKED_0105A4B_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE"
        ),
        "dataset_persistent_id": DATASET_PID,
        "dataset_version": "1.1",
        "files": out,
        "gates": gates,
        "deepcore_b4ritm_byte_lock_complete": passed,
        "binary_content_parsed": False,
        "observed_residual_execution_allowed": False,
        "bsm_interpretation_allowed": False,
        "sterile_authority_substitution_forbidden": True,
        "git_sha": git_sha,
    }


def normalized_manifest(result: dict) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/0105a4b"))
    parser.add_argument("--git-sha")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    result = build_manifest(git_sha=args.git_sha)
    normalized = normalized_manifest(result)
    manifest = args.output_dir / "deepcore_b4ritm_direct_byte_manifest.json"
    manifest.write_text(normalized, encoding="utf-8")
    digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    (args.output_dir / "manifest_sha256.txt").write_text(digest + "\n", encoding="utf-8")
    print(normalized, end="")
    print(f"manifest_sha256={digest}")
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
