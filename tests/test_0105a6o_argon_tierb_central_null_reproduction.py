import math
import numpy as np
from scripts.run_0105a6o_argon_tierb_central_null_reproduction_v2 import EXPECTED_GRID, TARGET, ROBUST, q


def test_frozen_grid_is_exactly_960_and_decimal_centers():
    assert EXPECTED_GRID.shape == (960, 3)
    assert np.array_equal(EXPECTED_GRID[0], np.array([5.0, 0.525, 0.15]))
    assert np.array_equal(EXPECTED_GRID[-1], np.array([115.0, 0.875, 4.65]))


def test_q_matches_frozen_one_bin_formula():
    n=np.array([2.0]); s={"S":np.array([1.0]),"P":np.array([0.0]),"D":np.array([0.0]),"B":np.array([0.0])}
    got=q([2.0,497.0,33.0,3152.0],n,s,3152.0,None)
    # mu=2; all Gaussian penalties are zero.
    expected=2.0*(2.0-2.0*math.log(2.0))
    assert abs(got-expected)<1e-12


def test_cevns_has_no_sm_gaussian_penalty():
    n=np.array([0.0]); s={"S":np.array([1.0]),"P":np.array([0.0]),"D":np.array([0.0]),"B":np.array([0.0])}
    assert abs(q([128.0,497.0,33.0,3152.0],n,s,3152.0)-256.0)<1e-12
    assert abs(q([159.0,497.0,33.0,3152.0],n,s,3152.0)-318.0)<1e-12


def test_negative_normalization_is_forbidden():
    n=np.array([1.0]); s={k:np.array([0.25]) for k in "SPDB"}
    assert math.isinf(q([-1.0,497.0,33.0,3152.0],n,s,3152.0))


def test_publication_and_dual_anchor_thresholds_are_frozen():
    assert TARGET == {"NC":(159.0,2.0),"NP":(553.0,3.0),"ND":(10.0,3.0),"NB":(3131.0,3.0),"sigma_profile":(43.0,2.0),"Z_stat":(3.9,0.15)}
    assert ROBUST == {"NC":1.0,"NP":1.0,"ND":1.0,"Z_stat":0.05,"sigma_profile":0.5}
