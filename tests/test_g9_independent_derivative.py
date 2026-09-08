import math
import pytest
from nmir.g9_independent_derivative_v2 import simpson,mass_derivative,dyadic,roots
from nmir.gravity_extended import RadialDensityProfile

def test_adaptive_simpson_polynomial():
    assert simpson(lambda x:x**4,0.0,1.0)==pytest.approx(0.2,rel=1e-11,abs=1e-12)

def test_uniform_sphere_projection_and_derivative():
    p=RadialDensityProfile((0.0,1.0),(1.0,1.0)); x=0.37
    mass,dmass=mass_derivative(p,x,1.0)
    em=4*math.pi/3*(1-(1-x*x)**1.5); ed=4*math.pi*x*math.sqrt(1-x*x)
    assert mass==pytest.approx(em,rel=2e-9)
    assert dmass==pytest.approx(ed,rel=2e-9)

def test_known_multi_turn_root_set():
    grid=tuple((i+0.37)/100 for i in range(100)); fn=lambda x:(x-.2)*(x-.5)*(x-.8)
    assert [r.root for r in roots(fn,grid)]==pytest.approx([.2,.5,.8],abs=1e-11)

def test_fixed_dyadic_mesh_is_result_independent():
    assert dyadic((0.,1.,2.),.25,1.25)==pytest.approx((.375,.5,.625,.75,.875,1.125))
