"""Independent COHERENT CENNS-10 Ar Analysis-A SM CEvNS normalization.

Scientific scope is frozen by research/prereg/0074a_coherent_argon_sm_benchmark.md.
The implementation intentionally does not use the release CEvNS PDF normalization.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from pathlib import Path
from typing import Iterable

GF_GEV2 = 1.1663787e-5
HBARC_GEV_FM = 0.1973269804
GEV2_TO_CM2 = 0.3893793721e-27
AVOGADRO = 6.02214076e23
M_MU_GEV = 0.1056583755
M_PI_GEV = 0.13957039
U_TO_GEV = 0.93149410242
AR40_ATOMIC_MASS_U = 39.9623831237

Z_AR40 = 18
N_AR40 = 22
RP_AR40_FM = 3.448
RN_AR40_FM = 3.55
HELM_SKIN_FM = 0.9
GVP_NUE = 0.0401
GVP_NUMU = 0.0318
GVN = -0.5094

POT = 13.8e22
NU_PER_POT_PER_FLAVOR = 0.09
BASELINE_M = 27.5
FIDUCIAL_MASS_KG = 24.4


@dataclass(frozen=True)
class EfficiencyPoint:
    recoil_kevnr: float
    efficiency: float


def load_efficiency(path: str | Path) -> list[EfficiencyPoint]:
    points: list[EfficiencyPoint] = []
    for raw in Path(path).read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        cols = line.split()
        if len(cols) < 3:
            raise ValueError(f"Malformed efficiency row: {raw!r}")
        tnr = float(cols[1])
        eps = float(cols[2])
        if not (0.0 <= eps <= 1.0):
            raise ValueError(f"Efficiency outside [0,1]: {eps}")
        points.append(EfficiencyPoint(tnr, eps))
    if len(points) < 2:
        raise ValueError("Need at least two efficiency points")
    if any(b.recoil_kevnr <= a.recoil_kevnr for a, b in zip(points, points[1:])):
        raise ValueError("Efficiency recoil grid must be strictly increasing")
    return points


def efficiency_at(t_kevnr: float, points: list[EfficiencyPoint]) -> float:
    if t_kevnr < points[0].recoil_kevnr or t_kevnr > points[-1].recoil_kevnr:
        return 0.0
    lo, hi = 0, len(points) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if points[mid].recoil_kevnr <= t_kevnr:
            lo = mid
        else:
            hi = mid
    a, b = points[lo], points[hi]
    if t_kevnr == a.recoil_kevnr:
        return a.efficiency
    w = (t_kevnr - a.recoil_kevnr) / (b.recoil_kevnr - a.recoil_kevnr)
    return a.efficiency + w * (b.efficiency - a.efficiency)


def spherical_j1(x: float) -> float:
    if abs(x) < 1e-5:
        x2 = x * x
        return x / 3.0 - x * x2 / 30.0 + x * x2 * x2 / 840.0
    return math.sin(x) / (x * x) - math.cos(x) / x


def helm_form_factor(q_gev: float, rms_fm: float) -> float:
    if q_gev == 0.0:
        return 1.0
    q_fm_inv = q_gev / HBARC_GEV_FM
    r0_sq = (5.0 / 3.0) * (rms_fm * rms_fm - 3.0 * HELM_SKIN_FM**2)
    if r0_sq <= 0.0:
        raise ValueError("Unphysical Helm radius")
    x = q_fm_inv * math.sqrt(r0_sq)
    return 3.0 * spherical_j1(x) / x * math.exp(-0.5 * (q_fm_inv * HELM_SKIN_FM) ** 2)


def inverse_recoil_threshold_gev(t_gev: float, nucleus_mass_gev: float) -> float:
    return 0.5 * (t_gev + math.sqrt(t_gev * t_gev + 2.0 * nucleus_mass_gev * t_gev))


def recoil_endpoint_gev(e_gev: float, nucleus_mass_gev: float) -> float:
    return 2.0 * e_gev * e_gev / (nucleus_mass_gev + 2.0 * e_gev)


def _michel_integrals(e_min: float, flavor: str) -> tuple[float, float]:
    """Return integral f(E)dE and integral f(E)/E^2 dE above e_min."""
    e_max = M_MU_GEV / 2.0
    if e_min >= e_max:
        return 0.0, 0.0
    lo = max(0.0, e_min)
    m = M_MU_GEV
    if flavor == "nue":
        def p0(e: float) -> float:
            return 32.0 * e**3 / m**3 - 48.0 * e**4 / m**4
        def p2(e: float) -> float:
            return 96.0 * e / m**3 - 96.0 * e**2 / m**4
    elif flavor == "numubar":
        def p0(e: float) -> float:
            return 16.0 * e**3 / m**3 - 16.0 * e**4 / m**4
        def p2(e: float) -> float:
            return 48.0 * e / m**3 - 32.0 * e**2 / m**4
    else:
        raise ValueError(flavor)
    return p0(e_max) - p0(lo), p2(e_max) - p2(lo)


def nucleus_mass_gev() -> float:
    return AR40_ATOMIC_MASS_U * U_TO_GEV


def _weak_charge(t_gev: float, flavor: str, form_factor: bool = True) -> float:
    q_gev = math.sqrt(max(0.0, 2.0 * nucleus_mass_gev() * t_gev))
    if form_factor:
        fp = helm_form_factor(q_gev, RP_AR40_FM)
        fn = helm_form_factor(q_gev, RN_AR40_FM)
    else:
        fp = fn = 1.0
    gvp = GVP_NUE if flavor == "nue" else GVP_NUMU
    return gvp * Z_AR40 * fp + GVN * N_AR40 * fn


def target_nuclei() -> float:
    return FIDUCIAL_MASS_KG * 1000.0 / AR40_ATOMIC_MASS_U * AVOGADRO


def fluence_per_flavor_cm2() -> float:
    return NU_PER_POT_PER_FLAVOR * POT / (4.0 * math.pi * BASELINE_M**2) / 1.0e4


def _differential_rate_kernel_cm2_per_gev(t_gev: float, flavor: str, *, form_factor: bool = True) -> float:
    qweak = _weak_charge(t_gev, flavor, form_factor=form_factor)
    return GF_GEV2**2 * nucleus_mass_gev() / math.pi * qweak * qweak * GEV2_TO_CM2


def source_averaged_dsigma_dt_cm2_per_gev(t_gev: float, flavor: str, *, form_factor: bool = True) -> float:
    m = nucleus_mass_gev()
    e_min = inverse_recoil_threshold_gev(t_gev, m)
    pref = _differential_rate_kernel_cm2_per_gev(t_gev, flavor, form_factor=form_factor)
    a = m * t_gev / 2.0
    if flavor == "numu_prompt":
        e0 = (M_PI_GEV**2 - M_MU_GEV**2) / (2.0 * M_PI_GEV)
        if e_min > e0:
            return 0.0
        return pref * max(0.0, 1.0 - a / (e0 * e0))
    if flavor in ("nue", "numubar"):
        i0, i2 = _michel_integrals(e_min, flavor)
        return pref * max(0.0, i0 - a * i2)
    raise ValueError(flavor)


def _trapezoid(values: Iterable[float], step: float) -> float:
    vals = list(values)
    if len(vals) < 2:
        return 0.0
    return step * (0.5 * vals[0] + sum(vals[1:-1]) + 0.5 * vals[-1])


def accepted_cross_section_cm2(flavor: str, efficiency: list[EfficiencyPoint], *, n_t: int = 4000, apply_efficiency: bool = True, form_factor: bool = True) -> float:
    if n_t < 20:
        raise ValueError("n_t too small")
    t_max_kev = efficiency[-1].recoil_kevnr
    dt_gev = (t_max_kev * 1.0e-6) / n_t
    values = []
    for i in range(n_t + 1):
        t_gev = i * dt_gev
        eps = efficiency_at(t_gev * 1.0e6, efficiency) if apply_efficiency else 1.0
        values.append(eps * source_averaged_dsigma_dt_cm2_per_gev(t_gev, flavor, form_factor=form_factor))
    return _trapezoid(values, dt_gev)


def calculate_events(efficiency: list[EfficiencyPoint], *, n_t: int = 4000, apply_efficiency: bool = True, form_factor: bool = True) -> dict[str, float]:
    scale = target_nuclei() * fluence_per_flavor_cm2()
    components = {}
    for flavor in ("numu_prompt", "nue", "numubar"):
        components[flavor] = scale * accepted_cross_section_cm2(flavor, efficiency, n_t=n_t, apply_efficiency=apply_efficiency, form_factor=form_factor)
    components["total"] = sum(components.values())
    return components
