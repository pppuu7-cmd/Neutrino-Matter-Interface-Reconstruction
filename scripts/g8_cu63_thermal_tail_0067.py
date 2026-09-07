#!/usr/bin/env python3
import hashlib, json, math, urllib.request
import numpy as np

URL='https://www.sns.ias.edu/~jnb/SNdata/Export/Models/bp98stdmodel.dat'
E_BAR=0.162496486 # MeV
GF=1.1663787e-11 # MeV^-2
ALPHA=1/137.035999084
ME=0.51099895 # MeV
SIN2=0.2312
GV=-(1+4*SIN2); GA=-1.0
HBAR=6.582119569e-22 # MeV s
HBARC=1.973269804e-11 # MeV cm
KB=8.617333262e-11 # MeV/K
NA=6.02214076e23
RSUN=6.957e10 # cm
AU=1.495978707e13 # cm


def fd_ratio(ne_cm3,T):
    # Exact nonrelativistic Fermi correction n'_e/n_e from Haxton-Lin n'_e=∫f(1-f).
    nn=ne_cm3*HBARC**3
    pref=(2.0/math.pi**2)*(2*ME*T)**1.5
    target=nn/pref
    x=np.linspace(0,8,4001)
    def ints(eta):
        y=x*x-eta
        f=np.where(y>50,np.exp(-y),1/(np.exp(y)+1))
        i=np.trapezoid(x*x*f,x)
        ip=np.trapezoid(x*x*f*(1-f),x)
        return i,ip
    lo,hi=-20,10
    for _ in range(80):
        mid=(lo+hi)/2; val,_=ints(mid)
        if val<target: lo=mid
        else: hi=mid
    i,ip=ints((lo+hi)/2)
    return ip/i


def spectral_kernel(T,Ebar,n=6000):
    # Eq. (9), differential in Ebar; adaptive upper scale sufficient for Wien tail.
    emax=max(0.5, Ebar+60*T)
    e=np.linspace(0,emax,n)
    w=e+Ebar
    ng=1/np.expm1(w/T)
    y=ng*(e*e)*(Ebar*Ebar)/w*(w*w-(2/3)*e*Ebar)
    return np.trapezoid(y,e)


def parse(txt):
    rows=[]
    for line in txt.splitlines():
        s=line.strip().split()
        if len(s)==12:
            try: rows.append([float(v) for v in s])
            except ValueError: pass
    return np.array(rows)


def calc(rows,Ebar=E_BAR,kernel_n=6000):
    r=rows[:,1]*RSUN; temp=rows[:,2]; rho=rows[:,3]; X=rows[:,6]
    # electron molecular weight mu_e=2/(1+X), as in Haxton-Lin
    ne=NA*rho*(1+X)/2
    b=np.empty(len(r)+1); b[0]=0; b[-1]=RSUN
    b[1:-1]=(r[:-1]+r[1:])/2
    vol=4*math.pi/3*(b[1:]**3-b[:-1]**3)
    emiss=[]; ratios=[]
    coupling=GV*GV+5*GA*GA
    for n_e,TK in zip(ne,temp):
        T=KB*TK
        rat=fd_ratio(n_e,T); ratios.append(rat)
        nprime_nat=n_e*rat*HBARC**3
        C=nprime_nat*GF**2*ALPHA/(6*math.pi**4*ME**2)*coupling
        qnat=C*spectral_kernel(T,Ebar,kernel_n)
        qphys=qnat/(HBAR*HBARC**3) # cm^-3 s^-1 MeV^-1
        emiss.append(qphys)
    flux=float(np.sum(np.array(emiss)*vol)/(4*math.pi*AU**2))
    return flux,float(min(ratios)),float(max(ratios))

def main():
    raw=urllib.request.urlopen(URL,timeout=30).read(); txt=raw.decode()
    rows=parse(txt)
    f162,rmin,rmax=calc(rows,E_BAR,6000)
    f162_hi,_,_=calc(rows,E_BAR,12000)
    f005,_,_=calc(rows,0.005,6000)
    rel=abs(f162_hi-f162)/f162_hi
    out={'status':'PASS_SOURCE_TAIL_RECOMPUTED' if rel<1e-3 and 1e7<=f005<=1e10 else 'SCIENTIFIC_FAIL_MODEL',
         'bp98_url':URL,'bp98_sha256':hashlib.sha256(raw).hexdigest(),'rows':len(rows),
         'Ebar_MeV':E_BAR,'flux_162_cm-2_s-1_MeV-1':f162_hi,'flux_5keV_cm-2_s-1_MeV-1':f005,
         'grid_relative_change':rel,'fd_ratio_min':rmin,'fd_ratio_max':rmax,
         'authority':'Haxton-Lin Eq.(9), BP98 radial T,rho,X; ordinary Compton only (dominant >~5 keV)'}
    print(json.dumps(out,indent=2,sort_keys=True))
    if out['status']!='PASS_SOURCE_TAIL_RECOMPUTED': raise SystemExit(2)
if __name__=='__main__': main()
