import json

from scripts.pin_0100c_kato_nagakura_metadata import STELLAR_25_MD5, build_result, inventory, is_mesa25_name


def emission_fixture():
    return {
        "id": 20618971,
        "metadata": {
            "doi": "10.5281/zenodo.20618971",
            "title": "individual progenitor neutrino data",
            "version": "v1.1",
            "publication_date": "2026-06-10",
        },
        "files": [
            {
                "key": "MESA_25msun.zip",
                "size": 123,
                "checksum": "md5:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {"content": "https://example.invalid/MESA_25msun.zip"},
            }
        ],
    }


def stellar_fixture():
    return {
        "id": 20822085,
        "metadata": {
            "doi": "10.5281/zenodo.20822085",
            "title": "stellar evolution models",
            "version": "v1",
        },
        "files": [
            {
                "key": "25msun.tar.gz",
                "size": 456,
                "checksum": f"md5:{STELLAR_25_MD5}",
                "links": {"content": "https://example.invalid/25msun.tar.gz"},
            }
        ],
    }


def test_inventory_preserves_checksum_and_url():
    out = inventory(stellar_fixture())
    assert out[0]["checksum_type"] == "md5"
    assert out[0]["checksum_value"] == STELLAR_25_MD5
    assert out[0]["download_url"].endswith("25msun.tar.gz")


def test_mesa25_candidate_match_is_name_based_only():
    assert is_mesa25_name("MESA_25msun.zip")
    assert not is_mesa25_name("HOSHI_25msun.zip")
    assert not is_mesa25_name("MESA_20msun.zip")


def test_result_is_nonterminal_even_when_metadata_is_complete():
    result = build_result(json.dumps(emission_fixture()).encode(), json.dumps(stellar_fixture()).encode(), "abc")
    assert result["status"] == "PASS_0100C_ZENODO_METADATA_DISCOVERED_NONTERMINAL"
    assert all(result["gates"].values())
    assert result["emission"]["mesa25_candidate_count"] == 1
    assert result["heavy_archive_download_allowed"] is True
    assert result["terminal_physics_execution_allowed"] is False
    assert result["snapshot_mapping_authority_closed"] is False
