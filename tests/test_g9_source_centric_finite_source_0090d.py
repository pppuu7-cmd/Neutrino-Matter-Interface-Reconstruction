import importlib.util
from pathlib import Path

import numpy as np

SCRIPT=Path(__file__).resolve().parents[1]/"scripts"/"g9_source_centric_finite_source_0090d.py"
spec=importlib.util.spec_from_file_location("g9_0090d",SCRIPT)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


def test_frozen_sentinel_declarations():
    assert m.THETA_INDICES==(0,12,24)
    assert m.DELTA_M==(0.0,0.1,100.0)
    assert tuple(m.SOURCE_REPLICAS["L"])==(8,16,32)
    assert tuple(m.SOURCE_REPLICAS["H"])==(16,32,64)


def test_source_nodes_are_finite_and_positive_weighted():
    u,w=m.source_nodes(3.0,1.5,4,8)
    assert len(u)==32 and len(w)==32
    assert np.all(np.isfinite(u)) and np.all(u>=0.0)
    assert np.all(np.isfinite(w)) and np.all(w>0.0)


def test_convergence_metric_has_frozen_branches():
    d,lim=m.conv_metric(2.0,2.001)
    assert lim==m.REL_TOL and d>=0.0
    d2,lim2=m.conv_metric(1.0,1.0)
    assert lim2==m.ABS_SMALL_TOL and d2==0.0
