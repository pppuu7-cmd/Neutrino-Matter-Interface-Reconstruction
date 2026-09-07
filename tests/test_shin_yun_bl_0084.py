import importlib.util, io, tarfile

spec = importlib.util.spec_from_file_location('a','scripts/audit_shin_yun_bl_0084.py')
a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)

def make_tar(text):
    buf=io.BytesIO()
    with tarfile.open(fileobj=buf,mode='w:gz') as tf:
        b=text.encode(); ti=tarfile.TarInfo('main.tex'); ti.size=len(b); tf.addfile(ti,io.BytesIO(b))
    return buf.getvalue()

def test_context_binding_regexes():
    t=r'U(1)_{B-L} constraint from SN1987A gives g_{B-L} < 3 \times 10^{-10} for mass below O(10 MeV). We revise the previous bound.'
    r=a.classify_record(a.contexts(t)[0],'main.tex')
    assert r['numbers']
    assert any('SN' in x for x in r['observations'])
    assert r['revision_terms']

def test_approx_mass_not_numeric_endpoint():
    t=r'B-L supernova bound is g < 2 \times 10^{-9} for mass O(0.1 MeV).'
    r=a.classify_record(a.contexts(t)[0],'main.tex')
    assert any('O(' in x for x in r['mass_phrases']) or r['mass_phrases']==[]

def test_hash_fail_closed():
    res=a.audit(make_tar('B-L SN1987A g < 1e-9'))
    assert res['classification']=='INFRASTRUCTURE_FAIL_ARCHIVE_HASH'
