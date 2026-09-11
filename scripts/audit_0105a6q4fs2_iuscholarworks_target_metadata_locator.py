#!/usr/bin/env python3
import argparse, hashlib, json, re, urllib.parse, urllib.request

ENDPOINT='https://scholarworks.iu.edu/iuswrrest/api/discover/search/objects'
QUERY='"Towards an improved measurement of the CEVNS process with the CENNS-10 LAr Detector" "Benjamin Suh" "2025"'
SIZE='20'
TITLE='Towards an improved measurement of the CEVNS process with the CENNS-10 LAr Detector'
AUTHORS={'benjamin suh','benjamin d. suh'}
YEAR='2025'


def norm(s):
    return re.sub(r'\s+',' ',str(s)).strip().lower()


def metadata_values(md, allowed_tokens):
    vals=[]
    if not isinstance(md,dict):
        return vals
    for k,v in md.items():
        lk=str(k).lower()
        if not any(tok in lk for tok in allowed_tokens):
            continue
        seq=v if isinstance(v,list) else [v]
        for x in seq:
            if isinstance(x,dict):
                if 'value' in x and isinstance(x['value'],(str,int,float)):
                    vals.append(str(x['value']))
            elif isinstance(x,(str,int,float)):
                vals.append(str(x))
    return vals


def search_results(d):
    emb=d.get('_embedded',{}) if isinstance(d,dict) else {}
    sr=emb.get('searchResult',[]) if isinstance(emb,dict) else []
    if isinstance(sr,dict):
        # HAL variants may wrap a list one level lower.
        e2=sr.get('_embedded',{}) if isinstance(sr,dict) else {}
        for key in ('objects','searchResult'):
            if isinstance(e2,dict) and isinstance(e2.get(key),list):
                return e2[key]
        return [sr]
    return sr if isinstance(sr,list) else []


def indexable(result):
    if not isinstance(result,dict):
        return {}
    emb=result.get('_embedded',{})
    if isinstance(emb,dict) and isinstance(emb.get('indexableObject'),dict):
        return emb['indexableObject']
    if isinstance(result.get('indexableObject'),dict):
        return result['indexableObject']
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    ap.add_argument('--git-sha',required=True)
    args=ap.parse_args()
    requested=ENDPOINT+'?'+urllib.parse.urlencode({'query':QUERY,'size':SIZE})
    out={
      'gate':'0105a6q4fs2','git_sha':args.git_sha,'requested_url':requested,
      'exact_query':QUERY,'size':int(SIZE),'request_count':1,
      'item_links_followed':False,'identifier_guessed_or_constructed':False,
      'file_or_bitstream_downloaded':False,'dissertation_scientific_text_inspected':False,
      'likelihood_evaluated':False,'pseudo_data_generated':False,
      'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,
      'systematic_monte_carlo_execution_permission_percent':0,
      'observed_bsm_residual_permission_percent':0,
    }
    try:
        req=urllib.request.Request(requested,headers={'Accept':'application/json','User-Agent':'NMIR-q4fs2-metadata-locator/1.0'})
        with urllib.request.urlopen(req,timeout=45) as r:
            body=r.read()
            out.update(http_status=r.status,final_url=r.geturl(),content_type=r.headers.get('Content-Type',''),response_bytes=len(body),response_sha256=hashlib.sha256(body).hexdigest())
    except Exception as e:
        out.update(classification='BLOCKED_0105A6Q4FS2_IUSCHOLARWORKS_TARGET_METADATA_NOT_UNIQUELY_RESOLVED',transport_error=repr(e))
        open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); return
    try:
        d=json.loads(body.decode('utf-8')); out['json_parseable']=True
    except Exception as e:
        out.update(json_parseable=False,classification='BLOCKED_0105A6Q4FS2_IUSCHOLARWORKS_TARGET_METADATA_NOT_UNIQUELY_RESOLVED',json_error=repr(e))
        open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); return
    results=search_results(d)
    out['returned_search_result_count']=len(results)
    title_matches=[]
    for pos,res in enumerate(results):
        obj=indexable(res)
        if not isinstance(obj,dict):
            continue
        md=obj.get('metadata',{}) if isinstance(obj.get('metadata',{}),dict) else {}
        title_vals=[]
        if isinstance(obj.get('name'),str): title_vals.append(obj['name'])
        title_vals += metadata_values(md,('dc.title','title'))
        if not any(norm(v)==norm(TITLE) for v in title_vals):
            continue
        author_vals=metadata_values(md,('contributor.author','creator','author'))
        year_vals=metadata_values(md,('date.issued','issued','date'))
        author_ok=any(norm(v) in AUTHORS for v in author_vals)
        year_ok=any(YEAR == str(v).strip()[:4] for v in year_vals)
        uuid=obj.get('uuid') or obj.get('id')
        title_matches.append({
          'position':pos,'uuid':uuid if isinstance(uuid,str) else None,
          'exact_title_match':True,'author_match':author_ok,'year_match':year_ok,
          'author_values':author_vals,'year_values':year_vals,
        })
    out['exact_title_match_count']=len(title_matches)
    out['matches']=title_matches
    unique=(len(title_matches)==1)
    if unique:
        m=title_matches[0]
        complete=bool(m['author_match'] and m['year_match'] and m['uuid'])
    else:
        complete=False
    out['unique_frozen_identity_match']=complete
    if out.get('http_status')==200 and out.get('json_parseable') and complete:
        out['classification']='PASS_0105A6Q4FS2_IUSCHOLARWORKS_TARGET_METADATA_UNIQUE_MATCH_NONDISCOVERY'
    else:
        out['classification']='BLOCKED_0105A6Q4FS2_IUSCHOLARWORKS_TARGET_METADATA_NOT_UNIQUELY_RESOLVED'
    open(args.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')

if __name__=='__main__': main()
