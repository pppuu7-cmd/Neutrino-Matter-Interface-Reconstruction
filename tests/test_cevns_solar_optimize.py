from pathlib import Path

import pytest

from nmir.cevns_solar_optimize import (
    Target,
    cevns_sigma_above_threshold_cm2,
    git_blob_sha,
    helm_form_factor_sq,
    load_local_profile,
    rate_per_kg_day,
    spectrum_average_sigma_cm2,
)

AR40 = Target("Ar40", 18, 40)
BE7_PROFILE = Path("data/be7_bahcall1994_ground_profile.csv")
BE7_GS98_FLUX = 4.93e9 * 0.897


@pytest.mark.parametrize("a", [4, 12, 19, 40, 74, 132, 208])
def test_helm_zero_momentum_is_unity(a):
    assert helm_form_factor_sq(a, 0.0) == 1.0


@pytest.mark.parametrize("a", [4, 12, 19, 40, 74, 132, 208])
def test_helm_is_bounded_over_solar_q_support(a):
    for q_mev in [0.1, 1.0, 5.0, 10.0, 20.0, 40.0]:
        f2 = helm_form_factor_sq(a, q_mev)
        assert 0.0 <= f2 <= 1.000001


def test_git_blob_hash_matches_known_text_fixture():
    data = b"hello\n"
    # git hash-object --stdin for b"hello\n"
    assert git_blob_sha(data) == "ce013625030ba8dba906f756967f9e9ca394464a"


@pytest.mark.parametrize(
    "threshold_ev,expected_rate",
    [
        (10.0, 4.553823546552401e-3),
        (20.0, 2.0223206637544345e-3),
        (40.0, 3.973604373087567e-8),
    ],
)
def test_no_helm_reproduces_iteration_0042_ar40_be7(threshold_ev, expected_rate):
    profile = load_local_profile(BE7_PROFILE)
    sigma = spectrum_average_sigma_cm2(profile, threshold_ev, AR40, use_helm=False)
    rate = rate_per_kg_day(BE7_GS98_FLUX, sigma, AR40)
    assert rate == pytest.approx(expected_rate, rel=0.01)


def test_helm_never_increases_ar40_be7_rate():
    profile = load_local_profile(BE7_PROFILE)
    for threshold in [0.0, 10.0, 20.0, 40.0]:
        no_helm = spectrum_average_sigma_cm2(profile, threshold, AR40, use_helm=False)
        helm = spectrum_average_sigma_cm2(profile, threshold, AR40, use_helm=True)
        assert 0.0 <= helm <= no_helm * (1.0 + 1e-10)


def test_cross_section_monotone_in_threshold_for_fixed_energy():
    sigmas = [cevns_sigma_above_threshold_cm2(0.86258, t, AR40) for t in [0, 10, 20, 30, 40]]
    assert all(b <= a for a, b in zip(sigmas[:-1], sigmas[1:]))
