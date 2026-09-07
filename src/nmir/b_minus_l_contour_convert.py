"""Convention helpers for NMIR iteration 0072 B-L contour materialization.

These functions implement only frozen unit/convention changes.  They do not
supply an experimental exclusion contour and must not be used to turn a
secondary digitization into primary authority.
"""

from __future__ import annotations

import math

# CODATA-compatible hbar*c in eV m (precision more than adequate for contour work).
HBAR_C_EV_M = 1.973269804e-7

# Natural-unit constants used to map the Wagner et al. dimensionless Yukawa
# strength alpha_tilde to the dimensionless gauge coupling in
# L_int = g_BL V_mu J^(mu)_(B-L).
G_NEWTON_GEV_MINUS2 = 6.70883e-39
ATOMIC_MASS_UNIT_GEV = 0.93149410242

G_PER_SQRT_ALPHA = math.sqrt(
    4.0 * math.pi * G_NEWTON_GEV_MINUS2 * ATOMIC_MASS_UNIT_GEV**2
)


def mass_ev_from_range_m(lambda_m: float) -> float:
    """Return mediator mass in eV from Yukawa range lambda in metres."""
    if lambda_m <= 0.0:
        raise ValueError("lambda_m must be positive")
    return HBAR_C_EV_M / lambda_m


def range_m_from_mass_ev(mass_ev: float) -> float:
    """Return Yukawa/Compton range in metres from mediator mass in eV."""
    if mass_ev <= 0.0:
        raise ValueError("mass_ev must be positive")
    return HBAR_C_EV_M / mass_ev


def g_bl_from_alpha_tilde(alpha_tilde: float) -> float:
    """Map |alpha_tilde| to |g_BL| under Wagner et al. Eq. (4) convention.

    The primary convention is
      |alpha_tilde| = g_BL^2 / (4*pi*G_N*u^2)
    for q_tilde = B-L, after identifying the paper's dimensionless B-L
    fermion charge with the frozen NMIR current convention.
    """
    if alpha_tilde < 0.0:
        alpha_tilde = abs(alpha_tilde)
    return G_PER_SQRT_ALPHA * math.sqrt(alpha_tilde)


def alpha_tilde_from_g_bl(g_bl: float) -> float:
    """Inverse of :func:`g_bl_from_alpha_tilde` for coupling magnitude."""
    return (abs(g_bl) / G_PER_SQRT_ALPHA) ** 2


def convert_yukawa_point(lambda_m: float, alpha_tilde: float) -> tuple[float, float]:
    """Convert one primary (lambda[m], alpha_tilde) point to (m[eV], g_BL)."""
    return mass_ev_from_range_m(lambda_m), g_bl_from_alpha_tilde(alpha_tilde)
