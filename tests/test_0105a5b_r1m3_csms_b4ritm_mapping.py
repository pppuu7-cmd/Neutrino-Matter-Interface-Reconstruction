import importlib.util
from pathlib import Path

P=Path('scripts/audit_0105a5b_r1m3_csms_b4ritm_mapping.py')
spec=importlib.util.spec_from_file_location('r1m3',P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def test_complete_requires_all_five_buckets_and_experimental_anchor():
    text='''IceCube DeepCore B4RITM uses the CSMS DIS cross-section nuisance parameter xsec_DIS. The event-weight reweight ratio is explicitly defined. Up/down gives the sign convention and orientation. A prior width of 5% defines the amplitude. The covariance correlation matrix and normalization convention are fixed.'''
    complete,nctx,e=m.classify_texts([('frozen.txt',text)])
    assert complete and nctx>0
    assert all(e[k] for k in m.BUCKETS)

def test_missing_covariance_blocks():
    text='''IceCube DeepCore uses CSMS DIS cross-section nuisance parameter xsec_DIS with event-weight reweight ratio, up/down sign convention, and prior width 5%.'''
    complete,nctx,e=m.classify_texts([('frozen.txt',text)])
    assert nctx>0 and not complete
    assert not e['covariance']

def test_no_experiment_anchor_blocks_generic_csms_theory():
    text='''CSMS DIS cross-section nuisance parameter uses event-weight reweight ratio, up/down sign convention, prior 5%, and covariance correlation matrix.'''
    complete,nctx,e=m.classify_texts([('theory.txt',text)])
    assert nctx==0 and not complete

def test_hard_prohibition_literals_present():
    src=P.read_text()
    assert "'standard_3nu_executed':False" in src
    assert "'systematic_monte_carlo_executed':False" in src
    assert "'observed_bsm_residual_inspected':False" in src
    assert "'network_requests_executed':False" in src
