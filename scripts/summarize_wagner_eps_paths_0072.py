#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, io, json, re, tarfile, urllib.request
from collections import defaultdict

URL='https://arxiv.org/e-print/1207.2442'; TARGET='WEP_figure6.eps'
NUM=r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?'
WORD_RE=re.compile(rf'(?<!\S)({NUM}|[A-Za-z][A-Za-z0-9]*)(?!\S)')
DRAW_OPS={'C','M','L','SN','SL','N','CFN'}
ARITY={'C':3,'M':2,'L':2,'SL':1,'translate':2,'scale':2,'setlinecap':1,'setlinejoin':1,'setgray':1,'setmiterlimit':1}
ZERO_ARITY={'SN','N','CFN','gsave','grestore','showpage','stroke','newpath','closepath'}

def _code_lines(text: str):
    for line in text.splitlines():
        stripped=line.lstrip()
        if not stripped or stripped.startswith('%'):
            continue
        # Skip PostScript literal-string/definition lines entirely: figure labels are
        # drawn as geometry elsewhere and these definitions must not become operators.
        if stripped.startswith('/') and ('(' in stripped or '{' in stripped):
            continue
        if '%' in line: line=line.split('%',1)[0]
        if line.strip(): yield line

def raw_tokens(text: str) -> list[str]:
    toks=[]
    for line in _code_lines(text): toks.extend(WORD_RE.findall(line))
    return toks

def tokenize_eps(text: str) -> list[str]:
    """Regression-facing drawing-token stream.

    Keeps only numeric operands and the small drawing vocabulary. Parsing itself uses
    raw_tokens() so nuisance operators can consume their operands fail-closed.
    """
    return [t for t in raw_tokens(text) if re.fullmatch(NUM,t) or t in DRAW_OPS]

def parse_paths(text: str):
    stack=[]; color=(0.0,0.0,0.0); width=None; path=[]; paths=[]
    def popn(n):
        if len(stack)<n:
            stack.clear(); return None
        vals=stack[-n:]; del stack[-n:]; return vals
    def flush():
        nonlocal path
        if len(path)>=2:
            xs=[p[0] for p in path]; ys=[p[1] for p in path]
            paths.append({'color':list(color),'linewidth':width,'n':len(path),'bbox':[min(xs),min(ys),max(xs),max(ys)],'first':list(path[0]),'last':list(path[-1]),'points':path[:]})
        path=[]
    for t in raw_tokens(text):
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
            flush(); stack.clear()
        elif t in ARITY:
            popn(ARITY[t])
        elif t in ZERO_ARITY:
            if t in ('stroke','newpath','closepath'): flush()
            stack.clear()
        else:
            stack.clear()
    flush(); return paths

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    req=urllib.request.Request(URL,headers={'User-Agent':'NMIR-0072a-path-parser/1.3'})
    with urllib.request.urlopen(req,timeout=60) as r: body=r.read()
    with tarfile.open(fileobj=io.BytesIO(body),mode='r:gz') as tf: eps=tf.extractfile(tf.getmember(TARGET)).read()
    text=eps.decode('latin-1',errors='replace'); paths=parse_paths(text)
    by=defaultdict(list)
    for i,p in enumerate(paths): by[tuple(p['color'])].append((i,p))
    colors=[]
    for c, items in by.items():
        xs=[]; ys=[]
        for _,p in items: xs += [p['bbox'][0],p['bbox'][2]]; ys += [p['bbox'][1],p['bbox'][3]]
        longest=sorted(items,key=lambda z:z[1]['n'],reverse=True)[:20]
        colors.append({'color':list(c),'path_count':len(items),'bbox':[min(xs),min(ys),max(xs),max(ys)],'longest_paths':[{'index':i,'n':p['n'],'linewidth':p['linewidth'],'bbox':p['bbox'],'first':p['first'],'last':p['last']} for i,p in longest]})
    candidates=[]
    for i,p in enumerate(paths):
        if tuple(p['color'])!=(0.0,0.0,0.0) and p['n']>=10:
            candidates.append({'index':i,**p})
    out={'iteration':'0072a','parser_version':'1.3','eps_sha256':hashlib.sha256(eps).hexdigest(),'path_count':len(paths),'colors':sorted(colors,key=lambda x:(x['color'])),'candidate_nonblack_paths':candidates}
    with open(args.output,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({'path_count':len(paths),'colors':[(x['color'],x['path_count']) for x in colors],'candidate_nonblack_count':len(candidates)},sort_keys=True))
if __name__=='__main__': main()
