"""Frozen solar electron-density and production-distribution inputs for NMIR."""

from __future__ import annotations

import csv
import hashlib
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SolarMatterSource:
    model: str
    source_repo: str
    source_commit: str
    source_path: str
    source_blob_sha: str
    reference: str
    radius_column: int
    density_log10_column: int
    production_columns: dict[str, int]
    density_units: str
    notes: str


_COMPONENTS = ("pp", "pep", "hep", "Be7", "B8", "N13", "O15", "F17")


def _manifest_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "solar_matter_manifest.csv"


def load_solar_matter_manifest(path: str | Path | None = None) -> dict[str, SolarMatterSource]:
    p = Path(path) if path is not None else _manifest_path()
    out: dict[str, SolarMatterSource] = {}
    with p.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            model = row["model"].strip()
            if not model or model in out:
                raise ValueError(f"duplicate/empty solar model: {model!r}")
            commit = row["source_commit"].strip()
            blob = row["source_blob_sha"].strip()
            if len(commit) != 40 or len(blob) != 40:
                raise ValueError(f"invalid immutable git identity for {model}")
            production = {name: int(row[f"{name}_column"]) for name in _COMPONENTS}
            if len(set(production.values())) != len(production):
                raise ValueError(f"duplicate production columns for {model}")
            out[model] = SolarMatterSource(
                model=model,
                source_repo=row["source_repo"].strip(),
                source_commit=commit,
                source_path=row["source_path"].strip(),
                source_blob_sha=blob,
                reference=row["reference"].strip(),
                radius_column=int(row["radius_column"]),
                density_log10_column=int(row["density_log10_column"]),
                production_columns=production,
                density_units=row["density_units"].strip(),
                notes=row["notes"].strip(),
            )
    return out


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def verify_solar_matter_blob(model: str, data: bytes, manifest: dict[str, SolarMatterSource] | None = None) -> None:
    m = load_solar_matter_manifest() if manifest is None else manifest
    if model not in m:
        raise KeyError(model)
    actual = git_blob_sha1(data)
    expected = m[model].source_blob_sha
    if actual != expected:
        raise ValueError(f"solar-matter blob mismatch for {model}: expected {expected}, got {actual}")


def raw_pinned_url(model: str, manifest: dict[str, SolarMatterSource] | None = None) -> str:
    m = load_solar_matter_manifest() if manifest is None else manifest
    src = m[model]
    return f"https://raw.githubusercontent.com/{src.source_repo}/{src.source_commit}/{src.source_path}"


def required_components() -> tuple[str, ...]:
    return _COMPONENTS
