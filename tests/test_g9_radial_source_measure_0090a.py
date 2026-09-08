import importlib.util
import math
from pathlib import Path
import sys

import numpy as np

SCRIPTS=Path(__file__).parents[1]/"scripts"
sys.path.insert(0,str(SCRIPTS))
P=SCRIPTS/"g9_radial_source_measure_0090a.py"
spec=importlib.util.spec_from_file_location("g9_0090a",P)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


def test_centered_radial_measure_normalizes():
    for s in (0.2,2.0,20.0):
        for a in (0.1,1.0,10.0):
            n=m.radial_normalization(s,0.0,a,64)
            assert abs(n-1.0)<=2e-12


def test_offset_radial_measure_arbitrary_tuple_smoke():
    # Preflight implementation smoke only. It carries no quadrature-accuracy
    # authority for arbitrary non-sentinel tuples. Scientific H1=2e-10 remains
    # unchanged inside run_shard on every prospectively frozen sentinel.
    # See research/prereg/0090a_amendment2_preflight_no_accuracy_gate.md.
    for s,d,a in ((1.0,0.25,0.3),(1.0,2.0,0.4),(3.0,3.0,1.0),(10.0,1.0,20.0)):
        n=m.radial_normalization(s,d,a,64)
        assert math.isfinite(n)
        assert n>0.0


def test_phi_fraction_degenerate_and_geometric_cases():
    a=2.0
    assert m.phi_fraction(np.array([0.0]),np.array([1.0]),a)[0]==1.0
    assert m.phi_fraction(np.array([0.0]),np.array([3.0]),a)[0]==0.0
    assert m.phi_fraction(np.array([1.0]),np.array([0.0]),a)[0]==1.0
    assert m.phi_fraction(np.array([3.0]),np.array([0.0]),a)[0]==0.0
    got=m.phi_fraction(np.array([a]),np.array([a]),a)[0]
    assert abs(got-1/3)<1e-14


def test_source_interval_boundaries_are_frozen_geometry_only():
    got=m.source_intervals(4.0,1.0,2.0)
    pts=[got[0][0]]+[b for _,b in got]
    assert pts==[0.0,2.0,3.0,5.0]
    got=m.source_intervals(1.0,4.0,3.5)
    pts=[got[0][0]]+[b for _,b in got]
    assert pts==[3.0,3.5,5.0]


def test_monotone_abs_partition_contains_turn_and_zero():
    turn=0.013
    x0=0.024
    assert m.monotone_abs_segments(turn,x0)==((m.XMIN,turn),(turn,x0),(x0,m.XMAX))


def test_convergence_uses_excess_not_full_mu():
    assert math.isclose(m.convergence(2.0,2.005),0.005/1.005,rel_tol=1e-13)
    assert m.convergence(1.0+1e-12,1.0+2e-12)<=1e-10
