#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, io, json, math, tarfile, urllib.request
from collections import defaultdict

from summarize_wagner_eps_paths_0072 import URL, TARGET, parse_paths

EPS_SHA='4adafc21e896aa3e19490a586e9249fb9b7c947ad9cbe9efd3416d5e00466882'
BLACK=(0.0,0.0,0.0)
AXIS_WIDTH=0.011
TOL=5e-7


def close(a,b,tol=TOL): return abs(a-b) <= tol

def seg(p):
    if p['n'] != 2: return None
    x0,y0=p['first']; x1,y1=p['last']
    return x0,y0,x1,y1,abs(x1-x0),abs(y1-y0)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-0072a-axis-extractor/1.0'})
    with urllib.request.urlopen(req,timeout=60) as r: body=r.read()
    with tarfile.open(fileobj=io.BytesIO(body),mode='r:gz') as tf: eps=tf.extractfile(tf.getmember(TARGET)).read()
    sha=hashlib.sha256(eps).hexdigest()
    if sha != EPS_SHA: raise SystemExit(f'FAIL_CLOSED EPS SHA mismatch {sha}')
    paths=parse_paths(eps.decode('latin-1',errors='replace'))

    black=[]
    for i,p in enumerate(paths):
        if tuple(p['color']) != BLACK: continue
        s=seg(p)
        if s is None: continue
        x0,y0,x1,y1,dx,dy=s
        black.append({'index':i,'linewidth':p['linewidth'],'first':[x0,y0],'last':[x1,y1],'dx':dx,'dy':dy})

    # Frame candidates are long, axis-width, exactly horizontal/vertical black vector segments.
    horiz=[]; vert=[]
    for q in black:
        if q['linewidth'] is None or abs(q['linewidth']-AXIS_WIDTH)>1e-6: continue
        x0,y0=q['first']; x1,y1=q['last']; dx=q['dx']; dy=q['dy']
        if dy <= TOL and dx >= 4.5:
            horiz.append({**q,'xmin':min(x0,x1),'xmax':max(x0,x1),'y':0.5*(y0+y1)})
        if dx <= TOL and dy >= 3.5:
            vert.append({**q,'x':0.5*(x0+x1),'ymin':min(y0,y1),'ymax':max(y0,y1)})

    # Infer the left plotting box only from a 5-ish-unit horizontal frame wholly left of x=6.9.
    left_h=[h for h in horiz if h['xmax'] <= 6.9 and 4.8 <= h['xmax']-h['xmin'] <= 5.2]
    if not left_h:
        raise SystemExit('FAIL_CLOSED no left-panel horizontal frame candidate')
    # The repeated top/bottom frame segments must agree in x extent.
    groups=defaultdict(list)
    for h in left_h: groups[(round(h['xmin'],6),round(h['xmax'],6))].append(h)
    extent,hs=max(groups.items(),key=lambda kv:len(kv[1]))
    xlo,xhi=extent
    ys=sorted({round(h['y'],6) for h in hs})
    if len(ys)<2:
        # Supplement matching-x vertical frame extents if only one horizontal side is explicit.
        vmatch=[v for v in vert if close(v['x'],xlo,2e-6) or close(v['x'],xhi,2e-6)]
        yvals=[]
        for v in vmatch: yvals += [v['ymin'],v['ymax']]
        if yvals: ys=[round(min(yvals),6),round(max(yvals),6)]
    if len(ys)<2: raise SystemExit('FAIL_CLOSED cannot infer left-panel y extent')
    ylo,yhi=min(ys),max(ys)

    # Axis ticks are short black axis-width segments touching one of the inferred frame sides.
    xticks=[]
    yticks=[]
    for q in black:
        if q['linewidth'] is None or abs(q['linewidth']-AXIS_WIDTH)>1e-6: continue
        x0,y0=q['first']; x1,y1=q['last']; dx=q['dx']; dy=q['dy']
        if dx<=TOL and 0.02 <= dy <= 0.15 and xlo-TOL <= x0 <= xhi+TOL:
            if close(y0,ylo,2e-6) or close(y1,ylo,2e-6):
                xticks.append({'index':q['index'],'x':round(x0,6),'length':round(dy,6),'side':'bottom'})
            elif close(y0,yhi,2e-6) or close(y1,yhi,2e-6):
                xticks.append({'index':q['index'],'x':round(x0,6),'length':round(dy,6),'side':'top'})
        if dy<=TOL and 0.02 <= dx <= 0.15 and ylo-TOL <= y0 <= yhi+TOL:
            if close(x0,xlo,2e-6) or close(x1,xlo,2e-6):
                yticks.append({'index':q['index'],'y':round(y0,6),'length':round(dx,6),'side':'left'})
            elif close(x0,xhi,2e-6) or close(x1,xhi,2e-6):
                yticks.append({'index':q['index'],'y':round(y0,6),'length':round(dx,6),'side':'right'})

    def unique_ticks(rows,key,side):
        d={}
        for r in rows:
            if r['side']!=side: continue
            k=r[key]
            # Preserve the longest coincident tick if duplicated by redraw.
            if k not in d or r['length']>d[k]['length']: d[k]=r
        return [d[k] for k in sorted(d)]

    xb=unique_ticks(xticks,'x','bottom'); xt=unique_ticks(xticks,'x','top')
    yl=unique_ticks(yticks,'y','left'); yr=unique_ticks(yticks,'y','right')

    # Report length clusters rather than deciding major/minor after seeing physical labels.
    def clusters(rows):
        return sorted({round(r['length'],6) for r in rows})

    out={
      'iteration':'0072a', 'extractor_version':'1.0', 'eps_sha256':sha,
      'left_panel_box':{'x_min':xlo,'x_max':xhi,'y_min':ylo,'y_max':yhi},
      'frame_candidates':{'horizontal':horiz,'vertical':vert},
      'ticks':{'bottom':xb,'top':xt,'left':yl,'right':yr},
      'tick_length_clusters':{'bottom':clusters(xb),'top':clusters(xt),'left':clusters(yl),'right':clusters(yr)},
      'guard':'STRUCTURAL VECTOR GEOMETRY ONLY; no physical axis values or contour coordinates are assigned by this script.'
    }
    with open(args.output,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({'box':out['left_panel_box'],'n_bottom':len(xb),'n_top':len(xt),'n_left':len(yl),'n_right':len(yr),'clusters':out['tick_length_clusters']},sort_keys=True))

if __name__=='__main__': main()
