import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import g9_discrete_power_architecture_0099 as m


def synthetic_control():
    a = 1.0317920725205531e-5
    dv = a * 10.0 * 365.25 * 86400.0
    isp = 2663.0
    fp = 1.0 - math.exp(-dv / (isp * 9.80665))
    return {
        "z_au": 23.97365833326344,
        "a_hover_m_s2": a,
        "points": [{
            "point": "AN1.5B",
            "thrust_mN": 74.0,
            "Isp_s": isp,
            "thrust_to_power_mN_per_kW": 44.0,
            "propellant_fraction_10yr_ideal": fp,
        }],
    }


def test_prereg_and_amendment_are_pinned():
    assert m.PREREG_COMMIT == "7792fb3412eb9f3c932bc04f8ae357bdc4c0129f"
    assert m.MASS_INTERVAL_AMENDMENT_COMMIT == "01642bfdb9e96044dfdf4b81986eafbb51cb3bea"
    assert m.ACTIVE_LANES == (1, 2, 4)
    assert m.ELECTRIC_RESERVE == 0.25


def test_integer_mmrtg_rounding_and_low_power_reference():
    assert m.required_mmrtg(1681.8181818181818, 0.25) == 30
    assert m.required_mmrtg(1681.8181818181818, 0.0) == 23
    assert m.required_mmrtg(1681.8181818181818, 0.10) == 25


def test_feasible_interval_not_max_thrust_propellant_bug():
    c = synthetic_control()
    row = m.evaluate_configuration(c, c["points"][0], 1)
    assert row["N_MMRTG_primary"] == 30
    assert row["mass_interval_exists"] is True
    assert row["throughput_primary_pass"] is True
    assert row["active_mass_ceiling"] == "THRUST"
    assert 1600.0 < row["M0_lower_fixed_hardware_kg"] < 1700.0
    assert 7100.0 < row["M0_upper_kg"] < 7250.0
    assert 0.67 < row["f_residual_at_upper"] < 0.69
    assert row["PuO2_required_kg"] == 144.0
    assert row["Pu238_required_kg"] == 102.24
    assert row["MMRTG_thermal_BOL_W"] == 60000.0
    assert math.isclose(row["PuO2_production_equivalent_years"], 96.0)


def test_component_mass_proxy_is_explicit():
    one_installed_string = m.THRUSTER_WITH_HARNESS_KG + m.PPU_KG + m.LPA_KG + m.GIMBAL_KG
    assert math.isclose(one_installed_string, 59.1)
    # one active lane installs two strings plus two HPAs
    assert math.isclose(2.0 * one_installed_string + 2.0 * m.HPA_KG, 122.0)
