import hashlib

from scripts.pin_0105a3_coherent_zenodo_direct_bytes import (
    RELEASES,
    build_manifest,
    file_url,
    frozen_inventory_valid,
    hash_bytes,
)


def test_frozen_inventory_is_exactly_37_files():
    assert frozen_inventory_valid()
    assert len(RELEASES["csi"]["files"]) == 13
    assert len(RELEASES["ar"]["files"]) == 24
    assert sum(len(r["files"]) for r in RELEASES.values()) == 37


def test_file_url_encodes_plus_without_changing_filename_identity():
    url = file_url("3903810", "brnpdf+1sigEnergy.txt")
    assert "/records/3903810/files/" in url
    assert "brnpdf%2B1sigEnergy.txt" in url
    assert url.endswith("?download=1")


def test_hash_bytes_is_exact():
    data = b"opaque fixture only\n"
    md5, sha = hash_bytes(data)
    assert md5 == hashlib.md5(data).hexdigest()
    assert sha == hashlib.sha256(data).hexdigest()


def test_manifest_passes_when_fetcher_returns_bytes_matching_frozen_md5(monkeypatch):
    # Replace the frozen inventory with a tiny deterministic release so this
    # unit test validates control flow without downloading or consuming data.
    payload = b"fixture"
    md5 = hashlib.md5(payload).hexdigest()
    tiny = {
        "csi": {"record_id": "1", "doi": "d1", "version": "1.0", "files": {"a": md5}},
        "ar": {"record_id": "2", "doi": "d2", "version": "1.0", "files": {"b": md5}},
    }
    import scripts.pin_0105a3_coherent_zenodo_direct_bytes as mod

    monkeypatch.setattr(mod, "RELEASES", tiny)
    monkeypatch.setattr(mod, "frozen_inventory_valid", lambda: True)

    def fetcher(url):
        return payload, url

    out = build_manifest(fetcher=fetcher, git_sha="abc")
    # The production gate intentionally requires total count 37, so a tiny
    # fixture must remain blocked even though its individual hashes match.
    assert out["status"] == "BLOCKED_0105A3_COHERENT_ZENODO_BYTE_LOCK_INCOMPLETE"
    assert out["gates"]["all_provider_md5_match"] is True
    assert out["gates"]["exact_total_file_count_37"] is False
    assert out["observed_residual_execution_allowed"] is False


def test_provider_md5_mismatch_fails_closed(monkeypatch):
    payload = b"fixture"
    wrong = "0" * 32
    tiny = {
        "csi": {"record_id": "1", "doi": "d1", "version": "1.0", "files": {"a": wrong}},
        "ar": {"record_id": "2", "doi": "d2", "version": "1.0", "files": {"b": wrong}},
    }
    import scripts.pin_0105a3_coherent_zenodo_direct_bytes as mod

    monkeypatch.setattr(mod, "RELEASES", tiny)
    monkeypatch.setattr(mod, "frozen_inventory_valid", lambda: True)

    def fetcher(url):
        return payload, url

    out = build_manifest(fetcher=fetcher)
    assert out["gates"]["all_provider_md5_match"] is False
    assert out["coherent_event_byte_lock_complete"] is False
    assert out["status"].startswith("BLOCKED_")
