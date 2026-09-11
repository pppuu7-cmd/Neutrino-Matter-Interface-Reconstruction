#!/usr/bin/env python3
import argparse, hashlib, json, urllib.parse, urllib.request

ENDPOINT='https://scholarworks.iu.edu/iuswrrest/api/discover/search/objects'
SENTINEL='NMIR_ENDPOINT_CONTRACT_SENTINEL_0105A6Q4FS1'
TARGET_LITERALS=[
    'Benjamin Suh',
    'Benjamin D. Suh',
    'Towards an improved measurement of the CEVNS process with the CENNS-10 LAr Detector',
]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    ap.add_argument('--git-sha', required=True)
    args=ap.parse_args()
    qs=urllib.parse.urlencode({'query':SENTINEL,'size':'1'})
    requested=ENDPOINT+'?'+qs
    out={
      'gate':'0105a6q4fs1','git_sha':args.git_sha,'requested_url':requested,
      'target_specific_search_executed':False,'item_links_followed':False,
      'pdf_downloaded':False,'pdf_content_inspected':False,
      'likelihood_evaluated':False,'pseudo_data_generated':False,
      'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,
      'systematic_monte_carlo_execution_permission_percent':0,
      'observed_bsm_residual_permission_percent':0,
    }
    try:
        req=urllib.request.Request(requested, headers={'Accept':'application/json','User-Agent':'NMIR-q4fs1-authority-probe/1.0'})
        with urllib.request.urlopen(req, timeout=45) as r:
            body=r.read()
            out.update(http_status=r.status, final_url=r.geturl(), content_type=r.headers.get('Content-Type',''), response_bytes=len(body), response_sha256=hashlib.sha256(body).hexdigest())
    except Exception as e:
        out.update(classification='BLOCKED_0105A6Q4FS1_IUSCHOLARWORKS_METADATA_ENDPOINT_TRANSPORT_OR_SCHEMA_UNAVAILABLE', transport_error=repr(e))
        open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); return
    text=body.decode('utf-8','replace')
    exposed=[x for x in TARGET_LITERALS if x.lower() in text.lower()]
    out['unexpected_target_literals']=exposed
    if exposed:
        out['classification']='FAIL_0105A6Q4FS1_UNEXPECTED_TARGET_CONTENT_EXPOSURE'
        open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); return
    try:
        d=json.loads(text); out['json_parseable']=True
    except Exception:
        d=None; out['json_parseable']=False
    top=sorted(d.keys()) if isinstance(d,dict) else []
    out['top_level_keys']=top
    links=d.get('_links',{}) if isinstance(d,dict) else {}
    out['hal_link_relations']=sorted(links.keys()) if isinstance(links,dict) else []
    embedded=d.get('_embedded',{}) if isinstance(d,dict) else {}
    out['embedded_relations']=sorted(embedded.keys()) if isinstance(embedded,dict) else []
    schema_ok=bool(out['json_parseable'] and (out['hal_link_relations'] or out['embedded_relations']))
    out['machine_readable_discovery_structure']=schema_ok
    if out.get('http_status')==200 and schema_ok:
        out['classification']='PASS_0105A6Q4FS1_IUSCHOLARWORKS_METADATA_ENDPOINT_CONTRACT_VALIDATED_NONDISCOVERY'
    else:
        out['classification']='BLOCKED_0105A6Q4FS1_IUSCHOLARWORKS_METADATA_ENDPOINT_TRANSPORT_OR_SCHEMA_UNAVAILABLE'
    open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')

if __name__=='__main__': main()
