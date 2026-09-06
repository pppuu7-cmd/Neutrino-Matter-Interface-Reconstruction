# Iteration 0060 — genuinely long-range/growing-coordination Standard-Model operator audit

Date: 2026-09-07
Gate: G3 / F5-F6 residual outside bounded finite-range k-local closure
Scientific classification: `PASS_NO_SM_GROWING_COORDINATION_SURVIVOR`

## Prospective authority
Contract: `research/prereg/0060_long_range_sm_operator_scaling_audit.md`.
Preregistration commit: `3a52dc988cfb9ee05c9bf826fd316f636c923573`.
Frozen machine-readable evidence ledger: `data/g3_long_range_sm_operator_authority_0060.json`, created in commit `6490768312affbd9f1f213bb2da7db1cb8f26285`.

This is an analytic/primary-authority audit. No numerical workflow artifact is the scientific authority. Baseline CI run `34065084111` on the preregistration head completed SUCCESS and is infrastructure-only.

## Frozen scaling criterion
At fixed number density `rho`, for a pair/range kernel `K(r)` define

`I(R) = rho * integral_{r0}^{R} 4*pi*r^2*|K(r)| dr`.

For a Yukawa kernel

`K(r)=C exp(-m r)/r`, `m>0`,

one obtains

`I(R)=4*pi*rho*|C|*[exp(-m*r0)*(1+m*r0)-exp(-m*R)*(1+m*R)]/m^2`,

so `I(R)` approaches a finite constant as `R -> infinity`. Therefore any actual massive-mediator or exponentially screened kernel has fixed per-site integrated coordination in the thermodynamic limit.

## Operator inventory and findings

### 1. Direct W/Z electroweak exchange
PDG authority gives electroweak gauge-boson masses near `mW=80.3692 GeV` and `mZ=91.1876 GeV`. Their Compton ranges are approximately

- `hbar c / mW = 0.002455 fm`,
- `hbar c / mZ = 0.002164 fm`.

Thus direct W/Z exchange is extremely short-range. At nuclear/condensed-matter momentum transfers the propagators reduce to the ordinary local Fermi weak interaction. `I(R)` saturates; there is no growing-coordination loophole.

Primary authority: Particle Data Group 2026 W-mass review and Z listing.

### 2. Pion-range and multipion nuclear electroweak currents
Krebs, Epelbaum and Meissner derive renormalized one-, two- and three-nucleon axial currents in chiral EFT and include pion-pole / pion-exchange structure plus contact operators. A representative one-pion range is `hbar c / m_pi ~= 1.41 fm`.

Massive pion exchange therefore has exponential/Yukawa falloff and finite `I(infinity)`. Multi-pion pieces are not longer-ranged than a massless field. Contact pieces are not a growing-coordination mechanism and remain instead the independent absolute-coefficient residual isolated by iteration 0059.

Primary authority: arXiv:1610.03569.

### 3. Standard-Model neutrino electromagnetic properties
A massive Dirac neutrino in the minimally massive Standard-Model extension has a loop-induced magnetic moment (Fujikawa–Shrock). This is the one genuine photon-pole structure in the audited neutrino vertex, but its coupling is fixed by the tiny neutrino mass scale rather than being a free BSM enhancement.

For the charge-radius/anapole-type SM contribution, the effective neutrino electromagnetic form factor is proportional to `q^2` at low momentum transfer. The photon `1/q^2` propagator is therefore cancelled in the effective amplitude: this component is contact-like for the present long-range criterion rather than an unscreened `1/r` pair interaction.

The magnetic-moment photon channel can interact with macroscopic electromagnetic fields, but that does not create a new free passive collective response. Any coherent macroscopic field must carry its own electromagnetic field energy/current-source budget; NMIR already separately closes passive stable field/mediator free-gain claims in iterations 0031/0032/0038/0039. Thus the massless photon does not supply an *unclosed* superextensive neutrino-sourced passive gain under the preregistered survivor criterion.

Primary authorities: Fujikawa & Shrock, PRL 45, 963 (1980); Degrassi & Sirlin, PRD 39, 287 (1989); Bernabeu et al., PRD 62, 113012 (2000).

### 4. Collective correlations and criticality
A large matter correlation length is not itself a new microscopic neutrino interaction kernel. With the underlying SM weak kernel still finite-range/local, fixed-density cluster/saturation behavior and the already validated density/spin sum-rule and finite-range k-local bounds remain the relevant no-free-lunch constraints. Critical response can redistribute spectral weight or improve detectability, but it does not by itself create growing microscopic weak coordination or neutrino-sourced energy.

### 5. Other massless Standard-Model fields
The photon is the only relevant massless SM gauge field. Gluons are confined within hadrons and do not furnish a macroscopic neutrino-matter long-range vertex. Gravity is not part of the Standard Model operator inventory and is tracked separately under G9 focusing. No additional SM massless mediator satisfying the preregistered passive-response survivor criterion was identified.

## Prospective criterion check
The preregistration permits `PASS_NO_SM_GROWING_COORDINATION_SURVIVOR` if every audited actual SM class either:

1. has finite range/screening making `I(R)` saturate;
2. is already constrained by an extensive absolute energy/sum-rule budget; or
3. has a structure that does not realize the hypothesized passive nuclear/matter gain.

All frozen classes satisfy at least one of these conditions. No actual unclosed Standard-Model operator was found with growing per-site coordination at fixed density that could support free superextensive passive response.

Therefore the prospective classification is

`PASS_NO_SM_GROWING_COORDINATION_SURVIVOR`.

## Scope / anti-overclaim
This is **not** a universal theorem about every conceivable QFT operator. It closes the explicitly preregistered actual-SM operator inventory relevant to passive NMIR matter interfaces.

It also does **not** close iteration 0059's separate absolute contact-current coefficient residual. A contact operator can have uncertain absolute coefficient while still being local and non-growing in coordination. These are distinct questions.

The Standard-Model neutrino magnetic moment is not promoted to a useful engineering mechanism; its existence only ensures the photon class was not ignored. Any large magnetic moment beyond the minimal mass-linked SM expectation is BSM and remains locked.

## Scientific consequence
The genuinely long-range/growing-coordination loophole left outside iteration 0047 is now closed in the audited passive-SM scope. G3 therefore retains only the absolute short-range/contact coefficient residual from 0059 rather than a separate collective-scaling loophole.

Per the frozen next-action rule, the next independent highest-value survivor should move away from another generic G3 scaling toy model. G9 distant-source gravitational focusing utility is now preferred unless G8's thermal-solar anti-neutrino spectrum plus independently evaluated entrance-strength blockers have become resolvable.

## Provenance
- Preregistration commit: `3a52dc988cfb9ee05c9bf826fd316f636c923573`.
- Evidence-ledger commit: `6490768312affbd9f1f213bb2da7db1cb8f26285`.
- Baseline CI on prereg head: run `34065084111`, SUCCESS — infrastructure evidence only.
- Scientific authority: frozen primary-source ledger and analytic kernel scaling above; no hosted numerical artifact applies.

## Exact next gate
Reconcile `RECOVERY.md` and `NMIR_FUNNEL.md` through 0060, then preregister the next independent survivor. Preferred gate: G9 distant-source physical focusing utility — freeze one real distant neutrino source class and quantify unlensed flux, transparent-Sun lens geometry, finite source size, alignment probability/duty cycle, receiver-integrated magnification and net event/W/kg effect without multiplying any unvalidated gain.
