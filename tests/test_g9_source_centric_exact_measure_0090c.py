import importlib.util
from pathlib import Path

import numpy as np

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "g9_source_centric_exact_measure_0090c.py"
spec = importlib.util.spec_from_file_location("g9_0090c", SCRIPT)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_product_node_shapes_and_finiteness():
    for nq,nphi in m.REPLICAS.values():
        q,phi,w=m.product_nodes(nq,nphi)
        assert len(q)==nq*nphi
        assert len(phi)==len(q)==len(w)
        assert np.all(np.isfinite(q)) and np.all(np.isfinite(phi)) and np.all(np.isfinite(w))
        assert np.all(q>0.0) and np.all(q<1.0) and np.all(w>0.0)


def test_source_coordinate_mapping_smoke():
    q,phi,w=m.product_nodes(4,8)
    s=1.0; d=1.1
    r=s*np.sqrt(q)
    x=d+r*np.cos(phi); y=r*np.sin(phi); u=np.hypot(x,y)
    assert np.all(np.isfinite(u))
    assert np.all(u>=0.0)
    assert np.all(r<=s)


def test_fixed_cardinalities_are_declared():
    assert m.THETA_INDICES==(0,6,12,18,24)
    assert len(m.D_CONTROLS)==9
    assert tuple(m.REPLICAS["L"])==(16,32)
    assert tuple(m.REPLICAS["H"])==(32,64)
