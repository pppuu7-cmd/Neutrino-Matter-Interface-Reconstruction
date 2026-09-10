from pathlib import Path

from scripts.audit_0105a6q4e_argon_2022_review_authority_bound_count_law_locator import (
    Q4C_SCRIPT_GIT_BLOB_SHA1,
    TARGET_SHA256,
    TARGET_SIZE,
    TARGET_URL,
    git_blob_sha1,
    load_q4c_contract,
)

Q4C_PATH = Path("scripts/audit_0105a6q4c_argon_2022_review_count_law_locator.py")


def test_q4c_git_blob_is_exactly_frozen():
    assert git_blob_sha1(Q4C_PATH.read_bytes()) == Q4C_SCRIPT_GIT_BLOB_SHA1


def test_q4c_contract_loads_from_frozen_blob():
    q4c = load_q4c_contract(Q4C_PATH)
    flags = q4c.flags("pseudo-data generated with poisson event count using RooFit")
    assert flags["L1"] is True
    assert flags["L2"] is True
    assert flags["L3"] is True
    assert flags["L4"] is True
    assert flags["categories"] == [
        "DIRECT_COUNT_LAW_CANDIDATE",
        "IMPLEMENTATION_CONTRACT_CANDIDATE",
        "COUNT_GENERATION_CANDIDATE",
    ]


def test_q4c_contract_does_not_promote_l1_alone():
    q4c = load_q4c_contract(Q4C_PATH)
    assert q4c.flags("pseudo-data")['categories'] == []


def test_authority_bound_target_identity_is_frozen():
    assert TARGET_URL == "https://indico.global/event/13069/contributions/114762/attachments/53315/102415/JCZBLV2022_CEvNSReviewTalk.pdf"
    assert TARGET_SIZE == 18484736
    assert TARGET_SHA256 == "af0fb243be7d8433fbc003de1d963bee3b3510467cfbbd6b1990f1e6626de817"
