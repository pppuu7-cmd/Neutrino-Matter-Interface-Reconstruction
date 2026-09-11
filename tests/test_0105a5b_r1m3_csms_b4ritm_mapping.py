import importlib.util
from pathlib import Path

P=Path('scripts/audit_0105a5b_r1m3_csms_b4ritm_mapping.py')
spec=importlib.util.spec_from_file_location('r1m3',P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def test_lexical_diagnostics_are_not_scientific_classification():
    text='''IceCube DeepCore B4RITM uses the CSMS DIS cross-section nuisance parameter xsec_DIS. The event-weight reweight ratio is explicitly defined. Up/down gives the sign convention and orientation. A prior width of 5% defines the amplitude. The covariance correlation matrix and normalization convention are fixed.'''
    nctx,e=m.lexical_diagnostics([('frozen.txt',text)])
    assert nctx>0
    assert all(e[k] for k in m.BUCKETS)
    src=P.read_text()
    assert 'EVIDENCE_BUNDLE_ONLY_0105A5B_R1M3_UNCLASSIFIED' in src
    assert 'PASS_0105A5B_R1M3_CSMS_B4RITM_EXPERIMENTAL_MAPPING_COMPLETE_NONDISCOVERY' not in src

def test_negative_absence_statements_can_hit_keywords_but_cannot_self_pass():
    text='''IceCube DeepCore DIS-CSMS authority does not recover a complete provider-backed event-level transformation contract. The prior/range, sign/orientation and covariance/correlation normalization convention are not defined.'''
    nctx,e=m.lexical_diagnostics([('blocked.txt',text)])
    assert nctx>0
    assert e['transform'] and e['prior_range'] and e['covariance']
    assert 'scientific_mapping_complete_machine_claim\':False' in P.read_text().replace(' ', '')

def test_no_experiment_anchor_has_no_bounded_context():
    text='''CSMS DIS cross-section nuisance parameter uses event-weight reweight ratio, up/down sign convention, prior 5%, and covariance correlation matrix.'''
    nctx,e=m.lexical_diagnostics([('theory.txt',text)])
    assert nctx==0
    assert all(not e[k] for k in m.BUCKETS)

def test_hard_prohibition_literals_present():
    src=P.read_text()
    assert "'standard_3nu_executed':False" in src
    assert "'systematic_monte_carlo_executed':False" in src
    assert "'observed_bsm_residual_inspected':False" in src
    assert "'network_requests_executed':False" in src
