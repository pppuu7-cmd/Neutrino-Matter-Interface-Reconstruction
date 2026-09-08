import g9_full_ray_centric_survivor_scan_0090f as g


def test_frozen_grid_cardinality_and_orders():
    assert len(g.THETAS) == 25
    assert len(g.DELTAS_M) == 6
    assert len(g.RECEIVERS_M) == 3
    assert len(g.CONTROLS) == 3
    assert len(g.THETAS)*len(g.DELTAS_M) == 150
    assert len(g.CONTROLS)*len(g.RECEIVERS_M)*len(g.THETAS)*len(g.DELTAS_M) == 1350
    assert g.ANGULAR_ORDER == 32
    assert g.RADIAL_ORDER == 64


def test_parent_authority_is_exactly_bound():
    assert g.dual.CONTRACT == g.PARENT_CONTRACT
    assert g.dual.AMENDMENT == g.PARENT_AMENDMENT
    assert g.parent_evaluator_blob() == g.PARENT_EVALUATOR_BLOB


def test_survivor_semantics_are_nonzero_offset_mu_ge2():
    def survivor(theta,delta,mu):
        return theta > 0.0 and delta > 0.0 and mu >= 2.0
    assert survivor(1e-12,0.1,2.0)
    assert not survivor(1e-12,0.0,1e9)
    assert not survivor(1e-12,0.1,1.999999999)
