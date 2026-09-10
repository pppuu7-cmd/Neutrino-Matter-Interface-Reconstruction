import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"scripts"/"audit_0105a6f_argon_implementation_contract.py"
s=importlib.util.spec_from_file_location("a6f",P); a6f=importlib.util.module_from_spec(s); s.loader.exec_module(a6f)

def test_frozen_archive_identity():
    assert a6f.ARXIV_ID=="2003.10630v7"
    assert a6f.ARXIV_SHA256=="2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114"

def test_frozen_member_identities():
    assert a6f.MEMBER_SHA256["main.tex"]=="9e7785c68173921361722af9b95d99c05ff2cdafbf7565fc6b8a057b626b2c86"
    assert a6f.MEMBER_SHA256["supplemental.tex"]=="183ec77ea668c91611fef8f8e117f3796e36eed36d27026608d1830b11a60a57"

def test_exact_official_zenodo_record(): assert a6f.ZENODO_RECORD=="3903810"

def test_contexts_are_line_numbered_and_deterministic():
    c=a6f.contexts("zero\nLikelihood fit here\ntwo\nthree")
    assert c[0]["line"]==2 and c[0]["terms"]==["fit","likelihood"]
    assert [x["line"] for x in c[0]["context"]]==[1,2,3,4]

def test_permissions_remain_zero_and_no_fit_execution():
    t=P.read_text().lower()
    assert '"sm_null_reproduction_permission_percent":0' in t
    assert '"observed_bsm_residual_permission_percent":0' in t
    assert 'scientific_pass_classified":false' in t
    assert "minimize(" not in t and "fitto(" not in t
