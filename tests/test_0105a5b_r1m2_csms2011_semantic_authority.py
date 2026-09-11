import importlib.util
from pathlib import Path

P=Path('scripts/audit_0105a5b_r1m2_csms2011_semantic_authority.py')
spec=importlib.util.spec_from_file_location('r1m2',P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def test_frozen_source_and_member():
    assert m.EXPECTED_SHA256=='274b459c38d54c7b874a3353c622f9c807a1e55dcd2fc27214541e2d9f6015ce'
    assert m.MEMBER=='nucross.tex'

def test_quantitative_uncertainty_detector():
    text='''The neutrino cross section prediction has an uncertainty of 3 percent from the PDF.\nThe antineutrino cross section is also shown.'''
    r=m.inspect_text(text)
    assert r['semantic_pass'] is True
    assert r['quantitative_uncertainty_present'] is True

def test_nonquantitative_statement_blocks():
    r=m.inspect_text('PDF uncertainty affects the neutrino cross section prediction.')
    assert r['semantic_pass'] is False
