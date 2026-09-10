#!/usr/bin/env python3
"""0105a6o Tier-B COHERENT Ar central/null reproduction.

This executes only the prospectively preregistered release-consistent null
benchmark. It never constructs or inspects a BSM/model-agnostic residual.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, minimize

BENCHMARK = "NMIR-V2-0105A6O"
PREREG_COMMIT = "a94cbdf5a65618545bd4b1fb4f9fd6c120ae340e"
A6P_MANIFEST_SHA256 = "5b1df47a50dd4dbb2a7fbd5ee64346c2854bdbad0540bfa6f16637eb10b6bada"

EXPECTED_SHA256 = {
    "datanobkgsub.txt": "dabf3d80f13959f4b94b77c9b56f7347a645105801e8cc177424e7ffcf7c7f66",
    "cevnspdf.txt": "3b1d5b25749e8d8e1cfdf5c32e48f026ce4aafec0a80632b3a63273e6e0e1f37",
    "brnpdf.txt": "02664ce6a84eca8c6146b6502497bc5d8165df945da132193622334ff4ff826f",
    "delbrnpdf.txt": "ebccca6c1650b0ace71fdbaade7a80ea289a99ff3c120266ae6ecf0083df5c63",
    "bkgpdf.txt": "36c89291dde3032a19ca7a8e64510d036d7b40c34b0805ce475a13ccfa739dd1",
    "LArParametersAnlA.yaml": "a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e",
}

E_CENTERS = np.arange(5.0, 120.0, 10.0)
F90_CENTERS = np.arange(0.525, 0.9, 0.05)
T_CENTERS = np.arange(0.15, 4.9, 0.5)
EXPECTED_GRID = np.array([(e, f, t) for e in E_CENTERS for f in F90_CENTERS for t in T_CENTERS], dtype=float)

PUB_TARGETS = {
    "NC": (159.0, 2.0),
    "NP": (553.0, 3.0),
    "ND": (10.0, 3.0),
    "NB": (3131.0, 3.0),
    "sigma_profile": (43.0, 2.0),
    "Z_stat": (3.9, 0.15),
}
ROBUST = {"NC": 1.0, "NP": 1.0, "ND": 1.0, "Z_stat": 0.05, "sigma_profile": 0.5}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_4col(path: Path):
    arr = np.loadtxt(path, dtype=float)
    if arr.shape != (960, 4):
        raise ValueError(f"{path.name}: expected (960,4), observed {arr.shape}")
    return arr[:, :3], arr[:, 3]


def verify_grid(coords: np.ndarray, label: str):
    if coords.shape != EXPECTED_GRID.shape or not np.array_equal(coords, EXPECTED_GRID):
        # no rounding/tolerance repair is permitted by preregistration
        raise ValueError(f"{label}: coordinate grid differs from frozen exact numeric coordinates")


def structural_gate(files_dir: Path) -> dict:
    for name, expected in EXPECTED_SHA256.items():
        p = files_dir / name
        if not p.exists():
            raise ValueError(f"missing exact input {name}")
        if sha256_file(p) != expected:
            raise ValueError(f"SHA256 mismatch for {name}")

    arrays = {}
    for name in ("datanobkgsub.txt", "cevnspdf.txt", "brnpdf.txt", "delbrnpdf.txt", "bkgpdf.txt"):
        coords, vals = parse_4col(files_dir / name)
        verify_grid(coords, name)
        if not np.isfinite(vals).all() or (vals < 0).any():
            raise ValueError(f"{name}: non-finite or negative values")
        arrays[name] = vals

    sums = {name: float(vals.sum()) for name, vals in arrays.items()}
    checks = {
        "data_3752": abs(sums["datanobkgsub.txt"] - 3752.0) <= 1e-9,
        "cevns_128": abs(sums["cevnspdf.txt"] - 128.0) <= 0.05,
        "prompt_497": abs(sums["brnpdf.txt"] - 497.0) <= 0.05,
        "delayed_33": abs(sums["delbrnpdf.txt"] - 33.0) <= 0.05,
        "steady_matches_3152_or_3154": min(abs(sums["bkgpdf.txt"] - 3152.0), abs(sums["bkgpdf.txt"] - 3154.0)) <= 0.05,
    }
    if not all(checks.values()):
        raise ValueError(f"structural normalization gate failed: sums={sums}, checks={checks}")

    n = arrays["datanobkgsub.txt"]
    shapes = {
        "S": arrays["cevnspdf.txt"] / sums["cevnspdf.txt"],
        "P": arrays["brnpdf.txt"] / sums["brnpdf.txt"],
        "D": arrays["delbrnpdf.txt"] / sums["delbrnpdf.txt"],
        "B": arrays["bkgpdf.txt"] / sums["bkgpdf.txt"],
    }
    return {"n": n, "shapes": shapes, "sums": sums, "checks": checks}


def q_value(theta, n, shapes, B0: float, fixed_nc=None):
    if fixed_nc is None:
        NC, NP, ND, NB = map(float, theta)
    else:
        NC = float(fixed_nc)
        NP, ND, NB = map(float, theta)
    if min(NC, NP, ND, NB) < 0:
        return float("inf")
    mu = NC * shapes["S"] + NP * shapes["P"] + ND * shapes["D"] + NB * shapes["B"]
    if np.any(mu < 0) or np.any((mu <= 0) & (n > 0)):
        return float("inf")
    term = np.where(n > 0, mu - n * np.log(mu), mu)
    penalty = ((NP - 497.0) / 160.0) ** 2 + ((ND - 33.0) / 33.0) ** 2 + ((NB - B0) / 25.0) ** 2
    return float(2.0 * term.sum() + penalty)


def primary_best_fit(n, shapes, B0: float):
    starts = [
        [128.0, 497.0, 33.0, B0],
        [159.0, 553.0, 10.0, 3131.0],
        [0.0, 497.0, 33.0, B0],
        [256.0, 497.0, 33.0, B0],
    ]
    results = []
    for x0 in starts:
        r = minimize(
            q_value, x0=np.array(x0), args=(n, shapes, B0, None), method="L-BFGS-B",
            bounds=[(0.0, None)] * 4,
            options={"ftol": 1e-12, "gtol": 1e-9, "maxiter": 20000},
        )
        if r.success and np.isfinite(r.fun):
            results.append({"x0": x0, "x": r.x, "q": float(r.fun), "nit": int(r.nit), "message": str(r.message)})
    if not results:
        raise RuntimeError("no successful L-BFGS-B start")
    best = min(results, key=lambda x: x["q"])
    for r in results:
        if np.max(np.abs(r["x"] - best["x"])) > 1e-4 or abs(r["q"] - best["q"]) > 1e-7:
            raise RuntimeError("L-BFGS-B multi-start instability exceeds frozen tolerance")

    powell = minimize(
        q_value, x0=best["x"], args=(n, shapes, B0, None), method="Powell",
        bounds=[(0.0, None)] * 4,
        options={"xtol": 1e-10, "ftol": 1e-12, "maxiter": 50000},
    )
    if not powell.success or not np.isfinite(powell.fun):
        raise RuntimeError("Powell cross-check failed")
    if np.max(np.abs(powell.x - best["x"])) > 0.02 or abs(float(powell.fun) - best["q"]) > 1e-5:
        raise RuntimeError("Powell cross-check disagrees with primary optimum")
    return best, results, powell


def profile_backgrounds(n, shapes, B0: float, NC: float, start3):
    candidates = [np.array(start3, dtype=float), np.array([497.0, 33.0, B0], dtype=float)]
    outs = []
    for x0 in candidates:
        r = minimize(
            q_value, x0=x0, args=(n, shapes, B0, NC), method="L-BFGS-B",
            bounds=[(0.0, None)] * 3,
            options={"ftol": 1e-12, "gtol": 1e-9, "maxiter": 20000},
        )
        if r.success and np.isfinite(r.fun):
            outs.append(r)
    if not outs:
        raise RuntimeError(f"profile failed at NC={NC}")
    return min(outs, key=lambda r: r.fun)


def fit_branch(n, shapes, B0: float) -> dict:
    best, starts, powell = primary_best_fit(n, shapes, B0)
    NC, NP, ND, NB = map(float, best["x"])
    qbest = float(best["q"])
    bgstart = [NP, ND, NB]

    null = profile_backgrounds(n, shapes, B0, 0.0, bgstart)
    qnull = float(null.fun)
    q0 = max(0.0, qnull - qbest)
    z = math.sqrt(q0)

    def delta(nc):
        return float(profile_backgrounds(n, shapes, B0, float(nc), bgstart).fun - qbest - 1.0)

    lower_boundary = False
    if NC <= 0:
        lower = 0.0
        lower_boundary = True
    else:
        d0 = delta(0.0)
        if d0 <= 0:
            lower = 0.0
            lower_boundary = True
        else:
            lower = float(brentq(delta, 0.0, NC, xtol=1e-6, rtol=1e-12, maxiter=200))

    upper_hi = max(NC + 50.0, NC * 1.5, 50.0)
    for _ in range(30):
        if delta(upper_hi) > 0:
            break
        upper_hi *= 1.5
    else:
        raise RuntimeError("failed to bracket upper profile crossing")
    upper = float(brentq(delta, NC, upper_hi, xtol=1e-6, rtol=1e-12, maxiter=200))
    sigma_profile = (upper - lower) / 2.0

    vals = {"NC": NC, "NP": NP, "ND": ND, "NB": NB, "sigma_profile": sigma_profile, "Z_stat": z}
    publication_checks = {k: abs(vals[k] - target) <= tol for k, (target, tol) in PUB_TARGETS.items()}
    return {
        "B0": B0,
        "best_fit": {"NC": NC, "NP": NP, "ND": ND, "NB": NB, "Q": qbest},
        "null_fit": {"NC": 0.0, "NP": float(null.x[0]), "ND": float(null.x[1]), "NB": float(null.x[2]), "Q": qnull},
        "q0": q0,
        "Z_stat": z,
        "profile_1sigma": {"lower": lower, "upper": upper, "half_width": sigma_profile, "lower_is_physical_boundary": lower_boundary},
        "publication_checks": publication_checks,
        "publication_pass": all(publication_checks.values()),
        "lbfgsb_starts": [{"x0": r["x0"], "x": [float(x) for x in r["x"]], "Q": r["q"], "nit": r["nit"]} for r in starts],
        "powell_crosscheck": {"x": [float(x) for x in powell.x], "Q": float(powell.fun), "nit": int(powell.nit)},
    }


def run(files_dir: Path) -> dict:
    s = structural_gate(files_dir)
    branches = {"R3152": fit_branch(s["n"], s["shapes"], 3152.0), "R3154": fit_branch(s["n"], s["shapes"], 3154.0)}
    a = branches["R3152"]
    b = branches["R3154"]
    diffs = {
        "NC": abs(a["best_fit"]["NC"] - b["best_fit"]["NC"]),
        "NP": abs(a["best_fit"]["NP"] - b["best_fit"]["NP"]),
        "ND": abs(a["best_fit"]["ND"] - b["best_fit"]["ND"]),
        "Z_stat": abs(a["Z_stat"] - b["Z_stat"]),
        "sigma_profile": abs(a["profile_1sigma"]["half_width"] - b["profile_1sigma"]["half_width"]),
    }
    robust_checks = {k: diffs[k] <= ROBUST[k] for k in ROBUST}
    all_pub = all(x["publication_pass"] for x in branches.values())
    robust_pass = all(robust_checks.values())
    overall = all_pub and robust_pass
    return {
        "benchmark": BENCHMARK,
        "preregistration_commit": PREREG_COMMIT,
        "tier": "release-consistent independent reproduction",
        "tierA_exact_collaboration_internal_likelihood": "BLOCKED",
        "structural_gate": {"template_sums": s["sums"], "checks": s["checks"], "pass": True},
        "branches": branches,
        "dual_anchor_differences": diffs,
        "dual_anchor_robustness_checks": robust_checks,
        "dual_anchor_robustness_pass": robust_pass,
        "both_publication_targets_pass": all_pub,
        "classification": (
            "PASS_0105A6O_TIERB_ARGON_CENTRAL_NULL_REPRODUCTION_NONDISCOVERY"
            if overall else "BLOCKED_0105A6O_TIERB_ARGON_CENTRAL_NULL_REPRODUCTION_MISMATCH"
        ),
        "systematic_excursion_preregistration_permission_percent": 100 if overall else 0,
        "observed_bsm_residual_permission_percent": 0,
        "observed_bsm_residual_inspected": False,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--files-dir", required=True)
    ap.add_argument("--a6p-manifest", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--git-sha", required=True)
    ns = ap.parse_args()
    manifest_path = Path(ns.a6p_manifest)
    if sha256_file(manifest_path) != A6P_MANIFEST_SHA256:
        raise SystemExit("a6p manifest SHA256 mismatch")
    manifest = json.loads(manifest_path.read_text())
    if not manifest.get("central_ready"):
        raise SystemExit("a6p central_ready is false")
    try:
        result = run(Path(ns.files_dir))
    except Exception as exc:
        result = {
            "benchmark": BENCHMARK,
            "preregistration_commit": PREREG_COMMIT,
            "git_sha": ns.git_sha,
            "classification": "BLOCKED_0105A6O_TIERB_ARGON_CENTRAL_NULL_REPRODUCTION_EXECUTION_OR_STRUCTURAL_FAILURE",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "systematic_excursion_preregistration_permission_percent": 0,
            "observed_bsm_residual_permission_percent": 0,
            "observed_bsm_residual_inspected": False,
        }
    else:
        result["git_sha"] = ns.git_sha
    out = Path(ns.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
