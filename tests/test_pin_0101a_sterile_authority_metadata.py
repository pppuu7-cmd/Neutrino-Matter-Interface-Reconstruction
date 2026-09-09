import json

from scripts.pin_0101a_sterile_authority_metadata import build_result, summarize_dataverse, summarize_hepdata


def hep_fixture():
    return {
        "record": {"title": "Search for light sterile neutrinos with two neutrino beams at MicroBooNE"},
        "data_tables": [
            {"name": "Unconstrained 14 channels"},
            {"name": "Constrained nu_e channels"},
            {"name": "14 channel covariance matrix"},
        ],
        "resources": [
            {"description": "Delta chi2 grid for sterile-neutrino hypotheses", "url": "https://example.invalid/grid.txt"}
        ],
        "doi": "10.17182/hepdata.166435.v1",
    }


def ice_fixture():
    return {
        "status": "OK",
        "data": {
            "id": 123,
            "persistentUrl": "https://doi.org/10.7910/DVN/QKL28Z",
            "latestVersion": {
                "versionNumber": 1,
                "versionMinorNumber": 0,
                "versionState": "RELEASED",
                "releaseTime": "2024-01-01T00:00:00Z",
                "files": [
                    {
                        "description": "sterile scan",
                        "dataFile": {
                            "id": 456,
                            "filename": "scan.csv",
                            "contentType": "text/csv",
                            "filesize": 42,
                            "checksum": {"type": "MD5", "value": "0123456789abcdef0123456789abcdef"},
                            "persistentId": "doi:10.7910/DVN/QKL28Z/ABCDEF",
                        },
                    }
                ],
            },
        },
    }


def test_hepdata_summary_finds_tables_and_grid_resource():
    out = summarize_hepdata(hep_fixture())
    assert out["table_count"] == 3
    assert out["table_names"][0] == "Unconstrained 14 channels"
    assert any("grid" in item["value"].lower() for item in out["resource_candidates"])


def test_dataverse_summary_preserves_version_file_and_checksum():
    out = summarize_dataverse(ice_fixture())
    assert out["file_count"] == 1
    assert out["version_state"] == "RELEASED"
    assert out["files"][0]["checksum_type"] == "MD5"
    assert out["files"][0]["checksum_value"] == "0123456789abcdef0123456789abcdef"


def test_build_result_is_nonterminal_and_never_claims_joint_likelihood():
    result = build_result(json.dumps(hep_fixture()).encode(), json.dumps(ice_fixture()).encode(), "abc")
    assert result["status"] == "PASS_0101A_AUTHORITY_METADATA_DISCOVERED_NONTERMINAL"
    assert result["terminal_physics_execution_allowed"] is False
    assert result["joint_global_likelihood_claim_allowed"] is False
    assert all(result["gates"].values())
