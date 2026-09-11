from pathlib import Path
SRC=Path('scripts/audit_0105a6q5d_argon_four_file_bounded_semantic_evidence_inventory.py').read_text()

def test_prereg_bound(): assert 'b0d5a15e8bcba061fc2c3000fff0e299828caf72' in SRC
def test_complete_four_file_set():
    for n in ['CENNS10AnlAEfficiency.txt','readYAMLParameters.py','PlotExtractedData.C','LArParametersAnlA.yaml']: assert n in SRC
def test_frozen_categories():
    for c in ["'E1'","'E2'","'E3'","'E4'","'E5'","'E6'"]: assert c in SRC
    for token in ['poisson','multinomial','likelihood','nuisance','gaussian','systematic','morph','covariance','3152','3154','efficiency','threshold']: assert token in SRC
def test_fixed_context_window(): assert 'lo=max(0,i-2); hi=min(len(lines),i+3)' in SRC
def test_source_identity_before_inventory():
    assert 'len(b)==size and md5==emd5 and sha==esha' in SRC
    assert 'FAIL_0105A6Q5D_SOURCE_BYTE_IDENTITY_MISMATCH' in SRC
def test_no_scientific_execution():
    for x in ["pseudo_data_generated':False","likelihood_evaluated':False","fit_executed':False","nuisance_profiled':False","systematic_monte_carlo_executed':False","observed_bsm_residual_inspected':False"]: assert x in SRC
def test_permissions_zero():
    for x in ["systematic_monte_carlo_preregistration_permission_percent':0","systematic_monte_carlo_execution_permission_percent':0","observed_bsm_residual_permission_percent':0"]: assert x in SRC
def test_terminal_classes():
    for x in ['PASS_0105A6Q5D_BOUNDED_SEMANTIC_EVIDENCE_INVENTORY_COMPLETE_NONDISCOVERY','FAIL_0105A6Q5D_SOURCE_BYTE_IDENTITY_MISMATCH','BLOCKED_0105A6Q5D_SOURCE_TRANSPORT_OR_DECODE_FAILURE']: assert x in SRC
