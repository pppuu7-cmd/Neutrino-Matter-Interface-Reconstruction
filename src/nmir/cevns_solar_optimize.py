"""Real-nucleus full-solar CEvNS inverse optimization.

Physics-only ideal event-rate ranking at fixed target kg. Detector efficiency,
metastable amplification and stored-energy accounting deliberately live outside
this module. Exact frozen isotope masses are used because endpoint rates can be
highly sensitive to sub-percent mass shifts.
"""

from __future__ import annotations

import csv
import hashlib
import io
import math
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from .baseline import G_F_GEV2, GEV2_TO_CM2, N_A, weak_charge

M_U_MEV = 931.49410242
HBARC_MEV_FM = 197.3269804
SIN2_THETA_W = 0.23857
SECONDS_PER_DAY = 86400.0


@dataclass(frozen=True)
class Target:
    name: str
    z: int
    a: int
    atomic_mass_u: float

    @property
    def n(self) -> int:
        return self.a - self.z

    @property
    def mass_mev(self) -> float:
        return self.atomic_mass_u * M_U_MEV


@dataclass(frozen=True)
class SpectrumSpec:
    component: str
    kind: str
    source_repo: str
    source_commit: str
    source_path: str
    source_blob_sha: str
    line_energy_mev: float | None
    line_weight: float | None


def read_targets(path: str | Path) -> list[Target]:
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    targets: list[Target] = []
    for row in rows:
        if not row.get("atomic_mass_u"):
            raise ValueError("exact-mass target table requires atomic_mass_u")
        targets.append(Target(row["name"], int(row["Z"]), int(row["A"]), float(row["atomic_mass_u"])))
    return targets


def read_fluxes(path: str | Path, branch: str = "b16_gs98_flux_cm2_s") -> dict[str, float]:
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        return {row["component"]: float(row[branch]) for row in csv.DictReader(handle)}


def read_manifest(path: str | Path) -> dict[str, SpectrumSpec]:
    specs: dict[str, SpectrumSpec] = {}
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            specs[row["component"]] = SpectrumSpec(
                component=row["component"],
                kind=row["kind"],
                source_repo=row["source_repo"],
                source_commit=row["source_commit"],
                source_path=row["source_path"],
                source_blob_sha=row["source_blob_sha"],
                line_energy_mev=float(row["line_energy_mev"]) if row["line_energy_mev"] else None,
                line_weight=float(row["line_weight"]) if row["line_weight"] else None,
            )
    return specs


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def parse_two_column_spectrum(text: str) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        row = next(csv.reader(io.StringIO(raw), skipinitialspace=True))
        if len(row) < 2:
            continue
        points.append((float(row[0]), float(row[1])))
    if len(points) < 2:
        raise ValueError("spectrum needs at least two points")
    if any(points[i + 1][0] <= points[i][0] for i in range(len(points) - 1)):
        raise ValueError("spectrum energies must increase strictly")
    if any(w < 0.0 for _, w in points):
        raise ValueError("spectrum weights must be non-negative")
    return points


def trapz(points: list[tuple[float, float]]) -> float:
    return sum(0.5 * (y0 + y1) * (x1 - x0) for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]))


def normalized(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    area = trapz(points)
    if not math.isfinite(area) or area <= 0.0:
        raise ValueError("non-positive spectrum area")
    return [(e, w / area) for e, w in points]


def fetch_pinned_spectrum(spec: SpectrumSpec, timeout_s: float = 30.0) -> list[tuple[float, float]]:
    if not spec.source_repo or not spec.source_commit or not spec.source_path or not spec.source_blob_sha:
        raise ValueError(f"{spec.component} has no pinned external spectrum")
    url = f"https://raw.githubusercontent.com/{spec.source_repo}/{spec.source_commit}/{spec.source_path}"
    with urllib.request.urlopen(url, timeout=timeout_s) as response:
        data = response.read()
    actual = git_blob_sha(data)
    if actual != spec.source_blob_sha:
        raise RuntimeError(f"Git blob mismatch for {spec.component}: {actual} != {spec.source_blob_sha}")
    return normalized(parse_two_column_spectrum(data.decode("utf-8-sig")))


def load_local_profile(path: str | Path) -> list[tuple[float, float]]:
    return normalized(parse_two_column_spectrum(Path(path).read_text(encoding="utf-8")))


def helm_form_factor_sq(a: int, q_mev: float) -> float:
    if a <= 0 or q_mev < 0.0:
        raise ValueError("invalid A or q")
    if q_mev == 0.0:
        return 1.0
    c = 1.23 * a ** (1.0 / 3.0) - 0.60
    diffuseness = 0.52
    skin = 0.90
    r2 = c * c + 7.0 * math.pi * math.pi * diffuseness * diffuseness / 3.0 - 5.0 * skin * skin
    radius = math.sqrt(max(r2, 0.0))
    x = q_mev * radius / HBARC_MEV_FM
    y = q_mev * skin / HBARC_MEV_FM
    if abs(x) < 1.0e-5:
        core = 1.0 - x * x / 10.0 + x**4 / 280.0
    else:
        j1 = math.sin(x) / (x * x) - math.cos(x) / x
        core = 3.0 * j1 / x
    value = core * math.exp(-0.5 * y * y)
    return value * value


def recoil_tmax_gev(e_nu_mev: float, target: Target) -> float:
    e = e_nu_mev * 1.0e-3
    m = target.mass_mev * 1.0e-3
    return 2.0 * e * e / (m + 2.0 * e)


def cevns_sigma_above_threshold_cm2(
    e_nu_mev: float,
    threshold_ev: float,
    target: Target,
    *,
    use_helm: bool = True,
    recoil_steps: int = 160,
) -> float:
    if e_nu_mev <= 0.0 or threshold_ev < 0.0 or recoil_steps < 8:
        raise ValueError("invalid CEvNS integration input")
    e = e_nu_mev * 1.0e-3
    m = target.mass_mev * 1.0e-3
    t0 = threshold_ev * 1.0e-9
    t1 = recoil_tmax_gev(e_nu_mev, target)
    if t0 >= t1:
        return 0.0
    q_w = weak_charge(target.z, target.n, SIN2_THETA_W)
    pref = G_F_GEV2**2 * q_w**2 * m / (4.0 * math.pi)
    nstep = recoil_steps + recoil_steps % 2
    h = (t1 - t0) / nstep

    def kernel(t_gev: float) -> float:
        recoil_shape = max(0.0, 1.0 - m * t_gev / (2.0 * e * e))
        if not use_helm:
            return recoil_shape
        q_mev = math.sqrt(max(0.0, 2.0 * (m * 1.0e3) * (t_gev * 1.0e3)))
        return recoil_shape * helm_form_factor_sq(target.a, q_mev)

    total = kernel(t0) + kernel(t1)
    for i in range(1, nstep):
        total += (4.0 if i % 2 else 2.0) * kernel(t0 + i * h)
    integral = h * total / 3.0
    return pref * integral * GEV2_TO_CM2


def spectrum_average_sigma_cm2(
    spectrum: list[tuple[float, float]], threshold_ev: float, target: Target, *, use_helm: bool = True
) -> float:
    points = normalized(spectrum)
    weighted = [(e, w * cevns_sigma_above_threshold_cm2(e, threshold_ev, target, use_helm=use_helm)) for e, w in points]
    return trapz(weighted)


def nuclei_per_kg(target: Target) -> float:
    return 1000.0 * N_A / target.atomic_mass_u


def rate_per_kg_day(flux_cm2_s: float, sigma_cm2: float, target: Target) -> float:
    return flux_cm2_s * sigma_cm2 * nuclei_per_kg(target) * SECONDS_PER_DAY


def component_rate(
    component: str,
    threshold_ev: float,
    target: Target,
    fluxes: dict[str, float],
    manifest: dict[str, SpectrumSpec],
    spectra: dict[str, list[tuple[float, float]]],
    *,
    use_helm: bool = True,
) -> float:
    if component == "pep":
        sigma = cevns_sigma_above_threshold_cm2(manifest["pep"].line_energy_mev or 1.442, threshold_ev, target, use_helm=use_helm)
        return rate_per_kg_day(fluxes["pep"], sigma, target)
    if component == "Be7_ground":
        sigma = spectrum_average_sigma_cm2(spectra[component], threshold_ev, target, use_helm=use_helm)
        return rate_per_kg_day(fluxes["Be7"] * 0.897, sigma, target)
    if component == "Be7_excited":
        sigma = spectrum_average_sigma_cm2(spectra[component], threshold_ev, target, use_helm=use_helm)
        return rate_per_kg_day(fluxes["Be7"] * 0.103, sigma, target)
    sigma = spectrum_average_sigma_cm2(spectra[component], threshold_ev, target, use_helm=use_helm)
    return rate_per_kg_day(fluxes[component], sigma, target)


def total_rate_row(
    target: Target,
    threshold_ev: float,
    fluxes: dict[str, float],
    manifest: dict[str, SpectrumSpec],
    spectra: dict[str, list[tuple[float, float]]],
    *,
    use_helm: bool = True,
) -> dict[str, object]:
    components = ["pp", "Be7_ground", "Be7_excited", "pep", "N13", "O15", "F17", "B8", "hep"]
    rates = {c: component_rate(c, threshold_ev, target, fluxes, manifest, spectra, use_helm=use_helm) for c in components}
    return {
        "target": target.name,
        "Z": target.z,
        "A": target.a,
        "atomic_mass_u": target.atomic_mass_u,
        "threshold_ev": threshold_ev,
        "components_events_per_kg_day": rates,
        "total_events_per_kg_day": sum(rates.values()),
        "dominant_component": max(rates, key=rates.get),
    }


def load_all_spectra(manifest: dict[str, SpectrumSpec], local_be7_ground: str | Path) -> dict[str, list[tuple[float, float]]]:
    spectra: dict[str, list[tuple[float, float]]] = {
        "Be7_ground": load_local_profile(local_be7_ground),
    }
    for component in ["pp", "hep", "B8", "N13", "O15", "F17", "Be7_excited"]:
        spectra[component] = fetch_pinned_spectrum(manifest[component])
    return spectra
