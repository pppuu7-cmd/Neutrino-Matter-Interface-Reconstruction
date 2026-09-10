import hashlib
import json
from urllib.parse import urlparse

import scripts.pin_0105a4d_deepcore_b4ritm_original_bytes as mod


def metadata_for(rows, *, identifier="DVN/B4RITM", authority="10.7910", version=(1, 0), state="RELEASED"):
    files = []
    for file_id, archival, representation, returned, size, md5 in rows:
        df = {
            "id": file_id,
            "filename": archival,
            "filesize": size,
            "checksum": {"type": "MD5", "value": md5},
        }
        if representation == "saved-original":
            df.update(
                {
                    "tabularData": True,
                    "originalFileFormat": "text/csv",
                    "originalFileName": returned,
                    "originalFileSize": size,
                }
            )
        else:
            df["tabularData"] = False
        files.append({"dataFile": df})
    return json.dumps(
        {
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
        }
    ).encode()


def test_frozen_contract_is_exact_11_with_9_saved_original_and_2_direct():
    assert mod.DATASET_DOI == "10.7910/DVN/B4RITM"
    assert mod.FORBIDDEN_STERILE_DOI == "10.7910/DVN/QKL28Z"
    assert mod.EXPECTED_VERSION == (1, 0)
    assert len(mod.FROZEN) == 11
    modes = [row[2] for row in mod.FROZEN]
    assert modes.count("saved-original") == 9
    assert modes.count("direct") == 2
    assert {row[0] for row in mod.FROZEN} == {
        11646859, 11674675, 11646858, 11646854, 11646853,
        11646851, 11646852, 11646856, 11646850, 11646855, 11674676,
    }


def test_saved_original_and_direct_urls_are_distinct_and_exact():
    assert mod.file_url(11646859, "saved-original") == (
        "https://dataverse.harvard.edu/api/access/datafile/11646859?format=original"
    )
    assert mod.file_url(11674675, "direct") == (
        "https://dataverse.harvard.edu/api/access/datafile/11674675"
    )


def test_exact_metadata_contract_passes_independent_of_api_file_order():
    raw = metadata_for(list(reversed(mod.FROZEN)))
    ok, identity, rows, gates = mod.metadata_valid(raw)
    assert ok is True
    assert identity["identifier"] == "DVN/B4RITM"
    assert len(rows) == 11
    assert gates["exact_11file_representation_metadata"] is True
    assert gates["exact_9_saved_original_2_direct"] is True


def test_changed_original_representation_metadata_blocks_before_fetch():
    raw_obj = json.loads(metadata_for(mod.FROZEN))
    first = raw_obj["data"]["latestVersion"]["files"][0]["dataFile"]
    first["originalFileName"] = "wrong.csv"
    raw = json.dumps(raw_obj).encode()
    calls = []

    def must_not_fetch(url):
        calls.append(url)
        raise AssertionError("payload fetch must remain locked after metadata mismatch")

    out = mod.build_manifest(raw, byte_fetcher=must_not_fetch, git_sha="fixture")
    assert out["status"] == "BLOCKED_0105A4D_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE"
    assert out["gates"]["exact_11file_representation_metadata"] is False
    assert calls == []
    assert out["binary_content_parsed"] is False
    assert out["observed_residual_execution_allowed"] is False


def test_archival_tabular_semantics_cannot_masquerade_as_saved_original():
    raw_obj = json.loads(metadata_for(mod.FROZEN))
    first = raw_obj["data"]["latestVersion"]["files"][0]["dataFile"]
    first["tabularData"] = False
    first.pop("originalFileName", None)
    first.pop("originalFileFormat", None)
    first.pop("originalFileSize", None)
    ok, _, _, gates = mod.metadata_valid(json.dumps(raw_obj).encode())
    assert ok is False
    assert gates["exact_11file_representation_metadata"] is False
    assert gates["exact_9_saved_original_2_direct"] is False


def test_qkl28z_or_wrong_release_blocks():
    raw_sterile = metadata_for(mod.FROZEN, identifier="DVN/QKL28Z")
    ok, _, _, gates = mod.metadata_valid(raw_sterile)
    assert ok is False
    assert gates["b4ritm_identity_release_exact"] is False

    raw_wrong_version = metadata_for(mod.FROZEN, version=(1, 1))
    ok, _, _, gates = mod.metadata_valid(raw_wrong_version)
    assert ok is False
    assert gates["b4ritm_identity_release_exact"] is False


def synthetic_contract():
    rows = []
    payloads = {}
    for i in range(11):
        file_id = 940000 + i
        payload = bytes([65 + i]) * (i + 1)
        mode = "saved-original" if i < 9 else "direct"
        archival = f"f{i}.tab" if mode == "saved-original" else f"f{i}.bin"
        returned = f"f{i}.csv" if mode == "saved-original" else archival
        payloads[file_id] = payload
        rows.append((file_id, archival, mode, returned, len(payload), hashlib.md5(payload).hexdigest()))
    return rows, payloads


def test_matching_11file_fixture_uses_exact_modes_and_passes(monkeypatch):
    rows, payloads = synthetic_contract()
    monkeypatch.setattr(mod, "FROZEN", rows)
    raw = metadata_for(list(reversed(rows)))
    seen = []

    def fetcher(url):
        seen.append(url)
        file_id = int(urlparse(url).path.rsplit("/", 1)[-1])
        return payloads[file_id], url

    out = mod.build_manifest(raw, byte_fetcher=fetcher, git_sha="fixture")
    assert out["status"] == "PASS_0105A4D_DEEPCORE_B4RITM_ORIGINAL_REPRESENTATION_BYTE_LOCK_NONDISCOVERY"
    assert len(out["files"]) == 11
    assert sum(url.endswith("?format=original") for url in seen) == 9
    assert sum("format=" not in url for url in seen) == 2
    assert out["gates"]["all_provider_md5_match"] is True
    assert out["gates"]["all_provider_sizes_match"] is True
    assert out["gates"]["all_sha256_recorded"] is True
    assert out["gates"]["all_request_modes_exact"] is True
    assert out["binary_content_parsed"] is False
    assert out["observed_residual_execution_allowed"] is False
    assert out["bsm_interpretation_allowed"] is False


def test_wrong_original_bytes_fail_closed_without_changing_contract(monkeypatch):
    rows, payloads = synthetic_contract()
    monkeypatch.setattr(mod, "FROZEN", rows)
    raw = metadata_for(rows)
    first_id = rows[0][0]

    def fetcher(url):
        file_id = int(urlparse(url).path.rsplit("/", 1)[-1])
        payload = payloads[file_id]
        if file_id == first_id:
            payload = b"wrong"
        return payload, url

    out = mod.build_manifest(raw, byte_fetcher=fetcher, git_sha="fixture")
    assert out["status"] == "BLOCKED_0105A4D_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE"
    assert out["gates"]["all_provider_md5_match"] is False
    assert out["gates"]["all_provider_sizes_match"] is False
    assert out["observed_residual_execution_allowed"] is False
