#!/usr/bin/env python3
"""Inventory the prospectively frozen Kato/Nagakura pre_sn_neutrino auxiliary archive.

The first pass records only archive/member identities and filename-based mapping
candidates. It deliberately does not use file contents to choose a stellar
snapshot or terminal neutrino spectrum.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import tarfile

EXPECTED_MD5 = "e7282d0a7241b60a602e82d5e0e9f47f"


def hash_file(path: Path, alg: str) -> str:
    h = hashlib.new(alg)
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def stream_sha256(fp) -> str:
    h = hashlib.sha256()
    for chunk in iter(lambda: fp.read(1024 * 1024), b""):
        h.update(chunk)
    return h.hexdigest()


def is_mapping_candidate(name: str) -> bool:
    low = name.lower()
    return any(token in low for token in (
        "profile", "history", "index", "mesa", "step", "time", "bounce",
        "neutrino", "inlist", "readme", "run_star", "log", "output"
    ))


def inventory(path: Path, git_sha: str | None = None) -> dict:
    md5 = hash_file(path, "md5")
    if md5 != EXPECTED_MD5:
        return {
            "benchmark": "NMIR-BENCHMARK-0100C1B",
            "status": "BLOCKED_0100C1B_AUXILIARY_ARCHIVE_HASH_MISMATCH",
            "expected_md5": EXPECTED_MD5,
            "observed_md5": md5,
            "terminal_physics_execution_allowed": False,
            "git_sha": git_sha,
        }
    if not tarfile.is_tarfile(path):
        return {
            "benchmark": "NMIR-BENCHMARK-0100C1B",
            "status": "BLOCKED_0100C1B_AUXILIARY_ARCHIVE_NOT_TAR",
            "observed_md5": md5,
            "terminal_physics_execution_allowed": False,
            "git_sha": git_sha,
        }

    members = []
    with tarfile.open(path, "r:*") as tf:
        for info in tf:
            if not info.isfile():
                continue
            fp = tf.extractfile(info)
            if fp is None:
                continue
            members.append({
                "path": info.name,
                "size": info.size,
                "sha256": stream_sha256(fp),
            })
    members.sort(key=lambda x: x["path"])
    manifest_bytes = (json.dumps(members, sort_keys=True, separators=(",", ":")) + "\n").encode()
    candidates = [m for m in members if is_mapping_candidate(m["path"])]
    gates = {
        "published_md5_matches": True,
        "archive_nonempty": len(members) > 0,
        "mapping_candidate_names_present": len(candidates) > 0,
    }
    return {
        "benchmark": "NMIR-BENCHMARK-0100C1B",
        "status": (
            "PASS_0100C1B_AUXILIARY_MANIFEST_LOCK_DISCOVERY_NONTERMINAL"
            if all(gates.values()) else
            "BLOCKED_0100C1B_AUXILIARY_MANIFEST_NO_MAPPING_CANDIDATES"
        ),
        "archive": {
            "expected_md5": EXPECTED_MD5,
            "observed_md5": md5,
            "sha256": hash_file(path, "sha256"),
            "member_count": len(members),
            "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        },
        "mapping_candidate_members": candidates,
        "member_manifest": members,
        "gates": gates,
        "content_based_snapshot_selection_performed": False,
        "snapshot_mapping_authority_closed": False,
        "terminal_physics_execution_allowed": False,
        "git_sha": git_sha,
        "terminal_next_step": "freeze this exact auxiliary manifest before reading candidate text files for an author-supplied spectrum-step to MESA-profile mapping rule",
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--archive", required=True, type=Path)
    p.add_argument("--output-dir", type=Path, default=Path("artifacts/0100c1b"))
    p.add_argument("--git-sha")
    args = p.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    result = inventory(args.archive, args.git_sha)
    (args.output_dir / "presn_auxiliary_manifest_discovery.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
