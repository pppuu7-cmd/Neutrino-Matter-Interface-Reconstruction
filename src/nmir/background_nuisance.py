from __future__ import annotations

import math

from .background_requirements import asimov_significance


def asimov_significance_with_background_uncertainty(
    signal: float,
    background: float,
    fractional_background_uncertainty: float,
) -> float:
    """Median discovery significance with a Gaussian background-normalization nuisance.

    Uses the standard Cowan-profile Asimov expression with
    sigma_b = fractional_background_uncertainty * background.
    """
    if signal <= 0 or background <= 0:
        raise ValueError("signal and background must be positive")
    if fractional_background_uncertainty < 0:
        raise ValueError("fractional_background_uncertainty must be non-negative")
    if fractional_background_uncertainty == 0:
        return asimov_significance(signal, background)

    sigma_b = fractional_background_uncertainty * background
    sigma_b2 = sigma_b * sigma_b
    spb = signal + background
    b2 = background * background

    numerator = spb * (background + sigma_b2)
    denominator = b2 + spb * sigma_b2
    if numerator <= 0 or denominator <= 0:
        raise ValueError("invalid logarithm arguments")

    term1 = spb * math.log(numerator / denominator)
    term2 = (b2 / sigma_b2) * math.log1p(
        (sigma_b2 * signal) / (background * (background + sigma_b2))
    )
    z2 = 2.0 * (term1 - term2)
    if z2 < -1e-12 or not math.isfinite(z2):
        raise ValueError("non-finite or negative profile-Asimov significance square")
    return math.sqrt(max(z2, 0.0))


def max_background_for_significance_with_uncertainty(
    signal: float,
    target_z: float,
    fractional_background_uncertainty: float,
    *,
    rtol: float = 1e-13,
) -> float:
    if signal <= 0 or target_z <= 0:
        raise ValueError("signal and target_z must be positive")
    if fractional_background_uncertainty < 0:
        raise ValueError("fractional_background_uncertainty must be non-negative")
    if rtol <= 0:
        raise ValueError("rtol must be positive")

    lo = 1e-15
    hi = max(1.0, signal)
    while asimov_significance_with_background_uncertainty(
        signal, hi, fractional_background_uncertainty
    ) > target_z:
        hi *= 2.0
        if not math.isfinite(hi):
            raise RuntimeError("failed to bracket background ceiling")

    for _ in range(256):
        mid = math.sqrt(lo * hi)
        z = asimov_significance_with_background_uncertainty(
            signal, mid, fractional_background_uncertainty
        )
        if z >= target_z:
            lo = mid
        else:
            hi = mid
        if hi / lo - 1.0 <= rtol:
            break

    result = math.sqrt(lo * hi)
    if result <= 0 or not math.isfinite(result):
        raise RuntimeError("invalid inverted background ceiling")
    return result
