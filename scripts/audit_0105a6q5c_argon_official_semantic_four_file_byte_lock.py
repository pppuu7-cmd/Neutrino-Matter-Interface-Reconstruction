#!/usr/bin/env python3
import argparse, hashlib, json, urllib.parse, urllib.request
from pathlib import Path

PREREG='dc855ab6367ecb7ac095ac2e7d36db358cef8b2a'
GATE='NMIR-V2-0105A6Q5C'
FILES={
'CENNS10AnlAEfficiency.txt':('https://zenodo.org/api/records/3903810/files/CENNS10AnlAEfficiency.txt/content',1804,'77139f1bb79dcf972a3a0ecc28a4a8f5','21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2'),
'readYAMLParameters.py':('https://zenodo.org/api/records/3903810/files/readYAMLParameters.py/content',1814,'708becd2d56cec1c2e672038581b8c7c','3f1660c54987b9d87f47eda2d19306c2fd061ada72cfb7d3857d996164dd3cd6'),
'PlotExtractedData.C':('https://zenodo.org/api/records/3903810/files/PlotExtractedData.C/content',14020,'1161762465460efdda35d4494a0d8547','c669946d425148fab271d97f99d079b83dbd8f060fea3dd57ac7e00ebecf7d5f'),
'LArParametersAnlA.yaml':('https://zenodo.org/api/records/3903810/files/LArParametersAnlA.yaml/content',4906,'cc9f2c60ce0c17809453e0caad9c4a38','a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e')}
class SameZenodo(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        u=urllib.parse.urlparse(urllib.parse.urljoin(req.full_url,newurl)); h=(u.hostname or '').lower()
        if not (h=='zenodo.org' or h.endswith('.zenodo.org')): raise RuntimeError('cross-provider redirect')
        return super().redirect_request(req,fp,code,msg,headers,newurl)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':GATE,'preregistration_commit':PREREG,'git_sha':a.git_sha,'files':{},'scientific_content_inspected':False,'pseudo_data_generated':False,'likelihood_evaluated':False,'observed_bsm_residual_inspected':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0}
    transport_fail=False; mismatch=False; opener=urllib.request.build_opener(SameZenodo())
    for name,(url,size,emd5,esha) in FILES.items():
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'NMIR-q5c-byte-lock/1.0','Accept':'application/octet-stream'})
            with opener.open(req,timeout=90) as r: b=r.read(); status=int(getattr(r,'status',r.getcode())); final=r.geturl()
            md5=hashlib.md5(b).hexdigest(); sha=hashlib.sha256(b).hexdigest(); sm=len(b)==size; mm=md5==emd5; hm=sha==esha
            if not (sm and mm and hm): mismatch=True
            out['files'][name]={'requested_url':url,'final_url':final,'status':status,'bytes':len(b),'md5':md5,'sha256':sha,'size_match':sm,'md5_match':mm,'sha256_match':hm}
        except Exception as e:
            transport_fail=True; out['files'][name]={'requested_url':url,'error':type(e).__name__+': '+str(e)}
    if transport_fail: cls='BLOCKED_0105A6Q5C_ZENODO_DIRECT_TRANSPORT_FAILURE'
    elif mismatch: cls='FAIL_0105A6Q5C_OFFICIAL_BYTE_IDENTITY_MISMATCH'
    else: cls='PASS_0105A6Q5C_ARGON_OFFICIAL_FOUR_SEMANTIC_FILES_BYTE_LOCKED_NONDISCOVERY'
    out['classification']=cls; data=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode(); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_bytes(data)
    print('CLASSIFICATION='+cls); print('RESULT_SHA256='+hashlib.sha256(data).hexdigest()); print('EXACT_MATCH_COUNT='+str(sum(1 for x in out['files'].values() if x.get('size_match') and x.get('md5_match') and x.get('sha256_match'))))
if __name__=='__main__': main()
