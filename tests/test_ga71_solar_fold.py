import pytest

from nmir.ga71_solar_fold import _weighted_capture_integrand


def test_zero_energy_endpoint_contributes_exactly_zero_without_calling_pee():
    def forbidden(_energy):
        raise AssertionError("Pee must not be evaluated where Ga capture cross section is zero")
    assert _weighted_capture_integrand(0.0, 1.0, forbidden) == 0.0


def test_zero_shape_contributes_zero_without_calling_pee():
    def forbidden(_energy):
        raise AssertionError("Pee must not be evaluated for zero spectral weight")
    assert _weighted_capture_integrand(1.0, 0.0, forbidden) == 0.0


def test_invalid_solar_model_fails_closed(tmp_path):
    from nmir.ga71_solar_fold import oscillated_ga71_snu
    with pytest.raises(ValueError):
        oscillated_ga71_snu("INVALID", tmp_path)
