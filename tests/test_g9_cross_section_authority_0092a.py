import math


def test_faser_15tev_conservative_cc_opacity():
    n_n = 1.7659857664161126e36
    coeff = 0.3e-38
    e_gev = 1500.0
    sigma = coeff * e_gev
    tau = n_n * sigma
    assert math.isclose(sigma, 4.5e-36, rel_tol=0.0, abs_tol=1e-50)
    assert math.isclose(tau, 7.946935948872507, rel_tol=1e-15)
    assert tau >= 1.0
    assert math.exp(-tau) < math.exp(-1.0)


def test_authority_separation_is_explicit():
    text = open('scripts/g9_cross_section_authority_0092a.py', encoding='utf-8').read()
    assert 'BLOCKED_G9_0092A_MEV_TOTAL_CROSS_SECTION_AUTHORITY' in text
    assert 'BLOCKED_G9_0092A_HIGH_ENERGY_AUTHORITY' in text
    assert 'SCIENTIFIC_FAIL_G9_TRANSPARENT_SUN_ASSUMPTION' in text
