import pytest

from nmir.ft_capture import (
    M_E_MEV,
    point_fermi_function,
    sigma_v_over_c_from_ft_cm2,
    tritium_low_energy_reference_cm2,
)


def test_point_fermi_function_is_enhanced_for_beta_minus():
    f = point_fermi_function(2, M_E_MEV + 18.5906e-3)
    assert f > 1.0
    assert f == pytest.approx(1.18472, rel=2e-5)


def test_tritium_ft_reproduces_published_capture_scale():
    # Cocco, Mangano & Messina (2007), Eq. (21):
    # sigma_NCB * (v_nu/c) = (7.84 +/- 0.03)e-45 cm^2.
    # The intentionally simple point-Coulomb Fermi function should reproduce
    # this precision-source benchmark to within 1%, not its quoted 0.4% error.
    sigma = tritium_low_energy_reference_cm2()
    assert sigma == pytest.approx(7.84e-45, rel=0.01)


def test_ft_scaling_is_inverse():
    e = M_E_MEV + 0.1
    f = point_fermi_function(2, e)
    s1 = sigma_v_over_c_from_ft_cm2(1000.0, e, f)
    s2 = sigma_v_over_c_from_ft_cm2(2000.0, e, f)
    assert s2 / s1 == pytest.approx(0.5)


def test_invalid_ft_inputs():
    with pytest.raises(ValueError):
        sigma_v_over_c_from_ft_cm2(0.0, M_E_MEV + 0.1, 1.0)
    with pytest.raises(ValueError):
        point_fermi_function(0, M_E_MEV + 0.1)
