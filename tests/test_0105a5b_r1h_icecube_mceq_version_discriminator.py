from pathlib import Path

SCRIPT=Path('scripts/audit_0105a5b_r1h_icecube_mceq_version_discriminator.py').read_text()
PREREG=Path('research/prereg/0105a5b_r1h_icecube_mceq_version_discriminator_preregistration.md').read_text()


def test_exact_authority_and_candidate_set():
    assert 'https://export.arxiv.org/e-print/2304.12236' in SCRIPT
    for s in ['mceq108','mceq_1_1_1','release_1_1_2','release_1_1_3','release_1_2_0','release_1_2_1','release_1_2_2','release_1_2_3','release_1_2_4','release_1_2_5','release_1_2_6']:
        assert s in SCRIPT and s in PREREG


def test_fail_closed_classes_and_permissions():
    assert 'PASS_0105A5B_R1H_ICECUBE_MCEQ_VERSION_UNIQUELY_DISCRIMINATED_NONDISCOVERY' in SCRIPT
    assert 'BLOCKED_0105A5B_R1H_ICECUBE_MCEQ_VERSION_NOT_UNIQUELY_DISCRIMINATED' in SCRIPT
    assert 'INFRASTRUCTURE_FAIL_0105A5B_R1H' in SCRIPT
    assert 'observed_bsm_residual_permission_percent":0' in SCRIPT
    assert 'systematic_monte_carlo_execution_permission_percent":0' in SCRIPT


def test_prohibited_mceq_implementation_fetch_absent():
    forbidden=['api.github.com/repos/mceq-project','raw.githubusercontent.com/mceq-project','github.com/mceq-project/MCEq/blob','github.com/mceq-project/MCEq/tree']
    for x in forbidden: assert x not in SCRIPT


def test_no_science_execution_markers():
    assert 'mceq_implementation_inspected":False' in SCRIPT
    assert 'standard_3nu_executed":False' in SCRIPT
    assert 'systematic_monte_carlo_executed":False' in SCRIPT
    assert 'observed_bsm_residual_inspected":False' in SCRIPT
