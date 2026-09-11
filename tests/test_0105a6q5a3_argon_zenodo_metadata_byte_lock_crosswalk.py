import importlib.util
from pathlib import Path

P=Path('scripts/audit_0105a6q5a3_argon_zenodo_metadata_byte_lock_crosswalk.py')
spec=importlib.util.spec_from_file_location('q5a3',P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def payload_from_expected():
    return {'id':3903810,'doi':'10.5281/zenodo.3903810','metadata':{'version':'v1'},'files':[{'key':k,'checksum':'md5:'+v} for k,v in m.EXPECTED.items()]}

def test_prereg_and_historical_authority_bound():
    src=P.read_text()
    assert 'c2365cd050cdac581934ae8ce6254afeff3d2bd3' in src
    assert '5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091' in src
    assert len(m.EXPECTED)==24

def test_exact_crosswalk_passes():
    cls,a=m.classify(payload_from_expected())
    assert cls=='PASS_0105A6Q5A3_ARGON_ZENODO_METADATA_EXACTLY_MATCHES_FROZEN_BYTE_LOCK_NONDISCOVERY'
    assert a['identity_ok'] and a['inventory_ok'] and a['crosswalk_ok']

def test_single_md5_drift_blocks():
    p=payload_from_expected(); p['files'][0]['checksum']='md5:'+'0'*32
    cls,a=m.classify(p)
    assert cls=='BLOCKED_0105A6Q5A3_ZENODO_FILENAME_MD5_CROSSWALK_DRIFT'
    assert len(a['md5_mismatches'])==1

def test_missing_file_blocks_inventory():
    p=payload_from_expected(); p['files'].pop()
    assert m.classify(p)[0]=='BLOCKED_0105A6Q5A3_ZENODO_INVENTORY_DRIFT'

def test_wrong_identity_blocks():
    p=payload_from_expected(); p['id']=1
    assert m.classify(p)[0]=='BLOCKED_0105A6Q5A3_ZENODO_RECORD_IDENTITY_FAILURE'

def test_no_release_payload_or_science_permissions():
    src=P.read_text()
    assert "URL=\"https://zenodo.org/api/records/3903810\"" in src
    for x in ["'release_file_bytes_downloaded':False","'release_file_bytes_rehashed':False","'scientific_release_content_inspected':False","'linked_file_urls_requested':False","'pseudo_data_generated':False","'likelihood_evaluated':False","'observed_bsm_residual_inspected':False","'bsm_fit_executed':False","'systematic_monte_carlo_execution_permission_percent':0"]: assert x in src
