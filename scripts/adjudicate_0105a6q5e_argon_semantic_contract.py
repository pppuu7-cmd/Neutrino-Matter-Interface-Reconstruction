#!/usr/bin/env python3
import argparse, hashlib, io, json, zipfile
from pathlib import Path

PREREG='7e414409b9f79da0a24090ef5ce3583d67a30e09'
GATE='NMIR-V2-0105A6Q5E'
Q5D_ZIP_SHA='269ff3984ff40b7010f35b755b4f1ef5207ba82ae285d08ef035b29b1d30a178'
Q5D_INNER_SHA='0c45f7cbba28c5a3a21222d45ff3bd6260ad9849629e71c3be9c82ddc875a324'
Q5D_CLASS='PASS_0105A6Q5D_BOUNDED_SEMANTIC_EVIDENCE_INVENTORY_COMPLETE_NONDISCOVERY'
Q5D_PREREG='b0d5a15e8bcba061fc2c3000fff0e299828caf72'
Q5D_HEAD='36fd99270bf11aec076849c6560a4315c3a4a72f'

def cat_windows(d,cat):
    out=[]
    for fn,cats in d['evidence'].items():
        for w in cats[cat]['windows']:
            text='\n'.join(x['text'] for x in w['lines'])
            out.append({'file':fn,'hit_line':w['hit_line'],'start_line':w['start_line'],'end_line':w['end_line'],'text':text})
    return out

def joined(ws): return '\n'.join(w['text'] for w in ws).casefold()
def refs(ws, needle=None):
    rr=[]
    for w in ws:
        if needle is None or needle.casefold() in w['text'].casefold():
            rr.append({'file':w['file'],'hit_line':w['hit_line'],'start_line':w['start_line'],'end_line':w['end_line']})
    return rr

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--q5d-zip',required=True); ap.add_argument('--output',required=True); ap.add_argument('--git-sha',required=True); a=ap.parse_args()
    zbytes=Path(a.q5d_zip).read_bytes(); zsha=hashlib.sha256(zbytes).hexdigest()
    out={'gate':GATE,'preregistration_commit':PREREG,'git_sha':a.git_sha,'q5d_artifact_zip_sha256':zsha,
         'pseudo_data_generated':False,'likelihood_evaluated':False,'fit_executed':False,'nuisance_profiled':False,'systematic_monte_carlo_executed':False,'observed_bsm_residual_inspected':False,
         'systematic_monte_carlo_execution_permission_percent':0,'observed_bsm_residual_permission_percent':0}
    try:
        if zsha != Q5D_ZIP_SHA: raise ValueError('q5d zip digest mismatch')
        with zipfile.ZipFile(io.BytesIO(zbytes)) as z: raw=z.read('result.json')
        inner=hashlib.sha256(raw).hexdigest(); out['q5d_inner_sha256']=inner
        if inner != Q5D_INNER_SHA: raise ValueError('q5d inner digest mismatch')
        d=json.loads(raw)
        if d.get('classification') != Q5D_CLASS or d.get('preregistration_commit') != Q5D_PREREG or d.get('git_sha') != Q5D_HEAD:
            raise ValueError('q5d provenance/class mismatch')
        if not all(x.get('exact_identity_match') for x in d.get('files',{}).values()) or len(d.get('files',{})) != 4:
            raise ValueError('q5d source identity invalid')

        e1=cat_windows(d,'E1'); e3=cat_windows(d,'E3'); e4=cat_windows(d,'E4'); e5=cat_windows(d,'E5')
        s1,s3,s4,s5=map(joined,(e1,e3,e4,e5))

        # F1: an explicit elementary count law must be present; generic likelihood language is insufficient.
        law_markers=['poisson','multinomial','fixed total','fixed-total','binomial','categorical']
        f1_hits=[m for m in law_markers if m in s1]
        f1='PASS_EXPLICIT' if f1_hits else 'BLOCKED_INCOMPLETE_OR_AMBIGUOUS'

        # F4: require an explicit application mode, not merely PDF/systematic labels.
        continuous=['morph','interpol']
        discrete=['excursion','plus1','minus1','+1sigma','-1sigma','+1 sigma','-1 sigma','separate fit','alternate fit','alternative fit']
        f4_mode=[m for m in continuous+discrete if m in s3]
        f4='PASS_EXPLICIT' if f4_mode else 'BLOCKED_INCOMPLETE_OR_AMBIGUOUS'

        # F6: correlation/independence evidence must be explicitly tied to nuisance/shape/systematic/PDF treatment.
        rel=['nuisance','shape','systematic','pdf']
        mode=['simultaneous','correlation','correlated','covariance','independent','joint','profile','separate']
        f6_contexts=[]
        for w in e4:
            t=w['text'].casefold()
            if any(r in t for r in rel) and any(m in t for m in mode): f6_contexts.append(w)
        f6='PASS_EXPLICIT' if f6_contexts else 'BLOCKED_INCOMPLETE_OR_AMBIGUOUS'

        has3152='3152' in s5; has3154='3154' in s5
        if not (has3152 and has3154):
            f7='NOT_APPLICABLE_NO_COMPETING_ANCHORS'
        else:
            precedence=['precedence','anchor','nominal','central']
            f7='PASS_EXPLICIT' if any(p in s5 for p in precedence) else 'BLOCKED_INCOMPLETE_OR_AMBIGUOUS'

        items={'F1':{'status':f1,'explicit_law_markers':f1_hits,'evidence_refs':refs(e1)},
               'F4':{'status':f4,'explicit_application_markers':f4_mode,'evidence_refs':refs(e3)},
               'F6':{'status':f6,'relevant_explicit_context_count':len(f6_contexts),'evidence_refs':refs(f6_contexts) if f6_contexts else refs(e4)},
               'F7':{'status':f7,'has_3152':has3152,'has_3154':has3154,'evidence_3152':refs(e5,'3152'),'evidence_3154':refs(e5,'3154')}}
        out['items']=items
        required=(f1=='PASS_EXPLICIT' and f4=='PASS_EXPLICIT' and f6=='PASS_EXPLICIT' and f7 in ('PASS_EXPLICIT','NOT_APPLICABLE_NO_COMPETING_ANCHORS'))
        out['classification']='PASS_0105A6Q5E_ARGON_RELEASE_SEMANTIC_CONTRACT_SUFFICIENT_NONDISCOVERY' if required else 'BLOCKED_0105A6Q5E_ARGON_RELEASE_SEMANTIC_CONTRACT_INCOMPLETE'
    except Exception as e:
        out['error']=type(e).__name__+': '+str(e); out['classification']='BLOCKED_0105A6Q5E_PARENT_EVIDENCE_INVALID'
    payload=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode(); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_bytes(payload)
    print('CLASSIFICATION='+out['classification']); print('RESULT_SHA256='+hashlib.sha256(payload).hexdigest()); print('ITEMS='+json.dumps(out.get('items',{}),sort_keys=True))
if __name__=='__main__': main()
