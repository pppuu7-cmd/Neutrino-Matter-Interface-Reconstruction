#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--curves-json',required=True); ap.add_argument('--output',required=True); args=ap.parse_args()
    d=json.load(open(args.curves_json,encoding='utf-8'))
    curves=[]
    for name,c in sorted(d['curves'].items(), key=lambda kv: kv[1].get('chain_index',999)):
        if c.get('family')!='blue': continue
        pts=c['points']; eps=[p['eps'] for p in pts]
        xs=[p[0] for p in eps]; ys=[p[1] for p in eps]
        lam=[p['lambda_m'] for p in pts]; alp=[p['abs_alpha_tilde'] for p in pts]
        mv=[p['m_V_eV'] for p in pts]; g=[p['g_BL_abs'] for p in pts]
        curves.append({
            'source_name':name,
            'chain_index':c['chain_index'],
            'n_segments':c['n_segments'],
            'n_vertices':len(pts),
            'eps_bbox':c['eps_bbox'],
            'first_eps':eps[0], 'last_eps':eps[-1],
            'x_direction':'increasing' if xs[-1]>=xs[0] else 'decreasing',
            'x_min':min(xs),'x_max':max(xs),'y_min':min(ys),'y_max':max(ys),
            'lambda_m_min':min(lam),'lambda_m_max':max(lam),
            'alpha_min':min(alp),'alpha_max':max(alp),
            'm_V_eV_min':min(mv),'m_V_eV_max':max(mv),
            'g_BL_min':min(g),'g_BL_max':max(g),
            'first_physical':{k:pts[0][k] for k in ['lambda_m','abs_alpha_tilde','m_V_eV','g_BL_abs']},
            'last_physical':{k:pts[-1][k] for k in ['lambda_m','abs_alpha_tilde','m_V_eV','g_BL_abs']},
        })
    gaps=[]
    for i,a in enumerate(curves):
        for j,b in enumerate(curves):
            if i>=j: continue
            pairs=[('a_last_b_first',a['last_eps'],b['first_eps']),('a_first_b_last',a['first_eps'],b['last_eps']),('a_last_b_last',a['last_eps'],b['last_eps']),('a_first_b_first',a['first_eps'],b['first_eps'])]
            best=min(pairs,key=lambda z:max(abs(z[1][0]-z[2][0]),abs(z[1][1]-z[2][1])))
            gaps.append({'chain_i':a['chain_index'],'chain_j':b['chain_index'],'pair':best[0],
                         'dx':abs(best[1][0]-best[2][0]),'dy':abs(best[1][1]-best[2][1]),
                         'chebyshev_eps':max(abs(best[1][0]-best[2][0]),abs(best[1][1]-best[2][1]))})
    out={'iteration':'0072d-diagnostic','parent_classification':d['classification'],'blue_chain_count':len(curves),
         'blue_chains':curves,'nearest_endpoint_gaps':sorted(gaps,key=lambda q:q['chebyshev_eps']),
         'guard':'Structural diagnostic only. No blue identity, merging, dropping, envelope selection, or scientific reclassification is performed.'}
    with open(args.output,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
