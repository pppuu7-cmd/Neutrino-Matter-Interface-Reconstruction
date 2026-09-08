#!/usr/bin/env python3
from __future__ import annotations

from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import urllib.error
import urllib.request

from nmir.g9_discrete_map_derivative import projected_mass_derivative_g_per_x
from nmir.g9_frozen_map_root_cert import (
    RootCertificationBlocked,
    base_fractions,
    stress_fractions,
    stress_mid_fractions,
    roots_from_probes,
    match_root_sets,
    sign_with_tau,
    bisect_root,
)
from nmir.g9_global_kernel import signed_map_cm
from nmir.gravity_extended import focal_distance_au, parse_model_s_text, projected_mass_g

MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = (
    "https://raw.githubusercontent.com/ramses-organisation/ramses/"
    + MODEL_S_COMMIT
    + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
)
CONTRACT = "e350cd19beec7c9d3ca9f43a439337ef9e88a099"
R = 6.96e10
X0S = (0.020, 0.024, 0.030)
DOMAIN = (1.0e-4, 1.0)
ROOT_MATCH_TOL = 2.0e-10
ROOT_WIDTH = 1.0e-12
FD_WIDTH = 5.0e-11
FD_ROOT_TOL = 5.0e-9


class ScientificRootFail(RuntimeError):
    pass


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def raw_sign(x: float) -> int:
    if not math.isfinite(x) or x == 0.0:
        return 0
    return -1 if x < 0.0 else 1


def piece_points(lo: float, hi: float, fractions: tuple[float, ...]) -> tuple[float, ...]:
    w = hi - lo
    return tuple(lo + f * w for f in fractions)


def main() -> None:
    try:
        payload = urllib.request.urlopen(MODEL_S_URL, timeout=30).read()
        blob = blob_sha(payload)
        if blob != MODEL_S_BLOB:
            raise RootCertificationBlocked("pinned Model-S blob mismatch")
        profile = parse_model_s_text(payload.decode())
        rs = profile.radius_fraction

        @lru_cache(maxsize=None)
        def mass(x: float) -> float:
            return projected_mass_g(profile, x, R)

        @lru_cache(maxsize=None)
        def dm(x: float) -> float:
            return projected_mass_derivative_g_per_x(profile, x, R)

        @lru_cache(maxsize=None)
        def focal(x: float) -> float:
            return focal_distance_au(profile, x, R)

        def y(x: float, z: float) -> float:
            return signed_map_cm(x, z, focal, R)

        def d_parts(x: float, z: float) -> tuple[float, float]:
            m = mass(x)
            dmx = dm(x)
            f = (x * R) ** 2 * 2.99792458e10**2 / (4.0 * 6.67430e-8 * m) / 1.495978707e13
            q = z / f
            term = x * q * dmx / m
            value = 1.0 + q - term
            scale = max(1.0, abs(1.0 + q), abs(term))
            if not (math.isfinite(value) and math.isfinite(scale)):
                raise RootCertificationBlocked("nonfinite exact signed-map derivative")
            return value, scale

        def dval(x: float, z: float) -> float:
            return d_parts(x, z)[0]

        def dsign(x: float, z: float) -> int:
            value, scale = d_parts(x, z)
            return sign_with_tau(value, scale)

        intervals: list[tuple[int, float, float]] = []
        for i, (a0, b0) in enumerate(zip(rs, rs[1:])):
            lo = max(a0, DOMAIN[0])
            hi = min(b0, DOMAIN[1])
            if hi > lo:
                intervals.append((i, lo, hi))
        if not intervals:
            raise RootCertificationBlocked("no Model-S intervals intersect root domain")

        z_controls = {str(x0): focal(x0) for x0 in X0S}
        all_roots: dict[str, list[dict]] = {str(x0): [] for x0 in X0S}
        interval_rows: list[dict] = []
        probe_count = 0

        # R1/R2: deterministic Q32/Q64 piecewise exact-derivative audit.
        for idx, lo, hi in intervals:
            row = {"source_interval_index": idx, "lo": lo, "hi": hi, "controls": {}}
            p32 = piece_points(lo, hi, base_fractions())
            p64 = piece_points(lo, hi, stress_fractions())
            for x0 in X0S:
                z = z_controls[str(x0)]
                # Force all required probes through the finite/threshold audit.
                for x in p64:
                    _ = dsign(x, z)
                    probe_count += 1
                fn = lambda x, z=z: dval(x, z)
                sf = lambda x, z=z: dsign(x, z)
                r32 = roots_from_probes(fn, sf, p32)
                r64 = roots_from_probes(fn, sf, p64)
                match_root_sets(r32, r64, ROOT_MATCH_TOL)
                for rb in r32:
                    contained = [r for r in r64 if rb.lo <= r.root <= rb.hi]
                    if len(contained) > 1:
                        raise RootCertificationBlocked("multiple Q64 roots inside one Q32 bracket")
                roots = []
                for r in r64:
                    rec = {
                        "root": r.root,
                        "bracket": [r.lo, r.hi],
                        "orientation": list(r.orientation),
                        "source_interval_index": idx,
                        "piece": [lo, hi],
                    }
                    roots.append(rec)
                    all_roots[str(x0)].append(rec)
                row["controls"][str(x0)] = {"interior_roots": roots}
            interval_rows.append(row)

        # Root uniqueness after de-duplication, as frozen.
        for x0 in X0S:
            roots = sorted(r["root"] for r in all_roots[str(x0)])
            for a, b in zip(roots, roots[1:]):
                if abs(b - a) <= 1.0e-10:
                    raise RootCertificationBlocked("non-unique interior roots after de-duplication")

        # R3: fixed-knot one-sided sign semantics at three frozen offsets.
        boundary_turns: dict[str, list[dict]] = {str(x0): [] for x0 in X0S}
        boundary_checks = 0
        for i in range(1, len(rs) - 1):
            k = rs[i]
            if not (DOMAIN[0] < k < DOMAIN[1]):
                continue
            a, b = rs[i - 1], rs[i + 1]
            wl, wr = k - a, b - k
            if wl <= 0.0 or wr <= 0.0:
                raise RootCertificationBlocked("nonpositive Model-S knot-adjacent width")
            for x0 in X0S:
                z = z_controls[str(x0)]
                left_signs = []
                right_signs = []
                for off in (2.0**-12, 2.0**-14, 2.0**-16):
                    sl = dsign(k - off * wl, z)
                    sr = dsign(k + off * wr, z)
                    boundary_checks += 2
                    if sl == 0 or sr == 0:
                        raise RootCertificationBlocked("near-zero knot-boundary derivative probe")
                    left_signs.append(sl)
                    right_signs.append(sr)
                if len(set(left_signs)) != 1 or len(set(right_signs)) != 1:
                    raise RootCertificationBlocked("unstable knot-boundary orientation")
                if left_signs[-1] != right_signs[-1]:
                    boundary_turns[str(x0)].append({
                        "knot": k,
                        "left_sign": left_signs[-1],
                        "right_sign": right_signs[-1],
                        "left_piece": [a, k],
                        "right_piece": [k, b],
                    })

        # R4a: original-authoritative-map finite-difference confirmation of every interior root.
        fd_confirmations: dict[str, list[dict]] = {str(x0): [] for x0 in X0S}
        for x0 in X0S:
            z = z_controls[str(x0)]
            for rec in all_roots[str(x0)]:
                root = rec["root"]
                lo, hi = rec["piece"]
                w = hi - lo
                expected = tuple(rec["orientation"])
                conf = {"root": root, "source_interval_index": rec["source_interval_index"], "scales": {}}
                for div in (4096.0, 8192.0, 16384.0):
                    h = w / div
                    blo, bhi = root - 8.0 * h, root + 8.0 * h
                    if not (lo < blo - h and bhi + h < hi):
                        raise RootCertificationBlocked("FD root-confirmation stencil cannot remain inside source piece")
                    def fds(t: float, h=h, z=z) -> float:
                        if not (lo < t - h and t + h < hi):
                            raise RootCertificationBlocked("FD bisection stencil left source piece")
                        return (y(t + h, z) - y(t - h, z)) / (2.0 * h * R)
                    fl, fh = fds(blo), fds(bhi)
                    osign = (raw_sign(fl), raw_sign(fh))
                    if 0 in osign or osign[0] == osign[1]:
                        raise RootCertificationBlocked("original-map FD bracket has no stable sign reversal")
                    if osign != expected:
                        raise ScientificRootFail("original-map FD turning orientation contradicts exact derivative")
                    rr = bisect_root(fds, blo, bhi, FD_WIDTH)
                    if abs(rr.root - root) > FD_ROOT_TOL:
                        raise ScientificRootFail("original-map FD root contradicts exact derivative beyond tolerance")
                    conf["scales"][str(int(div))] = {
                        "root": rr.root,
                        "delta_x": rr.root - root,
                        "orientation": list(rr.orientation),
                    }
                fd_confirmations[str(x0)].append(conf)

        # R4b: original-map one-sided secants for every labelled source-knot boundary turn.
        boundary_confirmations: dict[str, list[dict]] = {str(x0): [] for x0 in X0S}
        for x0 in X0S:
            z = z_controls[str(x0)]
            for bt in boundary_turns[str(x0)]:
                k = bt["knot"]
                a = bt["left_piece"][0]
                b = bt["right_piece"][1]
                wl, wr = k - a, b - k
                yk = y(k, z)
                scales = {}
                for off in (2.0**-12, 2.0**-14, 2.0**-16):
                    xl, xr = k - off * wl, k + off * wr
                    ls = (yk - y(xl, z)) / ((k - xl) * R)
                    rsx = (y(xr, z) - yk) / ((xr - k) * R)
                    signs = (raw_sign(ls), raw_sign(rsx))
                    if 0 in signs:
                        raise RootCertificationBlocked("zero/nonfinite original-map boundary secant")
                    if signs != (bt["left_sign"], bt["right_sign"]):
                        raise ScientificRootFail("original-map knot-boundary secant contradicts exact derivative")
                    scales[str(off)] = {"left": ls, "right": rsx, "signs": list(signs)}
                boundary_confirmations[str(x0)].append({"knot": k, "scales": scales})

        # R5: Q64 midpoint no-missed-root stress audit against original map FD derivative.
        stress_checks = 0
        for idx, lo, hi in intervals:
            w = hi - lo
            h = w / 16384.0
            mids = piece_points(lo, hi, stress_mid_fractions())
            for x0 in X0S:
                z = z_controls[str(x0)]
                roots_here = [r for r in all_roots[str(x0)] if r["source_interval_index"] == idx]
                for x in mids:
                    if not (lo < x - h and x + h < hi):
                        continue
                    exact_s = dsign(x, z)
                    inside = any(r["bracket"][0] <= x <= r["bracket"][1] for r in roots_here)
                    if exact_s == 0:
                        if inside:
                            continue
                        raise RootCertificationBlocked("near-zero exact derivative at Q64 stress midpoint")
                    fd = (y(x + h, z) - y(x - h, z)) / (2.0 * h * R)
                    fd_s = raw_sign(fd)
                    if fd_s == 0:
                        raise RootCertificationBlocked("zero/nonfinite original-map FD stress derivative")
                    if not inside and fd_s != exact_s:
                        raise RootCertificationBlocked("Q64 midpoint original-map/exact derivative sign disagreement")
                    stress_checks += 1

        # Frozen generating-map controls. z is constructed from the same authoritative map;
        # exact recovery is therefore x0 itself, but record both y residual and x error.
        generating = []
        for x0 in X0S:
            z = z_controls[str(x0)]
            resid = y(x0, z)
            if not math.isfinite(resid) or abs(resid) > 1.0e-5:
                raise ScientificRootFail("generating-map control fails authoritative y=0 identity")
            generating.append({"x0": x0, "observer_au": z, "recovered_x": x0, "x_error": 0.0, "y_cm": resid})

        result = {
            "status": "PASS_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION",
            "contract_commit": CONTRACT,
            "model_s_git_blob_sha1": blob,
            "domain": list(DOMAIN),
            "source_interval_count": len(intervals),
            "exact_probe_count": probe_count,
            "boundary_probe_count": boundary_checks,
            "stress_midpoint_checks": stress_checks,
            "observer_controls_au": z_controls,
            "interior_roots": all_roots,
            "boundary_turns": boundary_turns,
            "fd_confirmations": fd_confirmations,
            "boundary_confirmations": boundary_confirmations,
            "generating_controls": generating,
            "criteria": {
                "R1_finite_threshold_audit": True,
                "R2_Q32_Q64_root_match": True,
                "R3_knot_boundary_semantics": True,
                "R4_original_map_confirmation": True,
                "R5_no_missed_root_stress": True,
                "generating_map_controls": True,
            },
            "scope": "G9 frozen signed-map turning-root certification only; no y=+-r, area, kernel, one-ring, finite-source, persistent-source or BSM quantity",
        }
    except RootCertificationBlocked as exc:
        result = {
            "status": "BLOCKED_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION",
            "reason": str(exc),
            "contract_commit": CONTRACT,
            "model_s_git_blob_sha1": locals().get("blob"),
            "scope": "G9 frozen-map turning-root certification only",
        }
    except ScientificRootFail as exc:
        result = {
            "status": "SCIENTIFIC_FAIL_G9_FROZEN_MAP_ROOT_CONFIRMATION",
            "reason": str(exc),
            "contract_commit": CONTRACT,
            "model_s_git_blob_sha1": locals().get("blob"),
            "scope": "G9 frozen-map turning-root certification only",
        }
    except (OSError, urllib.error.URLError) as exc:
        result = {
            "status": "INFRASTRUCTURE_FAIL_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION",
            "reason": str(exc),
            "contract_commit": CONTRACT,
        }
    except Exception as exc:
        result = {
            "status": "INFRASTRUCTURE_FAIL_G9_FROZEN_MAP_TURNING_ROOT_CERTIFICATION",
            "reason": repr(exc),
            "contract_commit": CONTRACT,
            "model_s_git_blob_sha1": locals().get("blob"),
        }

    Path("g9_0089a_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"].startswith("SCIENTIFIC_FAIL") or result["status"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
