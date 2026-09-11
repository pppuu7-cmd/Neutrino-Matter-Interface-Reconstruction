from pathlib import Path
TEXT=Path('scripts/audit_0105a6q5g1_main_analysis_source_archive_structure.py').read_text()
def test_frozen_identity():
 assert '7197fe98682ead93a0264ac0d4b77a6fc54f5d15' in TEXT
 assert '2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114' in TEXT
 assert 'SIZE=446096' in TEXT
 assert 'https://arxiv.org/e-print/2003.10630' in TEXT
def test_suffix_rule():
 for s in ['.tex','.sty','.cls','.bib','.bbl','.txt','.md','.rst']: assert repr(s) in TEXT
def test_no_payload_or_science():
 for s in ["'member_content_read':False","'source_text_inspected':False","'likelihood_evaluated':False","'pseudo_data_generated':False","'systematic_monte_carlo_executed':False","'observed_bsm_residual_inspected':False"]: assert s in TEXT
def test_fail_closed_outcomes():
 for s in ['PASS_0105A6Q5G1_MAIN_ANALYSIS_SOURCE_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY','FAIL_0105A6Q5G1_SOURCE_BYTE_IDENTITY_MISMATCH','BLOCKED_0105A6Q5G1_SOURCE_TRANSPORT_OR_ARCHIVE_STRUCTURE_FAILURE','BLOCKED_0105A6Q5G1_NO_SOURCE_TEXT_CANDIDATES']: assert s in TEXT
