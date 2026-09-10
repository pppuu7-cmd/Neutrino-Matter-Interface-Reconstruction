#!/usr/bin/env python3
"""NMIR v2 0105a4d: lock exact B4RITM Saved Original bytes.

This is a provenance-only gate. Scientific payloads are treated as opaque
bytes and are discarded after size/MD5/SHA256 validation. Ingested tabular
files are fetched only through Dataverse's documented ``format=original``
route; the two non-tabular files are fetched directly.
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
PARENT_RAW_METADATA_SHA256 = "50b0e1ed9d939d1a2b2f4e497dd3841c9c73eb8ecaa4a589268d3ba75ad3d0db"
PARENT_NORMALIZED_INVENTORY_SHA256 = "1cfc666849a7cf200ef4cdaf47b926e9ece44b63a92d4e29710c5a0cba441baa"
METADATA_URL = (
    "https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId="
    + urllib.parse.quote(f"doi:{DATASET_DOI}", safe="")
)
TRANSIENT_HTTP = {429, 500, 502, 503, 504}

# file_id, archival_name, representation, returned/original_name, bytes, provider_md5
FROZEN = [
    (11646859, "data.tab", "saved-original", "data.csv", 4091, "59d03738e7fe61fe06a06b2140708373"),
    (11674675, "example.ipynb", "direct", "example.ipynb", 231264, "fd9ac548e6a6f136efb6c61058cc822f"),
    (11646858, "hs_numu_cc.tab", "saved-original", "hs_numu_cc.csv", 543795, "d9cfa0e209bb82af43c78474765be5e3"),
    (11646854, "hs_nu_nc_nue_cc.tab", "saved-original", "hs_nu_nc_nue_cc.csv", 543327, "75cffca2d2d099373c680a5f4088c195"),
    (11646853, "hs_nutau_cc.tab", "saved-original", "hs_nutau_cc.csv", 544770, "cd3c6335d25d1163c5df30aaff50be2a"),
    (11646851, "mc_mu.tab", "saved-original", "mc_mu.csv", 5815, "bc7133f3da6c1acf830a9e8d686bef4c"),
    (11646852, "mc_nue_cc.tab", "saved-original", "mc_nue_cc.csv", 6234527, "2150abf034ed873b798dfa61cbe7ac78"),
    (11646856, "mc_numu_cc.tab", "saved-original", "mc_numu_cc.csv", 44626533, "b60ccf0e0e447698d35b953a6e22552d"),
    (11646850, "mc_nu_nc.tab", "saved-original", "mc_nu_nc.csv", 3975602, "fb5eac7230c1ab1b4e8b1f019ed33e2b"),
    (11646855, "mc_nutau_cc.tab", "saved-original", "mc_nutau_cc.csv", 7266105, "cb62a96ed14491deef10bb8253a786ca"),
    (11674676, "readme.md", "direct", "readme.md", 7141, "848778cd0b870da83a6b925b89ba3d3d"),
]


def request_bytes(url: str, *, accept: str, attempts: int = 4, timeout: int = 180) -> tuple[bytes, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 NMIR/0105a4d", "Accept": accept},
    )
    last = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read(), response.geturl()
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in TRANSIENT_HTTP:
                raise RuntimeError(f"BLOCKED_0105A4D_HTTP_{exc.code} url={url}") from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last = exc
        if attempt < attempts:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"BLOCKED_0105A4D_TRANSPORT attempts={attempts} url={url}") from last


def fetch_metadata() -> bytes:
    return request_bytes(METADATA_URL, accept="application/json,*/*;q=0.8", timeout=90)[0]


def _canonical(rows):
    return sorted(rows, key=lambda r: (r[0], r[1], r[2], r[3], r[4], r[5]))


def parse_live_metadata(raw: bytes) -> tuple[dict, list[tuple]]:
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
    rows = []
    for item in latest.get("files") or []:
        df = item.get("dataFile") or {}
        checksum = df.get("checksum") or {}
        tabular = df.get("tabularData") is True
        representation = "saved-original" if tabular else "direct"
        returned_name = df.get("originalFileName") if tabular else df.get("filename")
        expected_size = df.get("originalFileSize") if tabular else df.get("filesize")
        rows.append(
            (
                df.get("id"),
                df.get("filename"),
                representation,
                returned_name,
                expected_size,
                checksum.get("value"),
                df.get("filesize"),
                df.get("tabularData") is True,
                df.get("originalFileFormat"),
            )
        )
    return identity, rows


def frozen_metadata_rows() -> list[tuple]:
    rows = []
    for file_id, archival, representation, returned, size, md5 in FROZEN:
        if representation == "saved-original":
            rows.append((file_id, archival, representation, returned, size, md5, size, True, "text/csv"))
        else:
            rows.append((file_id, archival, representation, returned, size, md5, size, False, None))
    return rows


def metadata_valid(raw: bytes) -> tuple[bool, dict, list[tuple], dict]:
    identity, rows = parse_live_metadata(raw)
    identity_ok = (
        identity.get("api_status") == "OK"
        and identity.get("identifier") == "DVN/B4RITM"
        and identity.get("authority") == "10.7910"
        and (identity.get("version_number"), identity.get("version_minor_number")) == EXPECTED_VERSION
        and identity.get("version_state") == "RELEASED"
    )
    no_sterile = "QKL28Z" not in json.dumps({"identity": identity, "rows": rows})
    exact_rows = _canonical(rows) == _canonical(frozen_metadata_rows())
    modes = [row[2] for row in rows]
    mode_counts_ok = modes.count("saved-original") == 9 and modes.count("direct") == 2
    gates = {
        "b4ritm_identity_release_exact": identity_ok,
        "exact_11file_representation_metadata": exact_rows and len(rows) == 11,
        "exact_9_saved_original_2_direct": mode_counts_ok,
        "sterile_authority_substitution_absent": no_sterile,
    }
    return all(gates.values()), identity, rows, gates


def file_url(file_id: int, representation: str) -> str:
    base = f"https://dataverse.harvard.edu/api/access/datafile/{file_id}"
    if representation == "saved-original":
        return base + "?format=original"
    if representation == "direct":
        return base
    raise ValueError(f"unknown representation: {representation}")


def build_manifest(metadata_raw: bytes, byte_fetcher=None, git_sha: str | None = None) -> dict:
    ok, identity, live_rows, metadata_gates = metadata_valid(metadata_raw)
    common = {
        "benchmark": "NMIR-V2-0105A4D",
        "dataset_doi": DATASET_DOI,
        "forbidden_sterile_doi": FORBIDDEN_STERILE_DOI,
        "dataset_version": "1.0",
        "parent_raw_metadata_sha256": PARENT_RAW_METADATA_SHA256,
        "parent_normalized_inventory_sha256": PARENT_NORMALIZED_INVENTORY_SHA256,
        "live_metadata_sha256": hashlib.sha256(metadata_raw).hexdigest(),
        "metadata_identity": identity,
        "live_representation_inventory": live_rows,
        "binary_content_parsed": False,
        "observed_residual_execution_allowed": False,
        "bsm_interpretation_allowed": False,
        "git_sha": git_sha,
    }
    if not ok:
        return {
            **common,
            "status": "BLOCKED_0105A4D_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE",
            "files": [],
            "gates": {
                **metadata_gates,
                "all_provider_md5_match": False,
                "all_provider_sizes_match": False,
                "all_sha256_recorded": False,
                "all_request_modes_exact": False,
            },
        }

    if byte_fetcher is None:
        byte_fetcher = lambda url: request_bytes(url, accept="application/octet-stream,*/*;q=0.8")

    records = []
    all_md5 = True
    all_size = True
    all_sha = True
    all_modes = True
    for file_id, archival, representation, returned_name, expected_size, provider_md5 in FROZEN:
        request_url = file_url(file_id, representation)
        if representation == "saved-original":
            all_modes &= request_url.endswith("?format=original")
        else:
            all_modes &= "format=" not in request_url
        payload, resolved_url = byte_fetcher(request_url)
        actual_md5 = hashlib.md5(payload).hexdigest()
        sha256 = hashlib.sha256(payload).hexdigest()
        md5_ok = actual_md5 == provider_md5
        size_ok = len(payload) == expected_size
        sha_ok = len(sha256) == 64
        all_md5 &= md5_ok
        all_size &= size_ok
        all_sha &= sha_ok
        records.append(
            {
                "file_id": file_id,
                "archival_name": archival,
                "representation": representation,
                "expected_returned_name": returned_name,
                "expected_size": expected_size,
                "actual_size": len(payload),
                "provider_md5": provider_md5,
                "actual_md5": actual_md5,
                "provider_md5_match": md5_ok,
                "size_match": size_ok,
                "sha256": sha256,
                "request_url": request_url,
                "resolved_url": resolved_url,
            }
        )
        del payload

    gates = {
        **metadata_gates,
        "exact_file_count_11": len(records) == 11,
        "all_provider_md5_match": all_md5,
        "all_provider_sizes_match": all_size,
        "all_sha256_recorded": all_sha,
        "all_request_modes_exact": all_modes,
        "binary_content_parsed": False,
        "observed_residual_execution_remains_locked": True,
        "bsm_interpretation_remains_locked": True,
    }
    required_true = [
        "b4ritm_identity_release_exact",
        "exact_11file_representation_metadata",
        "exact_9_saved_original_2_direct",
        "sterile_authority_substitution_absent",
        "exact_file_count_11",
        "all_provider_md5_match",
        "all_provider_sizes_match",
        "all_sha256_recorded",
        "all_request_modes_exact",
        "observed_residual_execution_remains_locked",
        "bsm_interpretation_remains_locked",
    ]
    passed = all(gates[k] for k in required_true) and not gates["binary_content_parsed"]
    return {
        **common,
        "status": (
            "PASS_0105A4D_DEEPCORE_B4RITM_ORIGINAL_REPRESENTATION_BYTE_LOCK_NONDISCOVERY"
            if passed
            else "BLOCKED_0105A4D_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE"
        ),
        "files": records,
        "gates": gates,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/0105a4d"))
    parser.add_argument("--git-sha")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    raw = fetch_metadata()
    result = build_manifest(raw, git_sha=args.git_sha)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    manifest = args.output_dir / "deepcore_b4ritm_original_representation_byte_manifest.json"
    manifest.write_text(text, encoding="utf-8")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    (args.output_dir / "manifest_sha256.txt").write_text(digest + "\n", encoding="utf-8")
    print(text, end="")
    print(f"manifest_sha256={digest}")
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
