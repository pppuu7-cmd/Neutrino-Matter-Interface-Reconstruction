#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import json
import os
from pathlib import Path

CONTRACT="c9d9e46860ef55bec2a5aaaafdac19f6e9de551b"
AMENDMENT="c95fd80e7b2a54d04f83103e7678acbe8c51f6c6"
PASS_SHARD="SHARD_PASS_G9_RAY_CENTRIC_DUAL_DISK"
BLOCKED="BLOCKED_G9_RAY_CENTRIC_DUAL_DISK_CONVOLUTION"
SCI_FAIL="SCIENTIFIC_FAIL_G9_DUAL_DISK_INVARIANT"
INFRA="INFRASTRUCTURE_FAIL_G9_0090E"


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True)
    args=ap.parse_args()
    files=sorted(Path(args.input).rglob("g9_0090e_shard_*.json"))
    head=os.getenv("GITHUB_SHA")
    if len(files)!=9:
        result={"status":INFRA,"reason":f"expected 9 shard JSONs, found {len(files)}","contract":CONTRACT,"amendment":AMENDMENT,"head_sha":head}
    else:
        rows=[]; payloads=[]; bad_contract=[]; bad_amendment=[]; bad_head=[]
        for p in files:
            d=json.loads(p.read_text()); payloads.append(d)
            if d.get("contract")!=CONTRACT: bad_contract.append(str(p))
            if d.get("amendment")!=AMENDMENT: bad_amendment.append(str(p))
            if d.get("head_sha")!=head: bad_head.append(str(p))
        statuses=collections.Counter(d.get("status","MISSING_STATUS") for d in payloads)
        pairs={(d.get("control_index"),d.get("receiver_index")) for d in payloads}
        for d in payloads:
            rows.extend(d.get("rows",[]))
        base={"contract":CONTRACT,"amendment":AMENDMENT,"head_sha":head,"shard_count":len(payloads),"status_counts":dict(statuses),
              "pair_count":len(pairs),"row_count":len(rows)}
        if bad_contract or bad_amendment or bad_head or len(pairs)!=9:
            result={**base,"status":INFRA,"reason":"shard contract/amendment/head/pair identity mismatch",
                    "bad_contract":bad_contract,"bad_amendment":bad_amendment,"bad_head":bad_head}
        elif statuses.get(INFRA,0) or "MISSING_STATUS" in statuses:
            result={**base,"status":INFRA,"reason":"one or more shard infrastructure failures"}
        elif statuses.get(SCI_FAIL,0):
            result={**base,"status":SCI_FAIL,"reason":"one or more shard scientific invariant failures"}
        elif statuses.get(BLOCKED,0):
            reasons=[{"control_index":d.get("control_index"),"receiver_index":d.get("receiver_index"),"reason":d.get("reason")}
                     for d in payloads if d.get("status")==BLOCKED]
            result={**base,"status":BLOCKED,"reason":"one or more fixed dual-disk sentinels missed frozen convergence/control criteria",
                    "blocked_reasons":reasons}
        elif statuses==collections.Counter({PASS_SHARD:9}) and len(rows)==81:
            result={**base,"status":"PASS_G9_RAY_CENTRIC_DUAL_DISK_SENTINEL_AUTHORITY",
                    "max_lh_discrepancy":max(float(d.get("max_lh_discrepancy",0.0)) for d in payloads),
                    "max_point_control_relative_error":max(float(d["point_control"]["relative_error"]) for d in payloads),
                    "max_smallest_source_point_limit_relative_error":max(float(d["point_control"]["smallest_source_relative_error"]) for d in payloads),
                    "max_overlap_symmetry_rel":max(float(d["overlap_controls"]["max_symmetry_rel"]) for d in payloads),
                    "max_overlap_scale_rel":max(float(d["overlap_controls"]["max_scale_rel"]) for d in payloads),
                    "mu_h_min":min(float(r["mu_h"]) for r in rows),"mu_h_max":max(float(r["mu_h"]) for r in rows)}
        else:
            result={**base,"status":INFRA,"reason":"unexpected shard status/cardinality combination"}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))
    if result["status"] in (INFRA,SCI_FAIL):
        raise SystemExit(1)


if __name__=="__main__": main()
