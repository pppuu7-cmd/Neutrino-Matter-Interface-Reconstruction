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
        assert np.all(np.diff(u) >= -1e-14*max(s,d,1.0))
        assert abs(u[0]-abs(d-s)) <= 2e-14*max(s,d,1.0)
        assert abs(u[-1]-(d+s)) <= 2e-14*max(s,d,1.0)


def test_fixed_preregistered_geometry_controls_use_endpoint_regularized_route():
    # Pre-result implementation conformance only. The hosted artifact, not this
    # unit test, carries scientific authority.
    for s,d,_ in m.analytic_controls():
        row=m.evaluate_pair(s,d,"unit-control")
        assert row["abs_error_l"] <= (m.CENTER_TOL if d == 0.0 else m.NORM_TOL)
        assert row["abs_error_h"] <= (m.CENTER_TOL if d == 0.0 else m.NORM_TOL)
        if d != 0.0:
            assert row["lh_abs"] <= m.NORM_TOL


def test_scale_controls_are_dimensionless():
    rows=[m.evaluate_pair(s,2.0*s,"scale") for s in (1e-6,1.0,1e6)]
    for key in ("n_l","n_h"):
        vals=[r[key] for r in rows]
        assert max(vals)-min(vals) <= m.SCALE_TOL
