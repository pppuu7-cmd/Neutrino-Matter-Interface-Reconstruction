from __future__ import annotations

from dataclasses import dataclass

P_LEADING_W_PER_KG = 1.2056895107775174e-9
R_ONE_BODY = 1.8988146448649366
R_EMPIRICAL_EXTRA = 1.01
SAFETY_FACTORS = (1.0, 3.0, 10.0, 100.0, 1000.0)


@dataclass(frozen=True)
class StressPoint:
    safety_factor: float
    r_two_body: float
    power_w_per_kg: float
    deficit_to_1w: float


def stressed_power_w_per_kg(r_two_body: float) -> float:
    if r_two_body < 0:
        raise ValueError("r_two_body must be nonnegative")
    amp = 1.0 + R_ONE_BODY + r_two_body
    return P_LEADING_W_PER_KG * amp * amp


def required_extra_amplitude_for_power(target_w_per_kg: float = 1.0) -> float:
    if target_w_per_kg <= 0:
        raise ValueError("target_w_per_kg must be positive")
    return (target_w_per_kg / P_LEADING_W_PER_KG) ** 0.5 - 1.0 - R_ONE_BODY


def stress_ladder() -> list[StressPoint]:
    out: list[StressPoint] = []
    for factor in SAFETY_FACTORS:
        r_two = factor * R_EMPIRICAL_EXTRA
        power = stressed_power_w_per_kg(r_two)
        out.append(
            StressPoint(
                safety_factor=factor,
                r_two_body=r_two,
                power_w_per_kg=power,
                deficit_to_1w=1.0 / power,
            )
        )
    return out


def classify() -> str:
    points = {p.safety_factor: p for p in stress_ladder()}
    bridge = required_extra_amplitude_for_power(1.0)
    bridge_ratio = bridge / R_EMPIRICAL_EXTRA
    p100 = points[100.0].power_w_per_kg
    if p100 < 1.0e-3 and bridge_ratio > 1.0e4:
        return "PASS_EMPIRICAL_STRENGTH_STRONG_NEGATIVE"
    if p100 < 1.0:
        return "PARTIAL_EMPIRICAL_STRENGTH_NEGATIVE"
    return "FAIL_EMPIRICAL_ENVELOPE_NOT_SMALL"
