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
    continuous_focal_distance_au,
    continuous_projected_mass_derivative_g_per_x,
    continuous_projected_mass_g,
)
from nmir.gravity_extended import (
    combined_scan_grid,
    focal_distance_au,
    parse_model_s_text,
    projected_mass_g,
    RadialDensityProfile,
)

MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = (
    "https://raw.githubusercontent.com/ramses-organisation/ramses/"
    + MODEL_S_COMMIT
    + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
)
CONTRACT = "5d99cd6cd4d3a5f1f9defecfbd7f4036c93b8636"
R = 6.96e10
DOMAIN = (1.0e-4, 1.0)
X_REF = (
    1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 2e-2, 2.4e-2, 3e-2,
    5e-2, 1e-1, 2e-1, 4e-1, 7e-1, 9e-1, 9.9e-1,
)


class ProjectionBlocked(RuntimeError):
    pass


class ImplementationFailure(RuntimeError):
    pass


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def rel(a: float, b: float) -> float:
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def _coeff(lo, hi, rlo, rhi):
    a = (rhi - rlo) / (hi - lo)
    return a, rlo - a * lo


def _toy_v0() -> dict:
    mp.mp.dps = 80
    tuples = (
        (mp.mpf("0.2"), mp.mpf("0.25"), mp.mpf("0.7"), mp.mpf("1.3"), mp.mpf("0.5")),
        (mp.mpf("0.4"), mp.mpf("0.4"), mp.mpf("0.8"), mp.mpf("-0.7"), mp.mpf("2.1")),
        (mp.mpf("0.03"), mp.mpf("0.1"), mp.mpf("0.9"), mp.mpf("0.2"), mp.mpf("4.0")),
    )
    worst = mp.mpf("0")
    for x, lo, hi, a, b in tuples:
        def q(u):
            return mp.sqrt(1 - (x/u)**2)
        def fa(u):
            qq = q(u)
            return (u*u*x*x/8)*(2/(1+qq)+qq) + x**4*mp.acosh(u/x)/8
        def fb(u):
            qq = q(u)
            return (u*x*x/3)*(1+qq+qq*qq)/(1+qq)
        exact = a*(fa(hi)-fa(lo)) + b*(fb(hi)-fb(lo))
        numeric = mp.quad(lambda u: u*u*(a*u+b)*(1-mp.sqrt(1-(x/u)**2)), [lo, hi])
        rr = abs(exact-numeric)/max(abs(exact), abs(numeric), mp.mpf("1e-100"))
        worst = max(worst, rr)
        if rr > mp.mpf("1e-12"):
            raise ImplementationFailure("V0 external antiderivative high-precision mismatch")

    toy = RadialDensityProfile((0.0, 0.15, 0.4, 0.75, 1.0), (9.0, 7.0, 4.0, 1.5, 0.3))
    r = 11.0
    worst_fd = 0.0
    vals = []
    for x in (0.03, 0.19, 0.52, 0.83):
        h = 2.0e-6
        f = lambda t: continuous_projected_mass_g(toy, t, r)
        fd = (-f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h))/(12*h)
        exact = continuous_projected_mass_derivative_g_per_x(toy, x, r)
        rr = rel(fd, exact)
        worst_fd = max(worst_fd, rr)
        if rr > 1e-9:
            raise ImplementationFailure("V0 toy five-point derivative mismatch")
        vals.append(f(x))
    if not all(math.isfinite(v) and v > 0.0 for v in vals) or not all(a < b for a,b in zip(vals, vals[1:])):
        raise ImplementationFailure("V0 toy mass positivity/monotonicity failure")
    return {"external_antiderivative_max_rel": float(worst), "toy_five_point_max_rel": worst_fd}


def _gauss_rule(n: int = 32):
    xs, ws = mp.gauss_quadrature(n, "legendre")
    return tuple(xs[i] for i in range(n)), tuple(ws[i] for i in range(n))


def _glint(fn, a, b, nodes, weights):
    if b == a:
        return mp.mpf("0")
    mid = (a+b)/2
    half = (b-a)/2
    return half * mp.fsum(w * fn(mid + half*x) for x,w in zip(nodes,weights))


def _mp_reference(profile, x_float: float, radius_cm: float, nodes, weights):
    x = mp.mpf(repr(x_float))
    rscale = mp.mpf(repr(radius_cm))
    rs = [mp.mpf(repr(v)) for v in profile.radius_fraction]
    ys = [mp.mpf(repr(v)) for v in profile.density_g_cm3]
    mass_parts = []
    deriv_parts = []
    for lo, hi, rlo, rhi in zip(rs, rs[1:], ys, ys[1:]):
        if lo >= 1:
            break
        hi = min(hi, mp.mpf(1))
        if hi <= lo:
            continue
        a, b = _coeff(lo, hi, rlo, rhi)
        rho = lambda u, a=a, b=b: a*u+b
        if hi <= x:
            mass_parts.append(_glint(lambda u: u*u*rho(u), lo, hi, nodes, weights))
        else:
            if lo < x:
                mass_parts.append(_glint(lambda u: u*u*rho(u), lo, x, nodes, weights))
                lower = x
            else:
                lower = lo
            th_lo = mp.mpf(0) if lower == x else mp.acos(x/lower)
            th_hi = mp.acos(x/hi)
            def mass_theta(th):
                c = mp.cos(th); s = mp.sin(th); u = x/c
                return x**3 * rho(u) * (2*mp.sin(th/2)**2) * s / c**4
            mass_parts.append(_glint(mass_theta, th_lo, th_hi, nodes, weights))
            def deriv_theta(th):
                c = mp.cos(th); u = x/c
                return x*x * rho(u) / (c*c)
            deriv_parts.append(_glint(deriv_theta, th_lo, th_hi, nodes, weights))
    factor = 4*mp.pi*rscale**3
    return factor*mp.fsum(mass_parts), factor*mp.fsum(deriv_parts)


def _v1(profile) -> dict:
    mp.mp.dps = 80
    nodes, weights = _gauss_rule(32)
    intervals = [(max(a, DOMAIN[0]), min(b, DOMAIN[1])) for a,b in zip(profile.radius_fraction, profile.radius_fraction[1:]) if min(b,DOMAIN[1]) > max(a,DOMAIN[0])]
    if not intervals:
        raise ImplementationFailure("V1 no source intervals in domain")
    picked = []
    for j in range(32):
        idx = round(j*(len(intervals)-1)/31)
        lo, hi = intervals[idx]
        picked.append(0.5*(lo+hi))
    xs = sorted(set(X_REF + tuple(picked)))
    worst_m = 0.0; worst_d = 0.0; worst_m_x = None; worst_d_x = None
    rows = []
    for x in xs:
        ref_m, ref_d = _mp_reference(profile, x, R, nodes, weights)
        got_m = continuous_projected_mass_g(profile, x, R)
        got_d = continuous_projected_mass_derivative_g_per_x(profile, x, R)
        rm = float(abs(mp.mpf(repr(got_m))-ref_m)/max(abs(ref_m),abs(mp.mpf(repr(got_m))),mp.mpf("1e-100")))
        rd = float(abs(mp.mpf(repr(got_d))-ref_d)/max(abs(ref_d),abs(mp.mpf(repr(got_d))),mp.mpf("1e-100"))) if x < 1.0 else 0.0
        if rm > worst_m: worst_m, worst_m_x = rm, x
        if rd > worst_d: worst_d, worst_d_x = rd, x
        if rm > 1e-10 or rd > 1e-9 or not (math.isfinite(got_m) and got_m > 0 and math.isfinite(got_d) and got_d >= 0):
            raise ImplementationFailure(f"V1 high-precision Model-S mismatch at x={x!r}")
        rows.append({"x": x, "mass_rel": rm, "derivative_rel": rd})
    return {"point_count":len(xs),"max_mass_rel":worst_m,"max_mass_rel_x":worst_m_x,
            "max_derivative_rel":worst_d,"max_derivative_rel_x":worst_d_x,"points":rows}


def _v2(profile) -> dict:
    rs = profile.radius_fraction
    checked = 0; worst = 0.0; worst_knot = None
    slack_rows = []
    for i in range(1, len(rs)-1):
        k = rs[i]
        if not (DOMAIN[0] < k < DOMAIN[1]):
            continue
        wl, wr = k-rs[i-1], rs[i+1]-k
        if wl <= 0 or wr <= 0:
            raise ImplementationFailure("V2 nonpositive adjacent source width")
        dk = continuous_projected_mass_derivative_g_per_x(profile, k, R)
        if not math.isfinite(dk):
            raise ProjectionBlocked("nonfinite exact derivative at source knot")
        ldist=[]; rdist=[]
        left=[]; right=[]
        for off in (2.0**-12,2.0**-14,2.0**-16):
            dl=continuous_projected_mass_derivative_g_per_x(profile,k-off*wl,R)
            dr=continuous_projected_mass_derivative_g_per_x(profile,k+off*wr,R)
            if not (math.isfinite(dl) and math.isfinite(dr)):
                raise ProjectionBlocked("nonfinite one-sided continuous derivative")
            left.append(dl); right.append(dr); ldist.append(abs(dl-dk)); rdist.append(abs(dr-dk))
        slack=1e-13*max(1.0,abs(dk))
        if any(b > a + slack for a,b in zip(ldist,ldist[1:])) or any(b > a + slack for a,b in zip(rdist,rdist[1:])):
            raise ProjectionBlocked("continuous source-knot derivative does not converge monotonically")
        scale=max(1.0,abs(dk))
        e=max(ldist[-1]/scale,rdist[-1]/scale)
        if e > 2e-5:
            raise ProjectionBlocked("continuous source-knot one-sided limit exceeds frozen agreement tolerance")
        checked+=1
        if e>worst: worst,worst_knot=e,k
        if e > 1e-7:
            slack_rows.append({"knot":k,"smallest_offset_scaled_error":e})
    return {"knot_count":checked,"max_smallest_offset_scaled_error":worst,"max_error_knot":worst_knot,
            "notable_over_1e-7":slack_rows[:32]}


def _v3(profile) -> dict:
    max_m=max_f=0.0; max_m_x=max_f_x=None; sum_m2=sum_f2=0.0; n=0
    for x in combined_scan_grid():
        if not (DOMAIN[0] <= x <= DOMAIN[1]):
            continue
        cm=continuous_projected_mass_g(profile,x,R); dm=projected_mass_g(profile,x,R)
        cf=continuous_focal_distance_au(profile,x,R); df=focal_distance_au(profile,x,R)
        rm=rel(cm,dm); rf=rel(cf,df)
        if rm>max_m: max_m,max_m_x=rm,x
        if rf>max_f: max_f,max_f_x=rf,x
        sum_m2+=rm*rm; sum_f2+=rf*rf; n+=1
    if n==0:
        raise ImplementationFailure("V3 empty comparison grid")
    out={"point_count":n,"max_mass_rel":max_m,"max_mass_rel_x":max_m_x,
         "max_focal_rel":max_f,"max_focal_rel_x":max_f_x,
         "rms_mass_rel":math.sqrt(sum_m2/n),"rms_focal_rel":math.sqrt(sum_f2/n)}
    if max_m>0.005 or max_f>0.005:
        raise ProjectionBlocked(json.dumps({"kind":"discrete_compatibility","metrics":out},sort_keys=True))
    return out


def main():
    result = {"contract_commit": CONTRACT}
    try:
        result["V0"] = _toy_v0()
        payload=urllib.request.urlopen(MODEL_S_URL,timeout=30).read()
        blob=blob_sha(payload)
        if blob!=MODEL_S_BLOB:
            raise ImplementationFailure("pinned Model-S blob mismatch")
        profile=parse_model_s_text(payload.decode())
        result["model_s_git_blob_sha1"]=blob
        result["V1"]=_v1(profile)
        try:
            result["V2"]=_v2(profile)
        except ProjectionBlocked as exc:
            result.update({"status":"BLOCKED_G9_CONTINUOUS_PROJECTION_KNOT_CONTINUITY","reason":str(exc),
                           "scope":"G9 continuous piecewise-linear projection authority only; no roots/areas/kernel"})
        else:
            try:
                result["V3"]=_v3(profile)
            except ProjectionBlocked as exc:
                reason=str(exc); metrics=None
                try:
                    parsed=json.loads(reason)
                    if parsed.get("kind")=="discrete_compatibility": metrics=parsed.get("metrics")
                except Exception:
                    pass
                if metrics is not None: result["V3"]=metrics
                result.update({"status":"BLOCKED_G9_CONTINUOUS_PROJECTION_DISCRETE_COMPATIBILITY","reason":"continuous/discrete map disagreement exceeds frozen 0.5%" if metrics else reason,
                               "scope":"G9 continuous piecewise-linear projection authority only; no roots/areas/kernel"})
            else:
                result.update({"status":"PASS_G9_CONTINUOUS_PIECEWISE_LINEAR_PROJECTION_AUTHORITY",
                               "scope":"G9 continuous piecewise-linear projection authority only; separate preregistration required for turning roots"})
    except ImplementationFailure as exc:
        result.update({"status":"INFRASTRUCTURE_FAIL_G9_CONTINUOUS_PROJECTION_IMPLEMENTATION","reason":str(exc)})
    except (OSError,urllib.error.URLError) as exc:
        result.update({"status":"INFRASTRUCTURE_FAIL_G9_CONTINUOUS_PROJECTION_IMPLEMENTATION","reason":str(exc)})
    except Exception as exc:
        result.update({"status":"INFRASTRUCTURE_FAIL_G9_CONTINUOUS_PROJECTION_IMPLEMENTATION","reason":repr(exc)})
    Path("g9_0089b_result.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))
    if result["status"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(1)


if __name__=="__main__":
    main()
