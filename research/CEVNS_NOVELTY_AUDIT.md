# CEvNS inverse-design novelty audit

Last updated: 2026-09-06
Status: literature-distance audit; **no novelty claim is frozen**.

## Purpose

Prevent NMIR from presenting a generic target/threshold CEvNS optimization as novel. The project must distinguish prior art from the narrower structures actually produced by the prospectively validated funnel.

## Close prior art A — solar neutrinos in cryogenic detectors

A. Bento et al., **“Solar Neutrinos in Cryogenic Detectors”**, arXiv:2405.02482 (2024).

The work treats solar CEvNS as the signal in low-threshold cryogenic solid-state experiments and explicitly studies scenarios defined by **target material, energy threshold and exposure**, including sensitivity to pp, Be7 and CNO solar-neutrino fluxes. It discusses eV-scale thresholds and tonne-year-scale future exposures for materials such as CaWO4 and Al2O3.

Consequence for NMIR:

- “solar CEvNS depends on target material and threshold” is **not novel**;
- “eV-scale threshold helps access low-energy solar components” is **not novel**;
- a generic material/threshold/exposure scan must not be sold as an NMIR discovery.

Primary link: `https://arxiv.org/abs/2405.02482`.

## Close prior art B — detector-level target assessment

Y. Havvat, **“Detector-level assessment of alternative target nuclei for CEvNS experiments under realistic experimental conditions”**, arXiv:2602.22234 (2026).

This study propagates CEvNS recoil spectra for several target nuclei through detector effects including threshold, energy smearing/noise and selection efficiencies, with Geant4-based detector modeling. It emphasizes target-dependent observability rather than only underlying cross sections.

Consequence for NMIR:

- “compare target nuclei after a detector response” is **not novel**;
- response matrices / efficiency turn-on as such are **not novel**;
- future NMIR detector work must justify why its inverse requirement, source decomposition, or validated target/source phase topology adds something beyond a standard detector-response comparison.

Primary link: `https://arxiv.org/abs/2602.22234`.

## Additional nearby program — NUCLEUS / low-threshold multi-target CEvNS

The NUCLEUS program has long emphasized multi-target cryogenic calorimetry, with light and heavy target species and O(10 eV) thresholds, both for CEvNS observability and statistical background discrimination. This further excludes broad claims that matching target mass to low recoil thresholds is a new concept.

## What iteration 0045 actually adds internally

NMIR's validated 0045 result is narrower:

1. exact physical isotope masses are used in endpoint-sensitive recoil kinematics, after the prospectively frozen `M=A u` approximation failed by ~30% for Be7/Ar40 at 40 eV;
2. the objective folds the full frozen solar pp + both Be7 branches + pep + CNO + B8 + hep source set;
3. real target nuclei are ranked at fixed target kg with actual Z/N and Helm finite-size response;
4. the preregistered six-threshold scan produced a **re-entrant winner sequence** `Pb -> Xe -> Se -> Pb`, associated with a source transition from Be7-dominated to B8-dominated accepted recoils;
5. iteration 0046 was prospectively frozen specifically to test whether this is a stable target/source **phase topology** or merely under-resolved threshold sampling.

These points are internally new results of NMIR, but **literature novelty is not yet established**.

## Tentative publishable niche — not yet a claim

A potentially distinctive contribution would require all of the following to survive audit:

- a prospectively validated, refined **solar-source-dependent target/threshold phase diagram** rather than a few example materials;
- exact treatment of thermally broadened near-endpoint solar lines and exact isotope masses where relative rates are endpoint-sensitive;
- explicit separation of target/source crossover physics from weak-interaction enhancement;
- an **inverse detector requirement**: derive the acceptance/threshold/background performance required to preserve each ideal source/target phase, then compare that requirement with primary experimental transfer-function evidence;
- reproducible preregistration, raw hosted validation and immutable failure retention.

Before manuscript novelty language is frozen, search explicitly for prior papers containing all or most of: full pp/Be7/pep/CNO/B8/hep CEvNS target optimization, threshold-dependent optimum-target crossover maps, re-entrant heavy-target behavior, or inverse detector acceptance requirements.

## Current conclusion

**NOVELTY STATUS: OPEN / PARTIALLY DIFFERENTIATED.**

The generic optimization problem has strong prior art. NMIR should claim only the specific prospectively validated structures that survive iteration 0046 and the later detector-transfer audit, and only after a broader literature comparison finds no equivalent result.
