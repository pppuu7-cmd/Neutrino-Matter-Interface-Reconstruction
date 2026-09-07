#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, io, json, math, tarfile, urllib.request
from collections import defaultdict

from summarize_wagner_eps_paths_0072 import URL, TARGET, parse_paths

EPS_SHA='4adafc21e896aa3e19490a586e9249fb9b7c947ad9cbe9efd3416d5e00466882'
BOX=(1.681,6.681,0.844,4.844)
WIDTH=0.010
CHAIN_TOL=1e-9
ROUNDTRIP_TOL=1e-9
G_CONST=2.70463357586823e-19
HBARC=1.973269804e-7
COLORS={
    'blue':(0.0,0.0,1.0),
    'red':(1.0,0.0,0.0),
    'orange':(1.0,0.5,0.0),
    'magenta':(1.0,0.0,1.0),
}
EXPECTED={'blue':3,'red':1,'orange':1,'magenta':2}


def dist(a,b): return max(abs(a[0]-b[0]),abs(a[1]-b[1]))

def inside(p):
    x0,x1,y0,y1=BOX; x,y=p
    return x0-1e-9<=x<=x1+1e-9 and y0-1e-9<=y<=y1+1e-9

def chain_family(records):
    chains=[]; cur=None
    for r in records:
        a=tuple(r['first']); b=tuple(r['last'])
        if cur is not None and dist(cur['points'][-1],a)<=CHAIN_TOL:
            cur['points'].append(b); cur['segment_indices'].append(r['index'])
        else:
            if cur is not None: chains.append(cur)
            cur={'points':[a,b],'segment_indices':[r['index']]}
    if cur is not None: chains.append(cur)
    return chains

def bbox(points):
    xs=[p[0] for p in points]; ys=[p[1] for p in points]
    return [min(xs),min(ys),max(xs),max(ys)]

def monotonic_x(points):
    ds=[points[i+1][0]-points[i][0] for i in range(len(points)-1)]
    return all(d>=-1e-12 for d in ds) or all(d<=1e-12 for d in ds)

def interp_y(points,x):
    pts=points if points[0][0]<=points[-1][0] else list(reversed(points))
    for i in range(len(pts)-1):
        x0,y0=pts[i]; x1,y1=pts[i+1]
        if min(x0,x1)-1e-12<=x<=max(x0,x1)+1e-12:
            if abs(x1-x0)<=1e-15: return 0.5*(y0+y1)
            t=(x-x0)/(x1-x0); return y0+t*(y1-y0)
    raise ValueError('x outside chain')

def transform_point(p,tr):
    x,y=p
    lx=tr['a_x']*x+tr['b_x']; la=tr['a_y']*y+tr['b_y']
    lam=10.0**lx; alpha=10.0**la
    return {'eps':[x,y],'log10_lambda_m':lx,'lambda_m':lam,'log10_abs_alpha_tilde':la,'abs_alpha_tilde':alpha,
            'm_V_eV':HBARC/lam,'g_BL_abs':G_CONST*math.sqrt(alpha)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--axis-calibration',required=True); ap.add_argument('--output',required=True); args=ap.parse_args()
    cal=json.load(open(args.axis_calibration,encoding='utf-8'))
    if cal.get('classification')!='PASS_WAGNER_AXIS_CALIBRATION': raise SystemExit('INFRASTRUCTURE_FAIL prerequisite axis calibration is not PASS')
    tr=cal['transform']
    req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-0072c-curve-extractor/1.0'})
    with urllib.request.urlopen(req,timeout=60) as r: body=r.read()
    with tarfile.open(fileobj=io.BytesIO(body),mode='r:gz') as tf: eps=tf.extractfile(tf.getmember(TARGET)).read()
    sha=hashlib.sha256(eps).hexdigest()
    if sha!=EPS_SHA: raise SystemExit('INFRASTRUCTURE_FAIL EPS hash mismatch')
    paths=parse_paths(eps.decode('latin-1',errors='replace'))

    records=defaultdict(list)
    for i,p in enumerate(paths):
        c=tuple(p['color']); fam=None
        for k,v in COLORS.items():
            if c==v: fam=k; break
        if fam is None or p['n']!=2 or p['linewidth'] is None or abs(p['linewidth']-WIDTH)>1e-12: continue
        if inside(tuple(p['first'])) and inside(tuple(p['last'])):
            records[fam].append({'index':i,'first':p['first'],'last':p['last']})

    long={}; dropped={}; topology={}
    for fam in COLORS:
        raw=chain_family(records[fam]); keep=[]; drop=[]
        for ch in raw:
            ch['n_segments']=len(ch['segment_indices']); ch['bbox']=bbox(ch['points']); ch['x_monotonic']=monotonic_x(ch['points'])
            (keep if ch['n_segments']>=3 else drop).append(ch)
        long[fam]=keep; dropped[fam]=drop
        topology[fam]={'retained_chain_count':len(keep),'dropped_fragment_count':len(drop),'expected_chain_count':EXPECTED[fam],
                       'segment_count':len(records[fam])}

    topology_ok=all(len(long[f])==EXPECTED[f] for f in EXPECTED)
    identity={}; identity_ok=topology_ok

    if len(long['blue'])==3 and all(ch['x_monotonic'] for ch in long['blue']):
        lo=max(ch['bbox'][0] for ch in long['blue']); hi=min(ch['bbox'][2] for ch in long['blue'])
        if hi<=lo:
            identity_ok=False; identity['blue']={'pass':False,'reason':'no common x overlap'}
        else:
            xs=[lo+(hi-lo)*i/20.0 for i in range(21)]
            orders=[]
            for x in xs:
                ys=[interp_y(ch['points'],x) for ch in long['blue']]
                orders.append(sorted(range(3),key=lambda i:ys[i],reverse=True))
            stable=all(o==orders[0] for o in orders)
            if not stable: identity_ok=False
            if stable:
                ord0=orders[0]
                labels={ord0[0]:'EW99',ord0[1]:'EW94',ord0[2]:'EW'}
            else: labels={}
            identity['blue']={'pass':stable,'common_x_eps':[lo,hi],'sample_orders':orders,'chain_label_by_index':{str(k):v for k,v in labels.items()}}
    else:
        identity_ok=False; identity['blue']={'pass':False,'reason':'expected 3 x-monotonic blue chains'}

    if len(long['red'])==1: identity['red']={'pass':True,'chain_label_by_index':{'0':'Princeton'}}
    else: identity_ok=False; identity['red']={'pass':False}
    if len(long['orange'])==1: identity['orange']={'pass':True,'chain_label_by_index':{'0':'Moscow'}}
    else: identity_ok=False; identity['orange']={'pass':False}
    if len(long['magenta'])==2:
        means=[sum(p[0] for p in ch['points'])/len(ch['points']) for ch in long['magenta']]
        order=sorted(range(2),key=lambda i:means[i])
        identity['magenta']={'pass':True,'mean_x_eps':means,'chain_label_by_index':{str(order[0]):'LLR_precession_inverse_square',str(order[1]):'LLR_differential_acceleration'}}
    else:
        identity_ok=False; identity['magenta']={'pass':False}

    labels={}
    for fam in ('blue','red','orange','magenta'):
        for k,v in identity.get(fam,{}).get('chain_label_by_index',{}).items(): labels[(fam,int(k))]=v

    transformed={}; max_rt=0.0
    for fam,chains in long.items():
        for j,ch in enumerate(chains):
            label=labels.get((fam,j),f'UNRESOLVED_{fam}_{j}')
            pts=[]
            for p in ch['points']:
                q=transform_point(p,tr); pts.append(q)
                xr=(q['log10_lambda_m']-tr['b_x'])/tr['a_x']; yr=(q['log10_abs_alpha_tilde']-tr['b_y'])/tr['a_y']
                max_rt=max(max_rt,abs(xr-p[0]),abs(yr-p[1]))
            transformed[label]={'family':fam,'chain_index':j,'n_segments':ch['n_segments'],'eps_bbox':ch['bbox'],'points':pts}
    roundtrip_ok=max_rt<=ROUNDTRIP_TOL
    if topology_ok and identity_ok and roundtrip_ok:
        classification='PASS_WAGNER_B_MINUS_L_VECTOR_CONTOURS_MATERIALIZED'
    elif any(not k.startswith('UNRESOLVED_') for k in transformed) and roundtrip_ok:
        classification='PARTIAL_PASS_WAGNER_VECTOR_CURVES'
    else:
        classification='SCIENTIFIC_FAIL_VECTOR_CURVE_IDENTITY'

    out={'iteration':'0072c','classification':classification,'eps_sha256':sha,'left_panel_box':list(BOX),'curve_width':WIDTH,
         'topology':topology,'identity':identity,'topology_pass':topology_ok,'identity_pass':identity_ok,
         'roundtrip_max_abs_eps':max_rt,'roundtrip_tolerance_eps':ROUNDTRIP_TOL,'roundtrip_pass':roundtrip_ok,
         'curves':transformed,
         'dropped_fragments':{f:[{'n_segments':c['n_segments'],'bbox':c['bbox'],'segment_indices':c['segment_indices']} for c in cs] for f,cs in dropped.items()},
         'exclusion_sense':'above each validated 95% CL upper-bound curve in |alpha_tilde|',
         'guard':'Primary Wagner curve family only; no global B-L allowed region and no NMIR enhancement calculation authorized.'}
    with open(args.output,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({'classification':classification,'topology':topology,'identity':identity,'roundtrip_max_abs_eps':max_rt,'labels':sorted(transformed)},sort_keys=True))

if __name__=='__main__': main()
