#!/usr/bin/env python3
import argparse, hashlib, json, urllib.parse, urllib.request, urllib.error
from pathlib import Path

PREREG_COMMIT="df83de59bf8cb66fcfe8009f3228f2b3a5b78174"
CEEM_URL="https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html"
TITLE="TOWARDS AN IMPROVED MEASUREMENT OF THE CEVNS PROCESS WITH THE CENNS-10 LAR DETECTOR"
SEARCH_URL="https://scholarworks.iu.edu/dspace/discover?query="+urllib.parse.quote('"'+TITLE+'"')
UA="NMIR-0105a6q4ft-transport-diagnostic/1.0"

def probe(url):
    req=urllib.request.Request(url,headers={"User-Agent":UA})
    try:
        with urllib.request.urlopen(req,timeout=120) as r:
            b=r.read()
            return {"requested_url":url,"final_url":r.geturl(),"status":int(getattr(r,"status",r.getcode())),"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"content_type":r.headers.get("Content-Type"),"error":None}
    except urllib.error.HTTPError as e:
        b=e.read()
        return {"requested_url":url,"final_url":e.geturl(),"status":int(e.code),"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"content_type":e.headers.get("Content-Type"),"error":type(e).__name__}
    except Exception as e:
        return {"requested_url":url,"final_url":None,"status":None,"bytes":0,"sha256":None,"content_type":None,"error":type(e).__name__+": "+str(e)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    probes=[probe(CEEM_URL),probe(SEARCH_URL)]
    cls="PASS_0105A6Q4FT_FROZEN_ENDPOINT_TRANSPORT_DIAGNOSTIC_NONDISCOVERY" if all(x['status']==200 for x in probes) else "BLOCKED_0105A6Q4FT_FROZEN_ENDPOINT_TRANSPORT_DIAGNOSTIC_IDENTIFIED"
    out={"benchmark":"NMIR-V2-0105A6Q4FT","preregistration_commit":PREREG_COMMIT,"git_sha":a.git_sha,"classification":cls,"probes":probes,"pdf_downloaded":False,"pdf_content_inspected":False,"likelihood_evaluated":False,"observed_bsm_residual_inspected":False,"systematic_monte_carlo_preregistration_permission_percent":0,"systematic_monte_carlo_execution_permission_percent":0,"observed_bsm_residual_permission_percent":0}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
