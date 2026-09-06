import math

from nmir.li7_full_response import (
    LI7_EX_TO_GS_STRENGTH_RATIO,
    LI7_TO_BE7_EX_THRESHOLD_MEV,
    li7_excited_sigma_cm2,
    li7_two_state_sigma_cm2,
)
from nmir.li7_ground_response import li7_ground_sigma_cm2


def test_li7_excited_branch_is_fail_closed_at_threshold():
    assert li7_excited_sigma_cm2(LI7_TO_BE7_EX_THRESHOLD_MEV) == 0.0
    assert li7_excited_sigma_cm2(LI7_TO_BE7_EX_THRESHOLD_MEV + 1e-6) > 0.0


def test_li7_excited_branch_uses_frozen_strength_ratio():
    enu = 5.0
    shifted_ground = li7_ground_sigma_cm2(enu - 0.429)
    assert math.isclose(
        li7_excited_sigma_cm2(enu) / shifted_ground,
        LI7_EX_TO_GS_STRENGTH_RATIO,
        rel_tol=2e-14,
    )


def test_li7_two_state_is_ground_below_excited_threshold():
    enu = 1.0
    assert li7_two_state_sigma_cm2(enu) == li7_ground_sigma_cm2(enu)


def test_li7_two_state_exceeds_ground_above_excited_threshold():
    assert li7_two_state_sigma_cm2(5.0) > li7_ground_sigma_cm2(5.0)
