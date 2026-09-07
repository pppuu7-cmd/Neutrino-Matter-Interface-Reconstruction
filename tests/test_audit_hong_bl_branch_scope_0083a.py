import importlib.util, pathlib, io, tarfile

P=pathlib.Path(__file__).resolve().parents[1]/"scripts"/"audit_hong_bl_branch_scope_0083a.py"
spec=importlib.util.spec_from_file_location("m0083a",P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def test_extract_upper_interval_and_hint_relations():
    s=m.compact(r"$e^{\prime}<1\times10^{-13}$. The region $1\times10^{-13}<e^{\prime}<5\times10^{-13}$ can be further excluded. A hint has $e^{\prime}\sim10^{-13}$.")
    rr=m.extract_relations(s)
    kinds=[x['kind'] for x in rr]
    assert 'upper_bound' in kinds
    assert 'interval' in kinds
    assert 'approx_value' in kinds
    assert any(x['kind']=='upper_bound' and abs(x['high']-1e-13)<1e-27 for x in rr)
    assert any(x['kind']=='interval' and abs(x['low']-1e-13)<1e-27 and abs(x['high']-5e-13)<1e-27 for x in rr)

def test_role_identity_for_cas_a_constraint_equation():
    text=m.compact(r"The constraint on the parameters of the $U(1)_{B-L}$ gauge boson from the Cas A observation is given by $e^{\prime}<1\times10^{-13}\label{eq:B-L_keyresult}$ if $m_{\gamma^\prime}<T_c(n^3P_2)=\mathcal{O}(0.1) MeV$ and $\eta=10^{-13}$.")
    rel=[r for r in m.extract_relations(text) if r['kind']=='upper_bound'][0]
    rec=m.branch_record('x.tex',text,rel)
    assert rec['observation']=='Cas A'
    assert rec['role']=='constraint_bound'
    assert rec['branch_resolved']
    assert any('eta=10^{-13}' in x.replace('\\','') or 'eta=10^{-13}' in x for x in rec['eta_scope'])

def test_role_identity_for_conditional_interval():
    text=m.compact(r"For Cas A we find therefore that the parametric region of $1\times10^{-13}<e^{\prime}<5\times10^{-13}$ can be further excluded by Cas A if $\eta<10^{-11}$.")
    rel=[r for r in m.extract_relations(text) if r['kind']=='interval'][0]
    rec=m.branch_record('x.tex',text,rel)
    assert rec['observation']=='Cas A'
    assert rec['role']=='conditional_additional_exclusion'
    assert rec['branch_resolved']

def test_hint_never_becomes_constraint():
    text=m.compact(r"The rapid cooling of Cas A might provide a hint for the $U(1)_{B-L}$ gauge boson with $e^{\prime}\sim10^{-13}$.")
    rel=[r for r in m.extract_relations(text) if r['kind']=='approx_value'][0]
    rec=m.branch_record('x.tex',text,rel)
    assert rec['role']=='possible_hint'
    assert rec['role']!='constraint_bound'

def test_exact_archive_hash_guard_is_deterministic():
    raw=io.BytesIO()
    with tarfile.open(fileobj=raw,mode='w') as tf:
        b=b'hello'; info=tarfile.TarInfo('a.tex'); info.size=len(b); tf.addfile(info,io.BytesIO(b))
    assert m.sha256(raw.getvalue())==m.sha256(raw.getvalue())
