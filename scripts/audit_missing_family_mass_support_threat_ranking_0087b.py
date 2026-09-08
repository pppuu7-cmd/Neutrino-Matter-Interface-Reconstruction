#!/usr/bin/env python3
"""NMIR 0087b — missing-family mass-support threat ranking."""
from __future__ import annotations

import json
import math
import pathlib

import validate_partial_bl_topology_relay_0087a as parent

LEDGER = pathlib.Path(__file__).resolve().parents[1] / "data" / "b_minus_l_primary_constraints_0071.json"
MIN_AREA = 0.01
YMAX = -5.0


def classify_interval(support, target):
    if support is None:
        return {"classification": "UNRESOLVED_MASS_SUPPORT_THREAT"}
    a, b = map(float, support)
    t0, t1 = map(float, target)
    if not (0 < a <= b and 0 < t0 <= t1 and all(math.isfinite(x) for x in (a,b,t0,t1))):
        raise ValueError("invalid positive finite mass interval")
    if b < t0:
        sep = math.log10(t0 / b)
        return {"classification":"PROVABLY_MASS_DISJOINT", "separation_decades":sep, "side":"below_target"}
    if a > t1:
        sep = math.log10(a / t1)
        return {"classification":"PROVABLY_MASS_DISJOINT", "separation_decades":sep, "side":"above_target"}
    lo, hi = max(a,t0), min(b,t1)
    width = max(0.0, math.log10(hi/lo)) if hi >= lo and lo > 0 else 0.0
    target_width = math.log10(t1/t0)
    return {
        "classification":"MASS_OVERLAP_THREAT",
        "overlap_interval_eV":[lo,hi],
        "overlap_width_decades":width,
        "target_log_width_decades":target_width,
        "overlap_fraction_of_target_log_width": (width/target_width if target_width > 0 else 0.0),
        "endpoint_contact_only": bool(abs(hi-lo) <= max(1e-15,1e-12*lo)),
    }


def bbn_support_from_ledger():
    obj = json.loads(LEDGER.read_text(encoding="utf-8"))
    rec = [c for c in obj.get("constraints",[]) if c.get("family")=="cosmology_BBN_CMB"]
    if len(rec) != 1:
        raise RuntimeError("expected exactly one cosmology_BBN_CMB ledger record")
    support = rec[0].get("mass_range_eV")
    if support != [1, 100000000.0] and support != [1, 1e8]:
        raise RuntimeError(f"unexpected BBN/CMB mass_range_eV: {support}")
    return [float(support[0]), float(support[1])]


def robust_target():
    solar, cmb_geoms, sn_geoms, wagner, meta = parent.build_authoritative_families()
    combos = [
        ("Majorana", "BODY_NATIVE"),
        ("Majorana", "CONCLUSION_SUMMARY"),
        ("Dirac", "BODY_NATIVE"),
        ("Dirac", "CONCLUSION_SUMMARY"),
    ]
    scenarios = {}
    xmins=[]; xmaxs=[]
    for csc, sv in combos:
        cname=f"CMB_{csc.upper()}_0080d"
        snname=f"SN1987A_{sv}_0084b"
        families={
            "SOLAR_CEVNS_0078c":solar,
            cname:cmb_geoms[csc],
            snname:sn_geoms[sv],
            "WAGNER_0085":wagner,
        }
        r=parent.analyze_window(families,YMAX)
        if not r["area_closure_pass"] or r["qualifying_component_count_ge_0p01"] != 2 or not r["N1"]:
            raise ValueError(f"0087a parent reproduction failed for {csc}/{sv}")
        permitted = parent.box(parent.XMIN,parent.YMIN,parent.XMAX,YMAX).difference(
            parent.unary_union([parent.clip_family(g,parent.box(parent.XMIN,parent.YMIN,parent.XMAX,YMAX)) for g in families.values()])
        )
        qual=parent.qualifying_components(permitted)
        if len(qual)!=2:
            raise ValueError("qualifying component reconstruction mismatch")
        low=min(qual,key=lambda p:p.area)
        xmin,ymin,xmax,ymax=low.bounds
        xmins.append(xmin); xmaxs.append(xmax)
        scenarios[f"{csc}__{sv}"]={
            "qualifying_component_areas_decade2":sorted([p.area for p in qual],reverse=True),
            "selected_smaller_component_area_decade2":low.area,
            "selected_component_bounds_log10_m_eV_log10_g":[xmin,ymin,xmax,ymax],
            "selected_mass_interval_eV":[10.0**xmin,10.0**xmax],
            "area_closure_relative_error":r["area_closure_relative_error"],
        }
    tx0=min(xmins); tx1=max(xmaxs)
    return {
        "definition":"union-envelope of the smaller of exactly two qualifying permitted components at y_max=-5 across four preserved scenarios",
        "log10_mass_interval_eV":[tx0,tx1],
        "mass_interval_eV":[10.0**tx0,10.0**tx1],
        "scenarios":scenarios,
        "input_authority":meta,
    }


def audit():
    target=robust_target()
    tint=target["mass_interval_eV"]
    bbn=bbn_support_from_ledger()
    families={
        "NA64_UNBROKEN_BL_0086c":{
            "support_eV":[1.0e7,1.0e9],
            "authority":"0086c exact source-native bminusl_unbroken.pdf: printed x anchors 10^-2,10^-1,10^0 GeV; outer anchors coincide with plot-frame x edges; y calibration blocked and unused",
        },
        "BBN_ESSEILI_KRIBS_0081a":{
            "support_eV":bbn,
            "authority":"0071 explicit mass_range_eV for cosmology_BBN_CMB; BBN y geometry remains 0081a-blocked",
        },
        "CERDENO_SN_TRANSPORT_0082c":{
            "support_eV":None,
            "authority":"0082c did not promote a physical x calibration; provisional 0082b anchor inventory is not reused",
        },
        "COHERENT_COMBINED_0074c":{
            "support_eV":None,
            "authority":"0074c has exact likelihood architecture but no promoted complete B-L mediator-mass contour support interval",
        },
        "FIFTH_FORCE_FINITE_MASS_0079":{
            "support_eV":None,
            "authority":"0079/0079a authorize only m_V->0 asymptote; no finite-mass interval",
        },
    }
    for rec in families.values():
        rec["threat_result"]=classify_interval(rec["support_eV"],tint)
    counts={}
    for rec in families.values():
        k=rec["threat_result"]["classification"]
        counts[k]=counts.get(k,0)+1
    return {
        "iteration":"0087b",
        "classification":"PASS_MISSING_FAMILY_MASS_SUPPORT_THREAT_RANKING",
        "parent_y_max_log10_g":YMAX,
        "minimum_component_area_decade2":MIN_AREA,
        "robust_low_mass_target":target,
        "missing_families":families,
        "threat_counts":counts,
        "cleared_by_mass_only":[k for k,v in families.items() if v["threat_result"]["classification"]=="PROVABLY_MASS_DISJOINT"],
        "remaining_mass_overlap_threats":[k for k,v in families.items() if v["threat_result"]["classification"]=="MASS_OVERLAP_THREAT"],
        "remaining_unresolved_mass_support_threats":[k for k,v in families.items() if v["threat_result"]["classification"]=="UNRESOLVED_MASS_SUPPORT_THREAT"],
        "guard":"Mass-support ranking only. No blocked-family y geometry, no raster/manual reading, no finite-mass fifth-force extrapolation, no global allowed-region claim, no BSM response scan.",
    }


def main():
    out=pathlib.Path("missing_family_mass_support_threat_ranking_0087b.json")
    try:
        result=audit()
    except (OSError,RuntimeError) as exc:
        result={"iteration":"0087b","classification":"BLOCKED_0087B_INPUT_AUTHORITY","reason":repr(exc)}
    except ValueError as exc:
        result={"iteration":"0087b","classification":"SCIENTIFIC_FAIL_0087B_PARENT_REPRODUCTION","reason":repr(exc)}
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2,sort_keys=True))
    if result["classification"]!="PASS_MISSING_FAMILY_MASS_SUPPORT_THREAT_RANKING":
        raise SystemExit(2)

if __name__=="__main__": main()
