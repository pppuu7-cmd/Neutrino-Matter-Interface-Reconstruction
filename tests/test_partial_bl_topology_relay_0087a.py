from scripts.validate_partial_bl_topology_relay_0087a import graph_from_overlaps, relay_test


def key(a,b):
    return f"{min(a,b)}__{max(a,b)}"


def test_relay_accepts_sn_articulation_chain():
    nodes={"WAGNER_0085","SN","CMB","SOLAR_CEVNS_0078c"}
    overlaps={
        key("WAGNER_0085","SN"):1.0,
        key("SN","CMB"):2.0,
        key("SN","SOLAR_CEVNS_0078c"):0.5,
        key("CMB","SOLAR_CEVNS_0078c"):0.4,
        key("WAGNER_0085","CMB"):0.0,
        key("WAGNER_0085","SOLAR_CEVNS_0078c"):0.0,
    }
    r=relay_test(nodes,overlaps,"SN","CMB")
    assert r["pass"] is True
    assert r["sn_removal_separates_wagner_from_cmb_and_solar"] is True


def test_relay_rejects_direct_wagner_cmb_bypass():
    nodes={"WAGNER_0085","SN","CMB","SOLAR_CEVNS_0078c"}
    overlaps={
        key("WAGNER_0085","SN"):1.0,
        key("SN","CMB"):2.0,
        key("SN","SOLAR_CEVNS_0078c"):0.5,
        key("CMB","SOLAR_CEVNS_0078c"):0.4,
        key("WAGNER_0085","CMB"):0.2,
        key("WAGNER_0085","SOLAR_CEVNS_0078c"):0.0,
    }
    r=relay_test(nodes,overlaps,"SN","CMB")
    assert r["pass"] is False


def test_overlap_threshold_is_frozen_at_0p01():
    nodes={"A","B"}
    adj,edges=graph_from_overlaps(nodes,{key("A","B"):0.009999})
    assert adj["A"] == set()
    adj2,edges2=graph_from_overlaps(nodes,{key("A","B"):0.01})
    assert "B" in adj2["A"]
