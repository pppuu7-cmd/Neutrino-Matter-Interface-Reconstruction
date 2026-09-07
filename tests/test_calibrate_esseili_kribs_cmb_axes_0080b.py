import pytest

pytest.importorskip("pymupdf")
from scripts.calibrate_esseili_kribs_cmb_axes_0080b import ols, loo_residuals, X_TEXT_TO_EXP, Y_TEXT_TO_EXP


def test_exact_affine_fit():
    xs=[1.0,2.0,3.0,4.0,5.0]
    ys=[-2.0,-1.0,0.0,1.0,2.0]
    a,b,res=ols(xs,ys)
    assert abs(a-1.0)<1e-14
    assert abs(b+3.0)<1e-14
    assert max(abs(x) for x in res)<1e-14
    assert max(abs(x) for x in loo_residuals(xs,ys))<1e-14


def test_frozen_x_tick_mapping_complete():
    assert sorted(X_TEXT_TO_EXP.values()) == list(range(-6,4))
    assert len(X_TEXT_TO_EXP)==10


def test_frozen_y_tick_mapping_complete():
    assert sorted(Y_TEXT_TO_EXP.values()) == list(range(-17,-2))
    assert len(Y_TEXT_TO_EXP)==15
