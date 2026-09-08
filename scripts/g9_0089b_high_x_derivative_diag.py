#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import urllib.error
import urllib.request

import mpmath as mp

from nmir.g9_continuous_projection import (
    _ja,
    _jb,
    continuous_projected_mass_derivative_g_per_x,
)
from nmir.gravity_extended import parse_model_s_text

CONTRACT = "0460ed7026167db314959c51509b7b6a9fd04328"
MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = (
    "https://raw.githubusercontent.com/ramses-organisation/ramses/"
    + MODEL_S_COMMIT
    + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
)
R = 6.96e10
X = 0.99999825


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def symrel_mp(a: mp.mpf, b: mp.mpf) -> mp.mpf:
    return abs(a - b) / max(abs(a), abs(b), mp.mpf("1e-100"))


def _mp_profile(profile):
    rs = [mp.mpf(repr(v)) for v in profile.radius_fraction]
    ys = [mp.mpf(repr(v)) for v in profile.density_g_cm3]
    return rs, ys


def references(profile, x_float: float = X, radius_cm: float = R):
    mp.mp.dps = 100
    x = mp.mpf(repr(x_float))
    rs, ys = _mp_profile(profile)
    theta_parts = []
    t_parts = []
    for lo, hi, rlo, rhi in zip(rs, rs[1:], ys, ys[1:]):
        if lo >= 1:
            break
        hi = min(hi, mp.mpf(1))
        if hi <= x or hi <= lo:
            continue
        lower = max(lo, x)
        a = (rhi - rlo) / (hi - lo)
        b = rlo - a * lo

        def rho(u):
            return a * u + b

        th_lo = mp.mpf(0) if lower == x else mp.acos(x / lower)
        th_hi = mp.acos(x / hi)
        theta_parts.append(
            mp.quad(lambda th: x * x * rho(x / mp.cos(th)) / (mp.cos(th) ** 2), [th_lo, th_hi])
        )

        t_lo = mp.sqrt(max(mp.mpf(0), lower * lower - x * x))
        t_hi = mp.sqrt(max(mp.mpf(0), hi * hi - x * x))
        t_parts.append(
            mp.quad(lambda t: x * rho(mp.sqrt(x * x + t * t)), [t_lo, t_hi])
        )

    factor = 4 * mp.pi * mp.mpf(repr(radius_cm)) ** 3
    return factor * mp.fsum(theta_parts), factor * mp.fsum(t_parts)


def cancellation_rows(profile, x: float = X):
    rows = []
    rs = profile.radius_fraction
    ys = profile.density_g_cm3
    for i, (lo, hi, rlo, rhi) in enumerate(zip(rs, rs[1:], ys, ys[1:])):
        if lo >= 1.0:
            break
        hi = min(hi, 1.0)
        if hi <= x or hi <= lo:
            continue
        lower = max(lo, x)
        a = (rhi - rlo) / (hi - lo)
        b = rlo - a * lo
        term_a = a * (_ja(hi, x) - _ja(lower, x))
        term_b = b * (_jb(hi, x) - _jb(lower, x))
        total = term_a + term_b
        ratio = (abs(term_a) + abs(term_b)) / max(abs(total), 1e-300)
        rows.append(
            {
                "interval_index": i,
                "lo": lo,
                "hi": hi,
                "lower": lower,
                "rho_lo": rlo,
                "rho_hi": rhi,
                "term_a": term_a,
                "term_b": term_b,
                "sum": total,
                "cancellation_ratio": ratio,
            }
        )
    return rows


def main():
    result = {"contract_commit": CONTRACT, "x": X}
    try:
        payload = urllib.request.urlopen(MODEL_S_URL, timeout=30).read()
        got_blob = blob_sha(payload)
        if got_blob != MODEL_S_BLOB:
            raise RuntimeError("pinned Model-S blob mismatch")
        profile = parse_model_s_text(payload.decode())
        result["model_s_git_blob_sha1"] = got_blob

        ref_theta, ref_t = references(profile)
        ref_rel = symrel_mp(ref_theta, ref_t)
        result["reference_theta"] = mp.nstr(ref_theta, 70)
        result["reference_t"] = mp.nstr(ref_t, 70)
        result["reference_symrel"] = float(ref_rel)
        result["cancellation_rows"] = cancellation_rows(profile)
        if ref_rel > mp.mpf("1e-20"):
            result["status"] = "INFRASTRUCTURE_FAIL_G9_0089B_HIGH_X_REFERENCE_DISAGREEMENT"
            result["reason"] = "100-digit theta-space and t-space references disagree"
        else:
            production = continuous_projected_mass_derivative_g_per_x(profile, X, R)
            consensus = (ref_theta + ref_t) / 2
            prod_rel = abs(mp.mpf(repr(production)) - consensus) / max(
                abs(mp.mpf(repr(production))), abs(consensus), mp.mpf("1e-100")
            )
            result["production_derivative"] = repr(production)
            result["consensus_reference"] = mp.nstr(consensus, 70)
            result["production_symrel"] = float(prod_rel)
            if prod_rel <= mp.mpf("1e-9"):
                result["status"] = "PASS_G9_0089B_HIGH_X_DERIVATIVE_CONFORMANCE_DIAGNOSTIC"
                result["reason"] = "production agrees with two independent 100-digit references at original V1 tolerance"
            else:
                result["status"] = "DIAG_G9_0089B_PRODUCTION_DERIVATIVE_STABILITY_DEFECT"
                result["reason"] = "independent references agree but production exceeds original V1 derivative tolerance"
    except (OSError, urllib.error.URLError, ValueError, RuntimeError) as exc:
        result["status"] = "INFRASTRUCTURE_FAIL_G9_0089B_HIGH_X_REFERENCE_DISAGREEMENT"
        result["reason"] = repr(exc)

    Path("g9_0089b_high_x_derivative_diag.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
