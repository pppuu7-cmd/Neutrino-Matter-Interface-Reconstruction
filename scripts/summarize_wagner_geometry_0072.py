#!/usr/bin/env python3
from __future__ import annotations
import argparse, json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--paths-json',default='data/wagner_eps_paths_0072.json'); ap.add_argument('--output',required=True); args=ap.parse_args()
    d=json.load(open(args.paths_json,encoding='utf-8'))
    colors=[]
    for c in d['colors']:
        colors.append({'color':c['color'],'path_count':c['path_count'],'bbox':c['bbox'],'top_paths':[{'index':p['index'],'n':p['n'],'linewidth':p['linewidth'],'bbox':p['bbox']} for p in c['longest_paths'][:5]]})
    nonblack=[{'index':p['index'],'color':p['color'],'linewidth':p['linewidth'],'n':p['n'],'bbox':p['bbox']} for p in d['candidate_nonblack_paths']]
    out={'iteration':'0072a','source_eps_sha256':d['eps_sha256'],'parser_version':d.get('parser_version'),'color_summary':colors,'long_nonblack_paths':nonblack,'note':'structural diagnostic only; no axis calibration or contour acceptance'}
    with open(args.output,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
