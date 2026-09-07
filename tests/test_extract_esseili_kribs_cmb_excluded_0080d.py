from scripts.extract_esseili_kribs_cmb_excluded_0080d import (
    DARK_BLUE, LIGHT_BLUE, GREEN, FORBIDDEN, AX, AY, BX, BY,
    to_phys_xy, to_pdf_xy, flatten_cubic, ck
)


def test_frozen_native_colors_are_distinct_and_green_forbidden():
    assert DARK_BLUE != LIGHT_BLUE
    assert GREEN in FORBIDDEN
    assert DARK_BLUE not in FORBIDDEN
    assert LIGHT_BLUE not in FORBIDDEN


def test_axis_round_trip():
    for x, y in [(100.0, 100.0), (300.0, 250.0), (600.0, 400.0)]:
        lm, lg = to_phys_xy(x, y)
        xr, yr = to_pdf_xy(lm, lg)
        assert abs(xr-x) < 1e-10
        assert abs(yr-y) < 1e-10


def test_cubic_refinement_monotone():
    p0=(0.0,0.0); p1=(0.0,1.0); p2=(1.0,1.0); p3=(1.0,0.0)
    coarse=flatten_cubic(p0,p1,p2,p3,0.02)
    fine=flatten_cubic(p0,p1,p2,p3,0.01)
    assert len(fine) >= len(coarse) >= 2
    assert coarse[0] == fine[0] == p0
    assert coarse[-1] == fine[-1] == p3


def test_color_rounding_matches_pinned_pdf_tuple_precision():
    assert ck((0.1999971,0.7333219,0.9333192)) == LIGHT_BLUE
