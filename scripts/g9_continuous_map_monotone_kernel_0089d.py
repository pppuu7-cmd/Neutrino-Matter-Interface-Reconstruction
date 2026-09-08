#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import urllib.request

import numpy as np

from nmir.g9_ccsn_lens import annular_point_source_receiver_mu
from nmir.g9_continuous_kernel import (
    KernelBlocked,
    KernelScientificFail,
    accepted_branch_interval,
    annular_area_cm2,
    branch_crossings,
    indicator_midpoint_area_cm2,
    merge_adjacent_with_parents,
)
from nmir.g9_continuous_projection import (
    continuous_focal_distance_au,
    continuous_projected_mass_derivative_g_per_x,
    continuous_projected_mass_g,
)
from nmir.gravity_extended import AU_CM, C_CGS, G_CGS, parse_model_s_text

CONTRACT = "8eab0935d54cb930495b55cbc3025225729f109c"
BULK_AMENDMENT = "33f7b72b7429993b09321cd5674fa1eff3219812"
MODEL_S_COMMIT = "cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b"
MODEL_S_BLOB = "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f"
MODEL_S_URL = (
    "https://raw.githubusercontent.com/ramses-organisation/ramses/"
    + MODEL_S_COMMIT
    + "/patch/global_star/modelS/data/cptrho.l5bi.d.15c"
)
R = 6.96e10
XMIN, XMAX = 1e-4, 1.0
RADII = tuple(10.0**i for i in range(10))
CONTROLS = (
    (0.020, 23.97365833326344, 0.01150432239489928),
    (0.024, 24.07633010302372, 0.013783440937996098),
    (0.030, 24.263861625478885, 0.01718034337813724),
)
GRID_NS = (2**18, 2**19)
REL_TOL = 0.005


class InfrastructureFail(RuntimeError):
    pass


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def relerr(a: float, b: float) -> float:
    return abs(a - b) / max(abs(a), abs(b), 1.0)


def scalar_y(profile, x: float, z: float) -> float:
    f = continuous_focal_distance_au(profile, x, R)
    return x * R * (1.0 - z / f)


def scalar_d(profile, x: float, z: float) -> float:
    m = continuous_projected_mass_g(profile, x, R)
    dm = continuous_projected_mass_derivative_g_per_x(profile, x, R)
    f = x * x * R * R * C_CGS * C_CGS / (4.0 * G_CGS * m) / AU_CM
    q = z / f
    return 1.0 + q - x * q * dm / m


def _bulk_focal_factory(profile):
    """0089c algebra, mass/focal only; fixed meshes remain validation-only."""
    rs = np.asarray(profile.radius_fraction, dtype=np.float64)
    ys = np.asarray(profile.density_g_cm3, dtype=np.float64)
    lo = rs[:-1]
    hi = np.minimum(rs[1:], 1.0)
    rho_lo = ys[:-1]
    rho_hi = ys[1:]
    keep = hi > lo
    lo, hi, rho_lo, rho_hi = lo[keep], hi[keep], rho_lo[keep], rho_hi[keep]
    a = (rho_hi - rho_lo) / (hi - lo)
    b = rho_lo - a * lo
    poly_full = a * (hi**4 - lo**4) / 4.0 + b * (hi**3 - lo**3) / 3.0
    factor = 4.0 * math.pi * R**3

    def evaluate(xs, chunk=128):
        xx = np.asarray(xs, dtype=np.float64)
        masses = np.empty_like(xx)
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
                mass_piece += np.where(cross, poly_cross, 0.0)
            q_hi = np.sqrt(np.maximum(0.0, (1.0 - x / hi[None, :]) * (1.0 + x / hi[None, :])))
            q_lo = np.sqrt(np.maximum(0.0, (1.0 - x / lower) * (1.0 + x / lower)))
            fa_hi = (
                (hi[None, :] ** 2 * x**2 / 8.0) * (2.0 / (1.0 + q_hi) + q_hi)
                + (x**4 / 8.0) * np.arccosh(np.maximum(hi[None, :] / x, 1.0))
            )
            fa_lo = (
                (lower**2 * x**2 / 8.0) * (2.0 / (1.0 + q_lo) + q_lo)
                + (x**4 / 8.0) * np.arccosh(np.maximum(lower / x, 1.0))
            )
            fb_hi = (hi[None, :] * x**2 / 3.0) * (1.0 + q_hi + q_hi**2) / (1.0 + q_hi)
            fb_lo = (lower * x**2 / 3.0) * (1.0 + q_lo + q_lo**2) / (1.0 + q_lo)
            cap = a[None, :] * (fa_hi - fa_lo) + b[None, :] * (fb_hi - fb_lo)
            mass_piece += np.where(active, cap, 0.0)
            masses[start:stop] = factor * np.sum(mass_piece, axis=1, dtype=np.float64)
        return xx**2 * R**2 * C_CGS**2 / (4.0 * G_CGS * masses) / AU_CM

    return evaluate


def conformance(profile, bulk):
    rs = [r for r in profile.radius_fraction if XMIN < r < XMAX]
    anchors = sorted(set([XMIN, *rs, XMAX]))
    cells = [(a, b) for a, b in zip(anchors, anchors[1:]) if b > a]
    pts = [1e-4, 3e-4, 1e-3, 0.003, 0.01, 0.02, 0.024, 0.03, 0.05, 0.1, 0.2, 0.4, 0.7, 0.9, 0.99, 0.99999825]
    for j in range(64):
        idx = round(j * (len(cells) - 1) / 63)
        a, b = cells[idx]
        pts.append(0.5 * (a + b))
    pts = sorted(set(pts))
    bf = bulk(pts)
    max_f = 0.0
    for x, f in zip(pts, bf):
        sf = continuous_focal_distance_au(profile, x, R)
        max_f = max(max_f, abs(float(f) - sf) / max(abs(float(f)), abs(sf), 1e-300))
    if max_f > 2e-11:
        raise InfrastructureFail("bulk/scalar focal conformance threshold exceeded")
    return {"point_count": len(pts), "max_focal_symrel": max_f}


def branch_record(profile, z: float, turn: float):
    branches = [(XMIN, turn, -1), (turn, XMAX, +1)]
    records = []
    for i, (lo, hi, expected) in enumerate(branches):
        probes = [lo + (hi - lo) * k / 16.0 for k in range(1, 16)]
        signs = []
        values = [scalar_y(profile, lo, z), scalar_y(profile, hi, z)]
        for x in probes:
            d = scalar_d(profile, x, z)
            if not math.isfinite(d) or d == 0.0:
                raise KernelBlocked("non-finite/zero fixed orientation probe")
            signs.append(1 if d > 0 else -1)
            values.append(scalar_y(profile, x, z))
        if any(s != expected for s in signs):
            raise KernelBlocked("fixed branch orientation contradicts 0089c topology")
        if not all(math.isfinite(v) for v in values):
            raise KernelBlocked("non-finite fixed branch map probe")
        records.append({"index": i, "lo": lo, "hi": hi, "orientation": expected, "probe_signs": signs})
    return records


def evaluate_control(profile, z: float, x0: float, turn: float):
    branches = branch_record(profile, z, turn)
    rows = []
    previous = -1.0
    for radius in RADII:
        accepted = []
        all_crossings = []
        roots_by_target = {0.0: [], radius: [], -radius: []}
        delimiters = []
        for br in branches:
            lo, hi = br["lo"], br["hi"]
            yfn = lambda x, z=z: scalar_y(profile, x, z)
            roots = branch_crossings(yfn, lo, hi, radius)
            for target, x in roots.items():
                residual = abs(yfn(x) - target)
                limit = max(1e-4, 2e-10 * radius)
                if residual > limit:
                    raise KernelScientificFail("crossing residual exceeds frozen V1 limit")
                roots_by_target[target].append(x)
                all_crossings.append({"branch": br["index"], "target_cm": target, "x": x, "residual_cm": residual})
            iv = accepted_branch_interval(yfn, lo, hi, radius, roots)
            local_points = sorted(set([lo, hi, *roots.values()]))
            for a, b in zip(local_points, local_points[1:]):
                mid = 0.5 * (a + b)
                truth = abs(yfn(mid)) <= radius
                # classification from the accepted interval itself
                classified = iv is not None and mid >= iv[0] and mid <= iv[1]
                if truth != classified:
                    raise KernelScientificFail("fixed midpoint classification replica failed")
                delimiters.append({"branch": br["index"], "lo": a, "hi": b, "accepted": classified})
            if iv is not None and iv[1] > iv[0]:
                accepted.append((iv[0], iv[1], br["index"]))
        for target, xs in roots_by_target.items():
            xs.sort()
            if any(b - a <= 1e-9 for a, b in zip(xs, xs[1:])):
                raise KernelScientificFail("same-target root uniqueness <=1e-9")
        zeros = roots_by_target[0.0]
        if not zeros or min(abs(x - x0) for x in zeros) > 1e-10:
            raise KernelScientificFail("generating y=0 root not recovered")
        merged = merge_adjacent_with_parents(accepted)
        area = annular_area_cm2(merged, R)
        if not math.isfinite(area) or area < 0.0 or area > math.pi * R**2 * (1.0 + 1e-10):
            raise KernelScientificFail("area finite/nonnegative/aperture invariant failed")
        if area + 1e-10 * math.pi * R**2 < previous:
            raise KernelScientificFail("accepted area is not non-decreasing")
        previous = area
        rows.append({
            "radius_cm": radius,
            "crossings": all_crossings,
            "accepted_intervals": merged,
            "area_cm2": area,
            "K_geometry_only": area / (math.pi * radius**2),
            "midpoint_subinterval_count": len(delimiters),
        })
    return branches, rows


def one_ring_checks(profile, rows, x0: float, z: float):
    focal = lambda x: continuous_focal_distance_au(profile, x, R)
    out = []
    by_r = {row["radius_cm"]: row for row in rows}
    for r in (100.0, 1000.0, 10000.0):
        row = by_r[r]
        containing = [iv for iv in row["accepted_intervals"] if iv["lo"] <= x0 <= iv["hi"]]
        if len(containing) != 1:
            raise KernelScientificFail("global interval set lacks unique inherited one-ring interval")
        iv = containing[0]
        local_mu = R**2 * (iv["hi"]**2 - iv["lo"]**2) / r**2
        exact_mu = annular_point_source_receiver_mu(x0, r, R, focal)[3]
        re = abs(local_mu - exact_mu) / max(abs(local_mu), abs(exact_mu), 1e-300)
        if re > REL_TOL:
            raise KernelScientificFail("inherited one-ring reproduction exceeds 0.5%")
        if row["K_geometry_only"] + 1e-12 < exact_mu:
            raise KernelScientificFail("global kernel does not contain inherited one-ring contribution")
        out.append({"radius_cm": r, "exact_one_ring_mu": exact_mu, "containing_interval_mu": local_mu, "relative_error": re})
    return out


def main():
    out = Path("g9_0089d_result.json")
    result = {"contract_commit": CONTRACT, "bulk_amendment_commit": BULK_AMENDMENT, "scope": "continuous radial area/kernel geometry only; K is geometry diagnostic"}
    try:
        payload = urllib.request.urlopen(MODEL_S_URL, timeout=30).read()
        blob = git_blob_sha1(payload)
        if blob != MODEL_S_BLOB:
            raise InfrastructureFail("pinned Model-S blob mismatch")
        profile = parse_model_s_text(payload.decode())
        result["model_s_git_blob_sha1"] = blob
        bulk = _bulk_focal_factory(profile)
        result["B0"] = conformance(profile, bulk)

        controls = []
        for x0, z, turn in CONTROLS:
            # exact generating distance must still reproduce from scalar authority
            z_scalar = continuous_focal_distance_au(profile, x0, R)
            if abs(z_scalar - z) / max(abs(z_scalar), abs(z)) > 5e-13:
                raise InfrastructureFail("0089c observer-distance provenance mismatch")
            branches, rows = evaluate_control(profile, z, x0, turn)
            controls.append({"x0": x0, "z_au": z, "turning_root": turn, "branches": branches, "kernel": rows, "one_ring": one_ring_checks(profile, rows, x0, z) if x0 == 0.024 else []})

        # V4: globally fixed meshes, each focal map evaluated once and reused for all radii/controls.
        grid_data = {}
        for n in GRID_NS:
            dx = (XMAX - XMIN) / n
            xs = XMIN + (np.arange(n, dtype=np.float64) + 0.5) * dx
            fs = bulk(xs)
            grid_data[n] = (xs, fs, dx)
        max_branch_grid = 0.0
        max_grid_refine = 0.0
        unresolved_narrow = False
        for control in controls:
            z = control["z_au"]
            area_by_n = {}
            for n, (xs, fs, dx) in grid_data.items():
                ys = xs * R * (1.0 - z / fs)
                vals = {}
                for radius in RADII:
                    vals[radius] = indicator_midpoint_area_cm2(xs, np.abs(ys) <= radius, dx=dx, radius_sun_cm=R)
                area_by_n[n] = vals
            for row in control["kernel"]:
                r = row["radius_cm"]
                a = row["area_cm2"]
                a18, a19 = area_by_n[2**18][r], area_by_n[2**19][r]
                rb = relerr(a, a19)
                rr = relerr(a18, a19)
                max_branch_grid = max(max_branch_grid, rb)
                max_grid_refine = max(max_grid_refine, rr)
                row["indicator_N2p18_area_cm2"] = a18
                row["indicator_N2p19_area_cm2"] = a19
                row["branch_vs_N2p19_relative_difference"] = rb
                row["N2p18_vs_N2p19_relative_difference"] = rr
                minw = min((iv["hi"] - iv["lo"] for iv in row["accepted_intervals"]), default=float("inf"))
                if (rb > REL_TOL or rr > REL_TOL) and minw < (XMAX - XMIN) / (2**19):
                    unresolved_narrow = True
        result["max_branch_vs_N2p19_relative_difference"] = max_branch_grid
        result["max_N2p18_vs_N2p19_relative_difference"] = max_grid_refine
        if max_branch_grid > REL_TOL or max_grid_refine > REL_TOL:
            if unresolved_narrow:
                raise KernelBlocked("fixed indicator replica cannot resolve a finite narrow accepted interval")
            raise KernelScientificFail("frozen V4 0.5% area-replica criterion failed")

        result["controls"] = controls
        result["status"] = "PASS_G9_CONTINUOUS_MAP_MONOTONE_KERNEL"
    except InfrastructureFail as exc:
        result["status"] = "INFRASTRUCTURE_FAIL_G9_CONTINUOUS_MAP_MONOTONE_KERNEL"
        result["reason"] = str(exc)
    except (OSError, urllib.error.URLError) as exc:
        result["status"] = "INFRASTRUCTURE_FAIL_G9_CONTINUOUS_MAP_MONOTONE_KERNEL"
        result["reason"] = str(exc)
    except KernelBlocked as exc:
        result["status"] = "BLOCKED_G9_CONTINUOUS_MAP_MONOTONE_KERNEL"
        result["reason"] = str(exc)
    except KernelScientificFail as exc:
        result["status"] = "SCIENTIFIC_FAIL_G9_CONTINUOUS_MAP_MONOTONE_KERNEL"
        result["reason"] = str(exc)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"].startswith("INFRASTRUCTURE_FAIL"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
