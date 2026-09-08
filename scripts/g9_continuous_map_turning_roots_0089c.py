#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import urllib.request

import numpy as np

from nmir.g9_continuous_projection import (
    continuous_focal_distance_au,
    continuous_projected_mass_derivative_g_per_x,
    continuous_projected_mass_g,
)
from nmir.gravity_extended import AU_CM, C_CGS, G_CGS, parse_model_s_text

CONTRACT = "1f96b318b437d6a5aecf815ef829ef09a8adc7e6"
BULK_AMENDMENT = "d2840a3974c2e4f6b530fa703410663a87dd0e50"
MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = (
    "https://raw.githubusercontent.com/ramses-organisation/ramses/"
    + MODEL_S_COMMIT
    + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
)
R = 6.96e10
XMIN = 1e-4
XMAX = 1.0
X0S = (0.020, 0.024, 0.030)
TAU_FACTOR = 2e-10


class Blocked(RuntimeError):
    pass


class ScientificFailRoot(RuntimeError):
    pass


class ScientificFailContinuity(RuntimeError):
    pass


class InfrastructureFail(RuntimeError):
    pass


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def symrel(a: float, b: float) -> float:
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


def _bulk_eval_factory(profile):
    rs = np.asarray(profile.radius_fraction, dtype=np.float64)
    ys = np.asarray(profile.density_g_cm3, dtype=np.float64)
    lo = rs[:-1]
    hi = np.minimum(rs[1:], 1.0)
    rho_lo = ys[:-1]
    rho_hi = ys[1:]
    keep = hi > lo
    lo = lo[keep]
    hi = hi[keep]
    rho_lo = rho_lo[keep]
    rho_hi = rho_hi[keep]
    a = (rho_hi - rho_lo) / (hi - lo)
    b = rho_lo - a * lo
    poly_full = a * (hi**4 - lo**4) / 4.0 + b * (hi**3 - lo**3) / 3.0
    factor = 4.0 * math.pi * R**3

    def bulk_eval(xs, need_derivative=True, chunk=96):
        xx = np.asarray(xs, dtype=np.float64)
        masses = np.empty_like(xx)
        derivs = np.empty_like(xx) if need_derivative else None
        for start in range(0, len(xx), chunk):
            stop = min(len(xx), start + chunk)
            x = xx[start:stop, None]
            full = hi[None, :] <= x
            active = hi[None, :] > x
            cross = (lo[None, :] < x) & active
            lower = np.maximum(lo[None, :], x)

            mass_piece = np.where(full, poly_full[None, :], 0.0)
            if np.any(cross):
                poly_cross = (
                    a[None, :] * (x**4 - lo[None, :] ** 4) / 4.0
                    + b[None, :] * (x**3 - lo[None, :] ** 3) / 3.0
                )
                mass_piece = mass_piece + np.where(cross, poly_cross, 0.0)

            # Above-x exact cap primitive. Values for inactive lanes are clipped
            # only to keep transcendental calls finite; masked lanes contribute 0.
            safe_hi_ratio = np.maximum(hi[None, :] / x, 1.0)
            safe_lo_ratio = np.maximum(lower / x, 1.0)
            q_hi = np.sqrt(np.maximum(0.0, (1.0 - x / hi[None, :]) * (1.0 + x / hi[None, :])))
            q_lo = np.sqrt(np.maximum(0.0, (1.0 - x / lower) * (1.0 + x / lower)))
            fa_hi = (
                (hi[None, :] ** 2 * x**2 / 8.0) * (2.0 / (1.0 + q_hi) + q_hi)
                + (x**4 / 8.0) * np.arccosh(safe_hi_ratio)
            )
            fa_lo = (
                (lower**2 * x**2 / 8.0) * (2.0 / (1.0 + q_lo) + q_lo)
                + (x**4 / 8.0) * np.arccosh(safe_lo_ratio)
            )
            fb_hi = (hi[None, :] * x**2 / 3.0) * (1.0 + q_hi + q_hi**2) / (1.0 + q_hi)
            fb_lo = (lower * x**2 / 3.0) * (1.0 + q_lo + q_lo**2) / (1.0 + q_lo)
            cap = a[None, :] * (fa_hi - fa_lo) + b[None, :] * (fb_hi - fb_lo)
            mass_piece = mass_piece + np.where(active, cap, 0.0)
            masses[start:stop] = factor * np.sum(mass_piece, axis=1, dtype=np.float64)

            if need_derivative:
                rho_lower = rho_lo[None, :] + a[None, :] * (lower - lo[None, :])
                t_lo = np.sqrt(np.maximum(0.0, (lower - x) * (lower + x)))
                t_hi = np.sqrt(np.maximum(0.0, (hi[None, :] - x) * (hi[None, :] + x)))
                dt = t_hi - t_lo
                delta_asinh = np.arcsinh(t_hi / x) - np.arcsinh(t_lo / x)
                delta_k = (
                    0.5 * (hi[None, :] * t_hi - lower * t_lo)
                    + 0.5 * x**2 * delta_asinh
                    - lower * dt
                )
                shell = rho_lower * dt + a[None, :] * delta_k
                shell = np.where(active, shell, 0.0)
                derivs[start:stop] = factor * xx[start:stop] * np.sum(shell, axis=1, dtype=np.float64)
        f = xx**2 * R**2 * C_CGS**2 / (4.0 * G_CGS * masses) / AU_CM
        return masses, derivs, f

    return bulk_eval


def scalar_values(profile, x: float):
    m = continuous_projected_mass_g(profile, x, R)
    d = continuous_projected_mass_derivative_g_per_x(profile, x, R)
    f = continuous_focal_distance_au(profile, x, R)
    return m, d, f


def d_from_values(x, z, m, dm, f):
    q = z / f
    term = x * q * dm / m
    d = 1.0 + q - term
    tau = TAU_FACTOR * max(1.0, abs(1.0 + q), abs(term))
    return d, tau, q, term


def scalar_d(profile, x: float, z: float) -> float:
    m, dm, f = scalar_values(profile, x)
    return d_from_values(x, z, m, dm, f)[0]


def scalar_y(profile, x: float, z: float) -> float:
    f = continuous_focal_distance_au(profile, x, R)
    return x * R * (1.0 - z / f)


def sign_cert(d: float, tau: float) -> int:
    if not math.isfinite(d):
        raise Blocked("nonfinite derivative")
    if abs(d) <= tau:
        return 0
    return 1 if d > 0.0 else -1


def bisection_d(profile, z, left, right, width=1e-12):
    fl = scalar_d(profile, left, z)
    fr = scalar_d(profile, right, z)
    if fl == 0.0:
        return left, (1 if fr > 0 else -1)
    if fr == 0.0:
        return right, (1 if fl < 0 else -1)
    if fl * fr > 0.0:
        raise Blocked(f"analytic root bracket lost sign change: {left},{right}")
    orientation = 1 if fl < 0.0 and fr > 0.0 else -1
    while right - left > width:
        mid = 0.5 * (left + right)
        fm = scalar_d(profile, mid, z)
        if fm == 0.0:
            left = right = mid
            break
        if fl * fm <= 0.0:
            right, fr = mid, fm
        else:
            left, fl = mid, fm
    return 0.5 * (left + right), orientation


def brackets_from_sequence(points, signs):
    brackets = []
    i = 0
    while i < len(points) - 1:
        s0, s1 = int(signs[i]), int(signs[i + 1])
        if s0 != 0 and s1 != 0 and s0 != s1:
            brackets.append((float(points[i]), float(points[i + 1])))
        i += 1
    for i, s in enumerate(signs):
        if int(s) != 0:
            continue
        if i == 0 or i == len(signs) - 1:
            raise Blocked("near-zero audit endpoint is not uniquely bracketed")
        sl, sr = int(signs[i - 1]), int(signs[i + 1])
        if sl == 0 or sr == 0 or sl == sr:
            raise Blocked(f"unresolved near-zero audit point at x={points[i]}")
        brackets.append((float(points[i - 1]), float(points[i + 1])))
    brackets.sort()
    merged = []
    for br in brackets:
        if not merged or br[0] > merged[-1][1]:
            merged.append(list(br))
        else:
            merged[-1][0] = min(merged[-1][0], br[0])
            merged[-1][1] = max(merged[-1][1], br[1])
    return [tuple(v) for v in merged]


def roots_for_sequence(profile, z, points, signs):
    roots = []
    for lo, hi in brackets_from_sequence(points, signs):
        root, orient = bisection_d(profile, z, lo, hi)
        roots.append({"x": root, "orientation": orient, "bracket": [lo, hi]})
    roots.sort(key=lambda r: r["x"])
    for a, b in zip(roots, roots[1:]):
        if b["x"] - a["x"] <= 1e-10:
            raise Blocked("root de-duplication uniqueness <=1e-10")
    return roots


def fd_derivative(profile, x, z, h):
    if x - h < XMIN or x + h > XMAX:
        raise Blocked("finite-difference stencil leaves global domain")
    return (scalar_y(profile, x + h, z) - scalar_y(profile, x - h, z)) / (2.0 * h * R)


def fd_root(profile, z, analytic_root, w, h):
    left = analytic_root - 8.0 * h
    right = analytic_root + 8.0 * h
    if left - h < XMIN or right + h > XMAX:
        raise Blocked("R4 fixed FD bracket/stencil leaves domain")
    fl = fd_derivative(profile, left, z, h)
    fr = fd_derivative(profile, right, z, h)
    if not (math.isfinite(fl) and math.isfinite(fr)):
        raise Blocked("R4 nonfinite finite-difference derivative")
    if fl * fr >= 0.0:
        raise ScientificFailRoot("analytic root not confirmed by stable fixed FD sign reversal")
    orient = 1 if fl < 0.0 and fr > 0.0 else -1
    while right - left > 5e-11:
        mid = 0.5 * (left + right)
        fm = fd_derivative(profile, mid, z, h)
        if fl * fm <= 0.0:
            right, fr = mid, fm
        else:
            left, fl = mid, fm
    return 0.5 * (left + right), orient


def bisection_y(profile, z, lo, hi):
    fl, fr = scalar_y(profile, lo, z), scalar_y(profile, hi, z)
    if fl == 0.0:
        return lo
    if fr == 0.0:
        return hi
    if fl * fr > 0.0:
        raise ScientificFailRoot("generating-map y=0 control lacks fixed-bracket sign change")
    while hi - lo > 1e-13:
        mid = 0.5 * (lo + hi)
        fm = scalar_y(profile, mid, z)
        if fl * fm <= 0.0:
            hi, fr = mid, fm
        else:
            lo, fl = mid, fm
    return 0.5 * (lo + hi)


def main():
    result = {
        "contract_commit": CONTRACT,
        "bulk_amendment_commit": BULK_AMENDMENT,
        "scope": "continuous-map turning roots only; no areas/kernel/utility",
    }
    out = Path("g9_0089c_result.json")
    try:
        payload = urllib.request.urlopen(MODEL_S_URL, timeout=30).read()
        blob = git_blob_sha1(payload)
        if blob != MODEL_S_BLOB:
            raise InfrastructureFail("pinned Model-S blob mismatch")
        profile = parse_model_s_text(payload.decode())
        result["model_s_git_blob_sha1"] = blob
        bulk_eval = _bulk_eval_factory(profile)

        rs = [r for r in profile.radius_fraction if XMIN < r < XMAX]
        anchors = sorted(set([XMIN, *rs, XMAX]))
        cells = [(a, b) for a, b in zip(anchors, anchors[1:]) if b > a]
        result["source_cell_count"] = len(cells)
        result["interior_source_knot_count"] = len(anchors) - 2

        # B0 bulk/scalar conformance, before any z controls or signs.
        b0_points = [1e-4, 3e-4, 1e-3, 0.003, 0.01, 0.02, 0.024, 0.03, 0.05, 0.1, 0.2, 0.4, 0.7, 0.9, 0.99, 0.99999825]
        for j in range(64):
            idx = round(j * (len(cells) - 1) / 63)
            a, b = cells[idx]
            b0_points.append(0.5 * (a + b))
        b0_points = sorted(set(b0_points))
        bm, bd, bf = bulk_eval(b0_points, need_derivative=True)
        max_m = max_d = max_f = 0.0
        for i, x in enumerate(b0_points):
            sm, sd, sf = scalar_values(profile, x)
            max_m = max(max_m, symrel(float(bm[i]), sm))
            max_d = max(max_d, symrel(float(bd[i]), sd))
            max_f = max(max_f, symrel(float(bf[i]), sf))
        result["B0"] = {"point_count": len(b0_points), "max_mass_symrel": max_m, "max_derivative_symrel": max_d, "max_focal_symrel": max_f}
        if max_m > 2e-11 or max_d > 2e-10 or max_f > 2e-11:
            result["status"] = "INFRASTRUCTURE_FAIL_G9_0089C_BULK_EVALUATOR_CONFORMANCE"
            result["reason"] = "bulk/scalar conformance threshold exceeded"
            out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
            print(json.dumps(result, indent=2, sort_keys=True))
            return

        # Frozen Q64 mesh; Q32 is the even-j subset plus anchors.
        point_flags = {float(a): True for a in anchors}
        for a, b in cells:
            w = b - a
            for j in range(1, 64):
                x = a + w * (j / 64.0)
                point_flags[x] = point_flags.get(x, False) or (j % 2 == 0)
        q64_points = np.asarray(sorted(point_flags), dtype=np.float64)
        q32_indices = np.asarray([i for i, x in enumerate(q64_points) if point_flags[float(x)]], dtype=np.int64)
        qm, qdm, qf = bulk_eval(q64_points, need_derivative=True)
        if not (np.all(np.isfinite(qm)) and np.all(qm > 0) and np.all(np.isfinite(qdm)) and np.all(qdm >= 0) and np.all(np.isfinite(qf)) and np.all(qf > 0)):
            raise Blocked("R1 nonfinite/nonphysical fixed-mesh continuous-map value")

        # z controls are generated only after B0 passed.
        z_controls = []
        for x0 in X0S:
            _, _, f0 = scalar_values(profile, x0)
            z_controls.append((x0, f0))
        result["z_controls_au"] = [{"x0": x0, "z_au": z} for x0, z in z_controls]

        per_control = []
        for x0, z in z_controls:
            q = z / qf
            term = q64_points * q * qdm / qm
            dvals = 1.0 + q - term
            tau = TAU_FACTOR * np.maximum.reduce([np.ones_like(q), np.abs(1.0 + q), np.abs(term)])
            signs = np.where(np.abs(dvals) <= tau, 0, np.where(dvals > 0, 1, -1)).astype(np.int8)
            if not np.all(np.isfinite(dvals)):
                raise Blocked("R1 nonfinite D_c")

            q32_points = q64_points[q32_indices]
            q32_signs = signs[q32_indices]
            roots32 = roots_for_sequence(profile, z, q32_points, q32_signs)
            roots64 = roots_for_sequence(profile, z, q64_points, signs)
            if len(roots32) != len(roots64):
                raise Blocked(f"Q32/Q64 root-count mismatch for x0={x0}: {len(roots32)} vs {len(roots64)}")
            for r32, r64 in zip(roots32, roots64):
                if abs(r32["x"] - r64["x"]) > 2e-10 or r32["orientation"] != r64["orientation"]:
                    raise Blocked(f"Q32/Q64 root mismatch for x0={x0}")

            # R3 all-source-knot one-sided stress using bulk accelerator.
            r3_pts = []
            r3_meta = []
            for i in range(1, len(anchors) - 1):
                k = anchors[i]
                lw = k - anchors[i - 1]
                rw = anchors[i + 1] - k
                row = []
                for delta in (2**-12, 2**-14, 2**-16):
                    row.append(k - lw * delta)
                row.append(k)
                for delta in (2**-16, 2**-14, 2**-12):
                    row.append(k + rw * delta)
                r3_meta.append((k, lw, rw, len(r3_pts)))
                r3_pts.extend(row)
            r3m, r3dm, r3f = bulk_eval(r3_pts, need_derivative=True)
            r3q = z / r3f
            r3term = np.asarray(r3_pts) * r3q * r3dm / r3m
            r3d = 1.0 + r3q - r3term
            r3tau = TAU_FACTOR * np.maximum.reduce([np.ones_like(r3q), np.abs(1.0 + r3q), np.abs(r3term)])
            r3sign = np.where(np.abs(r3d) <= r3tau, 0, np.where(r3d > 0, 1, -1)).astype(np.int8)
            r3_skipped_near_root = 0
            for k, lw, rw, off in r3_meta:
                neighborhood = (k - lw * 2**-12, k + rw * 2**-12)
                if any(neighborhood[0] <= r["x"] <= neighborhood[1] for r in roots64):
                    r3_skipped_near_root += 1
                    continue
                left = [int(v) for v in r3sign[off : off + 3]]
                sk = int(r3sign[off + 3])
                right = [int(v) for v in r3sign[off + 4 : off + 7]]
                if 0 in left or 0 in right or sk == 0:
                    raise Blocked(f"R3 near-zero ambiguity at source knot {k}")
                if len(set(left)) != 1 or len(set(right)) != 1:
                    raise Blocked(f"R3 unstable one-sided orientation at source knot {k}")
                if left[0] != right[0] or sk != left[0]:
                    raise ScientificFailContinuity(f"R3 stable derivative-continuity contradiction at source knot {k}")

            # R4 independent signed-map FD confirmation for every root.
            fd_confirmations = []
            for root in roots64:
                xr = root["x"]
                ci = max(0, min(len(cells) - 1, np.searchsorted(np.asarray(anchors), xr, side="right") - 1))
                a, b = cells[ci]
                if abs(xr - a) <= 2e-10 and ci > 0:
                    w = min(cells[ci - 1][1] - cells[ci - 1][0], b - a)
                elif abs(xr - b) <= 2e-10 and ci + 1 < len(cells):
                    w = min(b - a, cells[ci + 1][1] - cells[ci + 1][0])
                else:
                    w = b - a
                reps = []
                for denom in (4096.0, 8192.0, 16384.0):
                    h = w / denom
                    rfd, orient = fd_root(profile, z, xr, w, h)
                    if abs(rfd - xr) > 5e-9 or orient != root["orientation"]:
                        raise ScientificFailRoot(f"R4 FD root disagreement for x0={x0}, root={xr}")
                    reps.append({"denom": int(denom), "x": rfd, "abs_dx": abs(rfd - xr), "orientation": orient})
                fd_confirmations.append({"analytic_x": xr, "orientation": root["orientation"], "replicas": reps})

            # R5 Q64 subinterval midpoint FD stress, all fixed before results.
            mids = []
            minus = []
            plus = []
            mid_widths = []
            for a, b in cells:
                w = b - a
                h = w / 16384.0
                for j in range(64):
                    xm = a + w * ((j + 0.5) / 64.0)
                    mids.append(xm)
                    minus.append(xm - h)
                    plus.append(xm + h)
                    mid_widths.append(w)
            midm, middm, midf = bulk_eval(mids, need_derivative=True)
            _, _, fm = bulk_eval(minus, need_derivative=False)
            _, _, fp = bulk_eval(plus, need_derivative=False)
            mids_arr = np.asarray(mids)
            minus_arr = np.asarray(minus)
            plus_arr = np.asarray(plus)
            h_arr = (plus_arr - minus_arr) / 2.0
            yminus = minus_arr * R * (1.0 - z / fm)
            yplus = plus_arr * R * (1.0 - z / fp)
            fdmid = (yplus - yminus) / (2.0 * h_arr * R)
            midq = z / midf
            midterm = mids_arr * midq * middm / midm
            mida = 1.0 + midq - midterm
            midtau = TAU_FACTOR * np.maximum.reduce([np.ones_like(midq), np.abs(1.0 + midq), np.abs(midterm)])
            amid_sign = np.where(np.abs(mida) <= midtau, 0, np.where(mida > 0, 1, -1)).astype(np.int8)
            fd_sign = np.where(np.abs(fdmid) <= midtau, 0, np.where(fdmid > 0, 1, -1)).astype(np.int8)
            r5_checked = 0
            r5_skipped = 0
            for i, xm in enumerate(mids):
                if any(r["bracket"][0] <= xm <= r["bracket"][1] for r in roots64):
                    r5_skipped += 1
                    continue
                if amid_sign[i] == 0 or fd_sign[i] == 0:
                    raise Blocked(f"R5 near-zero ambiguity at x={xm}")
                if amid_sign[i] != fd_sign[i]:
                    raise Blocked(f"R5 analytic/FD midpoint sign disagreement at x={xm}")
                r5_checked += 1

            # R6 generating-map control.
            y_at_x0 = scalar_y(profile, x0, z)
            if abs(y_at_x0) / R > 1e-13:
                raise ScientificFailRoot(f"R6 direct generating y(x0) residual for {x0}")
            lo = max(XMIN, x0 * (1.0 - 2**-10))
            hi = min(XMAX, x0 * (1.0 + 2**-10))
            recovered = bisection_y(profile, z, lo, hi)
            if abs(recovered - x0) > 1e-12:
                raise ScientificFailRoot(f"R6 recovered x0 mismatch for {x0}: {recovered}")

            per_control.append(
                {
                    "x0": x0,
                    "z_au": z,
                    "q32_root_count": len(roots32),
                    "q64_root_count": len(roots64),
                    "roots": roots64,
                    "fd_confirmations": fd_confirmations,
                    "r3_source_knots_checked": len(r3_meta) - r3_skipped_near_root,
                    "r3_source_knots_skipped_near_certified_root": r3_skipped_near_root,
                    "r5_midpoints_checked": r5_checked,
                    "r5_midpoints_skipped_inside_root_bracket": r5_skipped,
                    "r6_recovered_x0": recovered,
                    "r6_abs_dx": abs(recovered - x0),
                }
            )

        result["controls"] = per_control
        result["status"] = "PASS_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION"
    except ScientificFailContinuity as exc:
        result["status"] = "SCIENTIFIC_FAIL_G9_CONTINUOUS_MAP_DERIVATIVE_CONTINUITY"
        result["reason"] = str(exc)
    except ScientificFailRoot as exc:
        result["status"] = "SCIENTIFIC_FAIL_G9_CONTINUOUS_MAP_ROOT_CONFIRMATION"
        result["reason"] = str(exc)
    except Blocked as exc:
        result["status"] = "BLOCKED_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION"
        result["reason"] = str(exc)
    except (OSError, ValueError, FloatingPointError, InfrastructureFail) as exc:
        result["status"] = "INFRASTRUCTURE_FAIL_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION"
        result["reason"] = repr(exc)

    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
