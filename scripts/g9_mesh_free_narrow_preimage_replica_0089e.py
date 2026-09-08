#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import urllib.error
import urllib.request

import mpmath as mp

from nmir.g9_ccsn_lens import annular_point_source_receiver_mu
from nmir.g9_continuous_projection import continuous_focal_distance_au
from nmir.gravity_extended import parse_model_s_text
from scripts.g9_continuous_map_monotone_kernel_0089d import evaluate_control as evaluate_control_double

CONTRACT = "da8e7c5664cf0980b3490926036231bea9270fcb"
MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = (
    "https://raw.githubusercontent.com/ramses-organisation/ramses/"
    + MODEL_S_COMMIT
    + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
)
R_STR = "6.96e10"
G_STR = "6.67430e-8"
C_STR = "2.99792458e10"
AU_STR = "1.495978707e13"
XMIN_STR, XMAX_STR = "1e-4", "1.0"
RADII = tuple(10.0**i for i in range(10))
CONTROLS = (
    (0.020, "23.97365833326344", "0.01150432239489928"),
    (0.024, "24.07633010302372", "0.013783440937996098"),
    (0.030, "24.263861625478885", "0.01718034337813724"),
)
DPS_LEVELS = (60, 90)
ROOT_WIDTH = mp.mpf("1e-20")
ROOT_AGREE = mp.mpf("2e-15")
AREA_REPLICA = mp.mpf("5e-7")
DOUBLE_X_TOL = 2e-11
REL_TOL = 0.005


class InfrastructureFail(RuntimeError):
    pass


class ReplicaBlocked(RuntimeError):
    pass


class ReplicaScientificFail(RuntimeError):
    pass


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def parse_model_s_decimal(text: str):
    rows: dict[str, tuple[mp.mpf, mp.mpf]] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split()
        if len(fields) < 3:
            continue
        try:
            r = mp.mpf(fields[0])
            rho = mp.mpf(fields[2])
        except (ValueError, TypeError):
            continue
        if 0 <= r <= 1 and rho >= 0:
            rows[mp.nstr(r, 100)] = (r, rho)
    ordered = sorted(rows.values(), key=lambda p: p[0])
    if len(ordered) < 2:
        raise InfrastructureFail("no usable Model-S decimal rows")
    if ordered[0][0] > 0:
        ordered.insert(0, (mp.mpf("0"), ordered[0][1]))
    return tuple(r for r, _ in ordered), tuple(rho for _, rho in ordered)


def _coeff(lo, hi, rlo, rhi):
    a = (rhi - rlo) / (hi - lo)
    b = rlo - a * lo
    return a, b


def _q(x, u):
    if u == x:
        return mp.mpf("0")
    return mp.sqrt((1 - x / u) * (1 + x / u))


def _fa(u, x):
    q = _q(x, u)
    return (u*u*x*x/8) * (2/(1+q) + q) + (x**4/8) * mp.acosh(u/x)


def _fb(u, x):
    q = _q(x, u)
    return (u*x*x/3) * (1 + q + q*q) / (1 + q)


def _poly(a, b, lo, hi):
    return a*(hi**4-lo**4)/4 + b*(hi**3-lo**3)/3


def projected_mass(rows, x):
    rs, ys = rows
    pieces = []
    for lo, hi, rlo, rhi in zip(rs, rs[1:], ys, ys[1:]):
        if lo >= 1:
            break
        hi = min(hi, mp.mpf("1"))
        if hi <= lo:
            continue
        a, b = _coeff(lo, hi, rlo, rhi)
        if hi <= x:
            pieces.append(_poly(a, b, lo, hi))
        elif lo >= x:
            pieces.append(a*(_fa(hi, x)-_fa(lo, x)) + b*(_fb(hi, x)-_fb(lo, x)))
        else:
            pieces.append(_poly(a, b, lo, x))
            pieces.append(a*(_fa(hi, x)-_fa(x, x)) + b*(_fb(hi, x)-_fb(x, x)))
    R = mp.mpf(R_STR)
    value = 4*mp.pi*R**3*mp.fsum(pieces)
    if not mp.isfinite(value) or value <= 0:
        raise ReplicaBlocked("non-finite/non-positive high-precision projected mass")
    return value


def focal_au(rows, x):
    R, G, c, AU = map(mp.mpf, (R_STR, G_STR, C_STR, AU_STR))
    mass = projected_mass(rows, x)
    return (x*R)**2*c*c/(4*G*mass)/AU


def signed_map(rows, x, z):
    R = mp.mpf(R_STR)
    return x*R*(1-z/focal_au(rows, x))


def bisect_target(yfn, lo, hi, target):
    yl, yr = yfn(lo)-target, yfn(hi)-target
    if not (mp.isfinite(yl) and mp.isfinite(yr)):
        raise ReplicaBlocked("non-finite target bracket")
    if yl == 0:
        return lo
    if yr == 0:
        return hi
    if yl*yr > 0:
        raise ReplicaBlocked("target not bracketed by frozen monotone branch")
    for _ in range(256):
        if hi-lo <= mp.mpf("1e-20"):
            return (lo+hi)/2
        mid = (lo+hi)/2
        ym = yfn(mid)-target
        if not mp.isfinite(ym):
            raise ReplicaBlocked("non-finite bisection map")
        if ym == 0:
            return mid
        if yl*ym <= 0:
            hi, yr = mid, ym
        else:
            lo, yl = mid, ym
    raise ReplicaBlocked("high-precision bisection width not reached")


def branch_interval(yfn, lo, hi, radius, parent):
    ylo, yhi = yfn(lo), yfn(hi)
    if ylo == yhi:
        raise ReplicaBlocked("frozen branch endpoints have equal map values")
    low_y, high_y = min(ylo, yhi), max(ylo, yhi)
    if high_y < -radius or low_y > radius:
        return None, []
    roots = []
    root_by_target = {}
    for target in (mp.mpf("0"), radius, -radius):
        if low_y <= target <= high_y:
            root = bisect_target(yfn, lo, hi, target)
            root_by_target[target] = root
            roots.append({"parent": parent, "target": target, "x": root, "residual": abs(yfn(root)-target)})
    keep_low, keep_high = max(low_y, -radius), min(high_y, radius)
    def x_for(value):
        if value == ylo:
            return lo
        if value == yhi:
            return hi
        if value in root_by_target:
            return root_by_target[value]
        return bisect_target(yfn, lo, hi, value)
    xa, xb = x_for(keep_low), x_for(keep_high)
    return (min(xa, xb), max(xa, xb), parent), roots


def merge_touching(intervals):
    rows = sorted(intervals, key=lambda t: t[0])
    out = []
    touch = mp.mpf("1e-20")
    for lo, hi, parent in rows:
        if hi < lo:
            raise ReplicaScientificFail("negative-width interval")
        if not out:
            out.append([lo, hi, [parent]])
            continue
        prev = out[-1]
        if lo < prev[1]-touch:
            raise ReplicaScientificFail("positive-width branch overlap")
        if abs(lo-prev[1]) <= touch:
            prev[1] = max(prev[1], hi)
            prev[2].append(parent)
        else:
            out.append([lo, hi, [parent]])
    return out


def evaluate_precision(text: str, dps: int):
    with mp.workdps(dps):
        rows = parse_model_s_decimal(text)
        controls = []
        for x0f, zstr, turnstr in CONTROLS:
            z, turn = mp.mpf(zstr), mp.mpf(turnstr)
            branches = [(mp.mpf(XMIN_STR), turn, 0), (turn, mp.mpf(XMAX_STR), 1)]
            prev_area = mp.mpf("-1")
            kernel = []
            for rf in RADII:
                radius = mp.mpf(str(rf))
                accepted, roots = [], []
                for lo, hi, parent in branches:
                    yfn = lambda x, z=z: signed_map(rows, x, z)
                    iv, rr = branch_interval(yfn, lo, hi, radius, parent)
                    roots.extend(rr)
                    if iv is not None and iv[1] > iv[0]:
                        accepted.append(iv)
                merged = merge_touching(accepted)
                area = mp.pi*mp.mpf(R_STR)**2*mp.fsum(iv[1]**2-iv[0]**2 for iv in merged)
                if not mp.isfinite(area) or area < 0 or area > mp.pi*mp.mpf(R_STR)**2*(1+mp.mpf("1e-12")):
                    raise ReplicaScientificFail("H2 area invariant failed")
                if prev_area >= 0 and area < prev_area:
                    raise ReplicaScientificFail("H2 area non-monotonic")
                prev_area = area
                kernel.append({"radius": radius, "roots": roots, "intervals": merged, "area": area})
            controls.append({"x0": mp.mpf(str(x0f)), "z": z, "turn": turn, "kernel": kernel})
        return controls


def topology_signature(row):
    return tuple(tuple(iv[2]) for iv in row["intervals"])


def toy_checks():
    with mp.workdps(60):
        # Monotone linear: |2x-1|<=0.2 -> [0.4,0.6].
        y1 = lambda x: 2*x-1
        iv, _ = branch_interval(y1, mp.mpf("0"), mp.mpf("1"), mp.mpf("0.2"), 0)
        if iv is None or abs(iv[0]-mp.mpf("0.4")) > 1e-18 or abs(iv[1]-mp.mpf("0.6")) > 1e-18:
            raise InfrastructureFail("monotone-linear toy failed")
        # One-turn surrogate split at x=0.5; both sides must contribute for small radius.
        y2 = lambda x: (x-mp.mpf("0.5"))**2-mp.mpf("0.04")
        pieces = []
        for p, (a,b) in enumerate(((mp.mpf("0"),mp.mpf("0.5")),(mp.mpf("0.5"),mp.mpf("1")))):
            z, _ = branch_interval(y2, a, b, mp.mpf("0.01"), p)
            if z is not None and z[1] > z[0]: pieces.append(z)
        if len(pieces) != 2:
            raise InfrastructureFail("one-turn quadratic toy failed")
        # Narrow preimage width 2e-9 in x, deliberately far below 0089d global grid spacing.
        y3 = lambda x: mp.mpf("1e9")*(x-mp.mpf("0.5"))
        iv, _ = branch_interval(y3, mp.mpf("0"), mp.mpf("1"), mp.mpf("1"), 0)
        if iv is None or abs((iv[1]-iv[0])-mp.mpf("2e-9")) > mp.mpf("1e-18"):
            raise InfrastructureFail("narrow linear preimage toy failed")
    return {"monotone_linear": True, "one_turn_quadratic": True, "narrow_linear": True}


def serialize(x):
    if isinstance(x, mp.mpf):
        return mp.nstr(x, 50)
    if isinstance(x, dict):
        return {str(k): serialize(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serialize(v) for v in x]
    return x


def main():
    out = Path("g9_0089e_result.json")
    result = {"contract_commit": CONTRACT, "scope": "mesh-free high-precision accepted-preimage geometry only"}
    try:
        payload = urllib.request.urlopen(MODEL_S_URL, timeout=30).read()
        blob = git_blob_sha1(payload)
        if blob != MODEL_S_BLOB:
            raise InfrastructureFail("pinned Model-S blob mismatch")
        text = payload.decode()
        result["H0"] = {"model_s_git_blob_sha1": blob, "toys": toy_checks()}

        replicas = {dps: evaluate_precision(text, dps) for dps in DPS_LEVELS}
        c60, c90 = replicas[60], replicas[90]
        max_root_delta = mp.mpf("0")
        max_residual_ratio = mp.mpf("0")
        max_area_rel = mp.mpf("0")
        max_double_x = 0.0
        max_double_area_rel = 0.0
        comparison = []
        profile_double = parse_model_s_text(text)

        for ci, ((x0f, zstr, turnstr), a60c, a90c) in enumerate(zip(CONTROLS, c60, c90)):
            _, double_rows = evaluate_control_double(profile_double, float(zstr), x0f, float(turnstr))
            for ri, (r60, r90, rd) in enumerate(zip(a60c["kernel"], a90c["kernel"], double_rows)):
                radius = mp.mpf(str(RADII[ri]))
                if topology_signature(r60) != topology_signature(r90):
                    raise ReplicaScientificFail("H1 precision topology mismatch")
                roots60 = {(q["parent"], mp.nstr(q["target"], 30)): q for q in r60["roots"]}
                roots90 = {(q["parent"], mp.nstr(q["target"], 30)): q for q in r90["roots"]}
                if set(roots60) != set(roots90):
                    raise ReplicaScientificFail("H1 precision root identity mismatch")
                for key in roots60:
                    q60, q90 = roots60[key], roots90[key]
                    delta = abs(q60["x"]-q90["x"])
                    max_root_delta = max(max_root_delta, delta)
                    if delta > mp.mpf("2e-15"):
                        raise ReplicaScientificFail("H1 x60-x90 threshold exceeded")
                    limit = max(mp.mpf("1e-8"), mp.mpf("2e-14")*radius)
                    for q in (q60, q90):
                        max_residual_ratio = max(max_residual_ratio, q["residual"]/limit)
                        if q["residual"] > limit:
                            raise ReplicaScientificFail("H1 map residual threshold exceeded")
                area_rel = abs(r60["area"]-r90["area"])/max(abs(r60["area"]),abs(r90["area"]),mp.mpf("1"))
                max_area_rel = max(max_area_rel, area_rel)
                if area_rel > mp.mpf("5e-7"):
                    raise ReplicaScientificFail("H2 60-vs-90 area threshold exceeded")

                sig90 = topology_signature(r90)
                sigd = tuple(tuple(iv["parents"]) for iv in rd["accepted_intervals"])
                if sig90 != sigd or len(r90["intervals"]) != len(rd["accepted_intervals"]):
                    raise ReplicaScientificFail("H3 double/high-precision topology mismatch")
                for hpiv, div in zip(r90["intervals"], rd["accepted_intervals"]):
                    for hx, dx in ((hpiv[0], div["lo"]), (hpiv[1], div["hi"])):
                        err = abs(float(hx)-float(dx))
                        max_double_x = max(max_double_x, err)
                        if err > DOUBLE_X_TOL:
                            raise ReplicaScientificFail("H3 double/high-precision endpoint threshold exceeded")
                hp_area = float(r90["area"])
                darea = float(rd["area_cm2"])
                are = abs(hp_area-darea)/max(abs(hp_area),abs(darea),1.0)
                max_double_area_rel = max(max_double_area_rel, are)
                if are > REL_TOL:
                    raise ReplicaScientificFail("H3 inherited 0.5% area threshold exceeded")
                comparison.append({"control": ci, "radius_cm": RADII[ri], "topology": sig90, "area90": r90["area"], "double_area": darea, "area_relative_error": are})

        # H4: inherited exact one-ring reference for x0=0.024 only.
        one_ring = []
        control90 = c90[1]
        focal_double = lambda x: continuous_focal_distance_au(profile_double, x, float(R_STR))
        for rf in (100.0, 1000.0, 10000.0):
            row = control90["kernel"][RADII.index(rf)]
            x0 = mp.mpf("0.024")
            containing = [iv for iv in row["intervals"] if iv[0] <= x0 <= iv[1]]
            if len(containing) != 1:
                raise ReplicaScientificFail("H4 unique inherited one-ring interval missing")
            iv = containing[0]
            hp_area = mp.pi*mp.mpf(R_STR)**2*(iv[1]**2-iv[0]**2)
            exact_mu = annular_point_source_receiver_mu(0.024, rf, float(R_STR), focal_double)[3]
            exact_area = math.pi*rf*rf*exact_mu
            re = abs(float(hp_area)-exact_area)/max(abs(float(hp_area)),abs(exact_area),1e-300)
            if re > REL_TOL:
                raise ReplicaScientificFail("H4 inherited one-ring area threshold exceeded")
            one_ring.append({"radius_cm": rf, "hp_interval_area_cm2": hp_area, "exact_area_cm2": exact_area, "relative_error": re})

        result["H1"] = {"max_abs_x60_x90": max_root_delta, "max_residual_to_limit_ratio": max_residual_ratio, "topology_identical": True}
        result["H2"] = {"max_area_60_90_relative_difference": max_area_rel, "all_area_invariants": True}
        result["H3"] = {"max_endpoint_abs_x_difference": max_double_x, "max_area_relative_difference": max_double_area_rel, "cases": comparison}
        result["H4"] = one_ring
        result["replica_90"] = c90
        result["status"] = "PASS_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA"
    except InfrastructureFail as exc:
        result["status"] = "INFRASTRUCTURE_FAIL_G9_0089E"; result["reason"] = str(exc)
    except (OSError, urllib.error.URLError, ImportError) as exc:
        result["status"] = "INFRASTRUCTURE_FAIL_G9_0089E"; result["reason"] = str(exc)
    except ReplicaBlocked as exc:
        result["status"] = "BLOCKED_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA"; result["reason"] = str(exc)
    except ReplicaScientificFail as exc:
        result["status"] = "SCIENTIFIC_FAIL_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA"; result["reason"] = str(exc)
    out.write_text(json.dumps(serialize(result), indent=2, sort_keys=True)+"\n")
    print(json.dumps(serialize(result), indent=2, sort_keys=True))
    if result["status"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
