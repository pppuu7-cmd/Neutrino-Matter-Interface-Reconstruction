#!/usr/bin/env python3
"""Inspect the already-frozen Kato/Nagakura MESA 25 Msun emission archive.

This is archive/provenance discovery only.  It verifies the top-level MD5 frozen
in 0100c1, inventories the ZIP, identifies the light-curve member and spectrum
step members, and proves only filename/step consistency.  It does not choose a
terminal evolutionary snapshot and does not run neutrino propagation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import zipfile

EXPECTED_NAME = "MESA_25M.zip"
EXPECTED_MD5 = "a6c8a5dffc13d301dda139ad75a0db71"
SPECTRUM_RE = re.compile(r"^spectrum(\d+)\.dat$", re.IGNORECASE)


def hash_file(path: Path, algorithm: str) -> str:
    h = hashlib.new(algorithm)
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_stream(fp) -> str:
    h = hashlib.sha256()
    for chunk in iter(lambda: fp.read(1024 * 1024), b""):
        h.update(chunk)
    return h.hexdigest()


def numeric_rows(data: bytes) -> list[list[float]]:
    rows: list[list[float]] = []
    for raw in data.decode("utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        toks = line.replace("D", "E").replace("d", "e").split()
        try:
            vals = [float(x) for x in toks]
        except ValueError:
            continue
        if vals and all(math.isfinite(v) for v in vals):
            rows.append(vals)
    return rows


def parse_lightcurve(data: bytes) -> dict:
    rows = numeric_rows(data)
    if not rows:
        raise ValueError("no numeric lightcurve rows")
    if any(len(r) < 2 for r in rows):
        raise ValueError("lightcurve rows require at least step and time columns")
    steps: list[int] = []
    times: list[float] = []
    widths: set[int] = set()
    for row in rows:
        step_float = row[0]
        step = int(round(step_float))
        if abs(step_float - step) > 1e-9:
            raise ValueError(f"non-integral lightcurve step {step_float}")
        steps.append(step)
        times.append(row[1])
        widths.add(len(row))
    if len(set(steps)) != len(steps):
        raise ValueError("duplicate lightcurve step numbers")
    return {
        "row_count": len(rows),
        "column_counts": sorted(widths),
        "steps": steps,
        "step_min": min(steps),
        "step_max": max(steps),
        "time_to_bounce_s_min": min(times),
        "time_to_bounce_s_max": max(times),
    }


def inventory_archive(path: Path, git_sha: str | None = None) -> dict:
    observed_md5 = hash_file(path, "md5")
    if observed_md5 != EXPECTED_MD5:
        return {
            "benchmark": "NMIR-BENCHMARK-0100C2",
            "status": "BLOCKED_0100C2_EMISSION_ARCHIVE_HASH_MISMATCH",
            "expected_md5": EXPECTED_MD5,
            "observed_md5": observed_md5,
            "terminal_physics_execution_allowed": False,
            "git_sha": git_sha,
        }

    with zipfile.ZipFile(path, "r") as zf:
        infos = [i for i in zf.infolist() if not i.is_dir()]
        light_infos = [
            i for i in infos
            if Path(i.filename).name.lower().startswith("lightcurve")
            and Path(i.filename).suffix.lower() == ".dat"
        ]
        spectrum_pairs: list[tuple[int, zipfile.ZipInfo]] = []
        for info in infos:
            m = SPECTRUM_RE.match(Path(info.filename).name)
            if m:
                spectrum_pairs.append((int(m.group(1)), info))

        manifest_rows = [
            {
                "path": i.filename,
                "uncompressed_size": i.file_size,
                "compressed_size": i.compress_size,
                "crc32": f"{i.CRC:08x}",
            }
            for i in sorted(infos, key=lambda x: x.filename)
        ]
        manifest_bytes = (json.dumps(manifest_rows, sort_keys=True, separators=(",", ":")) + "\n").encode()

        gates = {
            "published_md5_matches": True,
            "exactly_one_lightcurve_member": len(light_infos) == 1,
            "spectrum_members_present": len(spectrum_pairs) > 0,
            "spectrum_step_names_unique": len({s for s, _ in spectrum_pairs}) == len(spectrum_pairs),
        }

        light = None
        mapping = None
        if len(light_infos) == 1:
            li = light_infos[0]
            data = zf.read(li)
            try:
                parsed = parse_lightcurve(data)
            except ValueError as exc:
                parsed = {"parse_error": str(exc)}
                gates["lightcurve_numeric_parse"] = False
            else:
                gates["lightcurve_numeric_parse"] = True
                light_steps = set(parsed.pop("steps"))
                spectrum_steps = sorted(s for s, _ in spectrum_pairs)
                orphan = [s for s in spectrum_steps if s not in light_steps]
                gates["every_spectrum_step_exists_in_lightcurve"] = not orphan
                mapping = {
                    "spectrum_step_count": len(spectrum_steps),
                    "spectrum_step_min": min(spectrum_steps) if spectrum_steps else None,
                    "spectrum_step_max": max(spectrum_steps) if spectrum_steps else None,
                    "orphan_spectrum_steps": orphan,
                    "filename_mapping_rule": "spectrum<integer_step>.dat -> lightcurve first-column step",
                }
            light = {
                "member_path": li.filename,
                "member_size_bytes": li.file_size,
                "member_sha256": hashlib.sha256(data).hexdigest(),
                "parsed": parsed,
            }
        else:
            gates["lightcurve_numeric_parse"] = False
            gates["every_spectrum_step_exists_in_lightcurve"] = False

    all_pass = all(gates.values())
    return {
        "benchmark": "NMIR-BENCHMARK-0100C2",
        "status": (
            "PASS_0100C2_EMISSION_ARCHIVE_INVENTORIED_NONTERMINAL"
            if all_pass else "BLOCKED_0100C2_EMISSION_ARCHIVE_STRUCTURE_UNRESOLVED"
        ),
        "archive": {
            "name": path.name,
            "expected_name": EXPECTED_NAME,
            "expected_md5": EXPECTED_MD5,
            "observed_md5": observed_md5,
            "sha256": hash_file(path, "sha256"),
            "file_count": len(manifest_rows),
            "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        },
        "lightcurve": light,
        "spectrum_mapping": mapping,
        "gates": gates,
        "snapshot_selection_performed": False,
        "snapshot_mapping_to_stellar_profile_closed": False,
        "terminal_physics_execution_allowed": False,
        "git_sha": git_sha,
        "terminal_next_step": (
            "freeze the discovered internal emission structure, then inspect the separately frozen 25 Msun stellar archive and establish an explicit released-metadata time/profile mapping before selecting any terminal snapshot"
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--archive", required=True, type=Path)
    p.add_argument("--output-dir", default=Path("artifacts/0100c2"), type=Path)
    p.add_argument("--git-sha")
    args = p.parse_args()
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    result = inventory_archive(args.archive, args.git_sha)
    (out / "emission_archive_discovery.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"].startswith("PASS_") else 2


if __name__ == "__main__":
    raise SystemExit(main())
