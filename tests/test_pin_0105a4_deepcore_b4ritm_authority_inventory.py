import json

from scripts.pin_0105a4_deepcore_b4ritm_authority_inventory import build_result, normalize_dataverse


def fixture(identifier="B4RITM", state="RELEASED", checksum="abc123"):
    return {
        "status": "OK",
        "data": {
            "id": 123,
            "persistentUrl": f"https://doi.org/10.7910/DVN/{identifier}",
            "identifier": identifier,
            "protocol": "doi",
            "authority": "10.7910/DVN",
            "latestVersion": {
                "versionNumber": 2,
                "versionMinorNumber": 0,
                "versionState": state,
                "releaseTime": "2025-01-01T00:00:00Z",
                "files": [
                    {
                        "description": "analysis object",
                        "categories": ["Data"],
                        "dataFile": {
                            "id": 456,
                            "filename": "analysis.hdf5",
                            "contentType": "application/x-hdf5",
                            "filesize": 12345,
                            "persistentId": "doi:10.7910/DVN/B4RITM/ABCDEF",
                            "checksum": {"type": "MD5", "value": checksum},
                        },
                    }
                ],
            },
        },
    }


def raw(obj):
    return json.dumps(obj).encode()


def test_normalize_preserves_version_and_file_authority_fields():
    out = normalize_dataverse(raw(fixture()))
    assert out["api_status"] == "OK"
    assert out["version_number"] == 2
    assert out["version_minor_number"] == 0
    assert out["version_state"] == "RELEASED"
    assert out["file_count"] == 1
    assert out["files"][0]["filename"] == "analysis.hdf5"
    assert out["files"][0]["size_bytes"] == 12345
    assert out["files"][0]["checksum_type"] == "MD5"
    assert out["files"][0]["checksum_value"] == "abc123"


def test_b4ritm_fixture_passes_but_remains_nonterminal():
    out = build_result(raw(fixture()), "deadbeef")
    assert out["status"] == "PASS_0105A4_DEEPCORE_B4RITM_AUTHORITY_INVENTORY_NONTERMINAL"
    assert all(out["gates"].values())
    assert out["deepcore_consumed_byte_lock_complete"] is False
    assert out["observed_residual_execution_allowed"] is False


def test_qkl28z_sterile_release_cannot_substitute():
    out = build_result(raw(fixture(identifier="QKL28Z")))
    assert out["status"].startswith("BLOCKED_")
    assert out["gates"]["b4ritm_identity_ok"] is False
    assert out["gates"]["qkl28z_sterile_identity_absent"] is False


def test_unreleased_version_fails_closed():
    out = build_result(raw(fixture(state="DRAFT")))
    assert out["status"].startswith("BLOCKED_")
    assert out["gates"]["version_released"] is False


def test_missing_checksum_fails_closed():
    obj = fixture(checksum="")
    out = build_result(raw(obj))
    assert out["status"].startswith("BLOCKED_")
    assert out["gates"]["all_files_have_name_size_checksum"] is False


def test_empty_file_inventory_fails_closed():
    obj = fixture()
    obj["data"]["latestVersion"]["files"] = []
    out = build_result(raw(obj))
    assert out["status"].startswith("BLOCKED_")
    assert out["gates"]["inventory_nonempty"] is False
