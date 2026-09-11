#!/usr/bin/env python3
import argparse, hashlib, json, unicodedata, urllib.parse, urllib.request
from pathlib import Path

PREREG='b0d5a15e8bcba061fc2c3000fff0e299828caf72'
GATE='NMIR-V2-0105A6Q5D'
FILES={
'CENNS10AnlAEfficiency.txt':('https://zenodo.org/api/records/3903810/files/CENNS10AnlAEfficiency.txt/content',1804,'77139f1bb79dcf972a3a0ecc28a4a8f5','21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2'),
'readYAMLParameters.py':('https://zenodo.org/api/records/3903810/files/readYAMLParameters.py/content',1814,'708becd2d56cec1c2e672038581b8c7c','3f1660c54987b9d87f47eda2d19306c2fd061ada72cfb7d3857d996164dd3cd6'),
'PlotExtractedData.C':('https://zenodo.org/api/records/3903810/files/PlotExtractedData.C/content',14020,'1161762465460efdda35d4494a0d8547','c669946d425148fab271d97f99d079b83dbd8f060fea3dd57ac7e00ebecf7d5f'),
'LArParametersAnlA.yaml':('https://zenodo.org/api/records/3903810/files/LArParametersAnlA.yaml/content',4906,'cc9f2c60ce0c17809453e0caad9c4a38','a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e')}
CATS={
'E1':['poisson','multinomial','likelihood','extended','binned','unbinned','roofit','roorealvar','roodata','generate','pseudo'],
'E2':['nuisance','constraint','gaussian','normalization','normalisation','uncertainty','parameter','prior','penalty'],
'E3':['systematic','shape','morph','interpol','excursion','plus1','minus1','+1sigma','-1sigma','+1 sigma','-1 sigma','pdf'],
'E4':['simultaneous','correlation','correlated','covariance','independent','joint','profile'],
'E5':['3152','3154','anchor','nominal','central','precedence','cevns','events','counts'],
'E6':['efficiency','acceptance','interpol','spline','linear','node','threshold']}
class SameZenodo(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        u=urllib.parse.urlparse(urllib.parse.urljoin(req.full_url,newurl)); h=(u.hostname or '').lower()
        if not (h=='zenodo.org' or h.endswith('.zenodo.org')): raise RuntimeError('cross-provider redirect')
        return super().redirect_request(req,fp,code,msg,headers,newurl)
def norm(s): return unicodedata.normalize('NFKC',s).casefold()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    out={'gate':GATE,'preregistration_commit':PREREG,'git_sha':a.git_sha,'files':{},'evidence':{},'pseudo_data_generated':False,'likelihood_evaluated':False,'fit_executed':False,'nuisance_profiled':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0}
    opener=urllib.request.build_opener(SameZenodo()); transport=False; mismatch=False
    payloads={}
    for name,(url,size,emd5,esha) in FILES.items():
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'NMIR-q5d-semantic-inventory/1.0'})
            with opener.open(req,timeout=90) as r: b=r.read(); status=int(getattr(r,'status',r.getcode())); final=r.geturl()
            md5=hashlib.md5(b).hexdigest(); sha=hashlib.sha256(b).hexdigest(); ok=(len(b)==size and md5==emd5 and sha==esha)
            out['files'][name]={'status':status,'final_url':final,'bytes':len(b),'md5':md5,'sha256':sha,'exact_identity_match':ok}
            if not ok: mismatch=True
            payloads[name]=b
        except Exception as e:
            transport=True; out['files'][name]={'error':type(e).__name__+': '+str(e)}
    if transport: cls='BLOCKED_0105A6Q5D_SOURCE_TRANSPORT_OR_DECODE_FAILURE'
    elif mismatch: cls='FAIL_0105A6Q5D_SOURCE_BYTE_IDENTITY_MISMATCH'
    else:
        try:
            for name,b in payloads.items():
                lines=b.decode('utf-8',errors='replace').splitlines(); nlines=[norm(x) for x in lines]; fout={}
                for cat,toks in CATS.items():
                    hitidx=[i for i,s in enumerate(nlines) if any(t in s for t in toks)]
                    windows=[]
                    for i in hitidx:
                        lo=max(0,i-2); hi=min(len(lines),i+3)
                        windows.append({'hit_line':i+1,'start_line':lo+1,'end_line':hi,'lines':[{'line':j+1,'text':lines[j]} for j in range(lo,hi)]})
                    fout[cat]={'hit_count':len(hitidx),'windows':windows}
                out['evidence'][name]=fout
            cls='PASS_0105A6Q5D_BOUNDED_SEMANTIC_EVIDENCE_INVENTORY_COMPLETE_NONDISCOVERY'
        except Exception as e:
            out['processing_error']=type(e).__name__+': '+str(e); cls='BLOCKED_0105A6Q5D_SOURCE_TRANSPORT_OR_DECODE_FAILURE'
    out['classification']=cls
    data=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode(); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_bytes(data)
    print('CLASSIFICATION='+cls); print('RESULT_SHA256='+hashlib.sha256(data).hexdigest())
    if out['evidence']:
        print('HITS='+json.dumps({f:{c:v['hit_count'] for c,v in cats.items()} for f,cats in out['evidence'].items()},sort_keys=True))
if __name__=='__main__': main()
