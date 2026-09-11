from pathlib import Path

SCRIPT = Path("scripts/audit_0105a5b_r1f_mceq_repository_metadata_preflight.py").read_text(encoding="utf-8")
PREREG = Path("research/prereg/0105a5b_r1f_mceq_repository_metadata_preflight_preregistration.md").read_text(encoding="utf-8")


def test_exact_endpoints_frozen():
    assert 'https://api.github.com/repos/mceq-project/MCEq"' in SCRIPT
    assert 'https://api.github.com/repos/mceq-project/MCEq/releases?per_page=100' in SCRIPT
    assert 'https://api.github.com/repos/mceq-project/MCEq/tags?per_page=100' in SCRIPT
    assert 'mceq-project/MCEq' in PREREG


def test_no_content_or_archive_endpoints():
    lowered = SCRIPT.lower()
    for forbidden in ["/contents/", "/readme", "/tarball", "/zipball", "raw.githubusercontent.com", "/git/trees/"]:
        assert forbidden not in lowered


def test_permissions_remain_zero_and_no_science_execution():
    assert '"standard_3nu_executed": False' in SCRIPT
    assert '"systematic_monte_carlo_executed": False' in SCRIPT
    assert '"observed_bsm_residual_inspected": False' in SCRIPT
    assert '"observed_bsm_residual_permission_percent": 0' in SCRIPT
    assert '"systematic_monte_carlo_execution_permission_percent": 0' in SCRIPT


def test_pass_is_metadata_only():
    assert "PASS_0105A5B_R1F_MCEQ_REPOSITORY_METADATA_PINNABLE_NONDISCOVERY" in SCRIPT
    assert "source_code_inspected" in SCRIPT
    assert "source_archives_downloaded" in SCRIPT
