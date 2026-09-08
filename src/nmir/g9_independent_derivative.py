"""Independent continuous-derivative root locator for NMIR G9 iteration 0088.

This module proposes turning roots only. Authoritative map values remain the
existing pinned Model-S map and must be checked separately.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable, Sequence

from .gravity_extended import AU_CM, C_CGS, G_CGS, RadialDensityProfile, _interp_density


class RootCertificationBlocked(ValueError):
    pass


@dataclass(frozen=True)
class RootBracket:
    root: float
    lo: float
    hi: float


def adaptive_simpson(f: Callable[[float], float], a: float, b: float, tol: float = 1e-11, depth: int = 30) -> float:
    if a == b:
        return 0.0
    def simp(x0: float, x1: float) -> tuple[float, float, float, float]:
        xm = (x0 + x1) / 2.0
        f0, fm, f1 = f(x0), f(xm), f(x1)
        return (x1-x0)*(f0+4*fm+f1)/6.0, f0, fm, f1
    whole, f0, fm, f1 = simp(a, b)
    def rec(x0: float, x1: float, y0: float, ym: float, y1: float, s: float, atol: float, n: int) -> float:
        xm=(x0+x1)/2.0; xl=(x0+xm)/2.0; xr=(xm+x1)/2.0
        fl, fr = f(xl), f(xr)
        sl=(xm-x0)*(y0+4*fl+ym)/6.0; sr=(x1-xm)*(ym+4*fr+y1)/6.0
        s2=sl+sr
        if abs(s2-s)/15.0 <= max(atol, tol*abs(s2)):
            return s2+(s2-s)/15.0
        if n <= 0:
            raise RootCertificationBlocked("adaptive Simpson depth exhausted")
        return rec(x0,xm,y0,fl,ym,sl,atol/2,n-1)+rec(xm,x1,ym,fr,y1,sr,atol/2,n-1)
    return rec(a,b,f0,fm,f1,whole,tol,depth)


def _piecewise(f: Callable[[float], float], points: Sequence[float], tol: float) -> float:
    p=sorted(set(points)); n=max(1,len(p)-1); total=0.0
    for a,b in zip(p,p[1:]):
        if b>a:
            total += adaptive_simpson(f,a,b,tol/n)
    return total


def continuous_mass_and_derivative(profile: RadialDensityProfile, x: float, radius_cm: float, tol: float = 1e-11) -> tuple[float,float]:
    if not 0.0 < x < 1.0:
        raise ValueError("x must lie in (0,1)")
    rpts=list(profile.radius_fraction)+[x,0.0,1.0]
    def radial(u: float) -> float:
        if u<=0: return 0.0
        frac=1.0 if u<=x else 1.0-math.sqrt(max(0.0,1.0-(x/u)**2))
        return u*u*_interp_density(profile,u)*frac
    mass=4*math.pi*radius_cm**3*_piecewise(radial,rpts,tol)
    top=math.acos(x); tpts=[0.0,top]
    for r in profile.radius_fraction:
        if x<r<1.0: tpts.append(math.acos(x/r))
    def angular(t: float) -> float:
        c=math.cos(t); return _interp_density(profile,x/c)/(c*c)
    dmass=4*math.pi*radius_cm**3*x*x*_piecewise(angular,tpts,tol)
    return mass,dmass


def independent_derivative(profile: RadialDensityProfile, x: float, observer_au: float, radius_cm: float, tol: float = 1e-11) -> float:
    mass,dmass=continuous_mass_and_derivative(profile,x,radius_cm,tol)
    focal=(x*radius_cm)**2*C_CGS*C_CGS/(4*G_CGS*mass)/AU_CM
    q=observer_au/focal
    return 1.0+q-x*q*dmass/mass


def _bisect(fn: Callable[[float],float], lo: float, hi: float, width: float=1e-12) -> float:
    flo,fhi=fn(lo),fn(hi)
    if not (math.isfinite(flo) and math.isfinite(fhi)) or flo*fhi>0:
        raise RootCertificationBlocked("invalid sign-changing bracket")
    while hi-lo>width:
        mid=(lo+hi)/2; fm=fn(mid)
        if not math.isfinite(fm): raise RootCertificationBlocked("nonfinite derivative")
        if flo*fm<=0: hi,fhi=mid,fm
        else: lo,flo=mid,fm
    return (lo+hi)/2


def isolate_sign_roots(fn: Callable[[float],float], grid: Sequence[float]) -> tuple[RootBracket,...]:
    vals=[fn(x) for x in grid]; out=[]
    for lo,hi,fl,fh in zip(grid,grid[1:],vals,vals[1:]):
        if not (math.isfinite(fl) and math.isfinite(fh)):
            raise RootCertificationBlocked("nonfinite scan derivative")
        if fl*fh<0:
            out.append(RootBracket(_bisect(fn,lo,hi),lo,hi))
    return tuple(out)


def fixed_dyadic_points(grid: Sequence[float], lo: float, hi: float) -> tuple[float,...]:
    pts=[]
    for a,b in zip(grid,grid[1:]):
        if b<=lo or a>=hi: continue
        step=(b-a)/8.0
        for k in range(1,8):
            x=a+k*step
            if lo<x<hi: pts.append(x)
    return tuple(sorted(set(pts)))
