import pytest

from nmir.solar_flux import cno_total_flux_cm2_s, load_b16_fluxes, total_component_flux_cm2_s


def test_b16_gs98_reference_fluxes():
    fluxes = load_b16_fluxes("GS98")
    assert fluxes["pp"].flux_cm2_s == pytest.approx(5.98e10)
    assert fluxes["Be7"].flux_cm2_s == pytest.approx(4.93e9)
    assert fluxes["B8"].flux_cm2_s == pytest.approx(5.46e6)
    assert fluxes["B8"].relative_uncertainty == pytest.approx(0.12)


def test_b16_agss09met_reference_fluxes():
    fluxes = load_b16_fluxes("AGSS09met")
    assert fluxes["pp"].flux_cm2_s == pytest.approx(6.03e10)
    assert fluxes["Be7"].flux_cm2_s == pytest.approx(4.50e9)
    assert fluxes["B8"].flux_cm2_s == pytest.approx(4.50e6)


def test_cno_total_matches_published_component_sum():
    assert cno_total_flux_cm2_s("GS98") == pytest.approx(4.8829e8)
    assert cno_total_flux_cm2_s("AGSS09met") == pytest.approx(3.5126e8)


def test_high_and_low_z_total_fluxes_are_distinct():
    assert total_component_flux_cm2_s("GS98") != pytest.approx(total_component_flux_cm2_s("AGSS09met"))


def test_invalid_model_is_rejected():
    with pytest.raises(ValueError):
        load_b16_fluxes("unknown")
