import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import g9_betelgeuse_line_tracking_0097 as m


def test_0097a_provenance_and_astrometry_margin():
    assert m.PREREG_COMMIT == "53863048c2d5b5803c9e120794c21fe415f1b319"
    assert m.AMENDMENT_COMMIT == "3f873eb3ab8d90b931eb41f5ba25484fde843ced"
    sigma_alpha = math.sqrt(m.COSMIC_NOISE_MAS**2 + (m.MU_ALPHA_SIGMA_MASYR * m.HORIZON_JULIAN_YR)**2)
    sigma_delta = math.sqrt(m.COSMIC_NOISE_MAS**2 + (m.MU_DELTA_SIGMA_MASYR * m.HORIZON_JULIAN_YR)**2)
    eps = 3.0 * math.hypot(sigma_alpha, sigma_delta)
    assert math.isclose(eps, 13.148764200486678, rel_tol=0.0, abs_tol=1e-12)
    assert eps < m.BETA_SUPPORT_MAS


def test_downstream_passive_duty_uses_one_window_per_orbit():
    beta = m.mas_to_rad(m.BETA_SUPPORT_MAS)
    # With d_support=r*tan(beta), one downstream window has angular half-width
    # asin(tan(beta)); the duty fraction is t_cross/T = asin(tan(beta))/pi.
    f_one = math.asin(math.tan(beta)) / math.pi
    f_old_two_line_intersections = 2.0 * f_one
    assert math.isclose(f_one, 7.716049382716276e-08, rel_tol=1e-14)
    assert math.ceil(1.0 / f_one) == 12_960_000
    assert math.ceil(1.0 / f_old_two_line_intersections) == 6_480_000
    assert f_one < 1.0


def test_source_contains_no_two_crossing_duty_regression():
    text = (ROOT / "scripts" / "g9_betelgeuse_line_tracking_0097.py").read_text()
    assert "usable_downstream_crossings = 1" in text
    assert "f_duty = usable_downstream_crossings * t_cross_exact / T_orb" in text
    assert "f_duty = 2.0 * t_cross_exact / T_orb" not in text
