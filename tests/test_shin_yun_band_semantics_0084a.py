import importlib.util, io, tarfile
spec=importlib.util.spec_from_file_location('a','scripts/audit_shin_yun_band_semantics_0084a.py')
a=importlib.util.module_from_spec(spec); spec.loader.exec_module(a)

def tar(text):
    b=io.BytesIO()
    with tarfile.open(fileobj=b,mode='w:gz') as tf:
        x=text.encode(); ti=tarfile.TarInfo('main.tex'); ti.size=len(x); tf.addfile(ti,io.BytesIO(x))
    return b.getvalue()

def test_hash_fail_closed():
    assert a.audit(tar('x'))['classification']=='INFRASTRUCTURE_FAIL_ARCHIVE_HASH'

def test_normalization_keeps_semantic_tokens():
    t=a.norm(r"The parameter space excluded by SN1987A. e^\prime < 10^{-11} for m_{\gamma^\prime}<20\,MeV. e^\prime>1.5 \times 10^{-8} are allowed for m_{\gamma^\prime}<2m_e.")
    assert a.has(r'e\^\\prime\s*<\s*10\^\{-11\}',t)
    assert a.has(r'e\^\\prime\s*>\s*1\.5\s*\\times\s*10\^\{-8\}',t)

def test_domains_are_not_numerically_collapsed_in_output_source():
    src=open('scripts/audit_shin_yun_band_semantics_0084a.py').read()
    assert 'retain body <2 m_e and conclusion <1 MeV as distinct' in src
    assert '0.511' not in src
