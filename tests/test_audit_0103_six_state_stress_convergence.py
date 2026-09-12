from scripts.audit_0103_six_state_stress_convergence import run_audit

def test_0103x_stress_convergence():
    r=run_audit()
    assert r['status'].startswith('PASS_0103X_')
    assert all(r['gates'].values())
