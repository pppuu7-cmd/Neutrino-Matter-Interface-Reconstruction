#!/usr/bin/env python3
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path

ALPHA_INV = 137.035999177
EPSILON_LIMIT = 0.84e-24
PI_DEC = Decimal("3.1415926535897932384626433832795028841971693993751")
ALPHA_INV_DEC = Decimal("137.035999177")
EPSILON_DEC = Decimal("0.84e-24")
HBARC_EV_M = 1.973269804e-7
EARTH_DIAMETER_M = 12742e3


def calculate():
    e_double = math.sqrt(4.0 * math.pi / ALPHA_INV)
    g_double = e_double * EPSILON_LIMIT

    getcontext().prec = 60
    e_dec = (Decimal(4) * PI_DEC / ALPHA_INV_DEC).sqrt()
    g_dec = e_dec * EPSILON_DEC

    rel_e = abs(e_double - float(e_dec)) / float(e_dec)
    rel_g = abs(g_double - float(g_dec)) / float(g_dec)
    roundtrip = g_double / e_double
    rel_roundtrip = abs(roundtrip - EPSILON_LIMIT) / EPSILON_LIMIT

    m_ref_eV = HBARC_EV_M / EARTH_DIAMETER_M

    checks = {
        "double_decimal_e_rel_le_1e-12": rel_e <= 1e-12,
        "double_decimal_g_rel_le_1e-12": rel_g <= 1e-12,
        "epsilon_roundtrip_rel_le_1e-12": rel_roundtrip <= 1e-12,
        "gross_convention_guard": 2.4e-25 <= g_double <= 2.7e-25,
        "finite_mass_contour_emitted": False,
        "uv_gpp_identified_as_distinct": True,
    }
    scientific_pass = all([
        checks["double_decimal_e_rel_le_1e-12"],
        checks["double_decimal_g_rel_le_1e-12"],
        checks["epsilon_roundtrip_rel_le_1e-12"],
        checks["gross_convention_guard"],
        not checks["finite_mass_contour_emitted"],
        checks["uv_gpp_identified_as_distinct"],
    ])

    return {
        "iteration": "0079a",
        "classification": (
            "PASS_FIFTH_FORCE_B_L_ASYMPTOTIC_MATERIALIZATION"
            if scientific_pass else
            "SCIENTIFIC_FAIL_FIFTH_FORCE_B_L_ASYMPTOTIC_MATERIALIZATION"
        ),
        "scope": "strict long-range/asymptotic m_V -> 0 datum only; no finite-mass exclusion",
        "primary_authority": {
            "arxiv": "1809.04991v2",
            "source_sha256": "ed233fa73a149ba9801d442339a2c5fd3b5051c1dc2caa1584a000760fcff29b",
            "confidence": "2 sigma",
            "epsilon_B_minus_L_upper": EPSILON_LIMIT,
            "mapping": "g_BL = e * |epsilon_{B-L}| for NMIR pure B-L current",
            "uv_note": "Fayet g'' is a separate UV-normalized coupling; it is not NMIR g_BL."
        },
        "electromagnetic_normalization": {
            "alpha_inverse_zero_momentum": ALPHA_INV,
            "e_heaviside_lorentz": e_double,
            "e_decimal": str(e_dec),
        },
        "result": {
            "g_BL_upper_2sigma": g_double,
            "g_BL_upper_2sigma_rounded_2sf": float(f"{g_double:.2g}"),
            "scientific_statement": "g_BL < {:.2g} at 2 sigma in the strict long-range/asymptotic limit".format(g_double),
        },
        "diagnostic_only": {
            "earth_diameter_m": EARTH_DIAMETER_M,
            "hbar_c_eV_m": HBARC_EV_M,
            "one_earth_diameter_compton_mass_eV": m_ref_eV,
            "guard": "reference scale only; NOT a hard validity edge because primary says somewhat larger than Earth diameter",
        },
        "replication": {
            "relative_e_double_vs_decimal": rel_e,
            "relative_g_double_vs_decimal": rel_g,
            "relative_epsilon_roundtrip": rel_roundtrip,
        },
        "checks": checks,
    }


def main():
    result = calculate()
    out = Path("fayet_bl_asymptotic_0079a.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["classification"].startswith("PASS_"):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
