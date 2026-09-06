# Iteration 0040 — passive metastable / avalanche trigger gate

Date: 2026-09-06
Funnel gate: G2 / F0-F6
Prospective contract: `research/metastable_avalanche_prereg.md`
Prereg commit: `96e101b811838cc12e6bbcf788a6524c637c4fa7`
Scientific workflow head: `249aaeee4a1f841a4c97519b1b7e4ea4db234f1d`
Hosted run: `34048287780`
Hosted job: `101527189597`
Artifact: `9993764694`
Artifact ZIP SHA256: `c9221192087c1d38171fc849e2ff5bb44e3f5f76859c6fa12fb89e9ed8e4f619`

## Question
Can a passive metastable/non-convex medium turn a tiny neutrino interaction into a macroscopically large output, and does that output count as amplified neutrino-supplied energy or as release of stored medium free energy?

## General source-resolved first-law ledger
Let the metastable medium store releasable free energy

`DeltaF_store = F_m - F_s >= 0`.

Let a neutrino deposit trigger energy `epsilon_nu`, with NMIR guard

`0 <= epsilon_nu <= E_nu`.

With optional external assist `epsilon_assist`, an ideal triggered relaxation may output

`E_out,total = epsilon_nu + epsilon_assist + DeltaF_store`,

but the source ledger is

`E_out,nu = epsilon_nu`,
`E_out,assist = epsilon_assist`,
`E_out,medium = DeltaF_store`.

Therefore a signal gain

`G_signal = E_out,total / epsilon_nu`

may be enormous, while the neutrino-energy gain obeys

`G_nu-energy = E_out,nu / epsilon_nu <= 1`.

For cyclic operation, resetting the reservoir requires ideal external work at least equal to the replenished `DeltaF_store` (more in a dissipative real device). That reset work cannot be attributed to neutrino power.

## Barrier guard
For a deterministic one-shot energy trigger without fluctuations or bias assistance,

`epsilon_nu >= DeltaF_barrier`.

If `epsilon_nu < DeltaF_barrier`, deterministic triggering fails. Thermal/quantum fluctuations or external bias can alter the switching probability, but their contribution/noise must be accounted independently.

## Hosted validation
Raw log inspected. Dedicated tests: `7 passed in 0.03s`.

Frozen control:
- `epsilon_nu = 1 eV`;
- stored release `DeltaF_store = 1 MeV`;
- barrier `0.5 eV`;
- signal output `1,000,001 eV`;
- **signal gain = `1,000,001`**;
- **neutrino-energy gain = `1.0`**;
- ideal reset work = `1 MeV`.

Stored-energy scan at fixed 1-eV trigger:
- store `1 eV` -> signal gain `2`;
- `1 keV` -> `1001`;
- `1 MeV` -> `1,000,001`;
- `1 GeV` -> `1,000,000,001`;
- neutrino-energy gain remains exactly `1.0` in every triggered case.

5000 randomized positive source ledgers:
- max source-ledger relative residual `2.220192245414529e-16`;
- max neutrino-energy gain `1.0`.

Sub-barrier no-assist control correctly did not trigger. Adding explicit `0.3 eV` assist to a `0.2 eV` neutrino trigger and `0.5 eV` barrier allowed the event, with assist energy retained explicitly in the source ledger.

## Classification
For neutrino energy harvesting:

**PASS_METASTABLE_AVALANCHE_LEDGER / STRONG-NEGATIVE scoped.**

A metastable avalanche cannot multiply neutrino-supplied energy; excess output is stored medium/external-assist energy.

For detection/control:

**PASS-SURVIVOR.**

A passive metastable medium can genuinely amplify a neutrino-triggered microscopic event into a macroscopically observable signal. This is not speculative in principle: superheated bubble chambers already use metastability, and scintillating noble-liquid bubble chambers are explicitly being developed for CEvNS.

## External reality check
- Baxter et al., Phys. Rev. Lett. 118, 231301 (2017): first scintillating xenon bubble chamber demonstration; nuclear recoils nucleate bubbles while electron-recoil backgrounds are strongly suppressed; technology proposed for CEvNS.
- SBC collaboration: liquid-noble bubble chambers target sub-keV CEvNS nuclear recoils. SBC-LAr10 is a 10-kg argon physics-scale device.
- APS Global Physics Summit 2026 report: SBC-LAr10 saw first bubbles in October 2025 and is designed to explore bubble thresholds as low as about `40 eV` during calibration. This 40-eV figure is a design/calibration target, not yet promoted by NMIR to a fully demonstrated stable physics threshold.

## New design consequence
For CEvNS, metastability does not increase the weak cross section but can greatly improve event observability if the recoil exceeds the nucleation threshold. Therefore the next NMIR step is a **source-opening threshold map**: compute exact CEvNS kinematic thresholds for Ar and other bubble-chamber targets, especially the boundary between pp, Be7, pep/CNO and B8 solar sources.

The dominant solar Be7 line is especially interesting because the proposed `~40 eV` Ar threshold lies almost exactly at its recoil endpoint once the known solar thermal shift/broadening of the line is included.
