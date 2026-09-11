import importlib.util
from pathlib import Path

P=Path('scripts/audit_0105a5b_r1l2_barr2006_semantic_authority.py')
spec=importlib.util.spec_from_file_location('r1l2',P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def test_frozen_source_and_member():
    assert m.EXPECTED_SHA256=='f128800ae1eb18fb58c27ce91941b726f1bbf42a7f7ac17a273664f3a81da0f7'
    assert m.MEMBER=='uncertainflux.tex'

def test_semantic_detector_requires_wyz_plus_minus_and_variation():
    text='''W+ parameter changes atmospheric neutrino flux\nW- variation of pion flux\nY^+ uncertainty in kaon flux\nY^- parameter\nZ+ variation\nZ^- error in flux'''
    r=m.inspect_text(text)
    assert r['semantic_pass'] is True
    assert r['families']==['W','Y','Z']
    assert r['signs']==['+','-']

def test_incomplete_family_blocks():
    r=m.inspect_text('W+ parameter flux\nW- variation flux\nY+ uncertainty flux\nY- error flux')
    assert r['semantic_pass'] is False
