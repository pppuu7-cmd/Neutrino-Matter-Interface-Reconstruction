from __future__ import annotations

import math


def asimov_significance(signal: float, background: float) -> float:
    if signal <= 0 or background <= 0:
        raise ValueError("signal and background must be positive")
    x = 2.0 * ((signal + background) * math.log1p(signal / background) - signal)
    return math.sqrt(max(x, 0.0))


def max_background_for_significance(signal: float, target_z: float, *, rtol: float = 1e-13) -> float:
    if signal <= 0 or target_z <= 0:
        raise ValueError("signal and target_z must be positive")
    lo = 1e-15
    hi = max(1.0, signal)
    while asimov_significance(signal, hi) > target_z:
        hi *= 2.0
    for _ in range(256):
        mid = math.sqrt(lo * hi)
        z = asimov_significance(signal, mid)
        if z >= target_z:
            lo = mid
        else:
            hi = mid
        if hi / lo - 1.0 <= rtol:
            break
    return math.sqrt(lo * hi)
