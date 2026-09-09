#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path

PREREG_COMMIT = "7792fb3412eb9f3c932bc04f8ae357bdc4c0129f"
MASS_INTERVAL_AMENDMENT_COMMIT = "01642bfdb9e96044dfdf4b81986eafbb51cb3bea"
EXPECTED_0098_PREREG = "48e5904139e8782e046f4d6e7d3c548ec1880e18"
EXPECTED_0098_MMRTG_AMENDMENT = "fd6504fdfffe651078603eb62576610f66049424"
EXPECTED_0097_GEOMETRY_AMENDMENT = "3f873eb3ab8d90b931eb41f5ba25484fde843ced"
PARENT_PASS = "PASS_V2_G9_0098_REFERENCE_RESOURCE_SCALING_SURVIVES"
NOT_RUN = "NOT_RUN_V2_G9_0099_PARENT_REFERENCE_SCALING_NOT_PASSED"
PASS = "PASS_V2_G9_0099_DISCRETE_REFERENCE_ARCHITECTURE_SUPPORTED"
BLOCKED_POWER = "BLOCKED_V2_G9_0099_MMRTG_SUPPLY_AND_FISSION_FLIGHT_AUTHORITY"
FAIL_DISCRETE = "SCIENTIFIC_FAIL_V2_G9_0099_DISCRETE_MASS_POWER_OR_THROUGHPUT"
BLOCKED_AUTH = "BLOCKED_V2_G9_0099_EXTERNAL_HARDWARE_AUTHORITY"
INFRA = "INFRASTRUCTURE_FAIL_V2_G9_0099"

ACTIVE_LANES = (1, 2, 4)
ELECTRIC_RESERVE = 0.25
SENSITIVITY_RESERVES = (0.0, 0.10)
MMRTG_EOL_W = 74.8
MMRTG_MASS_KG = 45.0
MMRTG_PUO2_KG = 4.8
MMRTG_PU238_FRACTION = 0.71
MMRTG_THERMAL_BOL_W = 2000.0
PUO2_PRODUCTION_REFERENCE_KG_YR = 1.5
THRUSTER_WITH_HARNESS_KG = 14.0
PPU_KG = 36.0
LPA_KG = 3.1
GIMBAL_KG = 6.0
HPA_KG = 1.9
HPA_COUNT = 2
THROUGHPUT_PRIMARY_KG_PER_USED_STRING = 450.0
FISSION_KWE_SCALE = 10.0
FISSION_TENS_KWE_SCALE = 40.0


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def finite(*xs: float) -> bool:
    return all(math.isfinite(x) for x in xs)


def required_mmrtg(power_w: float, reserve: float) -> int:
    if not (finite(power_w, reserve) and power_w > 0.0 and 0.0 <= reserve < 1.0):
        raise ValueError("invalid integer power inputs")
    return int(math.ceil(power_w / ((1.0 - reserve) * MMRTG_EOL_W)))


def evaluate_configuration(control: dict, point: dict, n_active: int) -> dict:
    z = float(control["z_au"])
    a_hover = float(control["a_hover_m_s2"])
    thrust_mn = float(point["thrust_mN"])
    isp_s = float(point["Isp_s"])
    tp = float(point["thrust_to_power_mN_per_kW"])
    f_prop = float(point["propellant_fraction_10yr_ideal"])
    name = str(point["point"])
    if n_active not in ACTIVE_LANES:
        raise ValueError("unfrozen active-lane count")
    if not (finite(z, a_hover, thrust_mn, isp_s, tp, f_prop) and z > 0 and a_hover > 0 and thrust_mn > 0 and isp_s > 0 and tp > 0 and 0 < f_prop < 1):
        raise ValueError("invalid inherited parent point")

    thrust_n = thrust_mn * 1e-3
    q_n_w = tp * 1e-6
    p_one_w = thrust_n / q_n_w
    p_active_w = n_active * p_one_w
    n_mmrtg = required_mmrtg(p_active_w, ELECTRIC_RESERVE)
    n_installed = 2 * n_active
    string_mass = THRUSTER_WITH_HARNESS_KG + PPU_KG + LPA_KG + GIMBAL_KG
    propulsion_hw = n_installed * string_mass + HPA_COUNT * HPA_KG
    fixed_mass = n_mmrtg * MMRTG_MASS_KG + propulsion_hw

    m0_lower = fixed_mass / (1.0 - f_prop)
    m0_thrust_upper = n_active * thrust_n / a_hover
    m0_throughput_upper = (2.0 * n_active * THROUGHPUT_PRIMARY_KG_PER_USED_STRING) / f_prop
    m0_upper = min(m0_thrust_upper, m0_throughput_upper)
    interval_exists = m0_upper > m0_lower
    if math.isclose(m0_thrust_upper, m0_throughput_upper, rel_tol=1e-12, abs_tol=1e-9):
        active_ceiling = "TIE"
    elif m0_thrust_upper < m0_throughput_upper:
        active_ceiling = "THRUST"
    else:
        active_ceiling = "THROUGHPUT"

    residual = m0_upper * (1.0 - f_prop) - fixed_mass
    f_residual = residual / m0_upper
    prop_at_upper = f_prop * m0_upper
    per_used_string = prop_at_upper / (2.0 * n_active)
    sensitivities = {
        f"reserve_{int(round(r*100)):02d}pct": required_mmrtg(p_active_w, r)
        for r in SENSITIVITY_RESERVES
    }
    puo2 = n_mmrtg * MMRTG_PUO2_KG
    pu238 = puo2 * MMRTG_PU238_FRACTION
    thermal = n_mmrtg * MMRTG_THERMAL_BOL_W

    if not finite(p_one_w, p_active_w, propulsion_hw, fixed_mass, m0_lower, m0_thrust_upper, m0_throughput_upper, m0_upper, residual, f_residual, prop_at_upper, per_used_string, puo2, pu238, thermal):
        raise ValueError("non-finite discrete result")

    return {
        "z_au": z,
        "point": name,
        "n_active": n_active,
        "n_installed_strings": n_installed,
        "thrust_mN_per_active_thruster": thrust_mn,
        "Isp_s": isp_s,
        "propulsion_input_power_one_W": p_one_w,
        "propulsion_input_power_active_W": p_active_w,
        "primary_electrical_reserve_fraction": ELECTRIC_RESERVE,
        "N_MMRTG_primary": n_mmrtg,
        "N_MMRTG_sensitivities": sensitivities,
        "propulsion_hardware_mass_kg": propulsion_hw,
        "MMRTG_mass_kg": n_mmrtg * MMRTG_MASS_KG,
        "fixed_represented_hardware_mass_kg": fixed_mass,
        "f_prop_10yr_ideal": f_prop,
        "M0_lower_fixed_hardware_kg": m0_lower,
        "M0_thrust_upper_kg": m0_thrust_upper,
        "M0_throughput_upper_kg": m0_throughput_upper,
        "M0_upper_kg": m0_upper,
        "active_mass_ceiling": active_ceiling,
        "mass_interval_exists": interval_exists,
        "M_residual_at_upper_kg": residual,
        "f_residual_at_upper": f_residual,
        "xenon_total_at_upper_kg": prop_at_upper,
        "xenon_per_used_string_at_upper_kg": per_used_string,
        "throughput_primary_pass": per_used_string <= THROUGHPUT_PRIMARY_KG_PER_USED_STRING + 1e-9,
        "PuO2_required_kg": puo2,
        "Pu238_required_kg": pu238,
        "PuO2_production_equivalent_years": puo2 / PUO2_PRODUCTION_REFERENCE_KG_YR,
        "MMRTG_thermal_BOL_W": thermal,
        "within_10kWe_fission_scale": p_active_w <= FISSION_KWE_SCALE * 1000.0,
        "within_40kWe_fission_scale": p_active_w <= FISSION_TENS_KWE_SCALE * 1000.0,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    parent_path = Path(args.parent)
    try:
        parent = json.loads(parent_path.read_text())
        pstatus = str(parent.get("status", ""))
        base = {
            "prereg_commit": PREREG_COMMIT,
            "mass_interval_amendment_commit": MASS_INTERVAL_AMENDMENT_COMMIT,
            "head_sha": os.getenv("GITHUB_SHA"),
            "parent_status": pstatus,
            "parent_sha256": sha256(parent_path),
            "parent_run_id": os.getenv("PARENT_RUN_ID"),
            "parent_artifact_id": os.getenv("PARENT_ARTIFACT_ID"),
            "authorities": {
                "Advanced_NEXT": "NASA NTRS 20250008168 / 20250001749: NEXT-C derivative, 330 mN demonstrated, no significant mass/volume change claim",
                "NEXT_C_mass": "NASA NTRS 20210024276: thruster with harness <14 kg, PPU <36 kg",
                "NEXT_PMS": "NASA NTRS 20090004685: HPA 1.9 kg, LPA 3.1 kg",
                "NEXT_gimbal": "NASA AIAA-2007-5199 / NTRS: heritage gimbal 6 kg proxy",
                "NEXT_throughput": "NASA NTRS 20150004419: qualification requirement 450 kg; >900 kg demonstrated in LDT",
                "MMRTG": "NASA RPS FAQ: 4.8 kg PuO2/MMRTG, 71% Pu-238 by weight, multiple MMRTGs can be combined; 0098a 74.8 W EODL benchmark",
                "Pu238_supply_scale": "NASA FY2025 budget: ~1.5 kg plutonium oxide/year full operational capability target by 2026",
                "MMRTG_thermal": "NASA MMRTG public/NTRS reference: ~2000 W thermal and ~110 W electrical at beginning of mission",
                "fission": "NASA Kilopower 1-10 kWe relevant-environment technology; current FSP is lunar/Mars surface technology, not free-flying 24-AU flight authority",
            },
        }
        if pstatus != PARENT_PASS:
            result = {**base, "status": NOT_RUN, "reason": "0098 parent reference scaling did not pass"}
            Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
            print(json.dumps(result, indent=2, sort_keys=True))
            return

        if str(parent.get("prereg_commit", "")) != EXPECTED_0098_PREREG:
            raise ValueError("0098 prereg provenance mismatch")
        if str(parent.get("authority_amendment_commit", "")) != EXPECTED_0098_MMRTG_AMENDMENT:
            raise ValueError("0098 MMRTG amendment provenance mismatch")
        if str(parent.get("expected_0097_geometry_amendment_commit", "")) != EXPECTED_0097_GEOMETRY_AMENDMENT:
            raise ValueError("0098 lacks exact 0097a geometry provenance")

        controls = parent.get("electric_propulsion")
        if not isinstance(controls, list) or len(controls) != 3:
            raise ValueError("expected exactly three 0098 observer controls")

        configurations = []
        per_control = []
        for control in controls:
            pts = control.get("points")
            if not isinstance(pts, list) or len(pts) != 4:
                raise ValueError("expected four frozen Advanced NEXT points per control")
            z = float(control["z_au"])
            survivors = []
            for pt in pts:
                for n in ACTIVE_LANES:
                    row = evaluate_configuration(control, pt, n)
                    configurations.append(row)
                    if row["mass_interval_exists"] and row["throughput_primary_pass"]:
                        survivors.append(row)
            if survivors:
                best = max(survivors, key=lambda x: x["f_residual_at_upper"])
                per_control.append({
                    "z_au": z,
                    "survivor_count": len(survivors),
                    "best_survivor": {
                        "point": best["point"],
                        "n_active": best["n_active"],
                        "N_MMRTG_primary": best["N_MMRTG_primary"],
                        "f_residual_at_upper": best["f_residual_at_upper"],
                        "M0_lower_kg": best["M0_lower_fixed_hardware_kg"],
                        "M0_upper_kg": best["M0_upper_kg"],
                        "active_mass_ceiling": best["active_mass_ceiling"],
                    },
                })
            else:
                per_control.append({"z_au": z, "survivor_count": 0, "best_survivor": None})

        discrete_pass = all(x["survivor_count"] > 0 for x in per_control)
        if not discrete_pass:
            terminal = FAIL_DISCRETE
        else:
            # Public authority establishes the resource scale, not a currently allocatable inventory
            # of the required tens-to-hundreds of MMRTGs. The alternative fission branch is presently
            # technology-scale compatible but lacks directly applicable free-flying flight authority.
            terminal = BLOCKED_POWER

        surviving = [x for x in configurations if x["mass_interval_exists"] and x["throughput_primary_pass"]]
        result = {
            **base,
            "status": terminal,
            "discrete_mass_power_throughput_status": "PASS_REFERENCE_DISCRETE_MASS_POWER" if discrete_pass else FAIL_DISCRETE,
            "mmrtg_supply_status": "BLOCKED_CURRENT_ALLOCATABLE_PU238_MMRTG_AUTHORITY",
            "fission_branch_status": "POWER_SCALE_COMPATIBLE_BUT_FLIGHT_AUTHORITY_BLOCKED",
            "configuration_count": len(configurations),
            "surviving_configuration_count": len(surviving),
            "per_control": per_control,
            "global_surviving_extrema": {
                "min_N_MMRTG_primary": min((x["N_MMRTG_primary"] for x in surviving), default=None),
                "max_N_MMRTG_primary": max((x["N_MMRTG_primary"] for x in surviving), default=None),
                "min_positive_f_residual_at_upper": min((x["f_residual_at_upper"] for x in surviving), default=None),
                "max_f_residual_at_upper": max((x["f_residual_at_upper"] for x in surviving), default=None),
                "min_PuO2_required_kg": min((x["PuO2_required_kg"] for x in surviving), default=None),
                "max_PuO2_required_kg": max((x["PuO2_required_kg"] for x in surviving), default=None),
                "min_MMRTG_thermal_BOL_W": min((x["MMRTG_thermal_BOL_W"] for x in surviving), default=None),
                "max_MMRTG_thermal_BOL_W": max((x["MMRTG_thermal_BOL_W"] for x in surviving), default=None),
            },
            "configurations": configurations,
            "interpretation_guards": [
                "a nonempty mass interval is not spacecraft feasibility",
                "residual mass is not payload mass",
                "MMRTG supply block is not a physics no-go for active line holding",
                "fission power-scale compatibility is not flight qualification",
                "thermal integration, tankage, structure, avionics, detector/payload and reliability remain unclosed",
                "no detector-event, interaction, deposited-energy or useful-power gain is inferred",
            ],
        }
    except ValueError as exc:
        result = {
            "status": BLOCKED_AUTH,
            "reason": repr(exc),
            "prereg_commit": PREREG_COMMIT,
            "mass_interval_amendment_commit": MASS_INTERVAL_AMENDMENT_COMMIT,
            "head_sha": os.getenv("GITHUB_SHA"),
        }
    except Exception as exc:
        result = {
            "status": INFRA,
            "reason": repr(exc),
            "prereg_commit": PREREG_COMMIT,
            "mass_interval_amendment_commit": MASS_INTERVAL_AMENDMENT_COMMIT,
            "head_sha": os.getenv("GITHUB_SHA"),
        }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] == INFRA:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
