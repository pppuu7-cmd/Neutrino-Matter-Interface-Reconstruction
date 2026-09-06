from nmir.g8_positive_control import g8_positive_control


def test_glashow_energy_matches_frozen_6p3_pev_control():
    out = g8_positive_control()["glashow"]
    assert out["relative_error_to_6p3_pev"] < 0.02


def test_glashow_hadronic_peak_matches_frozen_control():
    out = g8_positive_control()["glashow"]
    assert out["relative_error_to_3p4e31"] < 0.10


def test_glashow_is_far_outside_solar_energy_domain():
    out = g8_positive_control()["glashow"]
    assert out["energy_mismatch_to_20_mev"] > 3.0e8


def test_glashow_cross_scale_is_many_orders_above_mev_cevns_control():
    out = g8_positive_control()["glashow"]
    assert out["cross_scale_ratio_to_xe132_cevns_1mev"] > 1.0e10


def test_li7_be7_line_is_event_richer_than_energy_rich():
    out = g8_positive_control()["li7_be7_narrow_line"]
    assert out["event_fraction"] > 0.20
    assert out["energy_moment_fraction"] < 0.05
    assert out["event_to_energy_fraction_ratio"] > 3.0


def test_positive_controls_keep_scope_separate():
    out = g8_positive_control()
    assert "POSITIVE_CONTROL_PASS" in out["glashow"]["classification"]
    assert out["li7_be7_narrow_line"]["classification"] == "NARROW_LINE_EVENT_GAIN_NOT_ENERGY_GAIN"
    assert "UNVALIDATED" in out["h3_he3_mossbauer_concept"]["classification"]
