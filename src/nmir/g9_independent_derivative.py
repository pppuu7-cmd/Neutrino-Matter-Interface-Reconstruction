"""Public 0088 root-locator API; continuous geometry is locator-only authority."""
from .g9_independent_derivative_v3 import (
    RootCertificationBlocked,
    RootBracket,
    converged_simpson as adaptive_simpson,
    mass_derivative as continuous_mass_and_derivative,
    derivative as independent_derivative,
    roots as isolate_sign_roots,
    dyadic as fixed_dyadic_points,
)

__all__ = [
    "RootCertificationBlocked",
    "RootBracket",
    "adaptive_simpson",
    "continuous_mass_and_derivative",
    "independent_derivative",
    "isolate_sign_roots",
    "fixed_dyadic_points",
]
