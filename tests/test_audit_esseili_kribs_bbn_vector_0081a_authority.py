from scripts.audit_esseili_kribs_bbn_vector_0081a_authority import (
    ADJACENCY_TOL_PT,
    COLOR_TOL,
    CROSS_TOL,
    FIT_TOL,
    color_close,
    dash_is_non_solid,
    fit_axis,
    is_dashed_red_overlay,
    point_to_bbox_distance,
)


def test_exact_log_axis_fit_passes_frozen_limits():
    ticks = [{"xc": float(i), "exponent": e} for i, e in enumerate([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3])]
    fit = fit_axis(ticks, "xc")
    assert fit["anchor_count"] >= 4
    assert fit["max_abs_residual_decade"] <= FIT_TOL
    assert fit["max_abs_loo_decade"] <= FIT_TOL
    assert CROSS_TOL == 0.015


def test_color_match_tolerance_is_frozen_to_one_8bit_step():
    assert color_close((0.2, 0.4, 0.6), (0.2 + 1/255, 0.4, 0.6))
    assert not color_close((0.2, 0.4, 0.6), (0.2 + 2/255 + 1e-4, 0.4, 0.6))
    assert COLOR_TOL > 1/255


def test_dashed_red_overlay_requires_both_red_and_non_solid():
    red_dashed = {"stroke_rgb": (0.9, 0.1, 0.1), "fill_rgb": None, "dashes": "[3 2] 0", "width": 1.0}
    red_solid = {"stroke_rgb": (0.9, 0.1, 0.1), "fill_rgb": None, "dashes": "[] 0", "width": 1.0}
    blue_dashed = {"stroke_rgb": (0.1, 0.1, 0.9), "fill_rgb": None, "dashes": "[3 2] 0", "width": 1.0}
    assert dash_is_non_solid(red_dashed["dashes"])
    assert is_dashed_red_overlay(red_dashed)
    assert not is_dashed_red_overlay(red_solid)
    assert not is_dashed_red_overlay(blue_dashed)


def test_bbox_distance_is_zero_inside_and_respects_adjacency_threshold():
    bbox = (10.0, 10.0, 20.0, 20.0)
    assert point_to_bbox_distance((15.0, 15.0), bbox) == 0.0
    assert point_to_bbox_distance((22.0, 15.0), bbox) == 2.0
    assert point_to_bbox_distance((22.0, 15.0), bbox) <= ADJACENCY_TOL_PT
    assert point_to_bbox_distance((23.0, 15.0), bbox) > ADJACENCY_TOL_PT
