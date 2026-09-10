#!/usr/bin/env python3
"""0105a6o3 certified Tier-B COHERENT Ar central/null reproduction.

Uses exact 0105a6p decimal-text inputs and the 0105a6o2 certified central
root. Publication and dual-anchor thresholds are copied unchanged from the
original pre-fit 0105a6o preregistration. NONDISCOVERY: no observed residual.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

BENCHMARK = "NMIR-V2-0105A6O3"
PREREG_COMMIT = "225c1dc5bd7df6896ebeac47646fb7b80e63b5e0"
ORIGINAL_A6O_PREREG_COMMIT = "a94cbdf5a65618545bd4b1fb4f9fd6c120ae340e"
A6P_MANIFEST_SHA256 = "5b1df47a50dd4dbb2a7fbd5ee64346c2854bdbad0540bfa6f16637eb10b6bada"
A6O2_RESULT_SHA256 = "e3790cb7e2459ef900fda2cfe430be8d47fe497c1365f9c12762bef3f9599d73"
EXPECTED_SHA256 = {
    "datanobkgsub.txt": "dabf3d80f13959f4b94b77c9b56f7347a645105801e8cc177424e7ffcf7c7f66",
    "cevnspdf.txt": "3b1d5b25749e8d8e1cfdf5c32e48f026ce4aafec0a80632b3a63273e6e0e1f37",
    "brnpdf.txt": "02664ce6a84eca8c6146b6502497bc5d8165df945da132193622334ff4ff826f",
    "delbrnpdf.txt": "ebccca6c1650b0ace71fdbaade7a80ea289a99ff3c120266ae6ecf0083df5c63",
    "bkgpdf.txt": "36c89291dde3032a19ca7a8e64510d036d7b40c34b0805ce475a13ccfa739dd1",
}
FILES = {
    "n": "datanobkgsub.txt",
    "S": "cevnspdf.txt",
    "P": "brnpdf.txt",
    "D": "delbrnpdf.txt",
    "B": "bkgpdf.txt",
}
PUB_TARGETS = {
    "NC": (mp.mpf("159"), mp.mpf("2.0")),
    "NP": (mp.mpf("553"), mp.mpf("3.0")),
    "ND": (mp.mpf("10"), mp.mpf("3.0")),
    "NB": (mp.mpf("3131"), mp.mpf("3.0")),
    "sigma_profile": (mp.mpf("43"), mp.mpf("2.0")),
    "Z_stat": (mp.mpf("3.9"), mp.mpf("0.15")),
}
ROBUSTNESS = {
    "NC": mp.mpf("1.0"),
    "NP": mp.mpf("1.0"),
    "ND": mp.mpf("1.0"),
    "Z_stat": mp.mpf("0.05"),
    "sigma_profile": mp.mpf("0.5"),
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_fourth(path: Path):
    coords, values = [], []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        fields = line.split()
        if len(fields) != 4:
            raise ValueError(f"{path.name}: invalid field count at line {line_number}")
        coords.append(tuple(fields[:3]))
        values.append(mp.mpf(fields[3]))
    if len(values) != 960:
        raise ValueError(f"{path.name}: expected 960 rows, observed {len(values)}")
    return coords, values


def load_exact(files_dir: Path):
    mp.mp.dps = 100
    for name, expected in EXPECTED_SHA256.items():
        path = files_dir / name
        if not path.exists() or sha256_file(path) != expected:
            raise ValueError(f"exact SHA256 mismatch: {name}")
    parsed = {key: parse_fourth(files_dir / name) for key, name in FILES.items()}
    reference = parsed["n"][0]
    if any(coords != reference for coords, _ in parsed.values()):
        raise ValueError("coordinate token mismatch")
    raw = {key: values for key, (_, values) in parsed.items()}
    if any(value < 0 for values in raw.values() for value in values):
        raise ValueError("negative exact input value")
    sums = {key: mp.fsum(values) for key, values in raw.items()}
    checks = {
        "data_3752": abs(sums["n"] - mp.mpf("3752")) <= mp.mpf("1e-9"),
        "cevns_128": abs(sums["S"] - mp.mpf("128")) <= mp.mpf("0.05"),
        "prompt_497": abs(sums["P"] - mp.mpf("497")) <= mp.mpf("0.05"),
        "delayed_33": abs(sums["D"] - mp.mpf("33")) <= mp.mpf("0.05"),
        "steady_3152_or_3154": min(abs(sums["B"] - mp.mpf("3152")), abs(sums["B"] - mp.mpf("3154"))) <= mp.mpf("0.05"),
    }
    if not all(checks.values()):
        raise ValueError("central structural normalization gate failed")
    shapes = {key: [value / sums[key] for value in raw[key]] for key in ("S", "P", "D", "B")}
    rows = list(zip(raw["n"], shapes["S"], shapes["P"], shapes["D"], shapes["B"]))
    return rows, sums, checks


def full_qgh(theta, rows, B0):
    Q = mp.mpf("0")
    g = [mp.mpf("0") for _ in range(4)]
    H = [[mp.mpf("0") for _ in range(4)] for _ in range(4)]
    for ni, Si, Pi, Di, Bi in rows:
        a = (Si, Pi, Di, Bi)
        mu = theta[0] * Si + theta[1] * Pi + theta[2] * Di + theta[3] * Bi
        if mu <= 0:
            return None, None, None
        Q += 2 * (mu - (ni * mp.log(mu) if ni > 0 else 0))
        factor = 2 * (1 - ni / mu)
        for j in range(4):
            g[j] += factor * a[j]
        if ni > 0:
            curvature = 2 * ni / (mu * mu)
            for j in range(4):
                for k in range(4):
                    H[j][k] += curvature * a[j] * a[k]
    centers = (None, mp.mpf("497"), mp.mpf("33"), B0)
    sigmas = (None, mp.mpf("160"), mp.mpf("33"), mp.mpf("25"))
    for j in range(1, 4):
        delta = theta[j] - centers[j]
        Q += (delta / sigmas[j]) ** 2
        g[j] += 2 * delta / sigmas[j] ** 2
        H[j][j] += 2 / sigmas[j] ** 2
    return Q, g, H


def profile_qgh(backgrounds, NC, rows, B0):
    NP, ND, NB = backgrounds
    Q = mp.mpf("0")
    g = [mp.mpf("0"), mp.mpf("0"), mp.mpf("0")]
    H = [[mp.mpf("0") for _ in range(3)] for _ in range(3)]
    for ni, Si, Pi, Di, Bi in rows:
        a = (Pi, Di, Bi)
        mu = NC * Si + NP * Pi + ND * Di + NB * Bi
        if mu <= 0:
            return None, None, None
        Q += 2 * (mu - (ni * mp.log(mu) if ni > 0 else 0))
        factor = 2 * (1 - ni / mu)
        for j in range(3):
            g[j] += factor * a[j]
        if ni > 0:
            curvature = 2 * ni / (mu * mu)
            for j in range(3):
                for k in range(3):
                    H[j][k] += curvature * a[j] * a[k]
    centers = (mp.mpf("497"), mp.mpf("33"), B0)
    sigmas = (mp.mpf("160"), mp.mpf("33"), mp.mpf("25"))
    for j in range(3):
        delta = backgrounds[j] - centers[j]
        Q += (delta / sigmas[j]) ** 2
        g[j] += 2 * delta / sigmas[j] ** 2
        H[j][j] += 2 / sigmas[j] ** 2
    return Q, g, H


def inf_norm(values):
    return max(abs(value) for value in values)


def principal_minors_3(H):
    first = H[0][0]
    second = H[0][0] * H[1][1] - H[0][1] * H[1][0]
    third = (
        H[0][0] * (H[1][1] * H[2][2] - H[1][2] * H[2][1])
        - H[0][1] * (H[1][0] * H[2][2] - H[1][2] * H[2][0])
        + H[0][2] * (H[1][0] * H[2][1] - H[1][1] * H[2][0])
    )
    return [first, second, third]


def solve_profile(NC, rows, B0):
    backgrounds = [mp.mpf("497"), mp.mpf("33"), B0]
    Q, g, H = profile_qgh(backgrounds, NC, rows, B0)
    if Q is None:
        raise RuntimeError("profile start outside positive-mu domain")
    backtracks_total = 0
    for iteration in range(201):
        if inf_norm(g) <= mp.mpf("1e-50"):
            minors = principal_minors_3(H)
            if not all(value > 0 for value in minors):
                raise RuntimeError("profile Hessian is not positive definite")
            return backgrounds, Q, inf_norm(g), iteration, minors, backtracks_total
        if iteration == 200:
            break
        matrix = mp.matrix(H)
        step = mp.lu_solve(matrix, -mp.matrix(g))
        alpha = mp.mpf("1")
        accepted = False
        for backtrack in range(81):
            candidate = [backgrounds[j] + alpha * step[j] for j in range(3)]
            if min(candidate) > 0:
                new_Q, new_g, new_H = profile_qgh(candidate, NC, rows, B0)
                if new_Q is not None and new_Q < Q:
                    backgrounds, Q, g, H = candidate, new_Q, new_g, new_H
                    backtracks_total += backtrack
                    accepted = True
                    break
            alpha /= 2
        if not accepted:
            raise RuntimeError(f"profile line search failed at NC={NC}")
    raise RuntimeError("profile Newton iteration cap exceeded")


def bisection_crossing(left, right, left_value, right_value, rows, B0, Q_best, cache):
    if left_value * right_value > 0:
        raise RuntimeError("profile crossing is not bracketed")
    iterations = 0
    while right - left > mp.mpf("1e-6"):
        middle = (left + right) / 2
        middle_value = profile_delta(middle, rows, B0, Q_best, cache)
        if left_value * middle_value <= 0:
            right, right_value = middle, middle_value
        else:
            left, left_value = middle, middle_value
        iterations += 1
    return (left + right) / 2, iterations


def profile_delta(NC, rows, B0, Q_best, cache):
    key = mp.nstr(NC, 110)
    if key not in cache:
        backgrounds, Q, grad_norm, iterations, minors, backtracks = solve_profile(NC, rows, B0)
        cache[key] = {
            "backgrounds": backgrounds,
            "Q": Q,
            "gradient_inf": grad_norm,
            "iterations": iterations,
            "minors": minors,
            "backtracks": backtracks,
        }
    return cache[key]["Q"] - Q_best - 1


def as_string(value, digits=60):
    return mp.nstr(value, digits, strip_zeros=False)


def parent_central_root(parent, branch_name):
    branch = parent["branches"][branch_name]
    if not branch.get("pass"):
        raise ValueError(f"parent certificate branch not PASS: {branch_name}")
    return [mp.mpf(value) for value in branch["P200"][0]["x"]]


def evaluate_branch(branch_name, B0, central, rows):
    Q_best, central_gradient, central_hessian = full_qgh(central, rows, B0)
    if Q_best is None or inf_norm(central_gradient) > mp.mpf("1e-30"):
        raise RuntimeError("parent central root does not certify under o3 exact objective")

    cache = {}
    null_backgrounds, Q_null, null_grad, null_iterations, null_minors, null_backtracks = solve_profile(mp.mpf("0"), rows, B0)
    cache[mp.nstr(mp.mpf("0"), 110)] = {
        "backgrounds": null_backgrounds,
        "Q": Q_null,
        "gradient_inf": null_grad,
        "iterations": null_iterations,
        "minors": null_minors,
        "backtracks": null_backtracks,
    }
    q0 = Q_null - Q_best
    Z = mp.sqrt(max(q0, mp.mpf("0")))
    NC_best = central[0]

    F0 = Q_null - Q_best - 1
    if F0 <= 0:
        lower = mp.mpf("0")
        lower_iterations = 0
        lower_boundary = True
    else:
        Fbest = profile_delta(NC_best, rows, B0, Q_best, cache)
        lower, lower_iterations = bisection_crossing(mp.mpf("0"), NC_best, F0, Fbest, rows, B0, Q_best, cache)
        lower_boundary = False

    Fbest = profile_delta(NC_best, rows, B0, Q_best, cache)
    upper_endpoint = 2 * NC_best
    Fupper = profile_delta(upper_endpoint, rows, B0, Q_best, cache)
    expansions = 0
    while Fupper <= 0 and expansions < 20:
        upper_endpoint *= 2
        Fupper = profile_delta(upper_endpoint, rows, B0, Q_best, cache)
        expansions += 1
    if Fupper <= 0:
        raise RuntimeError("upper profile crossing not bracketed within 20 expansions")
    upper, upper_iterations = bisection_crossing(NC_best, upper_endpoint, Fbest, Fupper, rows, B0, Q_best, cache)
    sigma_profile = (upper - lower) / 2

    values = {
        "NC": central[0],
        "NP": central[1],
        "ND": central[2],
        "NB": central[3],
        "sigma_profile": sigma_profile,
        "Z_stat": Z,
    }
    publication_checks = {
        key: abs(values[key] - target) <= tolerance
        for key, (target, tolerance) in PUB_TARGETS.items()
    }
    return {
        "branch": branch_name,
        "B0": as_string(B0),
        "best_fit": {key: as_string(values[key]) for key in ("NC", "NP", "ND", "NB")},
        "Q_best": as_string(Q_best),
        "central_gradient_inf": as_string(inf_norm(central_gradient)),
        "null_fit": {
            "NC": "0",
            "NP": as_string(null_backgrounds[0]),
            "ND": as_string(null_backgrounds[1]),
            "NB": as_string(null_backgrounds[2]),
            "Q": as_string(Q_null),
            "gradient_inf": as_string(null_grad),
            "iterations": null_iterations,
            "backtracks_total": null_backtracks,
        },
        "q0": as_string(q0),
        "Z_stat": as_string(Z),
        "profile_1sigma": {
            "lower": as_string(lower),
            "upper": as_string(upper),
            "half_width": as_string(sigma_profile),
            "lower_is_physical_boundary": lower_boundary,
            "lower_bisection_iterations": lower_iterations,
            "upper_bisection_iterations": upper_iterations,
            "upper_bracket_expansions": expansions,
            "unique_profile_points_solved": len(cache),
        },
        "publication_checks": publication_checks,
        "publication_pass": all(publication_checks.values()),
        "values_mp": values,
    }


def execute(files_dir: Path, parent_result_path: Path):
    mp.mp.dps = 100
    if sha256_file(parent_result_path) != A6O2_RESULT_SHA256:
        raise ValueError("0105a6o2 result SHA mismatch")
    parent = json.loads(parent_result_path.read_text(encoding="utf-8"))
    if parent.get("classification") != "PASS_0105A6O2_STRICT_CONVEX_UNIQUE_HIGH_PRECISION_OPTIMUM_NONDISCOVERY":
        raise ValueError("0105a6o2 parent classification is not PASS")

    rows, sums, structural_checks = load_exact(files_dir)
    branches = {}
    internal = {}
    for branch_name, B0_text in (("R3152", "3152"), ("R3154", "3154")):
        B0 = mp.mpf(B0_text)
        central = parent_central_root(parent, branch_name)
        evaluated = evaluate_branch(branch_name, B0, central, rows)
        internal[branch_name] = evaluated.pop("values_mp")
        branches[branch_name] = evaluated

    differences = {
        key: abs(internal["R3152"][key] - internal["R3154"][key])
        for key in ROBUSTNESS
    }
    robustness_checks = {key: differences[key] <= ROBUSTNESS[key] for key in ROBUSTNESS}
    both_publication = all(branch["publication_pass"] for branch in branches.values())
    robustness_pass = all(robustness_checks.values())

    if not both_publication:
        classification = "BLOCKED_0105A6O3_PUBLICATION_TARGET_MISMATCH"
    elif not robustness_pass:
        classification = "BLOCKED_0105A6O3_DUAL_ANCHOR_SENSITIVITY"
    else:
        classification = "PASS_0105A6O3_TIERB_ARGON_CERTIFIED_CENTRAL_NULL_REPRODUCTION_NONDISCOVERY"

    return {
        "benchmark": BENCHMARK,
        "preregistration_commit": PREREG_COMMIT,
        "original_a6o_preregistration_commit": ORIGINAL_A6O_PREREG_COMMIT,
        "parent_a6o2_result_sha256": A6O2_RESULT_SHA256,
        "structural_gate": {
            "checks": structural_checks,
            "template_sums": {key: as_string(value) for key, value in sums.items()},
            "pass": all(structural_checks.values()),
        },
        "branches": branches,
        "dual_anchor_differences": {key: as_string(value) for key, value in differences.items()},
        "dual_anchor_robustness_checks": robustness_checks,
        "dual_anchor_robustness_pass": robustness_pass,
        "both_publication_targets_pass": both_publication,
        "classification": classification,
        "shape_systematic_excursion_preregistration_permission_percent": 100 if classification.startswith("PASS_") else 0,
        "tierA_exact_collaboration_internal_likelihood": "BLOCKED",
        "observed_bsm_residual_permission_percent": 0,
        "observed_bsm_residual_inspected": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files-dir", required=True)
    parser.add_argument("--a6p-manifest", required=True)
    parser.add_argument("--a6o2-result", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--git-sha", required=True)
    args = parser.parse_args()

    try:
        manifest_path = Path(args.a6p_manifest)
        if sha256_file(manifest_path) != A6P_MANIFEST_SHA256:
            raise ValueError("a6p manifest SHA mismatch")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not manifest.get("central_ready"):
            raise ValueError("a6p central_ready false")
        result = execute(Path(args.files_dir), Path(args.a6o2_result))
        result["git_sha"] = args.git_sha
    except Exception as exc:
        result = {
            "benchmark": BENCHMARK,
            "preregistration_commit": PREREG_COMMIT,
            "git_sha": args.git_sha,
            "classification": "BLOCKED_0105A6O3_AUTHORITY_OR_NUMERICAL_CERTIFICATE_FAILURE",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "shape_systematic_excursion_preregistration_permission_percent": 0,
            "tierA_exact_collaboration_internal_likelihood": "BLOCKED",
            "observed_bsm_residual_permission_percent": 0,
            "observed_bsm_residual_inspected": False,
        }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
