#!/usr/bin/env python3
"""NMIR 0100c1d: prospectively frozen restricted mapping-evidence audit.

This script may read content only from the six archive members frozen in
research/locks/0100c1c_presn_auxiliary_manifest_lock.json. It does not run
oscillation physics and it never selects a stellar profile.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tarfile
import time
import urllib.error
import urllib.request
from pathlib import Path

DOWNLOAD_URL = "https://zenodo.org/api/records/20822085/files/pre_sn_neutrino.tar.gz/content"
EXPECTED_SIZE = 17_344_435
EXPECTED_MD5 = "e7282d0a7241b60a602e82d5e0e9f47f"
EXPECTED_SHA256 = "2aca20c46ab7fb0f7d2253da13a224d24453970b19470acc3e69df84909edc1b"
EXPECTED_MEMBER_COUNT = 44

CANDIDATES = {
    "pre_sn_neutrino/README.rst": (1726, "a97e371db4c82ed9cb5b1a2c5a7c1e43166db0037394df46461eb76b8861007f"),
    "pre_sn_neutrino/history_columns.list": (33551, "987dd88721f7751a17876541126854431448f150aa434a5077809fd06fefa232"),
    "pre_sn_neutrino/profile_columns.list": (29301, "1174c3591d72453fc1f54895003ecfbaeec2f7d0e4b682d65aaebab388122147"),
    "pre_sn_neutrino/inlist_common": (13204, "de5aa4ccb5a31b9f6b41b4367f0ed30991075e3d0e03facc6a66f1fb1714be92"),
    "pre_sn_neutrino/inlist_to_cc": (3391, "be7e528c6a5643d56c5a67e4e702c05a3a53c59da465b4e852a344d8a8a0e759"),
    "pre_sn_neutrino/src/run_star_extras.f90": (7730, "e13aba921d975be80e7a3c8046a1d31050dc3f2ddc01f3ba0fa2e777c87dbecd"),
}

EMISSION = re.compile(r"spectrum|lightcurve|core\s*bounce|core_bounce|time\s+to\s+bounce|pre_sn|presn|neutrino", re.I)
SNAPSHOT = re.compile(r"profile_number|profile\s+number|model_number|model\s+number|star_age|star\s+age|profile|save_model|saved\s+model", re.I)
RELATION = re.compile(r"step|index|time|number|write|save|history|when", re.I)
WINDOW_RADIUS = 5


def digest(path: Path, name: str) -> str:
    h = hashlib.new(name)
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def acquire(url: str, out: Path, attempts: int = 5) -> None:
    """Fetch the same frozen URL with bounded transport retries.

    Retrying 502/503/504/timeouts changes no authority identity or scientific
    criterion. A temporary file is promoted only after a complete response so
    a failed transport cannot masquerade as a cached authoritative archive.
    """
    tmp = out.with_suffix(out.suffix + ".partial")
    retryable_codes = {502, 503, 504}
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        tmp.unlink(missing_ok=True)
        req = urllib.request.Request(url, headers={"User-Agent": "NMIR-authority-audit/0100c1d"})
        try:
            with urllib.request.urlopen(req, timeout=180) as r, tmp.open("wb") as w:
                while True:
                    chunk = r.read(1024 * 1024)
                    if not chunk:
                        break
                    w.write(chunk)
            tmp.replace(out)
            return
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code not in retryable_codes or attempt == attempts:
                raise
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt == attempts:
                raise
        finally:
            if not out.exists():
                tmp.unlink(missing_ok=True)
        time.sleep(min(2 ** (attempt - 1), 16))
    assert last_error is not None
    raise last_error


def matching_windows(text: str) -> list[dict]:
    lines = text.splitlines()
    windows: list[dict] = []
    seen: set[tuple[int, int]] = set()
    for center in range(len(lines)):
        start = max(0, center - WINDOW_RADIUS)
        end = min(len(lines), center + WINDOW_RADIUS + 1)
        key = (start, end)
        if key in seen:
            continue
        block = "\n".join(lines[start:end])
        if EMISSION.search(block) and SNAPSHOT.search(block) and RELATION.search(block):
            seen.add(key)
            windows.append({
                "start_line": start + 1,
                "end_line": end,
                "text": block,
            })
    return windows


def run(archive: Path) -> dict:
    assert archive.stat().st_size == EXPECTED_SIZE, (archive.stat().st_size, EXPECTED_SIZE)
    assert digest(archive, "md5") == EXPECTED_MD5
    assert digest(archive, "sha256") == EXPECTED_SHA256

    results = []
    total_windows = 0
    with tarfile.open(archive, "r:gz") as tf:
        members = tf.getmembers()  # metadata inventory only; no non-candidate contents are extracted/read.
        assert len(members) == EXPECTED_MEMBER_COUNT, (len(members), EXPECTED_MEMBER_COUNT)
        by_name = {m.name: m for m in members}
        assert len(by_name) == len(members), "duplicate archive member names"
        for name, (expected_size, expected_sha) in CANDIDATES.items():
            member = by_name[name]
            assert member.isfile()
            assert member.size == expected_size, (name, member.size, expected_size)
            fh = tf.extractfile(member)
            assert fh is not None
            raw = fh.read()
            assert len(raw) == expected_size
            observed_sha = hashlib.sha256(raw).hexdigest()
            assert observed_sha == expected_sha, (name, observed_sha, expected_sha)
            text = raw.decode("utf-8", errors="strict")
            windows = matching_windows(text)
            total_windows += len(windows)
            results.append({
                "path": name,
                "size": len(raw),
                "sha256": observed_sha,
                "machine_candidate_window_count": len(windows),
                "machine_candidate_windows": windows,
            })

    status = (
        "BLOCKED_0100C_MAPPING_AUTHORITY_UNRESOLVED_AFTER_RESTRICTED_READ"
        if total_windows == 0
        else "REVIEW_REQUIRED_0100C_EXPLICIT_MAPPING_CANDIDATE_NONTERMINAL"
    )
    return {
        "benchmark": "NMIR-BENCHMARK-0100C1D",
        "archive": {
            "size": archive.stat().st_size,
            "md5": EXPECTED_MD5,
            "sha256": EXPECTED_SHA256,
            "member_count": EXPECTED_MEMBER_COUNT,
        },
        "content_read_allowlist": sorted(CANDIDATES),
        "content_read_count": len(CANDIDATES),
        "window_radius_lines": WINDOW_RADIUS,
        "machine_candidate_window_count": total_windows,
        "candidates": results,
        "classification": status,
        "snapshot_mapping_authority_closed": False,
        "snapshot_selected": False,
        "terminal_msw_execution_allowed": False,
        "note": "A nonzero candidate count is review-required only; this machine pass is not allowed to promote a candidate to mapping PASS.",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", type=Path)
    ap.add_argument("--out", type=Path, default=Path("artifacts/0100c1d/restricted_mapping_evidence.json"))
    args = ap.parse_args()
    archive = args.archive or Path("artifacts/0100c1d/pre_sn_neutrino.tar.gz")
    archive.parent.mkdir(parents=True, exist_ok=True)
    if not archive.exists():
        acquire(DOWNLOAD_URL, archive)
    report = run(archive)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
