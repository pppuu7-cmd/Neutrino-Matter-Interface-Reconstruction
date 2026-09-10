from scripts.audit_0105a6b_coherent_primary_publication_bytes import TARGETS, normalize


def test_only_two_frozen_primary_targets():
    assert set(TARGETS) == {"csi", "ar"}
    assert TARGETS["csi"]["arxiv"] == "1708.01294v1"
    assert TARGETS["ar"]["arxiv"] == "2003.10630v7"


def test_versioned_arxiv_urls_are_frozen():
    for cfg in TARGETS.values():
        assert cfg["url"] == f"https://arxiv.org/pdf/{cfg['arxiv']}"
        assert cfg["doi"]
        assert "COHERENT" not in cfg["url"]


def test_identity_normalization_is_format_only():
    assert normalize("First\n Measurement  of  CEvNS") == "First Measurement of CEvNS"
