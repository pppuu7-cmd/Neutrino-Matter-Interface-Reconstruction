"""NMIR v2 gate 0105d: composition/range identifiability controls.

This module implements coefficient-level pre-data identities only.  It does not
calculate observed event rates, likelihoods, p-values or BSM significances.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

from nmir.vector_mediator_bridge_0105b import mediator_mass_from_ratio_gev


@dataclass(frozen=True)
class EqualQRecovery:
    rho_gp_over_gn: float
    finite_q_factor: float
    mediator_mass_gev: float


def _finite(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def _nonnegative_int(name: str, value: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def composition_determinant(z1: int, n1: int, z2: int, n2: int) -> int:
    """Return Delta12 = Z1*N2 - Z2*N1."""
    z1 = _nonnegative_int("z1", z1)
    n1 = _nonnegative_int("n1", n1)
    z2 = _nonnegative_int("z2", z2)
    n2 = _nonnegative_int("n2", n2)
    return z1 * n2 - z2 * n1


def medium_charge_factor(rho: float, y_proton: float, y_neutron: float) -> float:
    rho = _finite("rho", rho)
    yp = _finite("y_proton", y_proton)
    yn = _finite("y_neutron", y_neutron)
    return yp * rho + yn


def nuclear_charge_factor(rho: float, z: int, n: int) -> float:
    rho = _finite("rho", rho)
    z = _nonnegative_int("z", z)
    n = _nonnegative_int("n", n)
    return z * rho + n


def normalized_scattering_to_forward_ratio(
    rho: float,
    mediator_mass_gev: float,
    q_gev: float,
    z: int,
    n: int,
    y_proton: float,
    y_neutron: float,
) -> float:
    """Return R=[(Z*rho+N)/(Yp*rho+Yn)]*mX^2/(mX^2+q^2)."""
    mass = _finite("mediator_mass_gev", mediator_mass_gev)
    q = _finite("q_gev", q_gev)
    if mass <= 0.0:
        raise ValueError("mediator_mass_gev must be > 0")
    if q < 0.0:
        raise ValueError("q_gev must be >= 0")
    a_medium = medium_charge_factor(rho, y_proton, y_neutron)
    a_target = nuclear_charge_factor(rho, z, n)
    if a_medium == 0.0:
        raise ValueError("forward medium charge factor is zero in this coordinate chart")
    finite_q_factor = mass * mass / (mass * mass + q * q)
    return (a_target / a_medium) * finite_q_factor


def recover_rho_from_two_targets_equal_q(
    ratio1: float,
    ratio2: float,
    z1: int,
    n1: int,
    z2: int,
    n2: int,
) -> float:
    """Recover rho from k=R1/R2 at common q, when compositions are nonparallel."""
    r1 = _finite("ratio1", ratio1)
    r2 = _finite("ratio2", ratio2)
    delta = composition_determinant(z1, n1, z2, n2)
    if delta == 0:
        raise ValueError("target compositions are proportional and do not identify rho")
    if r2 == 0.0:
        raise ValueError("ratio2 is zero; this ratio chart is singular")
    k = r1 / r2
    denominator = k * z2 - z1
    scale = max(1.0, abs(k * z2), abs(z1))
    if abs(denominator) <= 1e-14 * scale:
        raise ValueError("rho inversion denominator is singular")
    return (n1 - k * n2) / denominator


def recover_mass_from_target_ratio_equal_q_gev(
    ratio: float,
    rho: float,
    q_gev: float,
    z: int,
    n: int,
    y_proton: float,
    y_neutron: float,
) -> tuple[float, float]:
    """Recover (mX,f) after rho is known, with f=mX^2/(mX^2+q^2)."""
    ratio = _finite("ratio", ratio)
    q = _finite("q_gev", q_gev)
    if q <= 0.0:
        raise ValueError("q_gev must be > 0 for finite-range mass identification")
    a_medium = medium_charge_factor(rho, y_proton, y_neutron)
    a_target = nuclear_charge_factor(rho, z, n)
    if a_medium == 0.0:
        raise ValueError("forward medium charge factor is zero in this coordinate chart")
    if a_target == 0.0:
        raise ValueError("target charge factor is zero in this coordinate chart")
    f = ratio * a_medium / a_target
    if not 0.0 < f < 1.0:
        raise ValueError("recovered finite-q factor must satisfy 0 < f < 1")
    return mediator_mass_from_ratio_gev(f, q), f


def recover_equal_q_parameters(
    ratio1: float,
    ratio2: float,
    q_gev: float,
    z1: int,
    n1: int,
    z2: int,
    n2: int,
    y_proton: float,
    y_neutron: float,
) -> EqualQRecovery:
    """Recover rho and mX from two target/forward coefficient ratios at common q."""
    rho = recover_rho_from_two_targets_equal_q(ratio1, ratio2, z1, n1, z2, n2)
    mass, f = recover_mass_from_target_ratio_equal_q_gev(
        ratio1, rho, q_gev, z1, n1, y_proton, y_neutron
    )
    return EqualQRecovery(rho_gp_over_gn=rho, finite_q_factor=f, mediator_mass_gev=mass)
