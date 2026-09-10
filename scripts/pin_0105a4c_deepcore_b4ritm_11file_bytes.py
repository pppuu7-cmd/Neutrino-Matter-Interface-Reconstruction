#!/usr/bin/env python3
"""Corrected 0105a4c: exact B4RITM 11-file byte lock.

Scientific content is never parsed. The live Dataverse metadata inventory must
exactly reproduce the frozen parent 0105a4 tuples before opaque bytes are
retrieved and checked against provider MD5/size. SHA256 is recorded locally.
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

DATASET_DOI = "10.7910/DVN/B4RITM"
FORBIDDEN_STERILE_DOI = "10.7910/DVN/QKL28Z"
EXPECTED_VERSION = (1, 0)
METADATA_URL = (
    "https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId="
    + urllib.parse.quote(f"doi:{DATASET_DOI}", safe="")
)
TRANSIENT_HTTP = {429, 500, 502, 503, 504}
FROZEN = [
    (11646859, "data.tab", 4091, "59d03738e7fe61fe06a06b2140708373"),
    (11674675, "example.ipynb", 231264, "fd9ac548e6a6f136efb6c61058cc822f"),
    (11646858, "hs_numu_cc.tab", 543795, "d9cfa0e209bb82af43c78474765be5e3"),
    (11646854, "hs_nu_nc_nue_cc.tab", 543327, "75cffca2d2d099373c680a5f4088c195"),
    (11646853, "hs_nutau_cc.tab", 544770, "cd3c6335d25d1163c5df30aaff50be2a"),
    (11646851, "mc_mu.tab", 5815, "bc7133f3da6c1acf830a9e8d686bef4c"),
    (11646852, "mc_nue_cc.tab", 6234527, "2150abf034ed873b798dfa61cbe7ac78"),
    (11646856, "mc_numu_cc.tab", 44626533, "b60ccf0e0e447698d35b953a6e22552d"),
    (11646850, "mc_nu_nc.tab", 3975602, "fb5eac7230c1ab1b4e8b1f019ed33e2b"),
    (11646855, "mc_nutau_cc.tab", 7266105, "cb62a96ed14491deef10bb8253a786ca"),
    (11674676, "readme.md", 7141, "848778cd0b870da83a6b925b89ba3d3d"),
]


def request_bytes(url: str, *, accept: str, attempts: int = 4, timeout: int = 180) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 NMIR/0105a4c", "Accept": accept})
    last = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read(), response.geturl()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in TRANSIENT_HTTP:
                raise RuntimeError(f"BLOCKED_0105A4C_HTTP_{exc.code} url={url}") from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last = exc
        if attempt < attempts:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"BLOCKED_0105A4C_TRANSPORT attempts={attempts} url={url}") from last


def fetch_metadata() -> bytes:
    return request_bytes(METADATA_URL, accept="application/json,*/*;q=0.8", timeout=90)[0]


def parse_live_inventory(raw: bytes) -> tuple[dict, list[tuple[int, str, int, str]]]:
    obj = json.loads(raw.decode("utf-8"))
    data = obj.get("data") or {}
    latest = data.get("latestVersion") or {}
    identity = {
        "api_status": obj.get("status"),
        "identifier": data.get("identifier"),
        "authority": data.get("authority"),
        "persistent_url": data.get("persistentUrl"),
        "version_number": latest.get("versionNumber"),
        "version_minor_number": latest.get("versionMinorNumber"),
        "version_state": latest.get("versionState"),
    }
    files = []
    for item in latest.get("files") or []:
        df = item.get("dataFile") or {}
        checksum = df.get("checksum") or {}
        files.append((df.get("id"), df.get("filename"), df.get("filesize"), checksum.get("value")))
    return identity, files


def identity_and_inventory_valid(raw: bytes) -> tuple[bool, dict, list[tuple[int, str, int, str]]]:
    identity, files = parse_live_inventory(raw)
    expected_identity = identity.get("identifier") == "DVN/B4RITM" and identity.get("authority") == "10.7910"
    version_ok = (identity.get("version_number"), identity.get("version_minor_number")) == EXPECTED_VERSION
    released = identity.get("version_state") == "RELEASED"
    exact_inventory = files == FROZEN
    no_sterile = "QKL28Z" not in json.dumps({"identity": identity, "files": files})
    return expected_identity and version_ok and released and exact_inventory and no_sterile, identity, files


def file_url(file_id: int) -> str:
    return f"https://dataverse.harvard.edu/api/access/datafile/{file_id}"


def build_manifest(metadata_raw: bytes, byte_fetcher=None, git_sha: str | None = None) -> dict:
    ok, identity, live_files = identity_and_inventory_valid(metadata_raw)
    if not ok:
        return {
            "benchmark": "NMIR-V2-0105A4C",
            "status": "BLOCKED_0105A4C_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE",
            "metadata_identity": identity,
            "live_inventory": live_files,
            "frozen_inventory": FROZEN,
            "gates": {"live_metadata_exact_match": False},
            "binary_content_parsed": False,
            "observed_residual_execution_allowed": False,
            "bsm_interpretation_allowed": False,
            "git_sha": git_sha,
        }
    if byte_fetcher is None:
        byte_fetcher = lambda url: request_bytes(url, accept="application/octet-stream,*/*;q=0.8")

    records = []
    all_md5 = all_size = all_sha = True
    for file_id, filename, expected_size, provider_md5 in FROZEN:
        request_url = file_url(file_id)
        payload, resolved_url = byte_fetcher(request_url)
        actual_md5 = hashlib.md5(payload).hexdigest()
        sha256 = hashlib.sha256(payload).hexdigest()
        md5_ok = actual_md5 == provider_md5
        size_ok = len(payload) == expected_size
        sha_ok = len(sha256) == 64
        all_md5 &= md5_ok
        all_size &= size_ok
        all_sha &= sha_ok
        records.append({
            "file_id": file_id,
            "filename": filename,
            "expected_size": expected_size,
            "actual_size": len(payload),
            "provider_md5": provider_md5,
            "actual_md5": actual_md5,
            "provider_md5_match": md5_ok,
            "size_match": size_ok,
            "sha256": sha256,
            "request_url": request_url,
            "resolved_url": resolved_url,
        })
        del payload

    gates = {
        "live_metadata_exact_match": True,
        "exact_file_count_11": len(records) == 11,
        "all_provider_md5_match": all_md5,
        "all_provider_sizes_match": all_size,
        "all_sha256_recorded": all_sha,
        "binary_content_parsed": False,
        "observed_residual_execution_remains_locked": True,
        "bsm_interpretation_remains_locked": True,
        "sterile_authority_substitution_detected": False,
    }
    passed = all(gates[k] for k in [
        "live_metadata_exact_match", "exact_file_count_11", "all_provider_md5_match",
        "all_provider_sizes_match", "all_sha256_recorded",
        "observed_residual_execution_remains_locked", "bsm_interpretation_remains_locked",
    ]) and not gates["binary_content_parsed"] and not gates["sterile_authority_substitution_detected"]
    return {
        "benchmark": "NMIR-V2-0105A4C",
        "status": "PASS_0105A4C_DEEPCORE_B4RITM_11FILE_BYTE_LOCK_NONDISCOVERY" if passed else "BLOCKED_0105A4C_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE",
        "dataset_doi": DATASET_DOI,
        "dataset_version": "1.0",
        "metadata_sha256": hashlib.sha256(metadata_raw).hexdigest(),
        "files": records,
        "gates": gates,
        "binary_content_parsed": False,
        "observed_residual_execution_allowed": False,
        "bsm_interpretation_allowed": False,
        "git_sha": git_sha,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/0105a4c"))
    parser.add_argument("--git-sha")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    raw = fetch_metadata()
    result = build_manifest(raw, git_sha=args.git_sha)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    (args.output_dir / "deepcore_b4ritm_11file_byte_manifest.json").write_text(text, encoding="utf-8")
    digest = hashlib.sha256(text.encode()).hexdigest()
    (args.output_dir / "manifest_sha256.txt").write_text(digest + "\n", encoding="utf-8")
    print(text, end="")
    print(f"manifest_sha256={digest}")
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
