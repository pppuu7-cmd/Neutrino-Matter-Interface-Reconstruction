import json

from scripts.pin_0105a1_cross_regime_authority_metadata import (
    build_result,
    normalize_dataverse,
    normalize_zenodo,
)


def ice_fixture():
    return {
        "status": "OK",
        "data": {
            "id": 101,
            "persistentUrl": "https://doi.org/10.7910/DVN/B4RITM",
            "identifier": "B4RITM",
            "protocol": "doi",
            "authority": "10.7910/DVN",
            "latestVersion": {
                "versionNumber": 2,
                "versionMinorNumber": 0,
                "versionState": "RELEASED",
                "releaseTime": "2025-01-01T00:00:00Z",
                "files": [
                    {
                        "description": "binned events",
                        "categories": ["Data"],
                        "dataFile": {
                            "id": 202,
                            "filename": "data.csv",
                            "contentType": "text/csv",
                            "filesize": 1234,
                            "persistentId": "doi:10.7910/DVN/B4RITM/ABC123",
                            "checksum": {"type": "MD5", "value": "0123456789abcdef0123456789abcdef"},
                        },
                    }
                ],
            },
        },
    }


def zenodo_fixture(record_id, doi, key):
    return {
        "id": record_id,
        "doi": doi,
        "conceptdoi": doi,
        "created": "2020-01-01T00:00:00Z",
        "updated": "2020-01-02T00:00:00Z",
        "metadata": {"title": f"COHERENT {key}", "publication_date": "2020-01-01"},
        "files": [
            {
                "id": f"{key}-file",
                "key": f"{key}.zip",
                "size": 4321,
                "checksum": "md5:fedcba9876543210fedcba9876543210",
                "links": {"self": f"https://zenodo.org/api/files/example/{key}.zip"},
            }
        ],
    }


def test_dataverse_normalization_preserves_version_and_checksum():
    out = normalize_dataverse(json.dumps(ice_fixture()).encode())
    assert out["identifier"] == "B4RITM"
    assert out["version_number"] == 2
    assert out["file_count"] == 1
    assert out["files"][0]["checksum_type"] == "MD5"
    assert out["files"][0]["filesize"] == 1234


def test_zenodo_normalization_preserves_record_and_file_metadata():
    fixture = zenodo_fixture(3903810, "10.5281/zenodo.3903810", "ar")
    out = normalize_zenodo(json.dumps(fixture).encode())
    assert out["record_id"] == 3903810
    assert out["doi"] == "10.5281/zenodo.3903810"
    assert out["file_count"] == 1
    assert out["files"][0]["checksum"].startswith("md5:")


def test_build_result_passes_only_nonterminal_metadata_gate():
    ice = json.dumps(ice_fixture()).encode()
    csi = json.dumps(zenodo_fixture(1228631, "10.5281/zenodo.1228631", "csi")).encode()
    ar = json.dumps(zenodo_fixture(3903810, "10.5281/zenodo.3903810", "ar")).encode()
    result = build_result(ice, {"csi": csi, "ar": ar}, "abc")
    assert result["status"] == "PASS_0105A1_CROSS_REGIME_AUTHORITY_METADATA_INVENTORY_NONTERMINAL"
    assert result["observed_residual_execution_allowed"] is False
    assert result["joint_likelihood_claim_allowed"] is False
    assert result["consumed_byte_sha256_lock_complete"] is False
    assert all(result["gates"].values())


def test_missing_checksum_fails_closed():
    bad = zenodo_fixture(3903810, "10.5281/zenodo.3903810", "ar")
    bad["files"][0]["checksum"] = None
    result = build_result(
        json.dumps(ice_fixture()).encode(),
        {
            "csi": json.dumps(zenodo_fixture(1228631, "10.5281/zenodo.1228631", "csi")).encode(),
            "ar": json.dumps(bad).encode(),
        },
        "abc",
    )
    assert result["status"] == "BLOCKED_0105A1_AUTHORITY_METADATA_INCOMPLETE"
    assert result["gates"]["ar_files_have_size_and_checksum"] is False
