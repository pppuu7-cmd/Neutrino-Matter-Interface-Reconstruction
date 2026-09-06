# Iteration 0039 — passive convex homogeneous nonlinear mediator gate

Date: 2026-09-06
Funnel gate: G2 / F5-F6
Prospective contract: `research/nonlinear_homogeneous_mediator_prereg.md`
Prereg commit: `6849ff432ad277b07331a8e53db140c6e0fcb815`
Scientific workflow head: `79b63b24460ca06f002300de8275c198c34e1925`
Hosted run: `34048018268`
Hosted job: `101526462429`
Artifact: `9993688056`
Artifact ZIP SHA256: `7882c04acf1776652cb76f9920a695788091cac3ce6264b1056b3cad384d5cce`

## Question
Can a passive nonlinear or idealized critical collective coordinate evade the linear mediator energy-budget gates and generate a parametrically superextensive neutrino-coupled response while keeping the medium/free-energy budget extensive?

## Scoped class and exact identity
Let `V(x)` be differentiable, non-negative, strictly convex and positively p-homogeneous for fixed `p>1`:

`V(t x)=t^p V(x)`.

With a collective source `b`,

`H(x;b)=V(x)-b dot x`.

At the stable minimizer `x*`, `grad V(x*)=b`. Euler's theorem gives

`b dot x* = p V(x*)`,

hence

`H_min = -(p-1)V(x*)`,

and therefore

`|E_induced|=(p-1)V(x*)`.

Thus the nonlinearity changes only a finite coefficient for this class: the induced collective free-energy lowering has the same parametric scaling as the medium/free-energy budget itself.

## Collective N-scaling
For scalar prototype

`V=kappa |x|^p/p`, `b_N=g_N o0 N`, `g_N=g0/N^gamma`,

one finds

`V(x*) propto N^[p(1-gamma)/(p-1)]`.

Extensive total free energy requires

`gamma=1/p`.

At that scaling both stored and induced energy per particle are O(1). For `gamma<1/p`, apparent per-particle collective gain is accompanied by a superextensive medium/free-energy budget. For `gamma>1/p`, it decreases with N.

Controls:
- `p=2`: `gamma=1/2`, exactly matching the harmonic/Dicke gate;
- `p=4`: `gamma=1/4`, idealized quartic critical stabilizer, with `|E_induced|/V=3`.

## Hosted validation
Raw log inspected. Dedicated tests: `14 passed in 0.04s`.

Benchmark `N:1000 -> 1e6`:
- max Euler/stationarity identity absolute error: `1.7763568394002505e-15`;
- max extensive per-particle gain error from 1: `6.661338147750939e-16`;
- max unscaled analytic-gain relative error: `4.440892098500626e-16`.

Rows:
- `p=2`: unscaled per-particle gain `1000`, extensive gamma `0.5`, extensive gain `1.0`;
- `p=3`: unscaled gain `31.62277660`, extensive gamma `1/3`, extensive gain `~1.0`;
- `p=4`: unscaled gain `10.0`, extensive gamma `0.25`, extensive gain `1.0`, induced/stored `3.0`;
- `p=6`: unscaled gain `3.98107171`, extensive gamma `1/6`, extensive gain `~1.0`, induced/stored `5.0`.

## Classification
**PASS_NONLINEAR_HOMOGENEOUS_BUDGET / STRONG-NEGATIVE scoped.**

A passive stable convex fixed-p homogeneous nonlinear/critical mediator cannot provide free parametric N-gain at a fixed extensive free-energy budget. The apparent collective gain in an unscaled model is paid for by the same superextensive scaling of the medium/free-energy reservoir.

## Scope guards
This is not a theorem for non-convex/multistable media, first-order switching, mixed-degree crossover, driven/active media, explicitly time-dependent response, arbitrary critical fluctuations beyond this equilibrium homogeneous class, genuine higher-body neutrino interactions, BSM operators or gravity.

## Exact next survivor
The next G2 loophole is a passive **metastable/non-convex avalanche medium**. Such a medium can in principle use a tiny neutrino interaction to trigger a much larger release of stored free energy. The next gate must distinguish:
- useful event/control amplification, which may be enormous;
- neutrino-supplied deposited energy, which remains limited by the neutrino interaction;
- medium-supplied released energy, which must be debited from the stored free-energy reservoir.

This is a promising detector/amplifier concept even if it fails as a neutrino-energy-harvesting mechanism.
