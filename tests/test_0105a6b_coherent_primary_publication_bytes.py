from scripts.audit_0105a6b_coherent_primary_publication_bytes import (
    TARGETS,
    exact_versioned_arxiv_pdf_identity,
    normalize,
)


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


def test_exact_versioned_arxiv_identity_accepts_only_frozen_endpoint_shapes():
    for cfg in TARGETS.values():
        arxiv_id = cfg["arxiv"]
        assert exact_versioned_arxiv_pdf_identity(
            f"https://arxiv.org/pdf/{arxiv_id}", arxiv_id
        )
        assert exact_versioned_arxiv_pdf_identity(
            f"https://arxiv.org/pdf/{arxiv_id}.pdf", arxiv_id
        )
        assert not exact_versioned_arxiv_pdf_identity(
            f"https://arxiv.org/pdf/{arxiv_id.split('v')[0]}", arxiv_id
        )
        assert not exact_versioned_arxiv_pdf_identity(
            f"https://export.arxiv.org/pdf/{arxiv_id}", arxiv_id
        )
        assert not exact_versioned_arxiv_pdf_identity(
            f"https://arxiv.org/pdf/{arxiv_id}?download=1", arxiv_id
        )
