"""Frozen solar electron-density and production-distribution inputs for NMIR."""

from __future__ import annotations

import csv
import hashlib
import math
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


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


@dataclass(frozen=True)
class SolarMatterTable:
    radius_rsun: tuple[float, ...]
    electron_density_mol_cm3: tuple[float, ...]
    production: dict[str, tuple[float, ...]]


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


def parse_solar_matter_bytes(
    model: str,
    data: bytes,
    manifest: dict[str, SolarMatterSource] | None = None,
    *,
    verify_blob: bool = True,
) -> SolarMatterTable:
    """Parse a frozen B16 radial table after optional exact Git-blob verification."""
    m = load_solar_matter_manifest() if manifest is None else manifest
    if model not in m:
        raise KeyError(model)
    if verify_blob:
        verify_solar_matter_blob(model, data, m)
    src = m[model]
    rows: list[list[float]] = []
    for raw in data.decode("utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        rows.append([float(x) for x in line.split()])
    if len(rows) < 2:
        raise ValueError(f"solar-matter table for {model} has fewer than two data rows")
    required = [src.radius_column, src.density_log10_column, *src.production_columns.values()]
    ncol = max(required) + 1
    if any(len(row) < ncol for row in rows):
        raise ValueError(f"solar-matter table for {model} has too few columns")
    radius = tuple(row[src.radius_column] for row in rows)
    if any(not math.isfinite(r) for r in radius) or any(b <= a for a, b in zip(radius, radius[1:])):
        raise ValueError(f"solar-matter radius grid for {model} is non-finite or non-monotonic")
    ne = tuple(10.0 ** row[src.density_log10_column] for row in rows)
    if any((not math.isfinite(x)) or x <= 0.0 for x in ne):
        raise ValueError(f"solar-matter electron density for {model} is non-positive/non-finite")
    production = {
        comp: tuple(row[col] for row in rows)
        for comp, col in src.production_columns.items()
    }
    for comp, values in production.items():
        if any((not math.isfinite(x)) or x < 0.0 for x in values):
            raise ValueError(f"negative/non-finite production distribution for {model}/{comp}")
        if not any(x > 0.0 for x in values):
            raise ValueError(f"zero production distribution for {model}/{comp}")
    return SolarMatterTable(radius, ne, production)


def trapezoid_integral(x: Iterable[float], y: Iterable[float]) -> float:
    xs, ys = tuple(x), tuple(y)
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("x and y must have the same length >= 2")
    return sum(0.5 * (b - a) * (u + v) for a, b, u, v in zip(xs, xs[1:], ys, ys[1:]))


def production_integrals(table: SolarMatterTable) -> dict[str, float]:
    return {comp: trapezoid_integral(table.radius_rsun, vals) for comp, vals in table.production.items()}


def normalized_production_weights(table: SolarMatterTable, component: str) -> tuple[float, ...]:
    """Return node weights normalized using a trapezoidal quadrature measure.

    These weights are for diagnostics/production averaging on the native radial grid;
    they do not reinterpret the upstream distributions as per-zone probabilities.
    """
    if component not in table.production:
        raise KeyError(component)
    r = table.radius_rsun
    f = table.production[component]
    weights = [0.0] * len(r)
    for i in range(len(r) - 1):
        dr = r[i + 1] - r[i]
        weights[i] += 0.5 * dr * f[i]
        weights[i + 1] += 0.5 * dr * f[i + 1]
    total = sum(weights)
    if not math.isfinite(total) or total <= 0.0:
        raise ValueError(f"invalid production integral for {component}")
    return tuple(w / total for w in weights)


def materialize_solar_matter(output_dir: str | Path) -> dict[str, dict[str, float | str | int]]:
    """Download, exact-verify, parse and persist all pinned B16 matter tables."""
    outdir = Path(output_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    manifest = load_solar_matter_manifest()
    report: dict[str, dict[str, float | str | int]] = {}
    for model, src in manifest.items():
        with urllib.request.urlopen(raw_pinned_url(model, manifest), timeout=60) as response:
            data = response.read()
        verify_solar_matter_blob(model, data, manifest)
        table = parse_solar_matter_bytes(model, data, manifest, verify_blob=False)
        ints = production_integrals(table)
        target = outdir / Path(src.source_path).name
        target.write_bytes(data)
        row: dict[str, float | str | int] = {
            "git_blob_sha1": git_blob_sha1(data),
            "rows": len(table.radius_rsun),
            "r_min": table.radius_rsun[0],
            "r_max": table.radius_rsun[-1],
            "ne_min_mol_cm3": min(table.electron_density_mol_cm3),
            "ne_max_mol_cm3": max(table.electron_density_mol_cm3),
        }
        row.update({f"integral_{k}": v for k, v in ints.items()})
        report[model] = row
    return report


def _main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python -m nmir.solar_matter OUTPUT_DIR", file=sys.stderr)
        return 2
    report = materialize_solar_matter(argv[1])
    for model in sorted(report):
        fields = " ".join(f"{k}={v}" for k, v in report[model].items())
        print(f"{model} {fields}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv))
