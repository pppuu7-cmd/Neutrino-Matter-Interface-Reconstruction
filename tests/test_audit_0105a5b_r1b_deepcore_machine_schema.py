import csv
import hashlib
import io

import scripts.audit_0105a5b_r1b_deepcore_machine_schema as mod


def make_csv(columns, rows):
    s = io.StringIO(newline="")
    w = csv.DictWriter(s, fieldnames=columns)
    w.writeheader()
    w.writerows(rows)
    return s.getvalue().encode()


def grid():
    return [(float(e), float(z), float(p)) for e in range(10) for z in range(10) for p in (0, 1)]


def fixture_payloads():
    coords = grid()
    data_rows = []
    for i, (e, z, p) in enumerate(coords):
        data_rows.append({
            "count": "21715" if i == 0 else ("1" if 0 < i < 200 else "0"),
            "reco_energy": str(e), "reco_coszen": str(z), "pid": str(p),
        })
    # 21715 + 199 = 21914
    payloads = {
        "data.csv": make_csv(["count", "pid", "reco_coszen", "reco_energy"], data_rows),
    }
    mc_cols = sorted(mod.MC_REQUIRED)
    for name in ("mc_nue_cc.csv", "mc_numu_cc.csv", "mc_nu_nc.csv", "mc_nutau_cc.csv"):
        rows = []
        for e, z, p in coords[:4]:
            row = {c: "0" for c in mc_cols}
            row.update({
                "reco_energy": str(e), "reco_coszen": str(z), "pid": str(p),
                "pdg": "14", "true_energy": "20", "true_coszen": "-0.5",
                "weight": "1", "type": "1", "interaction": "0",
            })
            rows.append(row)
        payloads[name] = make_csv(mc_cols, rows)
    mu_rows = [
        {"count": "0.5", "abs_uncertainty": "0.1", "reco_energy": str(e), "reco_coszen": str(z), "pid": str(p)}
        for e, z, p in coords
    ]
    payloads["mc_mu.csv"] = make_csv(["count", "abs_uncertainty", "pid", "reco_coszen", "reco_energy"], mu_rows)
    hs_cols = sorted(mod.HS_REQUIRED)
    for name in ("hs_numu_cc.csv", "hs_nu_nc_nue_cc.csv", "hs_nutau_cc.csv"):
        rows = []
        for dm in (0.0020, 0.0025):
            for e, z, p in coords:
                row = {c: "0" for c in hs_cols}
                row.update({
                    "reco_energy": str(e), "reco_coszen": str(z), "pid": str(p),
                    "deltam31": str(dm), "intercept": "1",
                })
                rows.append(row)
        payloads[name] = make_csv(hs_cols, rows)
    return payloads


def checks_for(payloads):
    return [
        {"name": n, "sha256_match": True, "actual_sha256": hashlib.sha256(b).hexdigest()}
        for n, b in payloads.items()
    ]


def test_frozen_real_byte_authority_is_exactly_nine_saved_original_csvs():
    assert mod.DATASET_DOI == "10.7910/DVN/B4RITM"
    assert mod.FORBIDDEN_STERILE_DOI == "10.7910/DVN/QKL28Z"
    assert len(mod.FILES) == 9
    assert all(len(sha) == 64 for _, sha in mod.FILES.values())
    assert mod.file_url(11646859).endswith("/11646859?format=original")


def test_byte_barrier_fetches_all_before_analysis_and_requires_hashes(monkeypatch):
    payloads = fixture_payloads()
    tiny_contract = {n: (i + 1, hashlib.sha256(b).hexdigest()) for i, (n, b) in enumerate(payloads.items())}
    monkeypatch.setattr(mod, "FILES", tiny_contract)
    id_to_name = {v[0]: k for k, v in tiny_contract.items()}
    seen = []

    def fetcher(url):
        file_id = int(url.split("/")[-1].split("?")[0])
        seen.append(file_id)
        return payloads[id_to_name[file_id]]

    raw, checks = mod.byte_barrier(fetcher)
    assert len(seen) == 9
    assert len(raw) == 9
    assert all(c["sha256_match"] for c in checks)
    assert all(c["request_url"].endswith("?format=original") for c in checks)


def test_structurally_complete_fixture_passes_without_any_fit_or_residual():
    payloads = fixture_payloads()
    out = mod.analyze(payloads, checks_for(payloads))
    assert out["status"] == "PASS_0105A5B_R1B_MACHINE_SCHEMA_AUDIT_NONDISCOVERY"
    assert out["data_structure"]["exact_200_cells"] is True
    assert out["data_structure"]["observed_total_21914"] is True
    assert out["data_structure"]["unique_reco_energy_count"] == 10
    assert out["data_structure"]["unique_reco_coszen_count"] == 10
    assert out["data_structure"]["unique_pid_count"] == 2
    assert out["muon_structure"]["covers_all_200_data_coordinates"] is True
    assert out["gates"]["hypersurfaces_cover_full_grid_at_each_dm31_support"] is True
    assert len(out["nuisance_authority"]) == 18
    assert out["external_dependencies_still_required"] is True
    assert out["oscillated_expectation_computed"] is False
    assert out["chi2_computed"] is False
    assert out["nuisance_fit_executed"] is False
    assert out["observed_minus_null_residual_computed"] is False
    assert out["observed_residual_execution_allowed"] is False


def test_hash_mismatch_blocks_before_csv_decode(monkeypatch):
    payloads = fixture_payloads()
    checks = checks_for(payloads)
    checks[0]["sha256_match"] = False

    def must_not_parse(_):
        raise AssertionError("CSV parsing must not occur after byte mismatch")

    monkeypatch.setattr(mod, "parse_csv", must_not_parse)
    out = mod.analyze(payloads, checks)
    assert out["status"] == "BLOCKED_0105A5B_BYTE_AUTHORITY_MISMATCH"
    assert out["files"] == {}
    assert out["observed_residual_execution_allowed"] is False


def test_missing_detector_machine_alias_fails_schema_gate():
    payloads = fixture_payloads()
    cols, rows = mod.parse_csv(payloads["hs_numu_cc.csv"])
    new_cols = [c for c in cols if c != "bulk_ice_scatter"] + ["bulk_ice_scat"]
    new_rows = []
    for r in rows:
        r = dict(r)
        r["bulk_ice_scat"] = r.pop("bulk_ice_scatter")
        new_rows.append(r)
    payloads["hs_numu_cc.csv"] = make_csv(new_cols, new_rows)
    out = mod.analyze(payloads, checks_for(payloads))
    assert out["status"] == "BLOCKED_0105A5B_R1B_MACHINE_SCHEMA_OR_STRUCTURE_INCOMPLETE"
    assert out["schema_ok"]["hs_numu_cc.csv"] is False


def test_nuisance_classification_refuses_to_promote_external_flux_or_dis_response():
    schema = {name: True for name in mod.FILES}
    out = mod.classify_nuisances(schema)
    assert len(out) == 18
    assert out["dom_eff"]["class"] == "NATIVE_RELEASE_RESPONSE"
    assert out["xsec_MaCCQE"]["class"] == "NATIVE_RELEASE_PRIMITIVE_EXTERNAL_FORMULA"
    assert out["xsec_DIS_CSMS"]["class"] == "EXTERNAL_COMPUTATIONAL_AUTHORITY_REQUIRED"
    assert sum(v["class"] == "EXTERNAL_COMPUTATIONAL_AUTHORITY_REQUIRED" for v in out.values()) == 7
