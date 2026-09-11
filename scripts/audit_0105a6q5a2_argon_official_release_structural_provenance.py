#!/usr/bin/env python3
import argparse, hashlib, importlib.util, json, re, urllib.parse
from pathlib import Path
from html.parser import HTMLParser

PREREG_COMMIT='2897bd6c6d55f312dd4ab07cd528d4f3a3fa33fa'
GATE='NMIR-V2-0105A6Q5A2'
BASE_PATH=Path('scripts/audit_0105a6q5a_argon_official_release_provenance_inventory.py')

spec=importlib.util.spec_from_file_location('q5a_base', BASE_PATH)
base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)

CLASS_PASS='PASS_0105A6Q5A2_ARGON_OFFICIAL_RELEASE_STRUCTURAL_PROVENANCE_BOUND_NONDISCOVERY'
CLASS_LOCAL='BLOCKED_0105A6Q5A2_LOCAL_0105A3_AUTHORITY_BINDING_FAILURE'
CLASS_ORNL='BLOCKED_0105A6Q5A2_ORNL_STRUCTURAL_ROUTE_FAILURE'
CLASS_ZENODO='BLOCKED_0105A6Q5A2_ZENODO_RECORD_METADATA_FAILURE'
CLASS_ARXIV='BLOCKED_0105A6Q5A2_ARXIV_METADATA_FAILURE'
CLASS_TRANSPORT='BLOCKED_0105A6Q5A2_PROVIDER_TRANSPORT_FAILURE'

class A(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.hrefs=[]
    def handle_starttag(self,tag,attrs):
        if tag.casefold()=='a': self.hrefs.append(dict(attrs).get('href',''))

def inspect_ornl_structural(payload):
    p=A(); p.feed(payload.decode('utf-8',errors='replace')); p.close(); matches=[]
    for href in p.hrefs:
        u=urllib.parse.urlparse(urllib.parse.urljoin(base.ORNL_URL,href or ''))
        host=(u.hostname or '').casefold(); path=u.path.rstrip('/')
        if (host=='zenodo.org' or host.endswith('.zenodo.org')) and re.fullmatch(r'/(?:record|records)/3903810',path):
            matches.append({'hostname':host,'path':u.path,'query':u.query,'fragment':u.fragment})
    return {'pass':bool(matches),'matching_anchor_count':len(matches),'matches':matches}

def classify(local_ok,transport_ok,ornl_ok,zenodo_ok,arxiv_ok):
    if not local_ok:return CLASS_LOCAL
    if not transport_ok:return CLASS_TRANSPORT
    if not ornl_ok:return CLASS_ORNL
    if not zenodo_ok:return CLASS_ZENODO
    if not arxiv_ok:return CLASS_ARXIV
    return CLASS_PASS

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True)
    ap.add_argument('--local-record',default='research/iterations/0105a3_coherent_direct_byte_lock_recovery_pass_20260910.md'); a=ap.parse_args()
    local=base.check_local(a.local_record); providers={}; pred={'ornl':{'pass':False},'zenodo':{'pass':False},'arxiv':{'pass':False}}
    for name,url in (('ornl',base.ORNL_URL),('zenodo',base.ZENODO_URL),('arxiv',base.ARXIV_URL)):
        item=base.fetch(url,name); providers[name]=base.sanitized_transport(item)
        if item['ok']:
            try:
                pred[name]=inspect_ornl_structural(item['payload']) if name=='ornl' else (base.inspect_zenodo(item['payload']) if name=='zenodo' else base.inspect_arxiv(item['payload']))
            except Exception as e: pred[name]={'pass':False,'parse_error':type(e).__name__}
    transport=all(x['ok'] for x in providers.values()); cls=classify(local['pass'],transport,pred['ornl']['pass'],pred['zenodo']['pass'],pred['arxiv']['pass'])
    out={'gate':GATE,'preregistration_commit':PREREG_COMMIT,'git_sha':a.git_sha,'classification':cls,'local_0105a3_binding':local,'providers':providers,'predicates':pred,
         'release_file_bytes_downloaded':False,'release_file_bytes_rehashed':False,'scientific_release_content_inspected':False,'pseudo_data_generated':False,'likelihood_evaluated':False,'observed_bsm_residual_inspected':False,
         'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0}
    data=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode(); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_bytes(data)
    print('CLASSIFICATION='+cls); print('RESULT_SHA256='+hashlib.sha256(data).hexdigest()); print('ORNL_STRUCTURAL_MATCHES='+str(pred['ornl'].get('matching_anchor_count')))
if __name__=='__main__': main()
