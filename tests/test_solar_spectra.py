from pathlib import Path

import pytest

from nmir.solar_spectra import (
    SpectrumSource,
    be7_bookkeeping_weight_sum,
    git_blob_sha1,
    load_spectrum_manifest,
    materialize_spectrum,
    pinned_blob_components,
    pinned_continuum_components,
    raw_pinned_url,
    verify_materialized_spectrum,
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


def test_all_blob_backed_components_are_enumerated():
    assert pinned_blob_components() == (
        "B8",
        "Be7_excited",
        "Be7_ground",
        "F17",
        "N13",
        "O15",
        "hep",
        "pp",
    )


def test_be7_line_bookkeeping_is_normalized():
    assert be7_bookkeeping_weight_sum() == pytest.approx(1.0, rel=0, abs=1e-15)


def test_pep_line_energy_convention():
    assert load_spectrum_manifest()["pep"].line_energy_mev == pytest.approx(1.442)


def test_b8_baseline_is_ortiz_not_silent_alternative():
    b8 = load_spectrum_manifest()["B8"]
    assert b8.source_path == "Data/8B_shape_Ortiz_et_al.csv"
    assert b8.source_blob_sha == "570e8016d4cfd79808441d6275b8c651341bc3a6"


def test_git_blob_hash_matches_canonical_git_object_identity():
    assert git_blob_sha1(b"hello\n") == "ce013625030ba8dba906f756967f9e9ca394464a"


def test_raw_url_is_immutable_commit_url():
    url = raw_pinned_url("pp")
    assert "/michelelucente/PEANUTS/59e3a2ae102d58f42cc1146eaca2cae68be879ce/Data/pp_shape.csv" in url


def _fixture_manifest(data: bytes) -> dict[str, SpectrumSource]:
    return {
        "toy": SpectrumSource(
            component="toy",
            kind="continuum",
            reference="fixture",
            source_repo="owner/repo",
            source_commit="1" * 40,
            source_path="Data/toy.csv",
            source_blob_sha=git_blob_sha1(data),
            line_energy_mev=None,
            line_weight=None,
            notes="fixture",
        )
    }


def test_materializer_verifies_before_write(tmp_path: Path):
    payload = b"# toy\n0.1, 1.0\n"
    manifest = _fixture_manifest(payload)
    path = materialize_spectrum("toy", tmp_path, manifest=manifest, fetcher=lambda _: payload)
    assert path.read_bytes() == payload
    assert path.name == "toy__toy.csv"


def test_materializer_fails_closed_on_wrong_bytes(tmp_path: Path):
    payload = b"expected\n"
    manifest = _fixture_manifest(payload)
    with pytest.raises(ValueError, match="spectral blob mismatch"):
        materialize_spectrum("toy", tmp_path, manifest=manifest, fetcher=lambda _: b"wrong\n")
    assert list(tmp_path.iterdir()) == []


def test_line_cannot_be_materialized_as_blob(tmp_path: Path):
    with pytest.raises(ValueError):
        materialize_spectrum("pep", tmp_path, fetcher=lambda _: b"")


def test_direct_verification_rejects_unknown_component():
    with pytest.raises(KeyError):
        verify_materialized_spectrum("does-not-exist", b"x")
