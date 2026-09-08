#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path


def load_base():
    path=Path(__file__).with_name("g9_persistent_global_0090.py")
    spec=importlib.util.spec_from_file_location("g9_0090_base",path)
    if spec is None or spec.loader is None: raise RuntimeError("cannot load 0090 base")
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

base=load_base()
base.CONTRACT="cf8ffbcca69477939430272777f573d94e4b1e24"
AMENDMENT="f4d6538c551d724949089435707137d7155fd6ed"
_original_one_mu=base.one_mu


def exact_point_mu(profile,focal,z,turn,a):
    branches=((base.XMIN,turn),(turn,base.XMAX)); area=0.0; intervals=[]
    for bi,(lo,hi) in enumerate(branches):
        roots=base.invert_many(focal,z,lo,hi,[-a,a])
        pts=sorted(set([lo,hi,*[float(x) for x in roots]]))
        for left,right in zip(pts,pts[1:]):
            mid=0.5*(left+right); yy=abs(float(base.y_bulk(focal,z,[mid])[0]))
            if yy<=a:
                area+=math.pi*base.R**2*(right*right-left*left)
                intervals.append([left,right,bi])
    mu=1.0+area/(math.pi*a*a)
    return mu,{"accepted_area_cm2":area,"accepted_intervals":intervals,"method":"exact_point_annuli","amendment":AMENDMENT}


def one_mu(profile,focal,z,turn,a,s,delta,nr,na):
    if s==0.0 and delta==0.0:
        return exact_point_mu(profile,focal,z,turn,a)
    return _original_one_mu(profile,focal,z,turn,a,s,delta,nr,na)

base.one_mu=one_mu


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--control",type=int,required=True); ap.add_argument("--receiver",type=int,required=True); ap.add_argument("--output",required=True)
    args=ap.parse_args()
    try:
        result=base.run_shard(args.control,args.receiver); result["implementation_amendment"]=AMENDMENT
    except base.Blocked as e:
        result={"status":"BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS","reason":str(e),"control_index":args.control,"receiver_index":args.receiver,"implementation_amendment":AMENDMENT}
    except base.ScientificFail as e:
        result={"status":"SCIENTIFIC_FAIL_G9_PERSISTENT_GLOBAL_INVARIANT","reason":str(e),"control_index":args.control,"receiver_index":args.receiver,"implementation_amendment":AMENDMENT}
    except Exception as e:
        result={"status":"INFRASTRUCTURE_FAIL_G9_0090","reason":repr(e),"control_index":args.control,"receiver_index":args.receiver,"implementation_amendment":AMENDMENT}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="rows"},indent=2,sort_keys=True))
    if result["status"] not in ("SHARD_PASS","BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS"):
        raise SystemExit(1)

if __name__=="__main__": main()
