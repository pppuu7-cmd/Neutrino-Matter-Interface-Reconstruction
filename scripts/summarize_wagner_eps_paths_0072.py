#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, io, json, math, re, tarfile, urllib.request
from collections import defaultdict

URL='https://arxiv.org/e-print/1207.2442'; TARGET='WEP_figure6.eps'
NUM=r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?'
TOK_RE=re.compile(rf'({NUM}|C|M|L|SN|SL|N|CFN)')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-0072a-path-parser/1.0'})
    with urllib.request.urlopen(req,timeout=60) as r: body=r.read()
    with tarfile.open(fileobj=io.BytesIO(body),mode='r:gz') as tf: eps=tf.extractfile(tf.getmember(TARGET)).read()
    text=eps.decode('latin-1',errors='replace')
    toks=TOK_RE.findall(text)
    stack=[]; color=(0.0,0.0,0.0); width=None; path=[]; paths=[]
    def popn(n):
        nonlocal stack
        if len(stack)<n: return None
        vals=stack[-n:]; del stack[-n:]; return vals
    def flush():
        nonlocal path
        if len(path)>=2:
            xs=[p[0] for p in path]; ys=[p[1] for p in path]
            paths.append({'color':list(color),'linewidth':width,'n':len(path),'bbox':[min(xs),min(ys),max(xs),max(ys)],'first':list(path[0]),'last':list(path[-1]),'points':path[:]})
        path=[]
    for t in toks:
        if re.fullmatch(NUM,t): stack.append(float(t)); continue
        if t=='C':
            vals=popn(3)
            if vals is not None: color=tuple(vals)
        elif t=='SL':
            vals=popn(1)
            if vals is not None: width=vals[0]
        elif t=='M':
            vals=popn(2)
            if vals is not None:
                if path: flush()
                path=[tuple(vals)]
        elif t=='L':
            vals=popn(2)
            if vals is not None:
                if not path: path=[tuple(vals)]
                else: path.append(tuple(vals))
        elif t in ('SN','N','CFN'):
            flush()
    flush()
    by=defaultdict(list)
    for i,p in enumerate(paths): by[tuple(p['color'])].append((i,p))
    colors=[]
    for c, items in by.items():
        xs=[]; ys=[]
        for _,p in items:
            xs += [p['bbox'][0],p['bbox'][2]]; ys += [p['bbox'][1],p['bbox'][3]]
        longest=sorted(items,key=lambda z:z[1]['n'],reverse=True)[:20]
        colors.append({'color':list(c),'path_count':len(items),'bbox':[min(xs),min(ys),max(xs),max(ys)],'longest_paths':[{'index':i,'n':p['n'],'linewidth':p['linewidth'],'bbox':p['bbox'],'first':p['first'],'last':p['last']} for i,p in longest]})
    # Keep full points only for long non-black candidate curves; black is dominated by axes/text glyphs.
    candidates=[]
    for i,p in enumerate(paths):
        if tuple(p['color'])!=(0.0,0.0,0.0) and p['n']>=10:
            candidates.append({'index':i,**p})
    out={'iteration':'0072a','eps_sha256':hashlib.sha256(eps).hexdigest(),'path_count':len(paths),'colors':sorted(colors,key=lambda x:(x['color'])),'candidate_nonblack_paths':candidates}
    with open(args.output,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({'path_count':len(paths),'colors':[(x['color'],x['path_count']) for x in colors],'candidate_nonblack_count':len(candidates)},sort_keys=True))
if __name__=='__main__': main()
