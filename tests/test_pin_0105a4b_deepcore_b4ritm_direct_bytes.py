import hashlib

from scripts.pin_0105a4b_deepcore_b4ritm_direct_bytes import (
    DATASET_PID,
    FILES,
    build_manifest,
    file_url,
    frozen_inventory_valid,
    hash_bytes,
)


def test_frozen_inventory_is_exactly_four_b4ritm_files():
    assert DATASET_PID == "doi:10.7910/DVN/B4RITM"
    assert frozen_inventory_valid()
    assert len(FILES) == 4
    assert {x["file_id"] for x in FILES} == {6660756, 6660758, 6660757, 6660755}
    assert all("QKL28Z" not in x["persistent_id"] for x in FILES)


def test_dataverse_file_url_is_exact():
    assert file_url(6660758) == "https://dataverse.harvard.edu/api/access/datafile/6660758"


def test_hash_bytes_is_exact():
    data = b"opaque fixture only\n"
    md5, sha = hash_bytes(data)
    assert md5 == hashlib.md5(data).hexdigest()
    assert sha == hashlib.sha256(data).hexdigest()


def test_provider_mismatch_fails_closed(monkeypatch):
    import scripts.pin_0105a4b_deepcore_b4ritm_direct_bytes as mod

    payload = b"fixture"
    tiny = []
    for i, item in enumerate(FILES):
        x = dict(item)
        x["expected_size"] = len(payload)
        x["provider_md5"] = "0" * 32
        tiny.append(x)
    monkeypatch.setattr(mod, "FILES", tiny)

    def fetcher(url):
        return payload, url

    out = build_manifest(fetcher=fetcher, git_sha="abc")
    assert out["status"] == "BLOCKED_0105A4B_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE"
    assert out["gates"]["all_provider_md5_match"] is False
    assert out["deepcore_b4ritm_byte_lock_complete"] is False
    assert out["binary_content_parsed"] is False
    assert out["observed_residual_execution_allowed"] is False


def test_matching_fixture_passes_without_parsing(monkeypatch):
    import scripts.pin_0105a4b_deepcore_b4ritm_direct_bytes as mod

    payloads = {
        6660756: b"a",
        6660758: b"bb",
        6660757: b"ccc",
        6660755: b"dddd",
    }
    tiny = []
    for item in FILES:
        data = payloads[item["file_id"]]
        x = dict(item)
        x["expected_size"] = len(data)
        x["provider_md5"] = hashlib.md5(data).hexdigest()
        tiny.append(x)
    monkeypatch.setattr(mod, "FILES", tiny)

    def fetcher(url):
        file_id = int(url.rsplit("/", 1)[-1])
        return payloads[file_id], url

    out = build_manifest(fetcher=fetcher, git_sha="abc")
    assert out["status"] == "PASS_0105A4B_DEEPCORE_B4RITM_DIRECT_BYTE_LOCK_NONTERMINAL_NONDISCOVERY"
    assert out["deepcore_b4ritm_byte_lock_complete"] is True
    assert out["gates"]["all_provider_md5_match"] is True
    assert out["gates"]["all_provider_sizes_match"] is True
    assert out["gates"]["all_sha256_recorded"] is True
    assert out["binary_content_parsed"] is False
    assert out["observed_residual_execution_allowed"] is False
