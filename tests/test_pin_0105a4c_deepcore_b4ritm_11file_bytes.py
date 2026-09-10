import hashlib
import json

import scripts.pin_0105a4c_deepcore_b4ritm_11file_bytes as mod


def metadata_for(rows, *, identifier="DVN/B4RITM", authority="10.7910", version=(1, 0), state="RELEASED"):
    files = []
    for file_id, filename, size, md5 in rows:
        files.append({
            "dataFile": {
                "id": file_id,
                "filename": filename,
                "filesize": size,
                "checksum": {"type": "MD5", "value": md5},
            }
        })
    return json.dumps({
        "status": "OK",
        "data": {
            "identifier": identifier,
            "authority": authority,
            "persistentUrl": "https://doi.org/10.7910/DVN/B4RITM",
            "latestVersion": {
                "versionNumber": version[0],
                "versionMinorNumber": version[1],
                "versionState": state,
                "files": files,
            },
        },
    }).encode()


def test_frozen_parent_inventory_is_exact_11file_b4ritm_release():
    assert mod.DATASET_DOI == "10.7910/DVN/B4RITM"
    assert mod.EXPECTED_VERSION == (1, 0)
    assert len(mod.FROZEN) == 11
    assert {row[0] for row in mod.FROZEN} == {
        11646859, 11674675, 11646858, 11646854, 11646853,
        11646851, 11646852, 11646856, 11646850, 11646855, 11674676,
    }
    assert all(row[0] > 11_000_000 for row in mod.FROZEN)


def test_inventory_order_is_not_authority_semantics():
    raw = metadata_for(list(reversed(mod.FROZEN)))
    ok, identity, files = mod.identity_and_inventory_valid(raw)
    assert ok is True
    assert identity["identifier"] == "DVN/B4RITM"
    assert len(files) == 11


def test_changed_live_inventory_blocks_before_byte_fetch():
    changed = list(mod.FROZEN)
    file_id, filename, size, md5 = changed[0]
    changed[0] = (file_id, filename, size + 1, md5)
    raw = metadata_for(changed)
    calls = []

    def must_not_fetch(url):
        calls.append(url)
        raise AssertionError("byte fetch must remain locked after metadata mismatch")

    out = mod.build_manifest(raw, byte_fetcher=must_not_fetch, git_sha="fixture")
    assert out["status"] == "BLOCKED_0105A4C_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE"
    assert out["gates"]["live_metadata_exact_match"] is False
    assert calls == []
    assert out["binary_content_parsed"] is False
    assert out["observed_residual_execution_allowed"] is False


def test_qkl28z_or_wrong_version_blocks():
    raw_sterile = metadata_for(mod.FROZEN, identifier="DVN/QKL28Z")
    ok, _, _ = mod.identity_and_inventory_valid(raw_sterile)
    assert ok is False

    raw_wrong_version = metadata_for(mod.FROZEN, version=(1, 1))
    ok, _, _ = mod.identity_and_inventory_valid(raw_wrong_version)
    assert ok is False


def test_matching_synthetic_inventory_and_bytes_passes(monkeypatch):
    payloads = {
        910001: b"a",
        910002: b"bb",
        910003: b"ccc",
    }
    tiny = []
    for file_id, payload in payloads.items():
        tiny.append((file_id, f"f{file_id}.tab", len(payload), hashlib.md5(payload).hexdigest()))
    monkeypatch.setattr(mod, "FROZEN", tiny)
    raw = metadata_for(tiny)

    def fetcher(url):
        file_id = int(url.rsplit("/", 1)[-1])
        return payloads[file_id], f"https://dataverse.harvard.edu/api/access/datafile/{file_id}"

    out = mod.build_manifest(raw, byte_fetcher=fetcher, git_sha="fixture")
    # Synthetic fixture has 3 files, so production exact-count gate must still block.
    assert out["status"] == "BLOCKED_0105A4C_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE"
    assert out["gates"]["live_metadata_exact_match"] is True
    assert out["gates"]["all_provider_md5_match"] is True
    assert out["gates"]["all_provider_sizes_match"] is True
    assert out["gates"]["all_sha256_recorded"] is True
    assert out["gates"]["exact_file_count_11"] is False
    assert out["binary_content_parsed"] is False
    assert out["observed_residual_execution_allowed"] is False


def test_md5_mismatch_fails_closed_with_exact_11_metadata(monkeypatch):
    # Keep exact count 11 while using tiny synthetic bytes and matching synthetic metadata.
    payloads = {920000 + i: bytes([65 + i]) for i in range(11)}
    tiny = []
    for file_id, payload in payloads.items():
        tiny.append((file_id, f"f{file_id}.tab", len(payload), hashlib.md5(payload).hexdigest()))
    monkeypatch.setattr(mod, "FROZEN", tiny)
    raw = metadata_for(tiny)

    first = tiny[0][0]

    def fetcher(url):
        file_id = int(url.rsplit("/", 1)[-1])
        payload = payloads[file_id]
        if file_id == first:
            payload = b"wrong"
        return payload, url

    out = mod.build_manifest(raw, byte_fetcher=fetcher, git_sha="fixture")
    assert out["status"] == "BLOCKED_0105A4C_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE"
    assert out["gates"]["exact_file_count_11"] is True
    assert out["gates"]["all_provider_md5_match"] is False
    assert out["binary_content_parsed"] is False
    assert out["observed_residual_execution_allowed"] is False


def test_matching_11file_fixture_passes(monkeypatch):
    payloads = {930000 + i: bytes([97 + i]) * (i + 1) for i in range(11)}
    tiny = []
    for file_id, payload in payloads.items():
        tiny.append((file_id, f"f{file_id}.tab", len(payload), hashlib.md5(payload).hexdigest()))
    monkeypatch.setattr(mod, "FROZEN", tiny)
    raw = metadata_for(list(reversed(tiny)))

    def fetcher(url):
        file_id = int(url.rsplit("/", 1)[-1])
        return payloads[file_id], url

    out = mod.build_manifest(raw, byte_fetcher=fetcher, git_sha="fixture")
    assert out["status"] == "PASS_0105A4C_DEEPCORE_B4RITM_11FILE_BYTE_LOCK_NONDISCOVERY"
    assert out["gates"]["live_metadata_exact_match"] is True
    assert out["gates"]["exact_file_count_11"] is True
    assert out["gates"]["all_provider_md5_match"] is True
    assert out["gates"]["all_provider_sizes_match"] is True
    assert out["gates"]["all_sha256_recorded"] is True
    assert len(out["files"]) == 11
    assert out["binary_content_parsed"] is False
    assert out["observed_residual_execution_allowed"] is False
    assert out["bsm_interpretation_allowed"] is False
