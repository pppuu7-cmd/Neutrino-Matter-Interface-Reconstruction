#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path

PREREG_COMMIT = "48e5904139e8782e046f4d6e7d3c548ec1880e18"
AUTHORITY_AMENDMENT_COMMIT = "fd6504fdfffe651078603eb62576610f66049424"
PARENT_PASS = {
    "PASS_V2_G9_BETELGEUSE_ACTIVE_KINEMATICS_PASSIVE_FAIL",
    "PASS_V2_G9_BETELGEUSE_BOTH_ARCHITECTURES",
}
NOT_RUN = "NOT_RUN_V2_G9_0098_PARENT_ACTIVE_NOT_PASSED"
PASS = "PASS_V2_G9_0098_REFERENCE_RESOURCE_SCALING_SURVIVES"
FAIL = "SCIENTIFIC_FAIL_V2_G9_0098_REFERENCE_RESOURCE_CLOSURE"
BLOCKED = "BLOCKED_V2_G9_0098_PROPULSION_OR_POWER_AUTHORITY"
INFRA = "INFRASTRUCTURE_FAIL_V2_G9_0098"

G0 = 9.80665
AU_M = 149_597_870_700.0
GM_SUN = 1.3271244e20
HOURS_10_JULIAN_YR = 10.0 * 365.25 * 24.0
NEXT_DEMO_HOURS = 48_000.0
MMRTG_MASS_KG = 45.0
MMRTG_BOL_W = 110.0
# 0098a: lower edge of the traceable NETS-2020 EU EODL prediction 75.2 +/- 0.4 We.
MMRTG_EOL17_W = 74.8
P_REFLECT_1AU_PA = 9.1e-6
SAIL_REFERENCE_ACCEL_M_S2 = 0.35e-3

# NASA 2025 Advanced NEXT frozen table: thrust mN, Isp s, efficiency, thrust/power mN/kW.
NEXT_POINTS = {
    "AN1.5B": (74.0, 2663.0, 0.57, 44.0),
    "AN14": (87.0, 3137.0, 0.61, 40.0),
    "AN45A": (257.0, 2870.0, 0.63, 45.0),
    "2B": (330.0, 3397.0, 0.67, 40.0),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def finite(*xs: float) -> bool:
    return all(math.isfinite(x) for x in xs)


def evaluate_control(a_hover: float, delta_v: float) -> list[dict]:
    if not (finite(a_hover, delta_v) and a_hover > 0.0 and delta_v > 0.0):
        raise ValueError("invalid parent active-control demand")
    rps_eol_specific = MMRTG_EOL17_W / MMRTG_MASS_KG
    rps_bol_specific = MMRTG_BOL_W / MMRTG_MASS_KG
    rows = []
    for name, (thrust_mn, isp_s, efficiency, tp_mn_kw) in NEXT_POINTS.items():
        thrust_n = thrust_mn * 1e-3
        q_n_w = tp_mn_kw * 1e-6
        ve = isp_s * G0
        f_prop = 1.0 - math.exp(-delta_v / ve)
        p_per_mass = a_hover / q_n_w
        f_rps_eol = p_per_mass / rps_eol_specific
        f_rps_bol = p_per_mass / rps_bol_specific
        headroom = 1.0 - f_prop - f_rps_eol
        m_supported = thrust_n / a_hover
        if not finite(ve, f_prop, p_per_mass, f_rps_eol, f_rps_bol, headroom, m_supported):
            raise ValueError("non-finite electric-propulsion result")
        rows.append({
            "point": name,
            "thrust_mN": thrust_mn,
            "Isp_s": isp_s,
            "thruster_efficiency": efficiency,
            "thrust_to_power_mN_per_kW": tp_mn_kw,
            "exhaust_speed_m_s": ve,
            "propellant_fraction_10yr_ideal": f_prop,
            "required_propulsion_power_per_initial_mass_W_kg": p_per_mass,
            "MMRTG_EOL17_specific_power_W_kg": rps_eol_specific,
            "MMRTG_BOL_specific_power_W_kg": rps_bol_specific,
            "required_MMRTG_EOL_mass_fraction": f_rps_eol,
            "required_MMRTG_BOL_mass_fraction_sensitivity": f_rps_bol,
            "resource_headroom_propellant_plus_EOL_RPS": headroom,
            "max_supported_total_mass_at_published_thrust_kg": m_supported,
            "resource_scaling_positive": headroom > 0.0,
        })
    return rows


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
            "authority_amendment_commit": AUTHORITY_AMENDMENT_COMMIT,
            "head_sha": os.getenv("GITHUB_SHA"),
            "parent_status": pstatus,
            "parent_sha256": sha256(parent_path),
            "authorities": {
                "advanced_NEXT_2025": "NASA NTRS 20250001749 / IEPC-2025-133, Advanced NEXT performance table",
                "NEXT_endurance": "NASA NEXT LDT; frozen terminal lower-bound 48000 h; completed test authority reports 51184 h",
                "MMRTG": "NETS 2020/ORNL-hosted Whiting analysis: EU EODL 75.2 +/- 0.4 We; 0098a uses conservative 74.8 W with 45 kg system mass; NASA confirms 110 W BOL and 17-y lifetime modeling",
                "solar_sail_pressure": "NASA solar-sail physics: ideal reflection ~9.1e-6 N/m^2 at 1 AU",
                "solar_sail_reference": "NASA integrated solar-sail reference: characteristic acceleration ~0.35 mm/s^2 at 1 AU",
            },
        }
        if pstatus not in PARENT_PASS:
            result = {**base, "status": NOT_RUN, "reason": "0097 active-tracking parent did not pass"}
            Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
            print(json.dumps(result, indent=2, sort_keys=True))
            return

        controls = parent.get("observer_controls")
        if not isinstance(controls, list) or len(controls) != 3:
            raise ValueError("expected exactly three 0097 observer controls")

        electric = []
        all_positive = True
        for c in controls:
            z = float(c["z_au"])
            a_hover = float(c["a_hover_m_s2"])
            dv = float(c["delta_v_hover_10yr_m_s"])
            rows = evaluate_control(a_hover, dv)
            all_positive = all_positive and all(r["resource_scaling_positive"] for r in rows)
            electric.append({
                "z_au": z,
                "a_hover_m_s2": a_hover,
                "delta_v_hover_10yr_m_s": dv,
                "points": rows,
            })

        single_hours_ratio = NEXT_DEMO_HOURS / HOURS_10_JULIAN_YR
        two_hours_ratio = 2.0 * NEXT_DEMO_HOURS / HOURS_10_JULIAN_YR
        single_duration = "SINGLE_THRUSTER_DURATION_DEMONSTRATED" if single_hours_ratio >= 1.0 else "SINGLE_THRUSTER_DURATION_NOT_DEMONSTRATED"
        two_duration = "TWO_UNIT_HOURS_COVERAGE_SURVIVES" if two_hours_ratio >= 1.0 else "TWO_UNIT_HOURS_COVERAGE_FAILS"

        g_1au = GM_SUN / (AU_M * AU_M)
        sigma_ideal = P_REFLECT_1AU_PA / g_1au
        sail_ratio = SAIL_REFERENCE_ACCEL_M_S2 / g_1au
        sail_status = "REFERENCE_SOLAR_SAIL_HOVER_SURVIVES" if SAIL_REFERENCE_ACCEL_M_S2 >= g_1au else "REFERENCE_SOLAR_SAIL_HOVER_FAILS"

        terminal = PASS if all_positive and two_hours_ratio >= 1.0 else FAIL
        result = {
            **base,
            "status": terminal,
            "electric_propulsion": electric,
            "duration_authority": {
                "ten_julian_year_hours": HOURS_10_JULIAN_YR,
                "NEXT_demonstrated_hours_frozen_lower_bound": NEXT_DEMO_HOURS,
                "single_unit_coverage_ratio": single_hours_ratio,
                "two_unit_sequential_coverage_ratio": two_hours_ratio,
                "single_unit_status": single_duration,
                "two_unit_status": two_duration,
                "reliability_probability_assessed": False,
            },
            "solar_sail": {
                "solar_gravity_at_1AU_m_s2": g_1au,
                "ideal_reflection_pressure_at_1AU_N_m2": P_REFLECT_1AU_PA,
                "ideal_total_areal_density_ceiling_kg_m2": sigma_ideal,
                "ideal_total_areal_density_ceiling_g_m2": sigma_ideal * 1000.0,
                "NASA_reference_characteristic_accel_m_s2": SAIL_REFERENCE_ACCEL_M_S2,
                "reference_accel_over_required_gravity": sail_ratio,
                "status": sail_status,
            },
            "interpretation_guards": [
                "positive resource headroom is necessary, not sufficient, for spacecraft feasibility",
                "MMRTG accounting is propulsion-only and omits housekeeping/detector loads",
                "published thrust-to-power is not promoted to whole-spacecraft wall-plug efficiency",
                "two sequential thrusters are an endurance-hours diagnostic, not a reliability probability",
                "reference solar-sail failure is not a universal solar-sail no-go",
                "no detector-event, deposited-energy, or useful-power gain is inferred",
            ],
        }
    except Exception as exc:
        result = {
            "status": INFRA,
            "reason": repr(exc),
            "prereg_commit": PREREG_COMMIT,
            "authority_amendment_commit": AUTHORITY_AMENDMENT_COMMIT,
            "head_sha": os.getenv("GITHUB_SHA"),
        }
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] == INFRA:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
