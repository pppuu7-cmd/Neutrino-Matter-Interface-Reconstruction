import numpy as np
from scripts.run_0105a6o1_argon_optimizer_convergence_diagnostic_v2 import grad,hessian,kkt_inf


def test_gradient_matches_simple_one_bin_case():
    n=np.array([2.0]); s={"S":np.array([1.0]),"P":np.array([0.0]),"D":np.array([0.0]),"B":np.array([0.0])}
    g=grad([2.0,497.0,33.0,3152.0],n,s,3152.0)
    assert np.allclose(g,np.zeros(4),atol=1e-12)


def test_hessian_is_symmetric_psd_in_simple_case():
    n=np.array([2.0]); s={"S":np.array([1.0]),"P":np.array([0.0]),"D":np.array([0.0]),"B":np.array([0.0])}
    H=hessian([2.0,497.0,33.0,3152.0],n,s,3152.0)
    assert np.allclose(H,H.T,atol=0.0)
    assert np.linalg.eigvalsh(H).min()>=0.0


def test_kkt_lower_bound_one_sided_rule():
    assert kkt_inf(np.array([0.0,1.0]),np.array([2.0,0.0]))==0.0
    assert kkt_inf(np.array([0.0,1.0]),np.array([-2.0,0.0]))==2.0


def test_diagnostic_has_no_publication_or_bsm_thresholds():
    import scripts.run_0105a6o1_argon_optimizer_convergence_diagnostic_v2 as m
    src=open(m.__file__,encoding='utf-8').read()
    assert 'TARGET=' not in src and 'ROBUST=' not in src
    assert 'observed_bsm_residual_permission_percent":0' in src
