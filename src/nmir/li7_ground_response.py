"""Ground-state-only 7Li(nu_e,e-)7Be response from evaluated 7Be EC log(ft).

This module deliberately includes only the directly crossed gs<->gs matrix element.
It is a screening/lower-bound response, not a complete lithium-detector model.
"""
from __future__ import annotations

from .ft_capture import M_E_MEV, point_fermi_function, sigma_v_over_c_from_ft_cm2

LI7_TO_BE7_GS_THRESHOLD_MEV = 0.861815
LI7_GS_LOGFT = 3.324
LI7_GS_FT_S = 10.0 ** LI7_GS_LOGFT
BE7_DAUGHTER_Z = 4


def li7_ground_sigma_cm2(enu_mev: float) -> float:
    """Cross section for 7Li(gs)+nu_e -> 7Be(gs)+e-.

    Uses the evaluated 7Be(gs)->7Li(gs) EC log(ft), crossed to capture.
    The neutral-atom Q_EC is used as the screening threshold convention.
    Atomic/screening corrections at the sub-keV Be7-line edge are intentionally
    not hidden; the near-threshold Be7 contribution must be sensitivity-tested.
    """
    if enu_mev <= LI7_TO_BE7_GS_THRESHOLD_MEV:
        return 0.0
    kinetic_mev = enu_mev - LI7_TO_BE7_GS_THRESHOLD_MEV
    e_total = M_E_MEV + kinetic_mev
    f = point_fermi_function(BE7_DAUGHTER_Z, e_total)
    return sigma_v_over_c_from_ft_cm2(LI7_GS_FT_S, e_total, f)
