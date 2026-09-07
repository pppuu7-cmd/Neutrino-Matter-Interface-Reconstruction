import importlib.util, pathlib
P=pathlib.Path(__file__).resolve().parents[1]/'scripts'/'audit_hong_bl_branch_scope_0083a_r1.py'
spec=importlib.util.spec_from_file_location('m0083ar1',P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def one(text,kind):
    t=m.compact(text); r=[x for x in m.relations(t) if x['kind']==kind][0]; return m.record('x.tex',t,r)

def test_semicolon_does_not_truncate_cas_a_compatibility_statement():
    r=one(r"If $e^{\prime}<5\times10^{-13}$ for $U(1)_{B-L}$; the volume emission carries out little alteration of the standard cooling scenario which fits well to the Cas A data.",'upper_bound')
    assert r['observation']=='Cas A'
    assert r['role']=='standard_cooling_compatibility'

def test_latex_eta_is_source_statement_local():
    r=one(r"The constraint from Cas A is $e^{\prime}<1\times10^{-13}\label{eq:B-L_keyresult}$ if $m_{\gamma^\prime}<T_c(n^3P_2)=\mathcal{O}(0.1) MeV$ and $\eta=10^{-13}$.",'upper_bound')
    assert r['observation']=='Cas A' and r['role']=='constraint_bound'
    assert r['equation_label']=='eq:B-L_keyresult'
    assert any('10^{-13}' in x for x in r['eta_scope'])

def test_unrelated_eta_in_next_sentence_is_not_attached():
    t=m.compact(r"The conservative constraint from Cas A is $e^{\prime}<5\times10^{-13}\label{eq:B-L_keyresult_conserv}$ for $m_{\gamma^\prime}<T_c(n^3P_2)=\mathcal{O}(0.1) MeV$. Another branch has $\eta>10^{-8}$.")
    rel=[x for x in m.relations(t) if x['kind']=='upper_bound'][0]; r=m.record('x.tex',t,rel)
    assert r['eta_scope']==[]

def test_conditional_exclusion_precedes_otherwise_hint():
    r=one(r"The region $1\times10^{-13}<e^{\prime}<5\times10^{-13}$ can be further excluded by Cas A if $\eta<10^{-11}$, otherwise it implies evidence for $U(1)_{B-L}$.",'interval')
    assert r['role']=='conditional_additional_exclusion'
    assert r['observation']=='Cas A'
    assert any('10^{-11}' in x for x in r['eta_scope'])

def test_approximate_hint_remains_hint():
    r=one(r"The rapid cooling of Cas A might provide a hint for $U(1)_{B-L}$ with $e^{\prime}\sim10^{-13}$.",'approx_value')
    assert r['role']=='possible_hint'
