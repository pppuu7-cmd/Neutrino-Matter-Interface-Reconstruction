"""Independent COHERENT CsI first-observation SM CEvNS response.

Scientific scope is frozen by research/prereg/0074b_coherent_csi_sm_response_benchmark.md.
No B-L calculation is performed here.
"""
from __future__ import annotations
import math
from typing import Iterable

GF_GEV2 = 1.1663787e-5
HBARC_GEV_FM = 0.1973269804
GEV2_TO_CM2 = 0.3893793721e-27
AVOGADRO = 6.02214076e23
M_MU_GEV = 0.1056583755
M_PI_GEV = 0.13957039
U_TO_GEV = 0.93149410242
HELM_SKIN_FM = 0.9
GVP_NUE = 0.0401
GVP_NUMU = 0.0318
GVN = -0.5094

POT = 17.6e22
NU_PER_POT_PER_FLAVOR = 0.08
BASELINE_M = 19.3
DETECTOR_MASS_KG = 14.6
CS133_MASS_U = 132.90545196
I127_MASS_U = 126.9044719
CS133_Z, CS133_N = 55, 78
I127_Z, I127_N = 53, 74
CS133_RP_FM, I127_RP_FM = 4.804, 4.749
COMMON_RN_FM = 5.5
QF = 0.0878
LIGHT_YIELD_PE_PER_KEVEE = 13.348
ACC_A, ACC_K, ACC_X0 = 0.6655, 0.4942, 10.8507
PE_MIN, PE_MAX_EXCLUSIVE = 0, 30


def spherical_j1(x: float) -> float:
    if abs(x) < 1e-5:
        return x / 3.0 - x**3 / 30.0 + x**5 / 840.0
    return math.sin(x) / x**2 - math.cos(x) / x


def helm_form_factor(q_gev: float, rms_fm: float) -> float:
    if q_gev == 0.0:
        return 1.0
    q = q_gev / HBARC_GEV_FM
    r0sq = (5.0 / 3.0) * (rms_fm**2 - 3.0 * HELM_SKIN_FM**2)
    x = q * math.sqrt(r0sq)
    return 3.0 * spherical_j1(x) / x * math.exp(-0.5 * (q * HELM_SKIN_FM) ** 2)


def recoil_endpoint_gev(e_gev: float, m_gev: float) -> float:
    return 2.0 * e_gev**2 / (m_gev + 2.0 * e_gev)


def inverse_recoil_threshold_gev(t_gev: float, m_gev: float) -> float:
    return 0.5 * (t_gev + math.sqrt(t_gev**2 + 2.0 * m_gev * t_gev))


def _michel_integrals(e_min: float, flavor: str) -> tuple[float, float]:
    emax = M_MU_GEV / 2.0
    if e_min >= emax:
        return 0.0, 0.0
    lo = max(0.0, e_min)
    m = M_MU_GEV
    if flavor == "nue":
        p0 = lambda e: 32.0 * e**3 / m**3 - 48.0 * e**4 / m**4
        p2 = lambda e: 96.0 * e / m**3 - 96.0 * e**2 / m**4
    elif flavor == "numubar":
        p0 = lambda e: 16.0 * e**3 / m**3 - 16.0 * e**4 / m**4
        p2 = lambda e: 48.0 * e / m**3 - 32.0 * e**2 / m**4
    else:
        raise ValueError(flavor)
    return p0(emax) - p0(lo), p2(emax) - p2(lo)


def acceptance_at_pe_center(pe_integer: int) -> float:
    x = pe_integer + 0.5
    if x < 5.0:
        h = 0.0
    elif x < 6.0:
        h = 0.5
    else:
        h = 1.0
    return h * ACC_A / (1.0 + math.exp(-ACC_K * (x - ACC_X0)))


def poisson_acceptance(mu: float, *, apply_acceptance: bool = True, pe_max_exclusive: int = PE_MAX_EXCLUSIVE) -> tuple[float, float]:
    if mu < 0.0:
        raise ValueError("negative Poisson mean")
    p = math.exp(-mu)
    accepted = 0.0
    included = p
    if apply_acceptance:
        accepted += p * acceptance_at_pe_center(0)
    else:
        accepted += p
    for n in range(1, pe_max_exclusive):
        p *= mu / n
        included += p
        accepted += p * (acceptance_at_pe_center(n) if apply_acceptance else 1.0)
    return accepted, max(0.0, 1.0 - included)


def target_molecules() -> float:
    return DETECTOR_MASS_KG * 1000.0 / (CS133_MASS_U + I127_MASS_U) * AVOGADRO


def fluence_per_flavor_cm2() -> float:
    return NU_PER_POT_PER_FLAVOR * POT / (4.0 * math.pi * BASELINE_M**2) / 1.0e4


def _source_factor(t: float, m: float, flavor: str) -> float:
    emin = inverse_recoil_threshold_gev(t, m)
    a = m * t / 2.0
    if flavor == "numu_prompt":
        e0 = (M_PI_GEV**2 - M_MU_GEV**2) / (2.0 * M_PI_GEV)
        return 0.0 if emin > e0 else max(0.0, 1.0 - a / e0**2)
    i0, i2 = _michel_integrals(emin, flavor)
    return max(0.0, i0 - a * i2)


def _integrate(vals: Iterable[float], step: float) -> float:
    v = list(vals)
    return step * (0.5 * v[0] + sum(v[1:-1]) + 0.5 * v[-1])


def nucleus_events(*, z: int, n: int, mass_u: float, rp_fm: float, flavor: str, n_t: int = 4000, qf: float = QF, light_yield: float = LIGHT_YIELD_PE_PER_KEVEE, apply_acceptance: bool = True, form_factor: bool = True) -> tuple[float, float]:
    m = mass_u * U_TO_GEV
    emax = (M_PI_GEV**2 - M_MU_GEV**2) / (2.0 * M_PI_GEV) if flavor == "numu_prompt" else M_MU_GEV / 2.0
    tmax = recoil_endpoint_gev(emax, m)
    dt = tmax / n_t
    vals = []
    max_tail = 0.0
    for i in range(n_t + 1):
        t = i * dt
        q = math.sqrt(max(0.0, 2.0 * m * t))
        fp = helm_form_factor(q, rp_fm) if form_factor else 1.0
        fn = helm_form_factor(q, COMMON_RN_FM) if form_factor else 1.0
        gvp = GVP_NUE if flavor == "nue" else GVP_NUMU
        qw = gvp * z * fp + GVN * n * fn
        dsdt = GF_GEV2**2 * m / math.pi * qw**2 * GEV2_TO_CM2 * _source_factor(t, m, flavor)
        mu = light_yield * qf * t * 1.0e6
        acc, tail = poisson_acceptance(mu, apply_acceptance=apply_acceptance, pe_max_exclusive=100)
        max_tail = max(max_tail, tail)
        vals.append(dsdt * acc)
    sigma = _integrate(vals, dt)
    return target_molecules() * fluence_per_flavor_cm2() * sigma, max_tail


def calculate_events(*, n_t: int = 4000, qf: float = QF, light_yield: float = LIGHT_YIELD_PE_PER_KEVEE, apply_acceptance: bool = True, form_factor: bool = True) -> dict[str, float]:
    nuclei = {
        "Cs": (CS133_Z, CS133_N, CS133_MASS_U, CS133_RP_FM),
        "I": (I127_Z, I127_N, I127_MASS_U, I127_RP_FM),
    }
    out: dict[str, float] = {}
    max_tail = 0.0
    for name, pars in nuclei.items():
        for flavor in ("numu_prompt", "nue", "numubar"):
            val, tail = nucleus_events(z=pars[0], n=pars[1], mass_u=pars[2], rp_fm=pars[3], flavor=flavor, n_t=n_t, qf=qf, light_yield=light_yield, apply_acceptance=apply_acceptance, form_factor=form_factor)
            out[f"{name}_{flavor}"] = val
            max_tail = max(max_tail, tail)
    out["Cs_total"] = sum(out[f"Cs_{f}"] for f in ("numu_prompt", "nue", "numubar"))
    out["I_total"] = sum(out[f"I_{f}"] for f in ("numu_prompt", "nue", "numubar"))
    out["total"] = out["Cs_total"] + out["I_total"]
    out["max_poisson_tail"] = max_tail
    return out
