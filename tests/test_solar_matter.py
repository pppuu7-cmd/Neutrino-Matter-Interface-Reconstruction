import pytest

from nmir.solar_matter import (
    git_blob_sha1,
    load_solar_matter_manifest,
    raw_pinned_url,
    required_components,
    verify_solar_matter_blob,
)


def test_both_b16_matter_models_are_frozen():
    manifest = load_solar_matter_manifest()
    assert set(manifest) == {"B16_GS98", "B16_AGSS09met"}


def test_b16_column_contract_matches_published_table_layout():
    for src in load_solar_matter_manifest().values():
        assert src.radius_column == 0
        assert src.density_log10_column == 2
        assert src.production_columns == {
            "pp": 4,
            "pep": 5,
            "hep": 6,
            "Be7": 7,
            "B8": 8,
            "N13": 9,
            "O15": 10,
            "F17": 11,
        }
        assert src.density_units == "mol/cm^3"


def test_b16_blob_identities_are_exact():
    manifest = load_solar_matter_manifest()
    assert manifest["B16_GS98"].source_blob_sha == "f73c47cf6f2d77086634a5c180b50039e10805e7"
    assert manifest["B16_AGSS09met"].source_blob_sha == "d9bd29f3374c63e8ea898733a55fb7aa566a2c96"


def test_component_contract_complete():
    assert required_components() == ("pp", "pep", "hep", "Be7", "B8", "N13", "O15", "F17")


def test_git_blob_hash_reference():
    assert git_blob_sha1(b"hello\n") == "ce013625030ba8dba906f756967f9e9ca394464a"


def test_raw_url_is_commit_pinned():
    url = raw_pinned_url("B16_GS98")
    assert "59e3a2ae102d58f42cc1146eaca2cae68be879ce" in url
    assert url.endswith("Data/nudistr_b16_gs98.dat")


def test_wrong_matter_bytes_fail_closed():
    with pytest.raises(ValueError, match="solar-matter blob mismatch"):
        verify_solar_matter_blob("B16_GS98", b"wrong")


def test_unknown_model_rejected():
    with pytest.raises(KeyError):
        verify_solar_matter_blob("unknown", b"x")
