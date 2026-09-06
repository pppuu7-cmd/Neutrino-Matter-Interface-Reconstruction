import pytest

from nmir.ga71_response import (
    GA71_THRESHOLD_MEV,
    ga71_sigma_cm2,
    line_capture_snu,
    load_ga71_response,
    normalized_spectral_average_sigma_cm2,
    parse_two_column_spectrum,
)


def test_response_table_identity_and_monotonic_energy():
    points = load_ga71_response()
    assert len(points) == 59
    assert points[0].energy_mev == pytest.approx(0.240)
    assert points[0].best_cm2 == pytest.approx(13.10e-46)
    assert points[-1].energy_mev == pytest.approx(30.0)
    assert points[-1].best_cm2 == pytest.approx(878900e-46)


def test_threshold_and_tabulated_interpolation():
    assert ga71_sigma_cm2(GA71_THRESHOLD_MEV) == 0.0
    assert ga71_sigma_cm2(0.300) == pytest.approx(16.62e-46)
    assert ga71_sigma_cm2(10.0) == pytest.approx(57100e-46)
    assert 0.0 < ga71_sigma_cm2(0.236) < ga71_sigma_cm2(0.240)


def test_be7_two_line_average_reproduces_published_standard_spectrum_value():
    # Bahcall 1997: 89.7% dominant ~0.862-MeV line + 10.3% ~0.384-MeV line;
    # published standard-spectrum average is 71.7e-46 cm^2.
    avg = 0.897 * ga71_sigma_cm2(0.862) + 0.103 * ga71_sigma_cm2(0.384)
    assert avg / 1e-46 == pytest.approx(71.7, rel=2e-3)


def test_pep_line_is_close_to_published_204e46_value():
    # Interpolating the published specific-energy table at the nominal pep line.
    assert ga71_sigma_cm2(1.442) / 1e-46 == pytest.approx(204.0, rel=0.04)


def test_two_column_spectrum_parser_and_normalized_average():
    e, w = parse_two_column_spectrum("# demo\n0.24, 1\n0.30, 1\n0.40, 1\n")
    avg = normalized_spectral_average_sigma_cm2(e, w)
    assert 13.10e-46 < avg < 24.06e-46


def test_snu_conversion_for_line():
    # 1e10 cm^-2 s^-1 times 1e-46 cm^2 is exactly 1 SNU.
    assert line_capture_snu(1e10, 0.300) == pytest.approx(16.62)
    assert line_capture_snu(1e10, 0.300, 0.5) == pytest.approx(8.31)


def test_fail_closed_above_frozen_energy_range():
    with pytest.raises(ValueError):
        ga71_sigma_cm2(31.0)
