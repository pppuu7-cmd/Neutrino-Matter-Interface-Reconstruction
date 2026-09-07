#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math

MARGIN=1e-6
N=101
ENDPOINT_TOL=1e-9


def interp(points,x):
    pts=[tuple(p['eps']) for p in points]
    if pts[0][0]>pts[-1][0]: pts=list(reversed(pts))
    for i in range(len(pts)-1):
        x0,y0=pts[i]; x1,y1=pts[i+1]
        if x0-ENDPOINT_TOL<=x<=x1+ENDPOINT_TOL:
            if abs(x1-x0)<=1e-15: return 0.5*(y0+y1)
            t=(x-x0)/(x1-x0); return y0+t*(y1-y0)
    raise ValueError(f'x={x} outside chain')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--curves-json',required=True); ap.add_argument('--output',required=True); args=ap.parse_args()
    d=json.load(open(args.curves_json,encoding='utf-8'))
    blue=[]
    for name,c in d['curves'].items():
        if c.get('family')=='blue':
            blue.append({'old_name':name,'chain_index':c['chain_index'],'curve':c,'xmin':c['eps_bbox'][0],'xmax':c['eps_bbox'][2]})
    blue=sorted(blue,key=lambda q:q['chain_index'])
    if len(blue)!=4 or d['topology']['blue']['dropped_fragment_count']!=0:
        out={'iteration':'0072d','classification':'SCIENTIFIC_FAIL_WAGNER_BLUE_IDENTITY','reason':'requires exactly 4 retained blue chains and zero dropped fragments','blue_count':len(blue)}
    else:
        pairwise=[]; above={q['chain_index']:set() for q in blue}; below={q['chain_index']:set() for q in blue}; failures=[]
        for ia in range(len(blue)):
            for ib in range(ia+1,len(blue)):
                a,b=blue[ia],blue[ib]
                lo=max(a['xmin'],b['xmin']); hi=min(a['xmax'],b['xmax'])
                if hi < lo-ENDPOINT_TOL:
                    pairwise.append({'i':a['chain_index'],'j':b['chain_index'],'overlap':None,'status':'disjoint'})
                    continue
                if hi-lo<=ENDPOINT_TOL:
                    pairwise.append({'i':a['chain_index'],'j':b['chain_index'],'overlap':[lo,hi],'status':'endpoint_only'})
                    continue
                diffs=[]
                for k in range(N):
                    x=lo+(hi-lo)*k/(N-1)
                    diffs.append(interp(a['curve']['points'],x)-interp(b['curve']['points'],x))
                mind=min(diffs); maxd=max(diffs)
                if mind>=MARGIN:
                    status='i_above_j'; above[a['chain_index']].add(b['chain_index']); below[b['chain_index']].add(a['chain_index'])
                elif maxd<=-MARGIN:
                    status='j_above_i'; above[b['chain_index']].add(a['chain_index']); below[a['chain_index']].add(b['chain_index'])
                else:
                    status='crossing_or_tie'; failures.append([a['chain_index'],b['chain_index']])
                pairwise.append({'i':a['chain_index'],'j':b['chain_index'],'overlap':[lo,hi],'status':status,'min_y_i_minus_j':mind,'max_y_i_minus_j':maxd})

        allidx={q['chain_index'] for q in blue}
        top=[i for i in allidx if above[i]==(allidx-{i})]
        bottom=[i for i in allidx if below[i]==(allidx-{i})]
        # The literal all-pairs graph cannot compare disjoint EW94 components. For EW99/EW, require dominance versus every chain with which it overlaps;
        # because the two EW94 pieces are disjoint from each other, candidates are evaluated against their three actual overlaps.
        overlap_neighbors={i:set() for i in allidx}
        for p in pairwise:
            if p['status'] not in ('disjoint','endpoint_only'):
                overlap_neighbors[p['i']].add(p['j']); overlap_neighbors[p['j']].add(p['i'])
        top=[i for i in allidx if len(overlap_neighbors[i])==3 and above[i]==overlap_neighbors[i]]
        bottom=[i for i in allidx if len(overlap_neighbors[i])==3 and below[i]==overlap_neighbors[i]]
        labels={}; conditions={'pairwise_failures':failures,'top_candidates':top,'bottom_candidates':bottom}
        ok=(not failures and len(top)==1 and len(bottom)==1 and top[0]!=bottom[0])
        if ok:
            labels[top[0]]='EW99'; labels[bottom[0]]='EW'
            rem=sorted(allidx-{top[0],bottom[0]})
            # remaining pair must be disjoint/endpoint-only and each must be between top and bottom wherever overlapping
            p_rem=next(p for p in pairwise if {p['i'],p['j']}==set(rem))
            rem_disjoint=p_rem['status'] in ('disjoint','endpoint_only')
            between=True
            for r in rem:
                if not (top[0] in below[r] and bottom[0] in above[r]): between=False
            conditions['remaining_components']=rem; conditions['remaining_disjoint']=rem_disjoint; conditions['remaining_between']=between
            ok=ok and rem_disjoint and between
            if ok:
                means=[]
                for r in rem:
                    c=next(q for q in blue if q['chain_index']==r)['curve']
                    means.append((sum(p['eps'][0] for p in c['points'])/len(c['points']),r))
                means=sorted(means)
                labels[means[0][1]]='EW94_short'; labels[means[1][1]]='EW94_long'
                conditions['ew94_mean_x_order']=means
        classification='PASS_WAGNER_BLUE_IDENTITIES_RESOLVED' if ok else 'SCIENTIFIC_FAIL_WAGNER_BLUE_IDENTITY'
        relabelled={}
        if ok:
            for q in blue:
                lab=labels[q['chain_index']]
                relabelled[lab]={'chain_index':q['chain_index'],'source_old_name':q['old_name'],'n_segments':q['curve']['n_segments'],'eps_bbox':q['curve']['eps_bbox'],'points':q['curve']['points']}
        out={'iteration':'0072d','classification':classification,'frozen_margin_eps_y':MARGIN,'samples_per_overlap':N,
             'pairwise_orders':pairwise,'conditions':conditions,'chain_labels':{str(k):v for k,v in labels.items()},
             'resolved_curves':relabelled,
             'guard':'Semantic identity resolution only. 0072b physical points unchanged; EW94_short and EW94_long remain disconnected and must never be interpolated across their gap.'}
    with open(args.output,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({k:out.get(k) for k in ['classification','chain_labels','conditions','pairwise_orders']},indent=2,sort_keys=True))

if __name__=='__main__': main()
