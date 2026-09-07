#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math

THRESH=2e-3
SIDE_TOL=2e-6
X_MAJOR_INDICES=[0,2,4,6,8,10,12,14]
X_LOG=[-2.0,0.0,2.0,4.0,6.0,8.0,10.0,12.0]
Y_LOG=[-11.0,-10.0,-9.0,-8.0,-7.0,-6.0,-5.0]


def fit_affine(x,y):
    n=len(x); xm=sum(x)/n; ym=sum(y)/n
    den=sum((v-xm)**2 for v in x)
    if den<=0: raise ValueError('degenerate fit')
    a=sum((x[i]-xm)*(y[i]-ym) for i in range(n))/den
    b=ym-a*xm
    pred=[a*v+b for v in x]
    res=[pred[i]-y[i] for i in range(n)]
    return a,b,pred,res,max(abs(r) for r in res)


def max_pair_delta(a,b,key):
    if len(a)!=len(b): return math.inf
    return max((abs(a[i][key]-b[i][key]) for i in range(len(a))), default=0.0)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--axis-json',required=True)
    ap.add_argument('--tick-authority',required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    axes=json.load(open(args.axis_json,encoding='utf-8'))
    auth=json.load(open(args.tick_authority,encoding='utf-8'))

    if axes.get('eps_sha256') != auth['primary_source']['source_eps_sha256']:
        raise SystemExit('INFRASTRUCTURE_FAIL: EPS authority hash mismatch')
    bot=axes['ticks']['bottom']; top=axes['ticks']['top']; left=axes['ticks']['left']; right=axes['ticks']['right']
    structural_ok=(len(bot)==16 and len(top)==16 and len(left)==7 and len(right)==7)
    x_side_delta=max_pair_delta(bot,top,'x')
    y_side_delta=max_pair_delta(left,right,'y')
    side_ok=(x_side_delta<=SIDE_TOL and y_side_delta<=SIDE_TOL)

    if not structural_ok:
        classification='SCIENTIFIC_FAIL_VECTOR_CALIBRATION'
        out={'iteration':'0072b','classification':classification,'reason':'unexpected vector tick counts','counts':{'bottom':len(bot),'top':len(top),'left':len(left),'right':len(right)}}
    else:
        x=[bot[i]['x'] for i in X_MAJOR_INDICES]
        y=[r['y'] for r in left]
        # Fail closed if the frozen primary-source values have changed underneath the preregistration.
        if auth['axis_labels']['x']['printed_major_log10'] != X_LOG or auth['axis_labels']['y']['printed_major_log10'] != Y_LOG:
            raise SystemExit('INFRASTRUCTURE_FAIL: frozen tick authority does not match 0072b preregistration')
        ax,bx,px,rx,mx=fit_affine(x,X_LOG)
        ay,by,py,ry,my=fit_affine(y,Y_LOG)
        pass_fit=(mx<=THRESH and my<=THRESH and side_ok)
        classification='PASS_WAGNER_AXIS_CALIBRATION' if pass_fit else 'SCIENTIFIC_FAIL_VECTOR_CALIBRATION'
        box=axes['left_panel_box']
        out={
          'iteration':'0072b','classification':classification,
          'eps_sha256':axes['eps_sha256'],
          'frozen_threshold_decades':THRESH,'side_agreement_tolerance_eps':SIDE_TOL,
          'side_agreement':{'x_top_bottom_max_delta_eps':x_side_delta,'y_left_right_max_delta_eps':y_side_delta,'pass':side_ok},
          'x':{
            'major_tick_indices':X_MAJOR_INDICES,'eps_positions':x,'log10_values':X_LOG,
            'a':ax,'b':bx,'predicted_log10':px,'residuals_decades':rx,'max_abs_residual_decades':mx,
            'frame_log10_range':[ax*box['x_min']+bx,ax*box['x_max']+bx]
          },
          'y':{
            'eps_positions':y,'log10_values':Y_LOG,
            'a':ay,'b':by,'predicted_log10':py,'residuals_decades':ry,'max_abs_residual_decades':my,
            'frame_log10_range':[ay*box['y_min']+by,ay*box['y_max']+by]
          },
          'transform':{
            'log10_lambda_m':'a_x*x_eps+b_x','log10_abs_alpha_tilde':'a_y*y_eps+b_y',
            'a_x':ax,'b_x':bx,'a_y':ay,'b_y':by
          },
          'guard':'Axis calibration only. No exclusion-curve point is accepted by this subgate.'
        }
    with open(args.output,'w',encoding='utf-8') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,sort_keys=True))

if __name__=='__main__': main()
