from pathlib import Path
S=Path('scripts/audit_0105a5b_r1j2_pisa_methodology_semantic_locator.py').read_text()
P=Path('research/prereg/0105a5b_r1j2_pisa_methodology_semantic_locator_preregistration.md').read_text()
def test_frozen_source_and_candidates():
 assert 'e8d26d85195764037765661fb2e5236ec4284a712adbfd9738b7c3908593c6be' in S
 for x in ['bits.sty','elsarticle.cls','main.tex','sample.bib','text/valid.tex']: assert x in S and x in P
def test_complete_tags_and_classes():
 for t in ['contours_working_0.1','4.3a1','4.2.1','4.1.4','4.0','3.2.1','3.0','2.0.1','1.0.1','1.0']: assert t in S and t in P
 for c in ['PASS_0105A5B_R1J2_PISA_METHODOLOGY_EXPLICIT_IMPLEMENTATION_AUTHORITY_FOUND_NONDISCOVERY','BLOCKED_0105A5B_R1J2_PISA_METHODOLOGY_IMPLEMENTATION_STATE_NOT_IMMUTABLY_IDENTIFIED','BLOCKED_0105A5B_R1J2_NO_PISA_SEMANTIC_EVIDENCE','INFRASTRUCTURE_FAIL_0105A5B_R1J2']: assert c in S
def test_no_pisa_repository_fetch():
 assert 'api.github.com/repos/icecube/pisa' not in S.lower()
 assert 'raw.githubusercontent.com/icecube/pisa' not in S.lower()
def test_permissions_zero():
 for x in ["'pisa_repository_content_fetched':False","'standard_3nu_executed':False","'systematic_monte_carlo_executed':False","'observed_bsm_residual_inspected':False"]: assert x in S
