#!/usr/bin/env python3
import hashlib, json, os, re
from urllib.parse import urlparse
from urllib.request import Request, build_opener, HTTPRedirectHandler

GATE="NMIR-V2-0105A6Q5A3"
PREREG="c2365cd050cdac581934ae8ce6254afeff3d2bd3"
URL="https://zenodo.org/api/records/3903810"
EXPECTED={
'CENNS10AnlAEfficiency.txt':'77139f1bb79dcf972a3a0ecc28a4a8f5',
'CENNS10DataReleaseCompanion.pdf':'f0f67a11113f5d60c84421bb76e37728',
'LArParametersAnlA.yaml':'cc9f2c60ce0c17809453e0caad9c4a38',
'PlotExtractedData.C':'1161762465460efdda35d4494a0d8547',
'bkgpdf.txt':'ccc2df245a004a644cd04317d07b35df',
'brnpdf+1sigBRNTimingMean.txt':'edf00a561d1f934d3e8bef2c401e8d91',
'brnpdf+1sigEnergy.txt':'2ad879a7302d8ca2e25ef1e192f88183',
'brnpdf-1sigBRNTimingMean.txt':'937c7c0f53aff94600ed7dfffb69de8b',
'brnpdf-1sigEnergy.txt':'ea7dd87225a19fe75f28d3dec00e7441',
'brnpdf.txt':'7ccf0fdc0d0010d2c6570d620816e4df',
'brnpdfBRNTimingWidthSyst.txt':'5050ef987d122fae43eeef27b86ec1b2',
'cevnspdf+1sigF90.txt':'0237a293b243b371459bcb19bc2fa116',
'cevnspdf-1sigF90.txt':'b9bd9500b0c84b851f0d38e4869cad0f',
'cevnspdf.txt':'5601234e03bc9bbd01066591629e72c0',
'cevnspdfCEvNSTimingMeanSyst.txt':'24455c1cd2acf4f359cf0942deb7b29b',
'datanobkgsub.txt':'4346ec521e91a7227b2e34ff8f3c269b',
'delbrnpdf.txt':'5d57e91a773f03368d149dc5739b6a01',
'energydata1d.txt':'fb4122f9309e16df39de4d3f3224af56',
'f90data1d.txt':'4fa866380574a7d70f719ffcbab11806',
'readYAMLParameters.py':'708becd2d56cec1c2e672038581b8c7c',
'systerrors1denergy.txt':'d933e52f2c0dd8987e3535640194065f',
'systerrors1dpsd.txt':'2d0cb7ca23e3b0a3edfd2f0cb0e9d5dd',
'systerrors1dtime.txt':'98c920d71497cfa8b35bbd18fc8975c3',
'timingdata1d.txt':'a467365800489d105f7305a38751c9e5'}

class SameZenodoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        host=(urlparse(newurl).hostname or '').lower()
        if not (host=='zenodo.org' or host.endswith('.zenodo.org')):
            raise RuntimeError('cross-provider redirect forbidden')
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def norm_md5(value):
    s=str(value or '').strip().lower()
    if s.startswith('md5:'): s=s[4:]
    return s if re.fullmatch(r'[0-9a-f]{32}',s) else None

def extract_pairs(payload):
    out=[]
    for item in payload.get('files') or []:
        name=item.get('key') or item.get('filename') or ''
        out.append((name,norm_md5(item.get('checksum'))))
    return out

def classify(payload):
    rid=str(payload.get('id',''))
    doi=str(payload.get('doi') or (payload.get('metadata') or {}).get('doi') or '')
    version=str((payload.get('metadata') or {}).get('version') or '')
    pairs=extract_pairs(payload); names=[n for n,_ in pairs]
    identity_ok=(rid=='3903810' and doi=='10.5281/zenodo.3903810')
    inventory_ok=(len(pairs)==24 and len(set(names))==24 and all(bool(n) and bool(m) for n,m in pairs))
    current={n:m for n,m in pairs if n and m}
    crosswalk_ok=inventory_ok and current==EXPECTED
    if not identity_ok: cls='BLOCKED_0105A6Q5A3_ZENODO_RECORD_IDENTITY_FAILURE'
    elif not inventory_ok: cls='BLOCKED_0105A6Q5A3_ZENODO_INVENTORY_DRIFT'
    elif not crosswalk_ok: cls='BLOCKED_0105A6Q5A3_ZENODO_FILENAME_MD5_CROSSWALK_DRIFT'
    else: cls='PASS_0105A6Q5A3_ARGON_ZENODO_METADATA_EXACTLY_MATCHES_FROZEN_BYTE_LOCK_NONDISCOVERY'
    return cls,{'record_id':rid,'doi':doi,'version':version,'file_count':len(pairs),'identity_ok':identity_ok,'inventory_ok':inventory_ok,'crosswalk_ok':crosswalk_ok,'missing_from_live':sorted(set(EXPECTED)-set(current)),'extra_in_live':sorted(set(current)-set(EXPECTED)),'md5_mismatches':sorted(n for n in set(EXPECTED)&set(current) if EXPECTED[n]!=current[n]),'pairset_sha256':hashlib.sha256(json.dumps(sorted(current.items()),separators=(',',':'),ensure_ascii=False).encode()).hexdigest()}

def main():
    result={'gate':GATE,'preregistration_commit':PREREG,'git_sha':os.getenv('GITHUB_SHA'),'historical_run_id':34418207408,'historical_job_id':102834981270,'historical_artifact_id':10147580844,'historical_artifact_zip_sha256':'b4d93c5e121ddbf503f9dd837fff1c356fd704342d48c5d243213ac599e26da4','historical_manifest_sha256':'5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091','release_file_bytes_downloaded':False,'release_file_bytes_rehashed':False,'scientific_release_content_inspected':False,'linked_file_urls_requested':False,'pseudo_data_generated':False,'likelihood_evaluated':False,'nuisance_profiled':False,'observed_bsm_residual_inspected':False,'bsm_fit_executed':False,'systematic_monte_carlo_preregistration_permission_percent':0,'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0}
    try:
        req=Request(URL,headers={'User-Agent':'NMIR-provenance-audit/1.0','Accept':'application/json'})
        with build_opener(SameZenodoRedirect).open(req,timeout=30) as r:
            body=r.read(); final=r.geturl(); status=getattr(r,'status',None) or r.getcode(); ctype=r.headers.get('Content-Type','')
        host=(urlparse(final).hostname or '').lower()
        if not (host=='zenodo.org' or host.endswith('.zenodo.org')): raise RuntimeError('final provider not Zenodo')
        result['provider']={'requested_url':URL,'final_url':final,'status':status,'content_type':ctype,'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest()}
        if status!=200: raise RuntimeError(f'HTTP {status}')
        cls,audit=classify(json.loads(body.decode('utf-8'))); result['classification']=cls; result['audit']=audit
    except Exception as e:
        result['classification']='BLOCKED_0105A6Q5A3_ZENODO_METADATA_TRANSPORT_FAILURE'; result['error_type']=type(e).__name__; result['error']=str(e)
    with open('result.json','w',encoding='utf-8') as f: json.dump(result,f,indent=2,sort_keys=True,ensure_ascii=False)
    print(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False))

if __name__=='__main__': main()
