#!/usr/bin/env python3
from __future__ import annotations
import json, math, os
from pathlib import Path
from nmir.coherent_csi_sm_0074b import QF, LIGHT_YIELD_PE_PER_KEVEE, calculate_events

TARGET=173.0
TOL=48.0
MAX_REF=0.005
MAX_TAIL=1e-8


def good(x): return math.isfinite(x) and x >= 0.0


def main() -> int:
    coarse=calculate_events(n_t=1000)
    fine=calculate_events(n_t=4000)
    no_acc=calculate_events(n_t=2000, apply_acceptance=False)
    no_ff=calculate_events(n_t=2000, form_factor=False)
    qf_up=calculate_events(n_t=2000, qf=QF*1.01)
    ly_up=calculate_events(n_t=2000, light_yield=LIGHT_YIELD_PE_PER_KEVEE*1.01)
    ref=abs(fine['total']-coarse['total'])/fine['total']
    comps=[fine[k] for k in fine if k.startswith('Cs_') or k.startswith('I_')]
    checks={
      'within_frozen_173_pm_48': abs(fine['total']-TARGET) <= TOL,
      'refinement_le_0p5pct': ref <= MAX_REF,
      'components_finite_nonnegative': all(good(v) for v in comps),
      'disable_acceptance_not_lower': no_acc['total'] >= fine['total'],
      'F_equal_1_not_lower': no_ff['total'] >= fine['total'],
      'poisson_tail_le_1e8': fine['max_poisson_tail'] <= MAX_TAIL,
      'qf_local_monotonic': qf_up['total'] >= fine['total'],
      'light_yield_local_monotonic': ly_up['total'] >= fine['total'],
    }
    passed=all(checks.values())
    result={
      'schema':'nmir.coherent_csi_sm_0074b.v1',
      'classification':'PASS_COHERENT_CSI_SM_RESPONSE_BENCHMARK' if passed else 'SCIENTIFIC_FAIL_COHERENT_CSI_SM_RESPONSE_BENCHMARK',
      'frozen_target_events':TARGET,'frozen_tolerance_events':TOL,
      'coarse_events':coarse,'fine_events':fine,'refinement_fraction':ref,
      'no_acceptance_total_events':no_acc['total'],'unit_form_factor_total_events':no_ff['total'],
      'qf_up_total_events':qf_up['total'],'light_yield_up_total_events':ly_up['total'],
      'checks':checks,
      'guards':{'fit_134_used_as_target':False,'b_minus_l_scan_performed':False,'later_qf_substituted':False},
    }
    out=Path(os.environ.get('NMIR_0074B_RESULT','artifacts/coherent_0074b/result.json'))
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(out.read_text(),end='')
    return 0 if passed else 2

if __name__=='__main__': raise SystemExit(main())
