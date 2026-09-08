#!/usr/bin/env python3
"""NMIR 0089 — authority audit for exact derivative of frozen discrete G9 map."""
from __future__ import annotations

from bisect import bisect_right
import hashlib
import json
import math
from pathlib import Path
import urllib.error
import urllib.request

import mpmath as mp

from nmir.g9_discrete_map_derivative import (
    DiscreteMapDerivativeBoundary,
    finite_sum_projected_mass_g,
    projected_mass_derivative_g_per_x,
)
from nmir.gravity_extended import RadialDensityProfile, parse_model_s_text, projected_mass_g

MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = (
    "https://raw.githubusercontent.com/ramses-organisation/ramses/"
    + MODEL_S_COMMIT
    + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
)
GRAVITY_BLOB = "f8d48fb4eae87ff9c1f98ef543dae27c5f359e9c"
PREREG_COMMIT = "b64dd44f483e1753ebbcbb60e3f68f06a21f7ad5"
R = 6.96e10
MASS_TOL = 5e-13
DERIV_TOL = 1e-8
QVALUES = (0.25, 0.5, 0.75)
CONTROLS = (0.020, 0.024, 0.030)
MAX_REFERENCE_INTERVALS = 64


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def symrel(a: float, b: float) -> float:
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def fetch(url: str) -> bytes:
    last = None
    for _ in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NMIR-0089/1.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except Exception as exc:  # infrastructure only
            last = exc
    raise OSError(f"Model-S fetch failed: {last}")


def intervals(profile: RadialDensityProfile) -> list[tuple[int, float, float]]:
    rs = profile.radius_fraction
    return [(i, rs[i], rs[i + 1]) for i in range(len(rs) - 1) if rs[i + 1] > rs[i]]


def stratified_indices(profile: RadialDensityProfile) -> list[int]:
    ints = intervals(profile)
    n = len(ints)
    if n <= MAX_REFERENCE_INTERVALS:
        return list(range(n))

    selected: set[int] = set(range(min(4, n)))
    selected.update(range(max(0, n - 4), n))
    rs = profile.radius_fraction
    for control in CONTROLS:
        k = bisect_right(rs, control) - 1
        for j in (k - 1, k, k + 1):
            if 0 <= j < n:
                selected.add(j)

    # Deterministically fill the widest index gaps until 64 slots are occupied.
    # This uses interval order only, never derivative values.
    while len(selected) < MAX_REFERENCE_INTERVALS:
        remaining = [i for i in range(n) if i not in selected]
        if not remaining:
            break
        if not selected:
            pick = n // 2
        else:
            ordered = sorted(selected)
            def distance_to_selected(i: int) -> tuple[int, int]:
                d = min(abs(i - s) for s in ordered)
                return (d, -i)
            pick = max(remaining, key=distance_to_selected)
        selected.add(pick)
    return sorted(selected)


def _mp_profile(profile: RadialDensityProfile):
    rs = [mp.mpf(repr(x)) for x in profile.radius_fraction]
    ys = [mp.mpf(repr(y)) for y in profile.density_g_cm3]
    return rs, ys


def _mp_fraction(x, u):
    if u == 0 or u <= x:
        return mp.mpf(1)
    return 1 - mp.sqrt(1 - (x / u) ** 2)


def _mp_mass_on_interval(rs, ys, k: int, x, radius):
    a, b = rs[k], rs[k + 1]
    slope = (ys[k + 1] - ys[k]) / (b - a)
    rho_x = ys[k] + slope * (x - a)
    gx = x * x * rho_x

    terms = []
    # Fixed intervals wholly below the moving split.
    for j in range(k):
        g0 = rs[j] * rs[j] * ys[j]
        g1 = rs[j + 1] * rs[j + 1] * ys[j + 1]
        terms.append((rs[j + 1] - rs[j]) * (g0 + g1))

    ga = a * a * ys[k]
    gb = b * b * ys[k + 1]
    terms.append((x - a) * (ga + gx))
    terms.append((b - x) * (gx + gb * _mp_fraction(x, b)))

    # Fixed intervals wholly outside the split.
    for j in range(k + 1, len(rs) - 1):
        u0, u1 = rs[j], rs[j + 1]
        g0 = u0 * u0 * ys[j] * _mp_fraction(x, u0)
        g1 = u1 * u1 * ys[j + 1] * _mp_fraction(x, u1)
        terms.append((u1 - u0) * (g0 + g1))

    return 2 * mp.pi * radius**3 * mp.fsum(terms)


def _five_point(fn, x, h):
    return (fn(x - 2*h) - 8*fn(x - h) + 8*fn(x + h) - fn(x + 2*h)) / (12*h)


def _mp_symrel(a, b):
    return abs(a - b) / max(abs(a), abs(b), mp.mpf("1e-300"))


def mass_identity(profile: RadialDensityProfile):
    worst = {"relative_error": -1.0}
    count = 0
    for idx, a, b in intervals(profile):
        for q in QVALUES:
            x = a + q * (b - a)
            calc = finite_sum_projected_mass_g(profile, x, R)
            auth = projected_mass_g(profile, x, R)
            if not (math.isfinite(calc) and math.isfinite(auth) and calc > 0 and auth > 0):
                raise ValueError(f"nonfinite/nonpositive mass identity point interval={idx} q={q}")
            err = symrel(calc, auth)
            count += 1
            if err > worst["relative_error"]:
                worst = {"relative_error": err, "interval_index": idx, "q": q, "x": x,
                         "finite_sum_mass_g": calc, "authoritative_mass_g": auth}
    return {"point_count": count, "max_symmetric_relative_error": worst["relative_error"],
            "worst": worst, "passed": worst["relative_error"] <= MASS_TOL}


def derivative_reference(profile: RadialDensityProfile):
    mp.mp.dps = 80
    rs_mp, ys_mp = _mp_profile(profile)
    R_mp = mp.mpf(repr(R))
    chosen = stratified_indices(profile)
    ints = intervals(profile)
    worst_replica = {"relative_error": mp.mpf(-1)}
    worst_analytic = {"relative_error": mp.mpf(-1)}
    count = 0

    for ordinal in chosen:
        idx, a_float, b_float = ints[ordinal]
        a = rs_mp[idx]
        b = rs_mp[idx + 1]
        h = (b - a) / 1024
        for q in QVALUES:
            x_float = a_float + q * (b_float - a_float)
            x = mp.mpf(repr(x_float))
            fn = lambda t, idx=idx: _mp_mass_on_interval(rs_mp, ys_mp, idx, t, R_mp)
            d1 = _five_point(fn, x, h)
            d2 = _five_point(fn, x, h / 2)
            analytic_float = projected_mass_derivative_g_per_x(profile, x_float, R)
            analytic = mp.mpf(repr(analytic_float))
            if not (mp.isfinite(d1) and mp.isfinite(d2) and math.isfinite(analytic_float)):
                raise ValueError(f"nonfinite derivative reference interval={idx} q={q}")
            er = _mp_symrel(d1, d2)
            ea = _mp_symrel(analytic, d2)
            count += 1
            if er > worst_replica["relative_error"]:
                worst_replica = {"relative_error": er, "interval_index": idx, "q": q,
                                 "x": x, "h": h, "d_h": d1, "d_h2": d2}
            if ea > worst_analytic["relative_error"]:
                worst_analytic = {"relative_error": ea, "interval_index": idx, "q": q,
                                  "x": x, "analytic": analytic, "reference_h2": d2}

    def plain(obj):
        return {k: (float(v) if isinstance(v, mp.mpf) else v) for k, v in obj.items()}

    return {
        "selected_interval_ordinals": chosen,
        "selected_interval_count": len(chosen),
        "point_count": count,
        "max_reference_replica_symmetric_relative_error": float(worst_replica["relative_error"]),
        "max_analytic_reference_symmetric_relative_error": float(worst_analytic["relative_error"]),
        "worst_reference_replica": plain(worst_replica),
        "worst_analytic_reference": plain(worst_analytic),
        "passed": (worst_replica["relative_error"] <= DERIV_TOL and
                   worst_analytic["relative_error"] <= DERIV_TOL),
    }


def toy_profiles():
    return {
        "constant": RadialDensityProfile((0.0, 0.25, 0.6, 1.0), (1.0, 1.0, 1.0, 1.0)),
        "monotone_linear": RadialDensityProfile((0.0, 0.25, 0.6, 1.0), (4.0, 3.0, 2.0, 1.0)),
        "nonmonotone_positive": RadialDensityProfile((0.0, 0.2, 0.7, 1.0), (1.0, 3.0, 2.0, 4.0)),
    }


def toy_audit_one(profile: RadialDensityProfile):
    mp.mp.dps = 80
    rs_mp, ys_mp = _mp_profile(profile)
    R_mp = mp.mpf(repr(R))
    max_mass = 0.0
    max_rep = mp.mpf(0)
    max_der = mp.mpf(0)
    count = 0
    for idx, a_float, b_float in intervals(profile):
        a, b = rs_mp[idx], rs_mp[idx + 1]
        h = (b - a) / 1024
        for q in QVALUES:
            x_float = a_float + q * (b_float - a_float)
            x = mp.mpf(repr(x_float))
            m1 = finite_sum_projected_mass_g(profile, x_float, R)
            m2 = projected_mass_g(profile, x_float, R)
            max_mass = max(max_mass, symrel(m1, m2))
            fn = lambda t, idx=idx: _mp_mass_on_interval(rs_mp, ys_mp, idx, t, R_mp)
            d1 = _five_point(fn, x, h)
            d2 = _five_point(fn, x, h/2)
            da = mp.mpf(repr(projected_mass_derivative_g_per_x(profile, x_float, R)))
            max_rep = max(max_rep, _mp_symrel(d1, d2))
            max_der = max(max_der, _mp_symrel(da, d2))
            count += 1
    return {"point_count": count, "max_mass_rel": max_mass,
            "max_reference_replica_rel": float(max_rep), "max_derivative_rel": float(max_der),
            "passed": max_mass <= MASS_TOL and max_rep <= DERIV_TOL and max_der <= DERIV_TOL}


def boundary_integrity(profile: RadialDensityProfile):
    checked = 0
    failures = []
    for x in profile.radius_fraction:
        if not 0.0 < x <= 1.0:
            continue
        mass = projected_mass_g(profile, x, R)
        if not (math.isfinite(mass) and mass > 0):
            failures.append({"x": x, "reason": "nonfinite_or_nonpositive_mass"})
        if x < 1.0:
            try:
                projected_mass_derivative_g_per_x(profile, x, R)
            except DiscreteMapDerivativeBoundary:
                pass
            else:
                failures.append({"x": x, "reason": "exact_knot_not_rejected"})
        checked += 1
    return {"checked_positive_knots": checked, "failures": failures, "passed": not failures}


def audit():
    payload = fetch(MODEL_S_URL)
    blob = git_blob_sha1(payload)
    if blob != MODEL_S_BLOB:
        raise OSError(f"pinned Model-S blob mismatch: {blob}")

    root = Path(__file__).resolve().parents[1]
    gravity_bytes = (root / "src" / "nmir" / "gravity_extended.py").read_bytes()
    gravity_blob = git_blob_sha1(gravity_bytes)
    if gravity_blob != GRAVITY_BLOB:
        raise OSError(f"frozen gravity_extended blob mismatch: {gravity_blob}")

    prereg_bytes = (root / "research" / "prereg" / "0089_g9_frozen_discrete_map_derivative_authority.md").read_bytes()
    profile = parse_model_s_text(payload.decode())

    v1 = mass_identity(profile)
    v2 = derivative_reference(profile)
    toys = {name: toy_audit_one(p) for name, p in toy_profiles().items()}
    v3_pass = all(r["passed"] for r in toys.values())
    v4 = boundary_integrity(profile)

    passed = v1["passed"] and v2["passed"] and v3_pass and v4["passed"]
    classification = (
        "PASS_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY"
        if passed else
        "SCIENTIFIC_FAIL_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY"
    )
    return {
        "gate": "G9_0089_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY",
        "classification": classification,
        "prereg_commit": PREREG_COMMIT,
        "prereg_sha256": sha256(prereg_bytes),
        "model_s_git_blob_sha1": blob,
        "gravity_extended_git_blob_sha1": gravity_blob,
        "parsed_knot_count": len(profile.radius_fraction),
        "open_interval_count": len(intervals(profile)),
        "criteria": {"mass_identity_max_symrel": MASS_TOL, "derivative_reference_max_symrel": DERIV_TOL,
                     "high_precision_decimal_digits": 80, "q_values": list(QVALUES), "fd_h_fraction_of_interval": 1/1024},
        "V1_mass_identity": v1,
        "V2_high_precision_derivative": v2,
        "V3_toys": {"passed": v3_pass, "profiles": toys},
        "V4_piece_boundaries": v4,
        "scope": "Exact derivative authority for frozen discrete trapezoidal projected_mass_g on open Model-S knot intervals only; no roots, areas, kernel, persistent-source convolution or BSM.",
    }


def main():
    out = Path("g9_0089_derivative_authority.json")
    try:
        result = audit()
    except (OSError, urllib.error.URLError) as exc:
        result = {"gate": "G9_0089_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY",
                  "classification": "INFRASTRUCTURE_FAIL_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY",
                  "reason": repr(exc), "prereg_commit": PREREG_COMMIT}
    except DiscreteMapDerivativeBoundary as exc:
        result = {"gate": "G9_0089_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY",
                  "classification": "BLOCKED_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY",
                  "reason": repr(exc), "prereg_commit": PREREG_COMMIT}
    except Exception as exc:
        result = {"gate": "G9_0089_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY",
                  "classification": "SCIENTIFIC_FAIL_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY",
                  "reason": repr(exc), "prereg_commit": PREREG_COMMIT}
    out.write_text(json.dumps(result, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    if result["classification"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(3)
    if result["classification"] != "PASS_G9_FROZEN_DISCRETE_MAP_DERIVATIVE_AUTHORITY":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
