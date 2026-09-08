from shapely.geometry import box

import scripts.audit_partial_bl_topology_discovery_0087 as m


def test_N1_detects_two_nontrivial_permitted_components_from_barrier():
    # A full-height excluded vertical barrier splits the finite analysis window.
    fam = {"A": box(0.0, -25.0, 1.0, -2.0)}
    r = m.analyze_scenario("synthetic_barrier", fam)
    assert r["N1_disconnected_permitted_topology"] is True
    assert r["qualifying_component_count_ge_0p01"] == 2
    assert r["area_closure_pass"] is True


def test_N2_detects_bounded_multifamily_pocket():
    # Four independent excluded walls enclose a permitted central rectangle.
    fam = {
        "LEFT": box(-2.0, -16.0, -1.0, -10.0),
        "RIGHT": box(2.0, -16.0, 3.0, -10.0),
        "BOTTOM": box(-2.0, -17.0, 3.0, -16.0),
        "TOP": box(-2.0, -10.0, 3.0, -9.0),
    }
    r = m.analyze_scenario("synthetic_pocket", fam)
    assert r["N2_bounded_multifamily_pocket_or_corridor"] is True
    assert any(len(c["source_boundary_labels"]) >= 2 for c in r["N2_components"])
    assert r["area_closure_pass"] is True


def test_N3_is_not_invented_from_filled_or_band_geometries():
    fam = {"WAGNER_0085": box(-6.0, -20.0, -5.5, -2.0), "FILLED": box(4.0, -8.0, 5.0, -2.0)}
    r = m.analyze_scenario("semantic_guard", fam)
    assert r["N3_persistent_controlling_family_switch"] is False
    assert "not reinterpreted" in r["N3_detail"]["reason"]
