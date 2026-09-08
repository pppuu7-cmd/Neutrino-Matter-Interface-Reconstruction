import importlib.util
from pathlib import Path

import numpy as np

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "g9_endpoint_regularized_radial_measure_0090b.py"
spec = importlib.util.spec_from_file_location("g9_0090b", SCRIPT)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_centered_branch_is_analytic():
    for s in (1e-6, 1.0, 1e6):
        assert m.transformed_normalization(s, 0.0, 32) == 1.0
        assert m.transformed_normalization(s, 0.0, 64) == 1.0


def test_transformed_u_maps_partial_support_monotonically():
    for s, d in ((1.0,0.1),(1.0,0.9),(1.0,1.0),(1.0,2.0),(1.0,10.0)):
        t=np.linspace(0.0,np.pi,m.DIAG_N)
        u=m.transformed_u(t,s,d)
        assert np.all(np.isfinite(u))
        assert np.all(np.diff(u) >= -1e-14*max(s,d,1.0))
        assert abs(u[0]-abs(d-s)) <= 2e-14*max(s,d,1.0)
        assert abs(u[-1]-(d+s)) <= 2e-14*max(s,d,1.0)


def test_endpoint_regularized_route_is_finite_positive_smoke_only():
    # Amendment 0090b_amendment_preflight_scope.md: preflight carries no
    # H1/H2/H3 scientific accuracy authority. Exact thresholds are evaluated
    # only by the hosted authority script and cannot be relaxed there.
    for s,d,_ in m.analytic_controls():
        for order in m.ORDERS:
            n=m.transformed_normalization(s,d,order)
            assert np.isfinite(n)
            assert n > 0.0


def test_partial_omega_stays_in_geometric_range():
    for s,d in ((1.0,0.1),(1.0,0.9),(1.0,1.0),(1.0,1.1),(1.0,2.0),(1.0,10.0)):
        t=np.linspace(1e-6,np.pi-1e-6,33)
        u=m.transformed_u(t,s,d)
        om=m.omega_partial(u,s,d)
        assert np.all(np.isfinite(om))
        assert np.all(om >= 0.0)
        assert np.all(om <= 2.0*np.pi)
