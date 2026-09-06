"""Provenance-frozen solar-neutrino spectral input metadata for NMIR.

This module deliberately separates *spectral provenance* from spectral-number
normalization. Continuum/profile tables are referenced by an immutable upstream
repository commit plus blob SHA. Line rows encode bookkeeping line energies and
weights. Precision capture integration must materialize/verify the pinned table
bytes before use; silently substituting a different spectrum is forbidden.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SpectrumSource:
    component: str
    kind: str
    reference: str
    source_repo: str | None
    source_commit: str | None
    source_path: str | None
    source_blob_sha: str | None
    line_energy_mev: float | None
    line_weight: float | None
    notes: str


_ALLOWED_KINDS = {"continuum", "profile", "line"}


def _manifest_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "solar_spectrum_manifest.csv"


def load_spectrum_manifest(path: str | Path | None = None) -> dict[str, SpectrumSource]:
    p = Path(path) if path is not None else _manifest_path()
    out: dict[str, SpectrumSource] = {}
    with p.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            kind = row["kind"].strip()
            if kind not in _ALLOWED_KINDS:
                raise ValueError(f"unsupported spectrum kind: {kind}")
            component = row["component"].strip()
            if not component or component in out:
                raise ValueError(f"duplicate/empty component: {component!r}")
            src_repo = row["source_repo"].strip() or None
            src_commit = row["source_commit"].strip() or None
            src_path = row["source_path"].strip() or None
            src_sha = row["source_blob_sha"].strip() or None
            if kind in {"continuum", "profile"}:
                if not all((src_repo, src_commit, src_path, src_sha)):
                    raise ValueError(f"unpinned external spectrum: {component}")
                if len(src_commit) != 40 or len(src_sha) != 40:
                    raise ValueError(f"invalid git identity for {component}")
            e = float(row["line_energy_mev"]) if row["line_energy_mev"].strip() else None
            w = float(row["line_weight"]) if row["line_weight"].strip() else None
            if kind == "line" and (e is None or w is None or e <= 0 or not 0 < w <= 1):
                raise ValueError(f"invalid line convention for {component}")
            out[component] = SpectrumSource(
                component=component,
                kind=kind,
                reference=row["reference"].strip(),
                source_repo=src_repo,
                source_commit=src_commit,
                source_path=src_path,
                source_blob_sha=src_sha,
                line_energy_mev=e,
                line_weight=w,
                notes=row["notes"].strip(),
            )
    return out


def be7_bookkeeping_weight_sum(manifest: dict[str, SpectrumSource] | None = None) -> float:
    m = load_spectrum_manifest() if manifest is None else manifest
    return m["Be7_862"].line_weight + m["Be7_384"].line_weight  # type: ignore[operator]


def pinned_continuum_components(manifest: dict[str, SpectrumSource] | None = None) -> tuple[str, ...]:
    m = load_spectrum_manifest() if manifest is None else manifest
    return tuple(sorted(k for k, v in m.items() if v.kind == "continuum"))
