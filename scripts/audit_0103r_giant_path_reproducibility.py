#!/usr/bin/env python3
import hashlib
import json
import numpy as np

SCOPE = "ENGINEERING_ONLY_NOT_BETELGEUSE"


def field_xyz(x, y, z):
    return np.array([
        0.3 + 0.2*x + 0.11*y - 0.07*z + 0.03*y*z,
        np.sin(np.pi*x) + 0.13*y + 0.09*z + 0.02*y*z,
        np.cos(0.5*np.pi*x) - 0.05*y + 0.17*z - 0.04*y*z,
    ], dtype=float)


def bracket(coords, target):
    hi = int(np.searchsorted(coords, target, side="left"))
    if hi == 0:
        return 0, 0, 1.0, 0.0
    if hi == len(coords):
        j = len(coords)-1
        return j, j, 1.0, 0.0
    if coords[hi] == target:
        return hi, hi, 1.0, 0.0
    lo = hi-1
    w1 = float((target-coords[lo])/(coords[hi]-coords[lo]))
    return lo, hi, 1.0-w1, w1


def interpolate_line(x, y, z, cube, target_y, target_z):
    j0,j1,wy0,wy1 = bracket(y, target_y)
    k0,k1,wz0,wz1 = bracket(z, target_z)
    out = np.empty((3, len(x)), dtype=float)
    for i in range(len(x)):
        for c in range(3):
            f00 = cube[c,k0,j0,i]
            f01 = cube[c,k0,j1,i]
            f10 = cube[c,k1,j0,i]
            f11 = cube[c,k1,j1,i]
            out[c,i] = wz0*(wy0*f00+wy1*f01) + wz1*(wy0*f10+wy1*f11)
    return out, (j0,j1,wy0,wy1,k0,k1,wz0,wz1)


def run_once():
    x=np.linspace(-1.0,1.0,17)
    y=np.linspace(-1.0,1.0,13)
    z=np.linspace(-1.0,1.0,11)
    cube=np.empty((3,len(z),len(y),len(x)), dtype=float)
    for k,zz in enumerate(z):
        for j,yy in enumerate(y):
            for i,xx in enumerate(x):
                cube[:,k,j,i]=field_xyz(xx,yy,zz)

    ty,tz=0.13,-0.17
    line,w=interpolate_line(x,y,z,cube,ty,tz)
    analytic=np.stack([field_xyz(xx,ty,tz) for xx in x],axis=1)
    interpolation_residual=float(np.max(np.abs(line-analytic)))

    n=np.array([1.0,0.0,0.0])
    bpar=n@line
    bperp_proj=np.sqrt(np.maximum(0.0,np.sum(line*line,axis=0)-bpar*bpar))
    bperp_cross=np.linalg.norm(np.cross(line.T,n),axis=1)
    ray_identity_residual=float(np.max(np.abs(bperp_proj-bperp_cross)))

    line_rev=line[:,::-1]
    nrev=-n
    bpar_rev=nrev@line_rev
    bperp_rev=np.sqrt(np.maximum(0.0,np.sum(line_rev*line_rev,axis=0)-bpar_rev*bpar_rev))
    reversal_bperp_residual=float(np.max(np.abs(bperp_proj-bperp_rev[::-1])))
    reversal_bparallel_sign_residual=float(np.max(np.abs(bpar+bpar_rev[::-1])))

    # Exact grid-node interpolation check.
    node_line,_=interpolate_line(x,y,z,cube,float(y[4]),float(z[7]))
    exact_node=cube[:,7,4,:]
    exact_node_residual=float(np.max(np.abs(node_line-exact_node)))

    rng=np.random.default_rng(103)
    random_identity_residual=0.0
    for _ in range(64):
        B=rng.normal(size=3)
        nn=rng.normal(size=3); nn/=np.linalg.norm(nn)
        p1=np.sqrt(max(0.0,float(B@B-(B@nn)**2)))
        p2=float(np.linalg.norm(np.cross(B,nn)))
        random_identity_residual=max(random_identity_residual,abs(p1-p2))

    weights=[w[2],w[3],w[6],w[7]]
    valid_weights=(all(-1e-15 <= q <= 1+1e-15 for q in weights)
                   and abs(w[2]+w[3]-1)<=1e-15 and abs(w[6]+w[7]-1)<=1e-15)
    metrics={
        "scope":SCOPE,
        "grid_shape":[len(x),len(y),len(z)],
        "target_yz":[ty,tz],
        "interpolation_residual":interpolation_residual,
        "ray_identity_residual":ray_identity_residual,
        "random_identity_residual":float(random_identity_residual),
        "reversal_bperp_residual":reversal_bperp_residual,
        "reversal_bparallel_sign_residual":reversal_bparallel_sign_residual,
        "exact_node_residual":exact_node_residual,
        "bperp_max":float(np.max(bperp_proj)),
        "bperp_rms":float(np.sqrt(np.mean(bperp_proj*bperp_proj))),
        "valid_weights":bool(valid_weights),
        "strictly_monotonic_path":bool(np.all(np.diff(x)>0)),
        "all_finite":bool(np.isfinite(cube).all() and np.isfinite(line).all()),
    }
    canonical=json.dumps(metrics,sort_keys=True,separators=(",",":"),allow_nan=False)
    return metrics, hashlib.sha256(canonical.encode()).hexdigest()


def run_audit():
    a,ha=run_once(); b,hb=run_once()
    gates={
        "finite":a["all_finite"],
        "valid_interpolation_weights":a["valid_weights"],
        "analytic_bilinear_interpolation":a["interpolation_residual"] <= 1e-12,
        "ray_projection_identity":a["ray_identity_residual"] <= 1e-12,
        "random_projection_identity":a["random_identity_residual"] <= 1e-12,
        "ray_reversal_bperp":a["reversal_bperp_residual"] <= 1e-12,
        "ray_reversal_bparallel_sign":a["reversal_bparallel_sign_residual"] <= 1e-12,
        "exact_node_interpolation":a["exact_node_residual"] <= 1e-14,
        "monotonic_path":a["strictly_monotonic_path"],
        "repeat_hash_identical":ha == hb and a == b,
        "scope_guard":a["scope"] == SCOPE,
    }
    out={"audit":"NMIR-0103R-GIANT-PATH-REPRODUCIBILITY","metrics":a,
         "canonical_sha256":ha,"repeat_sha256":hb,"gates":gates}
    out["status"]="PASS_0103R_GIANT_PATH_REPRODUCIBILITY_ENGINEERING_ONLY" if all(gates.values()) else "FAIL_0103R_REPRODUCIBILITY"
    return out


if __name__ == "__main__":
    out=run_audit(); print(json.dumps(out,indent=2,sort_keys=True))
    if not all(out["gates"].values()): raise SystemExit(1)
