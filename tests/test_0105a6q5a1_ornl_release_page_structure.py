from pathlib import Path

SRC=Path('scripts/audit_0105a6q5a1_ornl_release_page_structure.py').read_text()

def test_frozen_endpoint_only():
    assert "https://coherent.ornl.gov/data-releases/" in SRC
    assert "urllib.request.urlopen" in SRC

def test_no_link_following_logic():
    assert "urljoin(final,href)" in SRC
    assert "urllib.request.urlopen(resolved" not in SRC
    assert "linked_resources_followed':False" in SRC

def test_frozen_classes_present():
    for s in ['PASS_0105A6Q5A1_ORNL_ZENODO_3903810_LINK_STRUCTURALLY_PRESENT_NONDISCOVERY','BLOCKED_0105A6Q5A1_ORNL_ZENODO_3903810_LINK_NOT_PRESENT','BLOCKED_0105A6Q5A1_ORNL_PAGE_TRANSPORT_FAILURE']:
        assert s in SRC

def test_hard_permissions_zero():
    assert "systematic_monte_carlo_preregistration_permission_percent':0" in SRC
    assert "systematic_monte_carlo_execution_permission_percent':0" in SRC
    assert "observed_bsm_residual_permission_percent':0" in SRC

def test_prereg_bound():
    assert 'f0c211182f71d7b27f3093e15ce29646072f5582' in SRC
