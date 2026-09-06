"""Provenance-frozen solar-neutrino spectral inputs for NMIR.

Continuum/profile tables are identified by immutable upstream repository commit
plus exact git blob SHA. They may be materialized on demand, but are accepted
only if the downloaded bytes reproduce the frozen blob identity exactly.
"""

from __future__ import annotations

import csv
import hashlib
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


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
BlobFetcher = Callable[[str], bytes]


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


def pinned_blob_components(manifest: dict[str, SpectrumSource] | None = None) -> tuple[str, ...]:
    m = load_spectrum_manifest() if manifest is None else manifest
    return tuple(sorted(k for k, v in m.items() if v.kind in {"continuum", "profile"}))


def git_blob_sha1(data: bytes) -> str:
    """Return the canonical Git object SHA-1 for exact blob bytes."""
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def verify_materialized_spectrum(component: str, data: bytes, manifest: dict[str, SpectrumSource] | None = None) -> None:
    """Fail closed unless materialized bytes match the frozen upstream blob SHA."""
    m = load_spectrum_manifest() if manifest is None else manifest
    if component not in m:
        raise KeyError(component)
    source = m[component]
    if source.kind not in {"continuum", "profile"} or source.source_blob_sha is None:
        raise ValueError(f"{component} is not a blob-backed spectrum")
    actual = git_blob_sha1(data)
    if actual != source.source_blob_sha:
        raise ValueError(
            f"spectral blob mismatch for {component}: expected {source.source_blob_sha}, got {actual}"
        )


def raw_pinned_url(component: str, manifest: dict[str, SpectrumSource] | None = None) -> str:
    """Return an immutable raw.githubusercontent URL for one pinned spectrum."""
    m = load_spectrum_manifest() if manifest is None else manifest
    source = m[component]
    if source.kind not in {"continuum", "profile"}:
        raise ValueError(f"{component} is not a blob-backed spectrum")
    assert source.source_repo and source.source_commit and source.source_path
    return f"https://raw.githubusercontent.com/{source.source_repo}/{source.source_commit}/{source.source_path}"


def _default_fetcher(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=30) as response:  # nosec B310: URL is constructed from frozen GitHub metadata
        return response.read()


def materialize_spectrum(
    component: str,
    destination_dir: str | Path,
    *,
    manifest: dict[str, SpectrumSource] | None = None,
    fetcher: BlobFetcher | None = None,
) -> Path:
    """Download, verify and atomically write one frozen spectrum.

    Verification happens before write. A corrupted or upstream-mismatched blob
    therefore never becomes an accepted local NMIR input.
    """
    m = load_spectrum_manifest() if manifest is None else manifest
    source = m[component]
    if source.kind not in {"continuum", "profile"} or source.source_path is None:
        raise ValueError(f"{component} is not a materializable spectrum")
    url = raw_pinned_url(component, m)
    data = (fetcher or _default_fetcher)(url)
    verify_materialized_spectrum(component, data, m)
    out_dir = Path(destination_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{component}__{Path(source.source_path).name}"
    target = out_dir / filename
    tmp = target.with_suffix(target.suffix + ".tmp")
    tmp.write_bytes(data)
    tmp.replace(target)
    return target


def materialize_all_spectra(
    destination_dir: str | Path,
    *,
    manifest: dict[str, SpectrumSource] | None = None,
    fetcher: BlobFetcher | None = None,
) -> dict[str, Path]:
    """Materialize every continuum/profile spectrum under the frozen manifest."""
    m = load_spectrum_manifest() if manifest is None else manifest
    return {
        component: materialize_spectrum(component, destination_dir, manifest=m, fetcher=fetcher)
        for component in pinned_blob_components(m)
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Materialize and SHA-verify pinned NMIR solar spectra")
    parser.add_argument("destination", nargs="?", default="artifacts/solar_spectra")
    args = parser.parse_args()
    written = materialize_all_spectra(args.destination)
    for component, path in written.items():
        print(f"{component}\t{path}\t{git_blob_sha1(path.read_bytes())}")
