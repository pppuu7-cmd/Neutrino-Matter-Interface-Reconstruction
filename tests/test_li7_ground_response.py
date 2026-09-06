import math

from nmir.li7_ground_response import (
    LI7_TO_BE7_GS_THRESHOLD_MEV,
    li7_ground_sigma_cm2,
)


def test_li7_ground_threshold_is_fail_closed():
    assert li7_ground_sigma_cm2(LI7_TO_BE7_GS_THRESHOLD_MEV - 1e-9) == 0.0
    assert li7_ground_sigma_cm2(LI7_TO_BE7_GS_THRESHOLD_MEV) == 0.0
    assert li7_ground_sigma_cm2(LI7_TO_BE7_GS_THRESHOLD_MEV + 1e-6) > 0.0


def test_li7_ground_pep_scale_from_evaluated_logft():
    # Frozen regression value for logft=3.324, Q_EC=861.815 keV, point-Coulomb Z=4.
    sigma = li7_ground_sigma_cm2(1.442)
    assert math.isclose(sigma, 5.560642060859964e-44, rel_tol=2e-12)


def test_li7_ground_cross_section_grows_above_threshold():
    assert li7_ground_sigma_cm2(5.0) > li7_ground_sigma_cm2(1.442)
    assert li7_ground_sigma_cm2(10.0) > li7_ground_sigma_cm2(5.0)
