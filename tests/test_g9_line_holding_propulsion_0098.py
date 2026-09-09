import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import g9_line_holding_propulsion_0098 as m


def test_frozen_duration_and_endurance_controls():
    assert m.HOURS_10_JULIAN_YR == 87660.0
    assert m.NEXT_DEMO_HOURS / m.HOURS_10_JULIAN_YR < 1.0
    assert 2.0 * m.NEXT_DEMO_HOURS / m.HOURS_10_JULIAN_YR > 1.0


def test_reference_scaling_has_positive_headroom_at_24au_order():
    r = 24.0 * m.AU_M
    a = m.GM_SUN / r**2
    dv = a * 10.0 * 365.25 * 86400.0
    rows = m.evaluate_control(a, dv)
    assert len(rows) == 4
    assert all(row["resource_scaling_positive"] for row in rows)
    assert min(row["resource_headroom_propellant_plus_EOL_RPS"] for row in rows) > 0.5
    assert all(row["max_supported_total_mass_at_published_thrust_kg"] > 1000.0 for row in rows)


def test_solar_sail_reference_is_below_static_hover_requirement():
    g1 = m.GM_SUN / m.AU_M**2
    sigma = m.P_REFLECT_1AU_PA / g1
    assert math.isclose(g1, 5.93e-3, rel_tol=0.01)
    assert 0.0014 < sigma < 0.0017
    assert m.SAIL_REFERENCE_ACCEL_M_S2 < g1
