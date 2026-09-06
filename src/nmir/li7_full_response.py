"""Two-state 7Li(nu_e,e-)7Be response for prospective external validation.

Normalization is anchored to the evaluated crossed gs<->gs log(ft) already used
by NMIR.  The independently measured 7Li(gs)->7Be*(429 keV) GT strength is
added only through a strength ratio, so no published neutrino cross section is
used to tune the model.
"""
from __future__ import annotations

from .li7_ground_response import LI7_TO_BE7_GS_THRESHOLD_MEV, li7_ground_sigma_cm2

LI7_TO_BE7_EXCITATION_MEV = 0.429
LI7_TO_BE7_EX_THRESHOLD_MEV = LI7_TO_BE7_GS_THRESHOLD_MEV + LI7_TO_BE7_EXCITATION_MEV

# Shao et al., EPJC 83, 799 (2023), using measured (3He,t) strengths.
LI7_GS_BF = 1.0
LI7_GS_BGT = 1.19
LI7_EX_BF = 0.0
LI7_EX_BGT = 1.06
GA_OVER_GV = 1.2723


def _allowed_strength(bf: float, bgt: float) -> float:
    return bf + GA_OVER_GV**2 * bgt


LI7_EX_TO_GS_STRENGTH_RATIO = _allowed_strength(LI7_EX_BF, LI7_EX_BGT) / _allowed_strength(
    LI7_GS_BF, LI7_GS_BGT
)


def li7_excited_sigma_cm2(enu_mev: float) -> float:
    """First-excited-state contribution with no neutrino-cross-section tuning.

    Shifting E_nu down by the 429-keV excitation gives the same outgoing
    electron phase space as the ground-state branch at the shifted energy.
    The result is then multiplied by the independently measured allowed-strength
    ratio.  Atomic screening/finite-size refinements remain outside this model.
    """
    if enu_mev <= LI7_TO_BE7_EX_THRESHOLD_MEV:
        return 0.0
    shifted = enu_mev - LI7_TO_BE7_EXCITATION_MEV
    return LI7_EX_TO_GS_STRENGTH_RATIO * li7_ground_sigma_cm2(shifted)


def li7_two_state_sigma_cm2(enu_mev: float) -> float:
    """Ground plus 429-keV first-excited-state charged-current response."""
    return li7_ground_sigma_cm2(enu_mev) + li7_excited_sigma_cm2(enu_mev)
