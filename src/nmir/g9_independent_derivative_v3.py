"""Globally converged nonsingular derivative locator for frozen NMIR 0088.

The quadrature engine is an implementation repair only: every transformed
piece is integrated by deterministic composite Simpson refinement until the
same frozen absolute+relative tolerance is met.  It remains a locator only.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
from .gravity_extended import AU_CM, C_CGS, G_CGS, _interp_density

class RootCertificationBlocked(ValueError):
    pass

@dataclass(frozen=True)
class RootBracket:
    root: float
    lo: float
    hi: float


def _composite_simpson(f, a: float, b: float, n: int) -> float:
    if a == b:
        return 0.0
    if n % 2:
        raise ValueError("n must be even")
    h = (b-a)/n
    acc = f(a) + f(b)
    acc += 4.0*sum(f(a+i*h) for i in range(1,n,2))
    acc += 2.0*sum(f(a+i*h) for i in range(2,n,2))
    return acc*h/3.0


def converged_simpson(f, a: float, b: float, tol: float=1e-11, max_n: int=65536) -> float:
    if a == b:
        return 0.0
    n = 8
    prev = _composite_simpson(f,a,b,n)
    while n < max_n:
        n *= 2
        cur = _composite_simpson(f,a,b,n)
        err = abs(cur-prev)/15.0
        if err <= max(tol, tol*abs(cur)):
            return cur + (cur-prev)/15.0
        prev = cur
    raise RootCertificationBlocked("composite Simpson convergence exhausted")


def _pieces(f, pts, tol: float) -> float:
    p=sorted(set(float(x) for x in pts)); n=max(1,len(p)-1); total=0.0
    for a,b in zip(p,p[1:]):
        if b>a:
            total += converged_simpson(f,a,b,tol/n)
    return total


def mass_derivative(profile, x: float, R: float, tol: float=1e-11):
    if not 0.0 < x <= 1.0:
        raise ValueError("x outside (0,1]")
    knots=[0.0,1.0]+[r for r in profile.radius_fraction if 0.0<r<1.0]
    total=_pieces(lambda u:u*u*_interp_density(profile,u),knots,tol)
    if x == 1.0:
        return 4.0*math.pi*R**3*total,0.0
    top=math.acos(x)
    ts=[0.0,top]+[math.acos(x/r) for r in profile.radius_fraction if x<r<1.0]
    def omitted(theta: float) -> float:
        c=math.cos(theta); s=math.sin(theta); u=x/c
        return _interp_density(profile,u)*x**3*s*s/(c**4)
    mass=4.0*math.pi*R**3*(total-_pieces(omitted,ts,tol))
    def d_integrand(theta: float) -> float:
        c=math.cos(theta)
        return _interp_density(profile,x/c)/(c*c)
    dmass=4.0*math.pi*R**3*x*x*_pieces(d_integrand,ts,tol)
    return mass,dmass


def derivative(profile,x: float,z: float,R: float,tol: float=1e-11) -> float:
    mass,dmass=mass_derivative(profile,x,R,tol)
    focal=(x*R)**2*C_CGS*C_CGS/(4.0*G_CGS*mass)/AU_CM
    q=z/focal
    return 1.0+q-x*q*dmass/mass


def bisect(fn,lo: float,hi: float,width: float=1e-12) -> float:
    fl,fh=fn(lo),fn(hi)
    if not(math.isfinite(fl) and math.isfinite(fh)) or fl*fh>0.0:
        raise RootCertificationBlocked("invalid sign bracket")
    if fl==0.0: return lo
    if fh==0.0: return hi
    while hi-lo>width:
        mid=(lo+hi)/2.0; fm=fn(mid)
        if not math.isfinite(fm): raise RootCertificationBlocked("nonfinite derivative")
        if fm==0.0: return mid
        if fl*fm<=0.0: hi,fh=mid,fm
        else: lo,fl=mid,fm
    return (lo+hi)/2.0


def roots(fn,grid):
    vals=[fn(x) for x in grid]
    if not all(math.isfinite(v) for v in vals):
        raise RootCertificationBlocked("nonfinite scan derivative")
    out=[]
    for lo,hi,fl,fh in zip(grid,grid[1:],vals,vals[1:]):
        if fl*fh<0.0:
            out.append(RootBracket(bisect(fn,lo,hi),lo,hi))
    return tuple(out)


def dyadic(grid,lo: float,hi: float):
    pts=[]
    for a,b in zip(grid,grid[1:]):
        if b<=lo or a>=hi: continue
        h=(b-a)/8.0
        for k in range(1,8):
            x=a+k*h
            if lo<x<hi: pts.append(x)
    return tuple(sorted(set(pts)))
