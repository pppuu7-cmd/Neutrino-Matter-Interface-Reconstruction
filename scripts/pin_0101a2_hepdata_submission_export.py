#!/usr/bin/env python3
"""Inventory the official HEPData original-submission export for NMIR 0101a.

This is transport/provenance discovery only.  It freezes the exact downloaded
submission-package bytes and member manifest, but it does not select a sterile
parameter region, confidence threshold, or combine MicroBooNE with IceCube.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import tarfile
import zipfile

INSPIRE_ID = "3088922"
VERSION = "1"
EXPORT_URL = f"https://www.hepdata.net/download/submission/ins{INSPIRE_ID}/{VERSION}/original"
HEPDATA_DOI = "10.17182/hepdata.166435.v1"


def hash_file(path: Path, algorithm: str = "sha256") -> str:
    h = hashlib.new(algorithm)
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _hash_stream(fp) -> str:
    h = hashlib.sha256()
    for chunk in iter(lambda: fp.read(1024 * 1024), b""):
        h.update(chunk)
    return h.hexdigest()


def _candidate(name: str) -> bool:
    low = name.lower()
    return any(token in low for token in ("chi", "grid", "sterile", "resource", "cov", "submission"))


def inventory_package(path: Path, git_sha: str | None = None) -> dict:
    members: list[dict] = []
    container = None

    if tarfile.is_tarfile(path):
        container = "tar"
        with tarfile.open(path, "r:*") as tf:
            for info in tf:
                if not info.isfile():
                    continue
                fp = tf.extractfile(info)
                if fp is None:
                    continue
                members.append(
                    {
                        "path": info.name,
                        "size": info.size,
                        "sha256": _hash_stream(fp),
                    }
                )
    elif zipfile.is_zipfile(path):
        container = "zip"
        with zipfile.ZipFile(path, "r") as zf:
            for info in zf.infolist():
                if info.is_dir():
                    continue
                with zf.open(info, "r") as fp:
                    digest = _hash_stream(fp)
                members.append(
                    {
                        "path": info.filename,
                        "size": info.file_size,
                        "sha256": digest,
                    }
                )
    else:
        return {
            "benchmark": "NMIR-BENCHMARK-0101A2",
            "status": "BLOCKED_0101A2_HEPDATA_EXPORT_UNRECOGNIZED_CONTAINER",
            "download_sha256": hash_file(path),
            "download_size": path.stat().st_size,
            "terminal_physics_execution_allowed": False,
            "joint_global_likelihood_claim_allowed": False,
            "git_sha": git_sha,
        }

    members.sort(key=lambda x: x["path"])
    manifest_bytes = (json.dumps(members, sort_keys=True, separators=(",", ":")) + "\n").encode()
    paths = [m["path"] for m in members]
    base_names = [Path(p).name.lower() for p in paths]
    submission_members = [p for p in paths if Path(p).name.lower() in {"submission.yaml", "submission.yml"}]
    yaml_members = [p for p in paths if Path(p).suffix.lower() in {".yaml", ".yml"}]
    candidate_members = [m for m in members if _candidate(m["path"])]

    gates = {
        "package_nonempty": len(members) > 0,
        "submission_yaml_present": len(submission_members) >= 1,
        "yaml_table_or_metadata_present": len(yaml_members) >= 1,
    }

    return {
        "benchmark": "NMIR-BENCHMARK-0101A2",
        "status": (
            "PASS_0101A2_HEPDATA_ORIGINAL_SUBMISSION_INVENTORIED_NONTERMINAL"
            if all(gates.values())
            else "BLOCKED_0101A2_HEPDATA_EXPORT_STRUCTURE_INCOMPLETE"
        ),
        "authority": {
            "hepdata_doi": HEPDATA_DOI,
            "inspire_id": INSPIRE_ID,
            "version": VERSION,
            "export_url": EXPORT_URL,
        },
        "package": {
            "container": container,
            "download_size": path.stat().st_size,
            "download_sha256": hash_file(path),
            "member_count": len(members),
            "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        },
        "submission_yaml_members": submission_members,
        "yaml_member_count": len(yaml_members),
        "candidate_resource_members": candidate_members,
        "member_manifest": members,
        "gates": gates,
        "parameter_region_selected": False,
        "confidence_threshold_selected": False,
        "joint_global_likelihood_claim_allowed": False,
        "terminal_physics_execution_allowed": False,
        "git_sha": git_sha,
        "terminal_next_step": (
            "freeze this exact package identity and manifest, then parse only the prospectively identified submission metadata/resource references needed to locate the released combined BNB+NuMI Delta-chi2 grid and confidence construction"
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--package", required=True, type=Path)
    p.add_argument("--output-dir", type=Path, default=Path("artifacts/0101a2"))
    p.add_argument("--git-sha")
    args = p.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result = inventory_package(args.package, args.git_sha)
    (args.output_dir / "hepdata_submission_export_discovery.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
