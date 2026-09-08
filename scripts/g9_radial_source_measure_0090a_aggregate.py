#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

CONTRACT="fb4aad7d1ffe23fb4863d09e26c0c3b20f47364c"
PASS="PASS_G9_RADIAL_SOURCE_MEASURE_QUADRATURE_AUTHORITY"
BLOCKED="BLOCKED_G9_RADIAL_SOURCE_MEASURE_QUADRATURE"
FAIL="SCIENTIFIC_FAIL_G9_RADIAL_SOURCE_MEASURE_INVARIANT"
INFRA="INFRASTRUCTURE_FAIL_G9_0090A"


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""): h.update(chunk)
    return h.hexdigest()


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True)
    args=ap.parse_args(); root=Path(args.input)
    files=sorted(root.rglob("g9_0090a_shard_*.json"))
    shards=[]; hashes={}
    for p in files:
        hashes[str(p.relative_to(root))]=sha256(p)
        shards.append(json.loads(p.read_text()))
    expected={(i,j) for i in range(3) for j in range(3)}
    got={(int(x.get("control_index",-1)),int(x.get("receiver_index",-1))) for x in shards}
    statuses=[x.get("status") for x in shards]
    if got!=expected or len(shards)!=9:
        status=INFRA; reason=f"missing/duplicate shards: got={sorted(got)} count={len(shards)}"
    elif any(s==INFRA for s in statuses):
        status=INFRA; reason="at least one shard infrastructure-failed"
    elif any(s==FAIL for s in statuses):
        status=FAIL; reason="at least one shard failed a scientific invariant"
    elif any(s==BLOCKED for s in statuses):
        status=BLOCKED; reason="at least one shard did not certify frozen radial quadrature"
    elif all(s=="SHARD_PASS" for s in statuses):
        status=PASS; reason="all nine frozen 0090a shards passed"
    else:
        status=INFRA; reason=f"unknown shard status set: {sorted(set(map(str,statuses)))}"
    max_norm=max((float(x.get("max_normalization_abs_error",0.0)) for x in shards if x.get("status")=="SHARD_PASS"),default=None)
    max_conv=max((float(x.get("max_lh_discrepancy",0.0)) for x in shards if x.get("status")=="SHARD_PASS"),default=None)
    max_point=max((float(x.get("point_control",{}).get("relative_error",0.0)) for x in shards if x.get("status")=="SHARD_PASS"),default=None)
    result={"status":status,"reason":reason,"contract":CONTRACT,"head_sha":os.getenv("GITHUB_SHA"),
            "shard_count":len(shards),"status_counts":{s:statuses.count(s) for s in sorted(set(statuses),key=str)},
            "max_normalization_abs_error":max_norm,"max_lh_discrepancy":max_conv,"max_point_control_relative_error":max_point,
            "shard_sha256":hashes,"shards":shards}
    out=Path(args.output); out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="shards"},indent=2,sort_keys=True))
    print(f"RESULT_JSON_SHA256={sha256(out)}")
    if status in (INFRA,FAIL): raise SystemExit(1)

if __name__=="__main__": main()
