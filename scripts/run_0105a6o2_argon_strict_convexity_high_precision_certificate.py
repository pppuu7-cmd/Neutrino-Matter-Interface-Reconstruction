#!/usr/bin/env python3
"""0105a6o2 strict-convexity and arbitrary-precision optimum certificate.

Nondiscovery only. Uses exact 0105a6p decimal-text central inputs and the
unchanged 0105a6o central objective. It performs no publication-target,
systematic-excursion, residual, or BSM classification.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

BENCHMARK = "NMIR-V2-0105A6O2"
PREREG_COMMIT = "07a61181b7fb2b8f7041250c3b9bf1de1aeee0e4"
AMENDMENT_COMMIT = "29c529ccdf1c4d586367e0dd1f7822e1e6999291"
A6P_MANIFEST_SHA256 = "5b1df47a50dd4dbb2a7fbd5ee64346c2854bdbad0540bfa6f16637eb10b6bada"
EXPECTED_SHA256 = {
    "datanobkgsub.txt": "dabf3d80f13959f4b94b77c9b56f7347a645105801e8cc177424e7ffcf7c7f66",
    "cevnspdf.txt": "3b1d5b25749e8d8e1cfdf5c32e48f026ce4aafec0a80632b3a63273e6e0e1f37",
    "brnpdf.txt": "02664ce6a84eca8c6146b6502497bc5d8165df945da132193622334ff4ff826f",
    "delbrnpdf.txt": "ebccca6c1650b0ace71fdbaade7a80ea289a99ff3c120266ae6ecf0083df5c63",
    "bkgpdf.txt": "36c89291dde3032a19ca7a8e64510d036d7b40c34b0805ce475a13ccfa739dd1",
}
NAMES = {
    "n": "datanobkgsub.txt",
    "S": "cevnspdf.txt",
    "P": "brnpdf.txt",
    "D": "delbrnpdf.txt",
    "B": "bkgpdf.txt",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_decimal_fourth(path: Path):
    values = []
    coordinates = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        fields = line.split()
        if len(fields) != 4:
            raise ValueError(f"{path.name}: line {line_number} does not have four fields")
        coordinates.append(tuple(fields[:3]))
        values.append(mp.mpf(fields[3]))
    if len(values) != 960:
        raise ValueError(f"{path.name}: expected 960 rows, observed {len(values)}")
    return coordinates, values


def load_exact(files_dir: Path, dps: int):
    mp.mp.dps = dps
    for name, expected in EXPECTED_SHA256.items():
        path = files_dir / name
        if not path.exists() or sha256_file(path) != expected:
            raise ValueError(f"exact SHA256 mismatch: {name}")

    parsed = {key: parse_decimal_fourth(files_dir / filename) for key, filename in NAMES.items()}
    reference_coordinates = parsed["n"][0]
    for key, (coordinates, _) in parsed.items():
        if coordinates != reference_coordinates:
            raise ValueError(f"coordinate token mismatch: {key}")

    raw = {key: values for key, (_, values) in parsed.items()}
    if any(value < 0 for values in raw.values() for value in values):
        raise ValueError("negative exact input value")

    sums = {key: mp.fsum(values) for key, values in raw.items()}
    shapes = {key: [value / sums[key] for value in raw[key]] for key in ("S", "P", "D", "B")}
    overlap = sum(1 for ni, si in zip(raw["n"], shapes["S"]) if ni > 0 and si > 0)

    strict_convexity = {
        "exact_sha256_all": True,
        "all_inputs_nonnegative": True,
        "positive_count_positive_signal_overlap_bins": overlap,
        "positive_count_positive_signal_overlap_exists": overlap > 0,
        "background_penalty_curvatures_strictly_positive": True,
        "algebraic_strict_convexity_certified": overlap > 0,
    }
    return raw["n"], shapes, sums, strict_convexity


def qgh(theta, n, shapes, B0):
    """Exact central objective, gradient, and Hessian at current mp precision."""
    Q = mp.mpf("0")
    gradient = mp.matrix(4, 1)
    hessian = mp.matrix(4, 4)
    for j in range(4):
        gradient[j] = mp.mpf("0")
        for k in range(4):
            hessian[j, k] = mp.mpf("0")

    keys = ("S", "P", "D", "B")
    for i, ni in enumerate(n):
        row = [shapes[key][i] for key in keys]
        mu = mp.fsum(theta[j] * row[j] for j in range(4))
        if mu <= 0:
            return None, None, None
        Q += 2 * (mu - (ni * mp.log(mu) if ni > 0 else 0))
        factor = 2 * (1 - ni / mu)
        for j in range(4):
            gradient[j] += factor * row[j]
        if ni > 0:
            curvature = 2 * ni / (mu * mu)
            for j in range(4):
                for k in range(4):
                    hessian[j, k] += curvature * row[j] * row[k]

    centers = (None, mp.mpf("497"), mp.mpf("33"), B0)
    sigmas = (None, mp.mpf("160"), mp.mpf("33"), mp.mpf("25"))
    for j in range(1, 4):
        delta = theta[j] - centers[j]
        Q += (delta / sigmas[j]) ** 2
        gradient[j] += 2 * delta / sigmas[j] ** 2
        hessian[j, j] += 2 / sigmas[j] ** 2
    return Q, gradient, hessian


def infinity_norm(vector):
    return max(abs(vector[j]) for j in range(4))


def leading_principal_minors(matrix):
    out = []
    for order in range(1, 5):
        block = mp.matrix(order, order)
        for i in range(order):
            for j in range(order):
                block[i, j] = matrix[i, j]
        out.append(mp.det(block))
    return out


def newton(files_dir: Path, B0_text: str, start, dps: int, gradient_tolerance_text: str):
    n, shapes, sums, strict_convexity = load_exact(files_dir, dps)
    B0 = mp.mpf(B0_text)
    theta = mp.matrix([mp.mpf(str(value)) for value in start])
    Q, gradient, hessian = qgh(theta, n, shapes, B0)
    if Q is None:
        raise RuntimeError("initial point outside positive-mu domain")

    tolerance = mp.mpf(gradient_tolerance_text)
    backtracks_total = 0
    for iteration in range(201):
        grad_norm = infinity_norm(gradient)
        if grad_norm <= tolerance:
            minors = leading_principal_minors(hessian)
            return {
                "x_mp": theta,
                "Q_mp": Q,
                "g_mp": gradient,
                "H_mp": hessian,
                "iterations": iteration,
                "backtracks_total": backtracks_total,
                "gradient_inf": grad_norm,
                "leading_principal_minors": minors,
                "hessian_positive_definite": all(value > 0 for value in minors),
                "sums": sums,
                "c1": strict_convexity,
            }
        if iteration == 200:
            break

        step = mp.lu_solve(hessian, -gradient)
        alpha = mp.mpf("1")
        accepted = False
        for backtrack in range(81):
            candidate = theta + alpha * step
            if min(candidate) > 0:
                new_Q, new_gradient, new_hessian = qgh(candidate, n, shapes, B0)
                if new_Q is not None and new_Q < Q:
                    theta, Q, gradient, hessian = candidate, new_Q, new_gradient, new_hessian
                    backtracks_total += backtrack
                    accepted = True
                    break
            alpha /= 2
        if not accepted:
            raise RuntimeError(f"line search failed before gradient target at iteration {iteration}")
    raise RuntimeError("Newton iteration cap exceeded")


def number_string(value, digits=95):
    return mp.nstr(value, digits, strip_zeros=False)


def serialize_solution(solution):
    return {
        "x": [number_string(solution["x_mp"][j]) for j in range(4)],
        "Q": number_string(solution["Q_mp"]),
        "gradient_inf": number_string(solution["gradient_inf"]),
        "iterations": solution["iterations"],
        "backtracks_total": solution["backtracks_total"],
        "leading_principal_minors": [number_string(value) for value in solution["leading_principal_minors"]],
        "hessian_positive_definite": solution["hessian_positive_definite"],
    }


def execute(files_dir: Path):
    branches = {}
    overall_pass = True
    for B0_text in ("3152", "3154"):
        starts = ([128, 497, 33, int(B0_text)], [256, 497, 33, int(B0_text)])
        p80 = [newton(files_dir, B0_text, start, 80, "1e-50") for start in starts]
        p200 = [newton(files_dir, B0_text, start, 200, "1e-80") for start in starts]

        mp.mp.dps = 200
        p200_start_spread = [abs(p200[0]["x_mp"][j] - p200[1]["x_mp"][j]) for j in range(4)]
        p80_to_p200_spreads = [
            [abs(low["x_mp"][j] - high["x_mp"][j]) for j in range(4)]
            for low, high in zip(p80, p200)
        ]
        objective_difference = abs(p200[0]["Q_mp"] - p200[1]["Q_mp"])

        checks = {
            "C1_strict_convexity": bool(p200[0]["c1"]["algebraic_strict_convexity_certified"]),
            "C2_P80_both_converged": all(sol["gradient_inf"] <= mp.mpf("1e-50") for sol in p80),
            "C2_P200_both_converged": all(sol["gradient_inf"] <= mp.mpf("1e-80") for sol in p200),
            "C3_P200_starter_agreement": max(p200_start_spread) <= mp.mpf("1e-60"),
            "C3_P80_to_P200_agreement": max(max(row) for row in p80_to_p200_spreads) <= mp.mpf("1e-40"),
            "C3_all_roots_interior": all(min(sol["x_mp"]) > 0 for sol in p80 + p200),
            "C3_P200_hessian_positive_definite": all(sol["hessian_positive_definite"] for sol in p200),
            "C3_P200_Q_agreement": objective_difference <= mp.mpf("1e-70"),
        }
        branch_pass = all(checks.values())
        overall_pass = overall_pass and branch_pass
        branches["R" + B0_text] = {
            "B0": B0_text,
            "C1": p200[0]["c1"],
            "P80": [serialize_solution(sol) for sol in p80],
            "P200": [serialize_solution(sol) for sol in p200],
            "P200_starter_spread": [number_string(value) for value in p200_start_spread],
            "P80_to_P200_spreads": [
                [number_string(value) for value in row] for row in p80_to_p200_spreads
            ],
            "P200_objective_difference": number_string(objective_difference),
            "checks": checks,
            "pass": branch_pass,
        }

    return {
        "benchmark": BENCHMARK,
        "preregistration_commit": PREREG_COMMIT,
        "precision_amendment_commit": AMENDMENT_COMMIT,
        "branches": branches,
        "classification": (
            "PASS_0105A6O2_STRICT_CONVEX_UNIQUE_HIGH_PRECISION_OPTIMUM_NONDISCOVERY"
            if overall_pass
            else "BLOCKED_0105A6O2_HIGH_PRECISION_OR_UNIQUENESS_CERTIFICATE_UNRESOLVED"
        ),
        "publication_target_classification_performed": False,
        "systematic_excursion_execution_performed": False,
        "observed_bsm_residual_permission_percent": 0,
        "observed_bsm_residual_inspected": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files-dir", required=True)
    parser.add_argument("--a6p-manifest", required=True)
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
        result = execute(Path(args.files_dir))
        result["git_sha"] = args.git_sha
    except Exception as exc:
        result = {
            "benchmark": BENCHMARK,
            "preregistration_commit": PREREG_COMMIT,
            "precision_amendment_commit": AMENDMENT_COMMIT,
            "git_sha": args.git_sha,
            "classification": "BLOCKED_0105A6O2_SOURCE_OR_RUNTIME_FAILURE",
            "error_type": type(exc).__name__,
            "error_message": str(exc),
            "publication_target_classification_performed": False,
            "systematic_excursion_execution_performed": False,
            "observed_bsm_residual_permission_percent": 0,
            "observed_bsm_residual_inspected": False,
        }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
