"""Nonsingular independent derivative locator for frozen NMIR 0088."""
from __future__ import annotations
from dataclasses import dataclass
import math
from .gravity_extended import AU_CM,C_CGS,G_CGS,_interp_density

class RootCertificationBlocked(ValueError): pass
@dataclass(frozen=True)
class RootBracket:
    root: float; lo: float; hi: float

def simpson(f,a,b,tol=1e-11,depth=30):
    def S(x0,x1):
        m=(x0+x1)/2; a0,am,a1=f(x0),f(m),f(x1)
        return (x1-x0)*(a0+4*am+a1)/6,a0,am,a1
    whole,f0,fm,f1=S(a,b)
    def rec(x0,x1,y0,ym,y1,s,atol,n):
        m=(x0+x1)/2; l=(x0+m)/2; r=(m+x1)/2; fl,fr=f(l),f(r)
        sl=(m-x0)*(y0+4*fl+ym)/6; sr=(x1-m)*(ym+4*fr+y1)/6; s2=sl+sr
        if abs(s2-s)/15<=max(atol,tol*abs(s2)): return s2+(s2-s)/15
        if n<=0: raise RootCertificationBlocked("adaptive Simpson depth exhausted")
        return rec(x0,m,y0,fl,ym,sl,atol/2,n-1)+rec(m,x1,ym,fr,y1,sr,atol/2,n-1)
    return 0.0 if a==b else rec(a,b,f0,fm,f1,whole,tol,depth)

def pieces(f,pts,tol):
    p=sorted(set(pts)); n=max(1,len(p)-1)
    return sum(simpson(f,a,b,tol/n) for a,b in zip(p,p[1:]) if b>a)

def mass_derivative(profile,x,R,tol=1e-11):
    if not 0<x<=1: raise ValueError("x outside (0,1]")
    knots=[0.0,1.0]+[r for r in profile.radius_fraction if 0<r<1]
    total=pieces(lambda u:u*u*_interp_density(profile,u),knots,tol)
    if x==1: return 4*math.pi*R**3*total,0.0
    top=math.acos(x); ts=[0.0,top]+[math.acos(x/r) for r in profile.radius_fraction if x<r<1]
    def omitted(t):
        c=math.cos(t); s=math.sin(t)
        return _interp_density(profile,x/c)*x**3*s*s/c**4
    mass=4*math.pi*R**3*(total-pieces(omitted,ts,tol))
    d=pieces(lambda t:_interp_density(profile,x/math.cos(t))/math.cos(t)**2,ts,tol)
    return mass,4*math.pi*R**3*x*x*d

def derivative(profile,x,z,R,tol=1e-11):
    m,dm=mass_derivative(profile,x,R,tol); F=(x*R)**2*C_CGS*C_CGS/(4*G_CGS*m)/AU_CM; q=z/F
    return 1+q-x*q*dm/m

def bisect(fn,lo,hi,width=1e-12):
    fl,fh=fn(lo),fn(hi)
    if not(math.isfinite(fl) and math.isfinite(fh)) or fl*fh>0: raise RootCertificationBlocked("invalid sign bracket")
    while hi-lo>width:
        m=(lo+hi)/2; fm=fn(m)
        if fl*fm<=0: hi,fh=m,fm
        else: lo,fl=m,fm
    return (lo+hi)/2

def roots(fn,grid):
    vals=[fn(x) for x in grid]; out=[]
    if not all(math.isfinite(v) for v in vals): raise RootCertificationBlocked("nonfinite scan derivative")
    for lo,hi,fl,fh in zip(grid,grid[1:],vals,vals[1:]):
        if fl*fh<0: out.append(RootBracket(bisect(fn,lo,hi),lo,hi))
    return tuple(out)
def dyadic(grid,lo,hi):
    pts=[]
    for a,b in zip(grid,grid[1:]):
        if b<=lo or a>=hi: continue
        h=(b-a)/8
        for k in range(1,8):
            x=a+k*h
            if lo<x<hi: pts.append(x)
    return tuple(sorted(set(pts)))
