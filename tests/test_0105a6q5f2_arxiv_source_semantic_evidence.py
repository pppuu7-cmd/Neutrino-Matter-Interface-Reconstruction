from pathlib import Path
import ast

SCRIPT=Path('scripts/audit_0105a6q5f2_arxiv_source_semantic_evidence.py')
TEXT=SCRIPT.read_text()

def test_frozen_prereg_and_source_identity():
 assert "58e32cedffb6c173079f8098513dbc1e81fbb4b6" in TEXT
 assert "5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde" in TEXT
 assert "SIZE=23805" in TEXT
 assert "https://arxiv.org/e-print/2006.12659" in TEXT

def test_complete_candidate_set_is_frozen():
 for name,size in [('authors_els.tex',4985),('CENNS10DataReleaseCompanion.bbl',1308),('CENNS10DataReleaseCompanion.bib',1274),('CENNS10DataReleaseCompanion.tex',27656)]:
  assert repr(name) in TEXT and str(size) in TEXT

def test_only_frozen_semantic_items_exist():
 tree=ast.parse(TEXT)
 assert all(x in TEXT for x in ["'F1'","'F4'","'F6'","'F7'"])
 for banned in ['NSI','magnetic moment','light mediator','Wilks','significance','discovery threshold']:
  assert banned not in TEXT

def test_no_scientific_fit_or_residual_execution():
 assert "'likelihood_evaluated':False" in TEXT
 assert "'pseudo_data_generated':False" in TEXT
 assert "'optimizer_executed':False" in TEXT
 assert "'systematic_monte_carlo_executed':False" in TEXT
 assert "'observed_bsm_residual_inspected':False" in TEXT
 assert "'observed_bsm_residual_permission_percent':0" in TEXT

def test_fail_closed_outcomes_present():
 assert 'FAIL_0105A6Q5F2_SOURCE_BYTE_IDENTITY_MISMATCH' in TEXT
 assert 'BLOCKED_0105A6Q5F2_SOURCE_TRANSPORT_OR_EXTRACTION_FAILURE' in TEXT
 assert 'BLOCKED_0105A6Q5F2_ARXIV_SOURCE_SEMANTIC_CONTRACT_INCOMPLETE' in TEXT
