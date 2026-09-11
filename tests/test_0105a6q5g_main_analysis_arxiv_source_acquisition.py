from pathlib import Path
TEXT=Path('scripts/audit_0105a6q5g_main_analysis_arxiv_source_acquisition.py').read_text()

def test_prereg_and_endpoint_frozen():
 assert 'e88ced9395b09c99b9634f39b8c11df5133fe754' in TEXT
 assert 'https://arxiv.org/e-print/2003.10630' in TEXT

def test_no_source_content_inspection():
 for s in ["'archive_opened':False","'member_listed':False","'source_text_inspected':False"]: assert s in TEXT
 assert 'tarfile' not in TEXT
 assert 'gzip' not in TEXT

def test_no_scientific_execution():
 for s in ["'likelihood_evaluated':False","'pseudo_data_generated':False","'systematic_monte_carlo_executed':False","'observed_bsm_residual_inspected':False","'observed_bsm_residual_permission_percent':0"]: assert s in TEXT

def test_fail_closed_outcomes():
 assert 'PASS_0105A6Q5G_MAIN_ANALYSIS_ARXIV_SOURCE_BYTES_ACQUIRED_NONDISCOVERY' in TEXT
 assert 'BLOCKED_0105A6Q5G_MAIN_ANALYSIS_SOURCE_TRANSPORT_FAILURE' in TEXT
 assert 'FAIL_0105A6Q5G_MAIN_ANALYSIS_PROVIDER_IDENTITY_FAILURE' in TEXT
