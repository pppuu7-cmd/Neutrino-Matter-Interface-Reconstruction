#!/usr/bin/env python3
"""0105a5b R1c: collect only frozen B4RITM coordinate-semantics authority evidence.

This program does NOT infer a coordinate mapping and therefore cannot emit an R1c PASS.
It fetches the frozen Dataverse B4RITM v1.0 metadata, verifies the requested release identity,
downloads only provider-listed text/documentation payloads, hashes them, and records literal
coordinate/binning evidence lines for subsequent strict classification against the preregistration.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

DOI = "10.7910/DVN/B4RITM"
FORBIDDEN_DOI = "10.7910/DVN/QKL28Z"
VERSION = "1.0"
API = "https://dataverse.harvard.edu/api"
TEXT_EXTENSIONS = {".txt", ".md", ".readme", ".csv", ".json", ".yaml", ".yml"}
EVIDENCE_TERMS = (
    "reco_energy", "reco energy", "reconstructed energy",
    "reco_coszen", "reco coszen", "reconstructed zenith", "coszen",
    "pid", "bin edge", "bin edges", "bin center", "bin centre", "binning",
)


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "NMIR-v2-0105a5b-r1c"})
    with urllib.request.urlopen(req, timeout=240) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "NMIR-v2-0105a5b-r1c"})
    with urllib.request.urlopen(req, timeout=240) as r:
        return r.read()


def version_url() -> str:
    pid = urllib.parse.quote(f"doi:{DOI}", safe="")
    return f"{API}/datasets/:persistentId/versions/{VERSION}?persistentId={pid}"


def documentation_candidate(label: str, content_type: str) -> bool:
    suffix = Path(label.lower()).suffix
    ct = (content_type or "").lower()
    name = label.lower()
    return (
        suffix in TEXT_EXTENSIONS
        or ct.startswith("text/")
        or "readme" in name
        or "description" in name
        or "documentation" in name
    )


def evidence_lines(text: str) -> list[str]:
    out: list[str] = []
    for line in text.splitlines():
        normalized = re.sub(r"\s+", " ", line).strip()
        low = normalized.lower()
        if normalized and any(term in low for term in EVIDENCE_TERMS):
            out.append(normalized[:2000])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--raw-dir", required=True)
    args = ap.parse_args()

    out_path = Path(args.output)
    raw_dir = Path(args.raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)

    meta = fetch_json(version_url())
    if meta.get("status") != "OK":
        result = {"status": "INFRASTRUCTURE_FAIL_0105A5B_R1C", "reason": "DATAVERSE_API_NOT_OK", "metadata": meta}
        out_path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
        return 2

    data = meta.get("data", {})
    version_number = str(data.get("versionNumber", ""))
    files = data.get("files", []) or []
    if version_number != VERSION:
        result = {
            "status": "BLOCKED_0105A5B_R1C_COORDINATE_SEMANTICS_AUTHORITY_INCOMPLETE",
            "reason": "FROZEN_RELEASE_VERSION_MISMATCH",
            "expected_version": VERSION,
            "actual_version": version_number,
        }
        out_path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
        return 3

    metadata_path = raw_dir / "b4ritm_v1_0_metadata.json"
    metadata_bytes = json.dumps(meta, indent=2, sort_keys=True).encode("utf-8")
    metadata_path.write_bytes(metadata_bytes)

    docs = []
    for item in files:
        df = item.get("dataFile", {}) or {}
        file_id = df.get("id")
        label = str(df.get("filename") or "")
        content_type = str(df.get("contentType") or "")
        if not file_id or not documentation_candidate(label, content_type):
            continue
        url = f"{API}/access/datafile/{int(file_id)}?format=original"
        payload = fetch_bytes(url)
        safe_name = f"{int(file_id)}_{Path(label).name}"
        (raw_dir / safe_name).write_bytes(payload)
        try:
            text = payload.decode("utf-8-sig")
            decode_ok = True
        except UnicodeDecodeError:
            text = ""
            decode_ok = False
        docs.append({
            "file_id": int(file_id),
            "filename": label,
            "content_type": content_type,
            "byte_count": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "provider_checksum": df.get("checksum"),
            "description": df.get("description", ""),
            "utf8_decoded": decode_ok,
            "coordinate_semantics_evidence_lines": evidence_lines(text) if decode_ok else [],
        })

    result = {
        "benchmark": "NMIR-V2-0105A5B-R1C-EVIDENCE",
        "dataset_doi": DOI,
        "forbidden_sterile_doi": FORBIDDEN_DOI,
        "frozen_version": VERSION,
        "metadata_sha256": hashlib.sha256(metadata_bytes).hexdigest(),
        "provider_file_count": len(files),
        "documentation_payload_count": len(docs),
        "documentation_payloads": docs,
        "status": "EVIDENCE_BUNDLE_ONLY_0105A5B_R1C_UNCLASSIFIED",
        "r1c_pass_declared": False,
        "oscillated_expectation_computed": False,
        "likelihood_computed": False,
        "nuisance_fit_executed": False,
        "observed_minus_null_residual_computed": False,
        "bsm_quantity_computed": False,
        "observed_bsm_residual_permission_percent": 0,
    }
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(result["status"])
    print(f"provider_file_count={len(files)}")
    print(f"documentation_payload_count={len(docs)}")
    print(f"metadata_sha256={result['metadata_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
