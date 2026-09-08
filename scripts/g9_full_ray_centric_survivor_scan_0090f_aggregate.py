#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import json
import os
from pathlib import Path

CONTRACT="fc277e3695ebeb2628d133b9385e7d7d2e12a5d5"
PASS_SHARD="SHARD_PASS_G9_FULL_RAY_CENTRIC_SCAN"
SCI_FAIL="SCIENTIFIC_FAIL_G9_FULL_RAY_CENTRIC_INVARIANT"
INFRA="INFRASTRUCTURE_FAIL_G9_0090F"


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True)
    args=ap.parse_args()
    files=sorted(Path(args.input).rglob("g9_0090f_shard_*.json"))
    head=os.getenv("GITHUB_SHA")
    if len(files)!=9:
        result={"status":INFRA,"reason":f"expected 9 shard JSONs, found {len(files)}","contract":CONTRACT,"head_sha":head}
    else:
        payloads=[]; rows=[]; bad_contract=[]; bad_head=[]
        for p in files:
            d=json.loads(p.read_text()); payloads.append(d)
            if d.get("contract")!=CONTRACT: bad_contract.append(str(p))
            if d.get("head_sha")!=head: bad_head.append(str(p))
            rows.extend(d.get("rows",[]))
        statuses=collections.Counter(d.get("status","MISSING_STATUS") for d in payloads)
        pairs={(d.get("control_index"),d.get("receiver_index")) for d in payloads}
        base={"contract":CONTRACT,"head_sha":head,"shard_count":len(payloads),"pair_count":len(pairs),
              "row_count":len(rows),"status_counts":dict(statuses)}
        if bad_contract or bad_head or len(pairs)!=9:
            result={**base,"status":INFRA,"reason":"shard contract/head/pair identity mismatch",
                    "bad_contract":bad_contract,"bad_head":bad_head}
        elif statuses.get(INFRA,0) or "MISSING_STATUS" in statuses:
            result={**base,"status":INFRA,"reason":"one or more shard infrastructure failures"}
        elif statuses.get(SCI_FAIL,0):
            reasons=[{"control_index":d.get("control_index"),"receiver_index":d.get("receiver_index"),"reason":d.get("reason")}
                     for d in payloads if d.get("status")==SCI_FAIL]
            result={**base,"status":SCI_FAIL,"reason":"one or more full-grid invariant failures","fail_reasons":reasons}
        elif statuses==collections.Counter({PASS_SHARD:9}) and len(rows)==1350:
            survivors=[r for r in rows if bool(r.get("finite_nonzero_survivor"))]
            top=sorted(survivors,key=lambda r:(-float(r["mu"]),int(r["control_index"]),int(r["receiver_index"]),
                                               int(r["theta_index"]),float(r["delta_m"])))[:50]
            def count(pred): return sum(1 for r in rows if pred(r))
            by_receiver={str(x):sum(1 for r in survivors if int(r["receiver_index"])==x) for x in range(3)}
            by_observer={str(x):sum(1 for r in survivors if int(r["control_index"])==x) for x in range(3)}
            by_theta={str(x):sum(1 for r in survivors if int(r["theta_index"])==x) for x in range(25)}
            offsets=sorted({float(r["delta_m"]) for r in rows})
            by_offset={format(x,"g"):sum(1 for r in survivors if float(r["delta_m"])==x) for x in offsets}
            n=len(survivors)
            status="PASS_G9_FULL_GRID_FINITE_NONZERO_SURVIVORS" if n else "PASS_G9_FULL_GRID_NO_FINITE_NONZERO_SURVIVOR"
            result={**base,"status":status,
                    "finite_nonzero_survivor_count":n,
                    "ge2_all_count":count(lambda r: bool(r["ge2"])),
                    "ge10_all_count":count(lambda r: bool(r["ge10"])),
                    "ge1e3_all_count":count(lambda r: bool(r["ge1e3"])),
                    "ge2_nonzero_offset_count":count(lambda r: float(r["delta_m"])>0 and bool(r["ge2"])),
                    "ge10_nonzero_offset_count":count(lambda r: float(r["delta_m"])>0 and bool(r["ge10"])),
                    "ge1e3_nonzero_offset_count":count(lambda r: float(r["delta_m"])>0 and bool(r["ge1e3"])),
                    "mu_min":min(float(r["mu"]) for r in rows),"mu_max":max(float(r["mu"]) for r in rows),
                    "survivor_counts_by_receiver_index":by_receiver,
                    "survivor_counts_by_observer_index":by_observer,
                    "survivor_counts_by_theta_index":by_theta,
                    "survivor_counts_by_offset_m":by_offset,
                    "top_finite_nonzero_survivors":top,
                    "max_point_control_relative_error":max(float(d["point_control"]["relative_error"]) for d in payloads),
                    "max_focal_drift":max(float(d["focal_drift"]) for d in payloads),
                    "max_batch_scalar_rel":max(float(d["batch_scalar_max_rel"]) for d in payloads)}
        else:
            result={**base,"status":INFRA,"reason":"unexpected full-grid status/cardinality combination"}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))
    if result["status"] in (INFRA,SCI_FAIL):
        raise SystemExit(1)

if __name__=="__main__": main()
