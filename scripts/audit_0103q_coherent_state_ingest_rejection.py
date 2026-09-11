#!/usr/bin/env python3
import copy
import json
import math

SCOPE="NONTERMINAL_DATA_INTEGRITY_ONLY"

BASE_META={
  "state_id":"SYNTHETIC_STATE_0103Q_V1",
  "coordinate_system":"cartesian",
  "handedness":"right",
  "grid_shape":[9,9,9],
  "x":[-1.0,-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75,1.0],
  "y":[-1.0,-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75,1.0],
  "z":[-1.0,-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75,1.0],
  "length_unit":"code_length",
  "B_unit":"code_B",
  "rho_unit":"code_rho",
  "Ye_convention":"electron_fraction_per_baryon_v1",
  "snapshot_time":695.0,
}

EXPECTED={
 "state_id":"STATE_ID_MISMATCH","grid_shape":"GRID_SHAPE_MISMATCH","x_shift":"COORDINATE_ARRAY_MISMATCH",
 "handedness":"HANDEDNESS_MISMATCH","length_unit":"LENGTH_UNIT_MISMATCH","missing_B_unit":"MISSING_B_UNIT",
 "rho_unit":"DENSITY_UNIT_MISMATCH","missing_Ye":"MISSING_YE_CONVENTION","snapshot_time":"SNAPSHOT_TIME_MISMATCH",
 "nonfinite_B":"NONFINITE_FIELD","nonfinite_rho":"NONFINITE_DENSITY","ray_oob":"RAY_OUT_OF_DOMAIN"
}

def payloads():
    return {"B_sample":[0.3,-0.2,0.7],"rho_sample":1.4,"ray_start":[-0.7,-0.6,-0.5],"ray_end":[0.7,0.6,0.5]}

def validate(mag,matter,payload):
    required=["state_id","coordinate_system","handedness","grid_shape","x","y","z","length_unit","B_unit","rho_unit","Ye_convention","snapshot_time"]
    for k in required:
        if k not in mag or k not in matter:
            return False,{"B_unit":"MISSING_B_UNIT","Ye_convention":"MISSING_YE_CONVENTION"}.get(k,"MISSING_METADATA")
    checks=[("state_id","STATE_ID_MISMATCH"),("coordinate_system","COORDINATE_SYSTEM_MISMATCH"),("handedness","HANDEDNESS_MISMATCH"),("grid_shape","GRID_SHAPE_MISMATCH"),("x","COORDINATE_ARRAY_MISMATCH"),("y","COORDINATE_ARRAY_MISMATCH"),("z","COORDINATE_ARRAY_MISMATCH"),("length_unit","LENGTH_UNIT_MISMATCH"),("rho_unit","DENSITY_UNIT_MISMATCH"),("Ye_convention","YE_CONVENTION_MISMATCH"),("snapshot_time","SNAPSHOT_TIME_MISMATCH")]
    for k,reason in checks:
        if mag[k]!=matter[k]: return False,reason
    if not all(math.isfinite(v) for v in payload["B_sample"]): return False,"NONFINITE_FIELD"
    if not math.isfinite(payload["rho_sample"]): return False,"NONFINITE_DENSITY"
    for point in (payload["ray_start"],payload["ray_end"]):
        for v,axis in zip(point,(mag["x"],mag["y"],mag["z"])):
            if v<min(axis) or v>max(axis): return False,"RAY_OUT_OF_DOMAIN"
    return True,"ACCEPT"

def fixture(name):
    mag=copy.deepcopy(BASE_META); matter=copy.deepcopy(BASE_META); p=payloads()
    if name=="state_id": matter["state_id"]="OTHER"
    elif name=="grid_shape": matter["grid_shape"]=[10,9,9]
    elif name=="x_shift": matter["x"]=[v+0.01 for v in matter["x"]]
    elif name=="handedness": matter["handedness"]="left"
    elif name=="length_unit": matter["length_unit"]="cm"
    elif name=="missing_B_unit": del matter["B_unit"]
    elif name=="rho_unit": matter["rho_unit"]="g_cm3"
    elif name=="missing_Ye": del matter["Ye_convention"]
    elif name=="snapshot_time": matter["snapshot_time"]=696.0
    elif name=="nonfinite_B": p["B_sample"][1]=float("nan")
    elif name=="nonfinite_rho": p["rho_sample"]=float("inf")
    elif name=="ray_oob": p["ray_end"]=[1.1,0.6,0.5]
    return mag,matter,p

def execute():
    pm=copy.deepcopy(BASE_META); pt=copy.deepcopy(BASE_META); pp=payloads()
    positive=validate(pm,pt,pp)
    rows=[]; propagation_count=0
    for name,expected in EXPECTED.items():
        decision=validate(*fixture(name));
        if decision[0]: propagation_count+=1
        rows.append({"case":name,"accepted":decision[0],"reason":decision[1],"expected":expected,"correct":(not decision[0] and decision[1]==expected)})
    return positive,rows,propagation_count

def run_audit():
    p1,r1,c1=execute(); p2,r2,c2=execute()
    deterministic=(p1==p2 and r1==r2 and c1==c2)
    gates={"positive_control":p1==(True,"ACCEPT"),"all_12_corruptions_rejected":all(x["correct"] for x in r1) and len(r1)==12,"deterministic_reason_codes":all(x["reason"]==x["expected"] for x in r1),"no_corrupted_propagation":c1==0,"repeat_deterministic":deterministic,"scope_guard":SCOPE=="NONTERMINAL_DATA_INTEGRITY_ONLY"}
    out={"audit":"NMIR-0103Q-COHERENT-STATE-INGEST-REJECTION","scope":SCOPE,"positive_control":{"accepted":p1[0],"reason":p1[1]},"negative_cases":r1,"corrupted_cases_reaching_propagation":c1,"gates":gates}
    out["status"]="PASS_0103Q_COHERENT_STATE_INGEST_REJECTION_NONTERMINAL" if all(gates.values()) else "FAIL_0103Q_COHERENT_STATE_INGEST_REJECTION"
    return out

if __name__=="__main__":
    r=run_audit(); print(json.dumps(r,indent=2,sort_keys=True,allow_nan=False)); raise SystemExit(0 if all(r["gates"].values()) else 1)
