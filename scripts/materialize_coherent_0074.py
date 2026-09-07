#!/usr/bin/env python3
"""Materialize official COHERENT 0074 Zenodo packages with byte-level hashes.

This script is input/provenance infrastructure only. It performs no likelihood
calculation and produces no B-L exclusion result.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sys
import urllib.request

RECORDS = {
    "argon_analysis_a": "3903810",
    "csi_first_observation": "1228631",
}


def digest(path: Path, algorithm: str) -> str:
    h = hashlib.new(algorithm)
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "NMIR-0074-materializer/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def download(url: str, out: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "NMIR-0074-materializer/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp, out.open("wb") as fh:
        while True:
            chunk = resp.read(1024 * 1024)
            if not chunk:
                break
            fh.write(chunk)


def materialize(label: str, record_id: str, root: Path) -> dict:
    api = f"https://zenodo.org/api/records/{record_id}"
    meta = get_json(api)
    files = meta.get("files") or []
    if not files:
        raise RuntimeError(f"Zenodo record {record_id} exposed no files")

    outdir = root / label
    outdir.mkdir(parents=True, exist_ok=True)
    rows = []
    for entry in files:
        key = entry["key"]
        links = entry.get("links") or {}
        url = links.get("content") or links.get("self")
        if not url:
            raise RuntimeError(f"No download URL for {record_id}:{key}")
        out = outdir / key
        out.parent.mkdir(parents=True, exist_ok=True)
        download(url, out)

        sha256 = digest(out, "sha256")
        md5 = digest(out, "md5")
        checksum = entry.get("checksum") or ""
        if checksum.startswith("md5:") and md5 != checksum.split(":", 1)[1]:
            raise RuntimeError(f"MD5 mismatch for {record_id}:{key}")
        expected_size = entry.get("size")
        actual_size = out.stat().st_size
        if expected_size is not None and actual_size != expected_size:
            raise RuntimeError(
                f"Size mismatch for {record_id}:{key}: {actual_size} != {expected_size}"
            )
        rows.append(
            {
                "key": key,
                "size_bytes": actual_size,
                "zenodo_checksum": checksum,
                "md5": md5,
                "sha256": sha256,
                "download_url": url,
            }
        )

    metadata = meta.get("metadata") or {}
    return {
        "label": label,
        "requested_record_id": record_id,
        "resolved_record_id": str(meta.get("id", record_id)),
        "conceptrecid": str(meta.get("conceptrecid", "")),
        "doi": metadata.get("doi") or meta.get("doi"),
        "title": metadata.get("title"),
        "publication_date": metadata.get("publication_date"),
        "version": metadata.get("version"),
        "record_api": api,
        "files": rows,
    }


def main() -> int:
    root = Path(os.environ.get("NMIR_0074_OUT", "artifacts/coherent_0074"))
    root.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema": "nmir.coherent_0074.materialization.v1",
        "scientific_scope": "primary input bytes only; no likelihood or B-L scan",
        "records": [],
    }
    for label, record_id in RECORDS.items():
        manifest["records"].append(materialize(label, record_id, root))
    manifest_path = root / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(manifest_path.read_text(), end="")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"NMIR_0074_MATERIALIZATION_FAIL: {exc}", file=sys.stderr)
        raise
