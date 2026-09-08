import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from nmir.g9_discrete_map_derivative import (
    DiscreteMapDerivativeBoundary,
    finite_sum_projected_mass_g,
    projected_mass_derivative_g_per_x,
)
from nmir.gravity_extended import RadialDensityProfile, projected_mass_g

R = 6.96e10


def rel(a, b):
    return abs(a-b)/max(abs(a), abs(b), 1e-300)


def profiles():
    return (
        RadialDensityProfile((0.0,0.25,0.6,1.0),(1.0,1.0,1.0,1.0)),
        RadialDensityProfile((0.0,0.25,0.6,1.0),(4.0,3.0,2.0,1.0)),
        RadialDensityProfile((0.0,0.2,0.7,1.0),(1.0,3.0,2.0,4.0)),
    )


def test_finite_sum_identity_on_preregistered_toys():
    for p in profiles():
        rs=p.radius_fraction
        for a,b in zip(rs,rs[1:]):
            for q in (0.25,0.5,0.75):
                x=a+q*(b-a)
                assert rel(finite_sum_projected_mass_g(p,x,R), projected_mass_g(p,x,R)) <= 5e-13


def test_analytic_derivative_matches_small_centered_difference_on_toys():
    for p in profiles():
        rs=p.radius_fraction
        for a,b in zip(rs,rs[1:]):
            for q in (0.25,0.5,0.75):
                x=a+q*(b-a)
                h=(b-a)/100000.0
                fd=(projected_mass_g(p,x+h,R)-projected_mass_g(p,x-h,R))/(2*h)
                exact=projected_mass_derivative_g_per_x(p,x,R)
                assert math.isfinite(exact)
                assert rel(exact,fd) <= 1e-8


def test_exact_fixed_knots_are_piece_boundaries():
    p=profiles()[0]
    for x in p.radius_fraction[1:-1]:
        with pytest.raises(DiscreteMapDerivativeBoundary):
            projected_mass_derivative_g_per_x(p,x,R)


def test_derivative_domain_rejects_endpoints():
    p=profiles()[0]
    with pytest.raises(ValueError):
        projected_mass_derivative_g_per_x(p,0.0,R)
    with pytest.raises(ValueError):
        projected_mass_derivative_g_per_x(p,1.0,R)
