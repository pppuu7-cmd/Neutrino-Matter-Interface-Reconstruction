#!/usr/bin/env python3
"""Prospective 7Li two-state response validation against published 8B averages."""
from __future__ import annotations

import json
from pathlib import Path

from nmir.b8_historical_audit import load_bahcall_lisi1996_spectrum
from nmir.li7_full_response import li7_excited_sigma_cm2, li7_two_state_sigma_cm2
from nmir.li7_ground_response import li7_ground_sigma_cm2

PUBLISHED_GS_CM2 = 2.470e-42
PUBLISHED_EX_CM2 = 1.289e-42
PUBLISHED_TOTAL_CM2 = 3.759e-42
# Frozen prospectively before hosted execution.  The NMIR model uses the
# evaluated gs log(ft) plus a point-Coulomb phase-space treatment, whereas the
# publication applies its own screening convention.  These are validation
# tolerances, not fit parameters.
COMPONENT_REL_TOL = 0.12
TOTAL_REL_TOL = 0.10


def trapz(y: list[float], x: list[float]) -> float:
    return sum(0.5 * (y[i] + y[i - 1]) * (x[i] - x[i - 1]) for i in range(1, len(x)))


def average(fn) -> float:
    energy, lam = load_bahcall_lisi1996_spectrum()
    return trapz([w * fn(e) for e, w in zip(energy, lam)], energy)


def rel_resid(value: float, reference: float) -> float:
    return value / reference - 1.0


def main() -> int:
    gs = average(li7_ground_sigma_cm2)
    ex = average(li7_excited_sigma_cm2)
    total = average(li7_two_state_sigma_cm2)
    result = {
        "spectrum": "Bahcall et al. PRC54 (1996), frozen NMIR table",
        "model": "evaluated gs logft + measured BGT(429 keV) strength ratio; no neutrino-xsec tuning",
        "ground_cm2": gs,
        "excited_cm2": ex,
        "total_cm2": total,
        "published_ground_cm2": PUBLISHED_GS_CM2,
        "published_excited_cm2": PUBLISHED_EX_CM2,
        "published_total_cm2": PUBLISHED_TOTAL_CM2,
        "ground_relative_residual": rel_resid(gs, PUBLISHED_GS_CM2),
        "excited_relative_residual": rel_resid(ex, PUBLISHED_EX_CM2),
        "total_relative_residual": rel_resid(total, PUBLISHED_TOTAL_CM2),
        "component_relative_tolerance": COMPONENT_REL_TOL,
        "total_relative_tolerance": TOTAL_REL_TOL,
    }
    result["scientific_pass"] = (
        abs(result["ground_relative_residual"]) <= COMPONENT_REL_TOL
        and abs(result["excited_relative_residual"]) <= COMPONENT_REL_TOL
        and abs(result["total_relative_residual"]) <= TOTAL_REL_TOL
    )
    out = Path("artifacts/li7_two_state_validation.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    # Do not turn a scientific FAIL into an infrastructure FAIL: always exit 0.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
