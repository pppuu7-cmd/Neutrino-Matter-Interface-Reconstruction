#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

CONTRACT="cf8ffbcca69477939430272777f573d94e4b1e24"
EXPECTED_POINT_MU={
    "0.02": {"1.0":2852164397.5627337,"10.0":285216441.56640047,"100.0":28521654.157074977},
    "0.024":{"1.0":2400495660.864837,"10.0":240049567.24071693,"100.0":24004960.16536005},
    "0.03": {"1.0":1954816649.2088397,"10.0":195481665.87663126,"100.0":19548168.04504079},
}
POINT_REL=0.005


def rel(a,b): return abs(a-b)/max(abs(a),abs(b),1e-300)

def sha256(path:Path)->str:
    h=hashlib.sha256(); h.update(path.read_bytes()); return h.hexdigest()


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True); args=ap.parse_args()
    root=Path(args.input); files=sorted(root.rglob("g9_0090_shard_*.json"))
    rows=[]; shard_meta=[]; statuses=[]; max_point=0.0; point_checks=[]
    for p in files:
        obj=json.loads(p.read_text()); statuses.append(obj.get("status","MISSING"))
        shard_meta.append({"path":str(p),"sha256":sha256(p),"status":obj.get("status"),"control_index":obj.get("control_index"),"receiver_index":obj.get("receiver_index")})
        if obj.get("status")!="SHARD_PASS": continue
        xkey=str(obj["x0"]); expected=EXPECTED_POINT_MU[xkey]
        for pc in obj["point_controls"]:
            want=expected[str(pc["a_m"])]; rr=rel(float(pc["mu"]),want); max_point=max(max_point,rr)
            point_checks.append({"x0":obj["x0"],"a_m":pc["a_m"],"mu":pc["mu"],"authority_mu":want,"relative":rr})
        rows.extend(dict(r,x0=obj["x0"],receiver_m=obj["receiver_m"],z_au=obj["z_au"]) for r in obj["rows"])
    unique={(m.get("control_index"),m.get("receiver_index")) for m in shard_meta}
    if len(files)!=9 or len(unique)!=9:
        status="INFRASTRUCTURE_FAIL_G9_0090"; reason=f"expected 9 unique shards, got {len(files)} files/{len(unique)} keys"
    elif any(s=="SCIENTIFIC_FAIL_G9_PERSISTENT_GLOBAL_INVARIANT" for s in statuses):
        status="SCIENTIFIC_FAIL_G9_PERSISTENT_GLOBAL_INVARIANT"; reason="at least one shard invariant failed"
    elif any(s=="INFRASTRUCTURE_FAIL_G9_0090" for s in statuses) or any(s not in ("SHARD_PASS","BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS") for s in statuses):
        status="INFRASTRUCTURE_FAIL_G9_0090"; reason="at least one shard infrastructure/noncanonical status"
    elif any(s=="BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS" for s in statuses):
        status="BLOCKED_G9_PERSISTENT_CONVOLUTION_NUMERICS"; reason="at least one shard could not certify frozen convolution numerics"
    elif max_point>POINT_REL:
        status="SCIENTIFIC_FAIL_G9_PERSISTENT_GLOBAL_INVARIANT"; reason="0089e point-control reproduction exceeds 0.5%"
    else:
        finite=[r for r in rows if r.get("finite_nonzero_survivor")]
        status="PASS_G9_PERSISTENT_KNOWN_DIRECTION_GLOBAL_SURVIVOR" if finite else "PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_PERSISTENT_GLOBAL"
        reason="all frozen shard/control checks passed"
    finite=[r for r in rows if r.get("finite_nonzero_survivor")]
    out={
        "status":status,"reason":reason,"contract_commit":CONTRACT,"shard_count":len(files),"unique_shards":len(unique),
        "shards":shard_meta,"row_count":len(rows),"expected_row_count":1350,"point_control_max_relative":max_point,
        "point_controls":point_checks,"finite_nonzero_survivor_count":len(finite),
        "grid_ge2_count":sum(bool(r.get("ge2")) for r in rows),"grid_ge10_count":sum(bool(r.get("ge10")) for r in rows),
        "grid_ge1e3_count":sum(bool(r.get("ge1e3")) for r in rows),
        "max_source_refinement_discrepancy":max((float(r.get("convergence",0.0)) for r in rows),default=0.0),
        "finite_survivor_examples":finite[:20],
        "scope":"G9 persistent/known-direction finite-source + deterministic positioning-error geometry only; no occurrence, duty realizability, detector or BSM gain",
    }
    if len(rows)!=1350 and status.startswith("PASS_"):
        out["status"]="INFRASTRUCTURE_FAIL_G9_0090"; out["reason"]="complete 1350-row frozen grid absent"
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ("point_controls","finite_survivor_examples","shards")},indent=2,sort_keys=True))
    if out["status"] in ("INFRASTRUCTURE_FAIL_G9_0090","SCIENTIFIC_FAIL_G9_PERSISTENT_GLOBAL_INVARIANT"): raise SystemExit(1)

if __name__=="__main__": main()
