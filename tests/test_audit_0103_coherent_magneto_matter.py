from scripts.audit_0103_coherent_magneto_matter import run_audit

def test_0103m_coherent_magneto_matter():
    r=run_audit()
    assert r['status'].startswith('PASS_0103M_')
    assert all(r['gates'].values())
