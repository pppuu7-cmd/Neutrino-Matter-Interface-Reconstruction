# NMIR G2 preregistration — passive convex homogeneous nonlinear mediator gate

Date: 2026-09-06
Status: prospectively frozen before hosted benchmark inspection.

## Question
Can a passive nonlinear or idealized critical collective coordinate evade the linear mediator energy-budget gates and generate a parametrically superextensive neutrino-coupled response while keeping the medium/free-energy budget extensive?

## Scoped class
Let `V(x)` be differentiable, non-negative, strictly convex and positively p-homogeneous for a fixed `p>1`:

`V(t x)=t^p V(x)` for `t>=0`.

Couple an external collective source `b` linearly:

`H(x;b)=V(x)-b dot x`.

This includes the harmonic case `p=2` and idealized homogeneous Landau critical stabilizers such as a positive quartic mode `p=4`. It does NOT cover non-convex/multistable potentials, first-order switching, driven/active media, explicit time dependence, arbitrary mixtures of homogeneous degrees, higher-body fundamental neutrino interactions, BSM operators or gravity.

## Exact identity
At a stable minimizer `x*`, `grad V(x*)=b`. Euler's theorem for p-homogeneous differentiable functions gives

`x* dot grad V(x*) = p V(x*)`,

therefore

`b dot x* = p V(x*)`,

`H_min = V(x*) - b dot x* = -(p-1)V(x*)`.

Thus the magnitude of the induced effective interaction/free-energy lowering is exactly

`|E_induced|=(p-1) V(x*)`.

A nonlinear passive homogeneous mode can change the finite coefficient `p-1`, but cannot create a parametrically different energy scale from the stored medium/free-energy scale `V(x*)`.

## N scaling
For a scalar prototype `V=kappa |x|^p/p`, collective source `b_N=g_N o0 N`, and `g_N=g0/N^gamma`,

`|x*|=(|b_N|/kappa)^(1/(p-1))`,

`V(x*) propto N^[p(1-gamma)/(p-1)]`.

The free energy is extensive iff

`gamma=1/p`.

Then both stored field/free energy and induced interaction are O(N), so their per-particle values remain O(1). If `gamma<1/p`, the apparent response gain is accompanied by a superextensive medium/free-energy budget. If `gamma>1/p`, the per-particle response vanishes asymptotically.

## Frozen hosted checks
For `p in {2,3,4,6}`:
1. equilibrium stationarity residual `<1e-12`;
2. `|E_induced| / V = p-1` within `1e-12`;
3. source work / V = p within `1e-12`;
4. for `N1=1e3`, `N2=1e6`, `gamma=1/p`, stored and induced energy/particle gains equal 1 within `1e-12`;
5. for `gamma=0`, measured per-particle gain matches analytic `(N2/N1)^[(1)/(p-1)]` within `1e-12`;
6. p=2 reproduces the harmonic `gamma=1/2` scaling; p=4 reproduces the quartic critical `gamma=1/4` scaling and `|E_induced|/V=3`.

## Classification contract
- `PASS_NONLINEAR_HOMOGENEOUS_BUDGET` if all exact/numerical checks pass.
- Scientific interpretation: **STRONG-NEGATIVE scoped** against free parametric N-gain from passive stable convex p-homogeneous nonlinear/critical mediators at fixed extensive free-energy budget.
- Non-convex/multistable, mixed-degree crossover, driven/active and truly higher-body neutrino-coupling classes remain OPEN regardless of PASS.
