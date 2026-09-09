#!/usr/bin/env python3
"""Pin nonterminal metadata inventories for NMIR-v2 gate 0105a1.

No observed residual or BSM statistic is evaluated here.
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

ICECUBE_DOI = "10.7910/DVN/B4RITM"
ICECUBE_API_URL = (
    "https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId="
    + urllib.parse.quote(f"doi:{ICECUBE_DOI}", safe="")
)
COHERENT_RELEASES = {
    "csi": {"record_id": 1228631, "doi": "10.5281/zenodo.1228631"},
    "ar": {"record_id": 3903810, "doi": "10.5281/zenodo.3903810"},
}

TRANSIENT_HTTP_CODES = frozenset({429, 500, 502, 503, 504})
RETRY_DELAYS_SECONDS = (2, 4, 8)
MAX_FETCH_ATTEMPTS = 1 + len(RETRY_DELAYS_SECONDS)


def fetch_bytes(url: str) -> bytes:
    host = urllib.parse.urlsplit(url).netloc
    last_error: BaseException | None = None
    for attempt in range(1, MAX_FETCH_ATTEMPTS + 1):
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 NMIR/0105a1 authority metadata pin",
                "Accept": "application/json, text/plain;q=0.9, */*;q=0.8",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code not in TRANSIENT_HTTP_CODES:
                raise RuntimeError(
                    f"BLOCKED_0105A1_METADATA_HTTP_{exc.code} host={host} attempt={attempt}"
                ) from exc
        except (urllib.error.URLError, TimeoutError, socket.timeout) as exc:
            last_error = exc

        if attempt < MAX_FETCH_ATTEMPTS:
            time.sleep(RETRY_DELAYS_SECONDS[attempt - 1])

    raise RuntimeError(
        f"BLOCKED_0105A1_METADATA_TRANSPORT host={host} attempts={MAX_FETCH_ATTEMPTS}"
    ) from last_error


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(data: bytes) -> dict:
    obj = json.loads(data.decode("utf-8"))
    if not isinstance(obj, dict):
        raise ValueError("metadata root must be a JSON object")
    return obj


def normalize_dataverse(raw: bytes) -> dict:
    obj = load_json(raw)
    data = obj.get("data") or {}
    latest = data.get("latestVersion") or {}
    files = []
    for item in latest.get("files") or []:
        data_file = item.get("dataFile") or {}
        checksum = data_file.get("checksum") or {}
        files.append(
            {
                "id": data_file.get("id"),
                "filename": data_file.get("filename"),
                "content_type": data_file.get("contentType"),
                "filesize": data_file.get("filesize"),
                "persistent_id": data_file.get("persistentId"),
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


def normalize_zenodo(raw: bytes) -> dict:
    obj = load_json(raw)
    metadata = obj.get("metadata") or {}
    files = []
    for item in obj.get("files") or []:
        links = item.get("links") or {}
        files.append(
            {
                "id": item.get("id"),
                "key": item.get("key"),
                "size": item.get("size"),
                "checksum": item.get("checksum"),
                "self_link": links.get("self"),
            }
        )
    return {
        "record_id": obj.get("id"),
        "doi": obj.get("doi") or metadata.get("doi"),
        "conceptdoi": obj.get("conceptdoi") or metadata.get("conceptdoi"),
        "title": metadata.get("title"),
        "publication_date": metadata.get("publication_date"),
        "created": obj.get("created"),
        "updated": obj.get("updated"),
        "file_count": len(files),
        "files": files,
    }


def _doi_consistent(returned: str | None, expected: str, record_id: int | None = None) -> bool:
    if returned:
        return returned.lower().strip() == expected.lower()
    return record_id is not None and expected.lower().endswith(str(record_id))


def build_result(icecube_raw: bytes, zenodo_raw: dict[str, bytes], git_sha: str | None) -> dict:
    ice = normalize_dataverse(icecube_raw)
    coh = {name: normalize_zenodo(raw) for name, raw in zenodo_raw.items()}

    ice_files_valid = all(
        bool(f.get("filename"))
        and isinstance(f.get("filesize"), int)
        and f["filesize"] > 0
        and bool(f.get("checksum_value"))
        for f in ice["files"]
    )
    persistent_text = " ".join(
        str(x or "") for x in (ice.get("persistent_url"), ice.get("identifier"), ice.get("authority"))
    ).lower()
    ice_identity_ok = "b4ritm" in persistent_text or ICECUBE_DOI.lower() in persistent_text

    zenodo_gates = {}
    for name, frozen in COHERENT_RELEASES.items():
        summary = coh[name]
        file_valid = all(
            bool(f.get("key"))
            and isinstance(f.get("size"), int)
            and f["size"] > 0
            and bool(f.get("checksum"))
            for f in summary["files"]
        )
        zenodo_gates[f"{name}_record_identity_ok"] = (
            summary.get("record_id") == frozen["record_id"]
            and _doi_consistent(summary.get("doi"), frozen["doi"], frozen["record_id"])
        )
        zenodo_gates[f"{name}_inventory_nonempty"] = summary["file_count"] > 0
        zenodo_gates[f"{name}_files_have_size_and_checksum"] = file_valid

    gates = {
        "icecube_dataverse_api_ok": ice.get("api_status") == "OK",
        "icecube_identity_ok": ice_identity_ok,
        "icecube_inventory_nonempty": ice["file_count"] > 0,
        "icecube_files_have_size_and_checksum": ice_files_valid,
        **zenodo_gates,
        "observed_residual_execution_remains_locked": True,
        "joint_likelihood_claim_remains_locked": True,
    }

    return {
        "benchmark": "NMIR-V2-0105A1",
        "status": (
            "PASS_0105A1_CROSS_REGIME_AUTHORITY_METADATA_INVENTORY_NONTERMINAL"
            if all(gates.values())
            else "BLOCKED_0105A1_AUTHORITY_METADATA_INCOMPLETE"
        ),
        "icecube_deepcore": {
            "expected_doi": ICECUBE_DOI,
            "metadata_url": ICECUBE_API_URL,
            "raw_metadata_sha256": sha256_bytes(icecube_raw),
            "inventory": ice,
        },
        "coherent": {
            name: {
                "expected_record_id": frozen["record_id"],
                "expected_doi": frozen["doi"],
                "metadata_url": f"https://zenodo.org/api/records/{frozen['record_id']}",
                "raw_metadata_sha256": sha256_bytes(zenodo_raw[name]),
                "inventory": coh[name],
            }
            for name, frozen in COHERENT_RELEASES.items()
        },
        "gates": gates,
        "observed_residual_execution_allowed": False,
        "joint_likelihood_claim_allowed": False,
        "consumed_byte_sha256_lock_complete": False,
        "git_sha": git_sha,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/0105a1"))
    parser.add_argument("--icecube-json", type=Path)
    parser.add_argument("--csi-json", type=Path)
    parser.add_argument("--ar-json", type=Path)
    parser.add_argument("--git-sha")
    args = parser.parse_args()

    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    ice_raw = args.icecube_json.read_bytes() if args.icecube_json else fetch_bytes(ICECUBE_API_URL)
    raw_by_name = {}
    for name, frozen in COHERENT_RELEASES.items():
        fixture = getattr(args, f"{name}_json")
        url = f"https://zenodo.org/api/records/{frozen['record_id']}"
        raw_by_name[name] = fixture.read_bytes() if fixture else fetch_bytes(url)

    (out / "icecube_deepcore_dataverse_metadata.json").write_bytes(ice_raw)
    for name, raw in raw_by_name.items():
        (out / f"coherent_{name}_zenodo_metadata.json").write_bytes(raw)

    result = build_result(ice_raw, raw_by_name, args.git_sha)
    normalized = json.dumps(result, indent=2, sort_keys=True) + "\n"
    (out / "cross_regime_authority_metadata_inventory.json").write_text(normalized, encoding="utf-8")
    (out / "normalized_inventory_sha256.txt").write_text(
        hashlib.sha256(normalized.encode("utf-8")).hexdigest() + "\n", encoding="utf-8"
    )
    print(normalized, end="")
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
