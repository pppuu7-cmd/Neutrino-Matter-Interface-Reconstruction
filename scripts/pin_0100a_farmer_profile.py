#!/usr/bin/env python3
"""Pin one authoritative Farmer et al. MESA profile for NMIR benchmark 0100a.

This script is provenance/validation infrastructure only. It never enables a terminal
physics result. The archive identity and deterministic model-selection contract are frozen
in research/prereg/0100a_farmer_source_profile_pinning.md.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path
import tarfile
from typing import Iterable

DATASET_DOI = "10.5281/zenodo.2641723"
DATASET_RECORD_URL = "https://zenodo.org/records/2641723"
ARCHIVE_NAME = "25_final_profiles.tar.gz"
ARCHIVE_URL = "https://zenodo.org/records/2641723/files/25_final_profiles.tar.gz?download=1"
EXPECTED_ARCHIVE_MD5 = "762af1b62365fbe15c102fbf6f2f9142"
MODEL_TOKEN = "25_79_0p005_ml"
PARSER_VERSION = "0100a-v1"
R_SUN_KM = 695700.0

RADIUS_ALIASES = ("radius_km", "radius_cm", "radius", "logr")
RHO_ALIASES = ("rho", "logrho")
YE_ALIASES = ("ye", "electron_fraction", "electronfraction")


def hash_file(path: Path, algorithm: str) -> str:
    h = hashlib.new(algorithm)
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _norm(name: str) -> str:
    return name.strip().strip("\"'").replace("-", "_").lower()


def _find_alias(names: list[str], aliases: Iterable[str]) -> tuple[int, str] | None:
    normalized = [_norm(n) for n in names]
    for alias in aliases:
        a = _norm(alias)
        if a in normalized:
            idx = normalized.index(a)
            return idx, names[idx]
    return None


def _all_float(tokens: list[str]) -> bool:
    try:
        for t in tokens:
            float(t.replace("D", "E").replace("d", "e"))
        return True
    except ValueError:
        return False


def _float(token: str) -> float:
    return float(token.replace("D", "E").replace("d", "e"))


def parse_mesa_profile(data: bytes) -> dict:
    text = data.decode("utf-8", errors="replace")
    lines = text.splitlines()

    candidates: list[tuple[int, list[str], tuple[int, str], tuple[int, str], tuple[int, str]]] = []
    for i, raw in enumerate(lines):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        names = stripped.split()
        r = _find_alias(names, RADIUS_ALIASES)
        rho = _find_alias(names, RHO_ALIASES)
        ye = _find_alias(names, YE_ALIASES)
        if r and rho and ye:
            candidates.append((i, names, r, rho, ye))

    if not candidates:
        raise ValueError("required MESA radius/density/Ye header not found")

    parsed_variants: list[dict] = []
    for header_i, names, r_info, rho_info, ye_info in candidates:
        rows: list[list[float]] = []
        started = False
        for raw in lines[header_i + 1 :]:
            stripped = raw.strip()
            if not stripped or stripped.startswith("#"):
                if started:
                    continue
                continue
            tokens = stripped.split()
            if len(tokens) < len(names) or not _all_float(tokens[: len(names)]):
                if started:
                    break
                continue
            started = True
            rows.append([_float(x) for x in tokens[: len(names)]])

        if len(rows) < 32:
            continue

        r_idx, r_name = r_info
        rho_idx, rho_name = rho_info
        ye_idx, ye_name = ye_info

        normalized: list[tuple[float, float, float]] = []
        for row in rows:
            r_raw, rho_raw, ye_raw = row[r_idx], row[rho_idx], row[ye_idx]
            r_key = _norm(r_name)
            rho_key = _norm(rho_name)

            if r_key == "radius_km":
                radius_km = r_raw
                r_transform = "identity_km"
            elif r_key == "radius_cm":
                radius_km = r_raw / 1.0e5
                r_transform = "cm_to_km"
            elif r_key == "radius":
                radius_km = r_raw * R_SUN_KM
                r_transform = "mesa_radius_Rsun_to_km"
            elif r_key == "logr":
                radius_km = (10.0 ** r_raw) * R_SUN_KM
                r_transform = "mesa_log10_R_Rsun_to_km"
            else:
                raise AssertionError(r_name)

            if rho_key == "rho":
                rho = rho_raw
                rho_transform = "identity_g_cm3"
            elif rho_key == "logrho":
                rho = 10.0 ** rho_raw
                rho_transform = "10pow_logrho_g_cm3"
            else:
                raise AssertionError(rho_name)

            normalized.append((radius_km, rho, ye_raw))

        normalized.sort(key=lambda x: x[0])
        finite = all(all(math.isfinite(v) for v in row) for row in normalized)
        strictly_increasing = all(normalized[i + 1][0] > normalized[i][0] for i in range(len(normalized) - 1))
        valid_ranges = all(r >= 0.0 and rho > 0.0 and 0.0 < ye <= 1.0 for r, rho, ye in normalized)

        gates = {
            "minimum_zone_count": len(normalized) >= 32,
            "finite_values": finite,
            "strictly_increasing_radius_after_canonical_sort": strictly_increasing,
            "physical_ranges": valid_ranges,
        }
        if all(gates.values()):
            parsed_variants.append(
                {
                    "header_line": header_i + 1,
                    "source_columns": {"radius": r_name, "rho": rho_name, "ye": ye_name},
                    "transformations": {"radius": r_transform, "rho": rho_transform, "ye": "identity"},
                    "rows": normalized,
                    "gates": gates,
                }
            )

    if len(parsed_variants) != 1:
        raise ValueError(f"expected exactly one valid MESA table in member, found {len(parsed_variants)}")
    return parsed_variants[0]


def scan_archive(archive_path: Path) -> list[dict]:
    accepted: list[dict] = []
    with tarfile.open(archive_path, mode="r:gz") as tf:
        for member in tf:
            if not member.isfile() or MODEL_TOKEN not in member.name:
                continue
            extracted = tf.extractfile(member)
            if extracted is None:
                continue
            data = extracted.read()
            try:
                parsed = parse_mesa_profile(data)
            except (ValueError, OverflowError):
                continue
            accepted.append(
                {
                    "member_path": member.name,
                    "member_size_bytes": member.size,
                    "member_sha256": sha256_bytes(data),
                    "parsed": parsed,
                }
            )
    return accepted


def summarize(rows: list[tuple[float, float, float]]) -> dict:
    radii = [x[0] for x in rows]
    rhos = [x[1] for x in rows]
    yes = [x[2] for x in rows]
    return {
        "zone_count": len(rows),
        "radius_km_min": min(radii),
        "radius_km_max": max(radii),
        "rho_g_cm3_min": min(rhos),
        "rho_g_cm3_max": max(rhos),
        "ye_min": min(yes),
        "ye_max": max(yes),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--output-dir", default=Path("artifacts/0100a"), type=Path)
    args = parser.parse_args()

    outdir: Path = args.output_dir
    outdir.mkdir(parents=True, exist_ok=True)

    observed_md5 = hash_file(args.archive, "md5")
    if observed_md5 != EXPECTED_ARCHIVE_MD5:
        raise SystemExit(
            f"BLOCKED_0100A_ARCHIVE_HASH_MISMATCH expected={EXPECTED_ARCHIVE_MD5} observed={observed_md5}"
        )

    accepted = scan_archive(args.archive)
    if not accepted:
        raise SystemExit("BLOCKED_0100A_PROFILE_MEMBER_NOT_FOUND")
    if len(accepted) > 1:
        names = [x["member_path"] for x in accepted]
        raise SystemExit(f"BLOCKED_0100A_AMBIGUOUS_ARCHIVE_MEMBER candidates={names}")

    selected = accepted[0]
    parsed = selected.pop("parsed")
    rows = parsed.pop("rows")

    csv_path = outdir / "source_profile.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["radius_km", "rho_g_cm3", "ye"])
        for r, rho, ye in rows:
            writer.writerow([f"{r:.17g}", f"{rho:.17g}", f"{ye:.17g}"])

    lock = {
        "benchmark": "NMIR-BENCHMARK-0100A",
        "status": "PASS_0100A_PROFILE_MEMBER_PINNED_NONTERMINAL",
        "dataset": {"doi": DATASET_DOI, "record_url": DATASET_RECORD_URL},
        "archive": {
            "name": ARCHIVE_NAME,
            "url": ARCHIVE_URL,
            "expected_md5": EXPECTED_ARCHIVE_MD5,
            "observed_md5": observed_md5,
        },
        "model_token": MODEL_TOKEN,
        "selected_member": selected,
        "source_table": parsed,
        "summary": summarize(rows),
        "normalized_csv_sha256": hash_file(csv_path, "sha256"),
        "parser_version": PARSER_VERSION,
        "git_sha": os.environ.get("GITHUB_SHA"),
        "terminal_physics_execution_allowed": False,
        "terminal_next_step": "freeze exact member path/hash and normalized CSV hash in a prospective 0100b lock before terminal MSW execution",
    }

    lock_path = outdir / "source_profile_lock.json"
    lock_path.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(lock, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
