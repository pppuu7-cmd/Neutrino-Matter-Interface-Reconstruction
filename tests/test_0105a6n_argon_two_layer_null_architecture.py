from scripts.evaluate_0105a6n_argon_two_layer_null_architecture import build_result


def test_gate_is_nondiscovery_and_no_fit():
    r = build_result("deadbeef")
    assert r["nondiscovery"] is True
    assert r["no_fit_performed"] is True
    assert r["observed_bsm_residual_inspected"] is False
    assert r["permissions"]["OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT"] == 0
    assert r["permissions"]["TIERA_EXACT_SM_NULL_REPRODUCTION_PERMISSION_PERCENT"] == 0


def test_all_frozen_architecture_fields_pass():
    r = build_result("deadbeef")
    assert set(r["fields"]) == {
        "A1_central_statistical_layer",
        "A2_normalization_constraint_layer",
        "A3_shape_systematic_architecture",
        "A4_published_statistic_layer",
        "A5_dual_anchor_conflict_containment",
        "A6_authority_separation",
    }
    assert all(v["status"] == "PASS" for v in r["fields"].values())
    assert r["classification"] == "PASS_0105A6N_TWO_LAYER_RELEASE_CONSISTENT_NULL_ARCHITECTURE_NONDISCOVERY"
    assert r["permissions"]["TIERB_ARGON_NULL_PREREGISTRATION_PERMISSION_PERCENT"] == 100


def test_frozen_hashes_are_exactly_preserved():
    r = build_result("deadbeef")
    e = r["frozen_evidence"]
    assert e["measurement_source_sha256"] == "2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114"
    assert e["release_source_sha256"] == "5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde"
    assert e["LArParametersAnlA_yaml_sha256"] == "a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e"
    assert e["CENNS10AnlAEfficiency_txt_sha256"] == "21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2"


def test_a6i_block_remains_historical_and_unmodified():
    r = build_result("deadbeef")
    assert r["historical_records"]["0105a6i_record_commit"] == "81e18eaf7713085b665a8e267e5d8c51c89c128a"
    assert "Tier-A 0105a6i remains BLOCKED" in r["fields"]["A6_authority_separation"]["basis"][0]
