#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import mpmath as mp

BASE = Path(__file__).with_name("g9_continuous_projection_authority_0089b.py")
spec = importlib.util.spec_from_file_location("g9_0089b_base", BASE)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load frozen 0089b base script")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def _v1_with_observability(profile) -> dict:
    mp.mp.dps = 80
    nodes, weights = base._gauss_rule(32)
    intervals = [
        (max(a, base.DOMAIN[0]), min(b, base.DOMAIN[1]))
        for a, b in zip(profile.radius_fraction, profile.radius_fraction[1:])
        if min(b, base.DOMAIN[1]) > max(a, base.DOMAIN[0])
    ]
    if not intervals:
        raise base.ImplementationFailure("V1 no source intervals in domain")
    picked = []
    for j in range(32):
        idx = round(j * (len(intervals) - 1) / 31)
        lo, hi = intervals[idx]
        picked.append(0.5 * (lo + hi))
    xs = sorted(set(base.X_REF + tuple(picked)))
    worst_m = 0.0
    worst_d = 0.0
    worst_m_x = None
    worst_d_x = None
    rows = []
    for x in xs:
        ref_m, ref_d = base._mp_reference(profile, x, base.R, nodes, weights)
        got_m = base.continuous_projected_mass_g(profile, x, base.R)
        got_d = base.continuous_projected_mass_derivative_g_per_x(profile, x, base.R)
        got_m_mp = mp.mpf(repr(got_m))
        got_d_mp = mp.mpf(repr(got_d))
        rm = float(abs(got_m_mp - ref_m) / max(abs(ref_m), abs(got_m_mp), mp.mpf("1e-100")))
        rd = (
            float(abs(got_d_mp - ref_d) / max(abs(ref_d), abs(got_d_mp), mp.mpf("1e-100")))
            if x < 1.0
            else 0.0
        )
        if rm > worst_m:
            worst_m, worst_m_x = rm, x
        if rd > worst_d:
            worst_d, worst_d_x = rd, x
        if rm > 1e-10 or rd > 1e-9 or not (
            math.isfinite(got_m)
            and got_m > 0
            and math.isfinite(got_d)
            and got_d >= 0
        ):
            details = {
                "kind": "V1_high_precision_Model_S_mismatch",
                "x": x,
                "got_mass": repr(got_m),
                "reference_mass": mp.nstr(ref_m, 50),
                "mass_rel": rm,
                "got_derivative": repr(got_d),
                "reference_derivative": mp.nstr(ref_d, 50),
                "derivative_rel": rd,
            }
            raise base.ImplementationFailure(json.dumps(details, sort_keys=True))
        rows.append({"x": x, "mass_rel": rm, "derivative_rel": rd})
    return {
        "point_count": len(xs),
        "max_mass_rel": worst_m,
        "max_mass_rel_x": worst_m_x,
        "max_derivative_rel": worst_d,
        "max_derivative_rel_x": worst_d_x,
        "points": rows,
    }


base._v1 = _v1_with_observability
base.main()
