import pytest

from nmir.solar_spectra import (
    be7_bookkeeping_weight_sum,
    load_spectrum_manifest,
    pinned_continuum_components,
)


def test_required_continuum_sources_are_pinned():
    assert pinned_continuum_components() == ("B8", "F17", "N13", "O15", "hep", "pp")


def test_all_external_spectra_have_exact_git_identities():
    manifest = load_spectrum_manifest()
    for item in manifest.values():
        if item.kind in {"continuum", "profile"}:
            assert item.source_repo == "michelelucente/PEANUTS"
            assert len(item.source_commit) == 40
            assert len(item.source_blob_sha) == 40


def test_be7_line_bookkeeping_is_normalized():
    assert be7_bookkeeping_weight_sum() == pytest.approx(1.0, rel=0, abs=1e-15)


def test_pep_line_energy_convention():
    assert load_spectrum_manifest()["pep"].line_energy_mev == pytest.approx(1.442)


def test_b8_baseline_is_ortiz_not_silent_alternative():
    b8 = load_spectrum_manifest()["B8"]
    assert b8.source_path == "Data/8B_shape_Ortiz_et_al.csv"
    assert b8.source_blob_sha == "570e8016d4cfd79808441d6275b8c651341bc3a6"
