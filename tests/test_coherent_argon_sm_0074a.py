import math

from nmir.coherent_argon_sm_0074a import (
    EfficiencyPoint,
    GEV2_TO_CM2,
    GF_GEV2,
    GVN,
    GVP_NUMU,
    N_AR40,
    Z_AR40,
    accepted_cross_section_cm2,
    calculate_events,
    efficiency_at,
    helm_form_factor,
    inverse_recoil_threshold_gev,
    nucleus_mass_gev,
    recoil_endpoint_gev,
    source_averaged_dsigma_dt_cm2_per_gev,
)


def simple_efficiency():
    return [EfficiencyPoint(0.0, 0.0), EfficiencyPoint(200.0, 1.0)]


def test_recoil_endpoint_inverse_roundtrip():
    m = nucleus_mass_gev()
    for e_mev in (5.0, 29.792, 52.8):
        e = e_mev * 1e-3
        t = recoil_endpoint_gev(e, m)
        assert math.isclose(inverse_recoil_threshold_gev(t, m), e, rel_tol=2e-13)


def test_helm_normalization_and_suppression():
    assert helm_form_factor(0.0, 3.448) == 1.0
    assert 0.0 < helm_form_factor(0.05, 3.448) < 1.0


def test_efficiency_interpolation_and_support():
    pts = [EfficiencyPoint(1.0, 0.0), EfficiencyPoint(3.0, 0.8)]
    assert efficiency_at(0.5, pts) == 0.0
    assert efficiency_at(4.0, pts) == 0.0
    assert math.isclose(efficiency_at(2.0, pts), 0.4)


def test_prompt_support_vanishes_above_endpoint():
    m = nucleus_mass_gev()
    e_prompt = 0.029792140909877435
    tmax = recoil_endpoint_gev(e_prompt, m)
    assert source_averaged_dsigma_dt_cm2_per_gev(tmax * 1.0001, "numu_prompt") == 0.0


def test_cross_section_normalization_no_hidden_factor_four():
    m = nucleus_mass_gev()
    ep = 0.029792140909877435
    q = GVP_NUMU * Z_AR40 + GVN * N_AR40
    tp = recoil_endpoint_gev(ep, m)
    exact = GF_GEV2**2 * m / math.pi * q*q * (tp - m*tp*tp/(4*ep*ep)) * GEV2_TO_CM2
    pts = [EfficiencyPoint(0.0, 1.0), EfficiencyPoint(tp * 1e6 * 1.001, 1.0)]
    sigma = accepted_cross_section_cm2(
        "numu_prompt", pts, n_t=8000, apply_efficiency=False, form_factor=False
    )
    assert math.isclose(sigma, exact, rel_tol=3e-7)


def test_all_flavor_components_nonnegative():
    pts = simple_efficiency()
    result = calculate_events(pts, n_t=300)
    assert result["total"] > 0
    assert all(result[k] >= 0 for k in ("numu_prompt", "nue", "numubar"))
