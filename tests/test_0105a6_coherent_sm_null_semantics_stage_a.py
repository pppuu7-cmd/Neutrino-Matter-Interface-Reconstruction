import importlib.util
from pathlib import Path

SCRIPT = Path('scripts/audit_0105a6_coherent_sm_null_semantics_stage_a.py')


def load_module():
    spec = importlib.util.spec_from_file_location('audit0105a6', SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_frozen_file_inventory_and_hashes():
    m = load_module()
    assert set(m.FILES) == {'csi', 'ar'}
    assert m.FILES['csi']['record'] == '1228631'
    assert m.FILES['ar']['record'] == '3903810'
    assert len(m.FILES['csi']) - 1 == 3
    assert len(m.FILES['ar']) - 1 == 4
    for det in ('csi', 'ar'):
        for key, value in m.FILES[det].items():
            if key != 'record':
                assert len(value) == 64
                int(value, 16)


def test_eight_frozen_evidence_categories():
    m = load_module()
    assert set(m.CATEGORIES) == {
        'observable_binning', 'sm_signal', 'detector_response', 'backgrounds',
        'nuisance', 'normalization', 'statistic', 'benchmark'
    }


def test_stage_a_cannot_authorize_reproduction_or_residual_by_construction():
    text = SCRIPT.read_text()
    assert 'likelihood_authority_complete"] = None' in text
    assert 'sm_null_reproduction_allowed"] = False' in text
    assert 'observed_bsm_residual_permission_percent": 0' in text
    assert 'PASS_0105A6_STAGE_A_AUTHORITY_INVENTORY_NONDISCOVERY' in text
