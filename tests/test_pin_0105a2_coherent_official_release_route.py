from scripts.pin_0105a2_coherent_official_release_route import (
    CALIBRATION_AUXILIARY_DOI,
    build_result,
)


def html(*links: str) -> bytes:
    anchors = "".join(f'<a href="{href}">release</a>' for href in links)
    return f"<html><body>{anchors}</body></html>".encode()


def test_official_route_fixture_passes_with_both_expected_records():
    out = build_result(
        html(
            "https://zenodo.org/record/1228631",
            "https://zenodo.org/records/3903810#files",
        ),
        "abc",
    )
    assert out["status"] == "PASS_0105A2_COHERENT_OFFICIAL_RELEASE_ROUTE_PINNED_NONTERMINAL"
    assert out["observed_zenodo_record_ids"] == ["1228631", "3903810"]
    assert out["event_byte_lock_complete"] is False
    assert out["observed_residual_execution_allowed"] is False


def test_missing_one_event_release_fails_closed():
    out = build_result(html("https://zenodo.org/record/1228631"))
    assert out["status"] == "BLOCKED_0105A2_COHERENT_OFFICIAL_RELEASE_ROUTE_UNRESOLVED"
    assert out["gates"]["ar_event_record_linked"] is False


def test_unrelated_zenodo_record_cannot_substitute():
    out = build_result(
        html(
            "https://zenodo.org/record/1228631",
            "https://zenodo.org/record/9999999",
        )
    )
    assert out["status"].startswith("BLOCKED_")
    assert "9999999" in out["observed_zenodo_record_ids"]
    assert out["gates"]["ar_event_record_linked"] is False


def test_non_zenodo_numeric_paths_are_ignored():
    out = build_result(
        html(
            "https://example.org/record/1228631",
            "https://zenodo.org/record/3903810",
        )
    )
    assert out["status"].startswith("BLOCKED_")
    assert out["observed_zenodo_record_ids"] == ["3903810"]


def test_calibration_dataset_role_is_explicitly_separate():
    out = build_result(
        html(
            "https://zenodo.org/record/1228631",
            "https://zenodo.org/record/3903810",
        )
    )
    assert out["separate_auxiliary_authority"]["doi"] == CALIBRATION_AUXILIARY_DOI
    assert "NOT CEvNS event-release substitute" in out["separate_auxiliary_authority"]["role"]
