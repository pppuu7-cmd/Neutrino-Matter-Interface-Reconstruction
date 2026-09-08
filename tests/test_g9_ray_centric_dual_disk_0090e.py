import math

import g9_ray_centric_dual_disk_0090e as g


def test_circle_overlap_exact_branches():
    assert g.circle_overlap(2.0,3.0,5.0) == 0.0
    assert g.circle_overlap(2.0,3.0,0.5) == math.pi*4.0
    assert g.circle_overlap(5.0,1.0,0.0) == math.pi


def test_circle_overlap_partial_symmetry_and_scale():
    s,a,h=2.3,1.7,2.1
    o=g.circle_overlap(s,a,h)
    assert 0.0 < o < math.pi*min(s,a)**2
    assert math.isclose(o,g.circle_overlap(a,s,h),rel_tol=2e-14,abs_tol=0.0)
    for c in (1e-6,1.0,1e6):
        oc=g.circle_overlap(c*s,c*a,c*h)/(c*c)
        assert math.isclose(oc,o,rel_tol=2e-13,abs_tol=1e-20)


def test_extreme_radius_partial_overlap_float_conformance():
    # Amendment 0090e-r1: conformance-only control for the cancellation regime.
    s=3.5903488968e-4
    a=100.0
    for frac in (-0.75,-0.1,0.0,0.1,0.75):
        h=a+frac*s
        o=g.circle_overlap(s,a,h)
        cap=math.pi*s*s
        assert math.isfinite(o)
        assert 0.0 <= o <= cap


def test_angular_kernel_centered_exact_and_split_sanity():
    s,a=4.0,2.0
    for y in (0.0,1.0,3.0,7.0):
        k=g.angular_kernel(y,s,0.0,a,16)
        exact=g.circle_overlap(s,a,y)/(math.pi*s*s)
        assert math.isfinite(k)
        assert math.isclose(k,exact,rel_tol=1e-15,abs_tol=1e-15)
    pts=g.angular_split_points(3.0,4.0,2.0,2.0)
    assert pts[0] == 0.0 and pts[-1] == math.pi
    assert all(b >= a for a,b in zip(pts[:-1],pts[1:]))


def test_fixed_overlap_controls_execute():
    out=g.fixed_overlap_controls()
    assert out["disjoint"] == 0.0
    assert math.isfinite(out["max_symmetry_rel"])
    assert math.isfinite(out["max_scale_rel"])
