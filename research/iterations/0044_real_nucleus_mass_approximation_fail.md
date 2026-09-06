# Iteration 0044 — real-nucleus full-solar CEvNS pilot: endpoint mass-approximation FAIL

Date: 2026-09-06
Gate: G2 / F3–F7
Status: **SCIENTIFIC/APPROXIMATION FAIL — frozen `M=A m_u` convention is inadequate at the 40-eV Ar-40 Be7 endpoint control**

## Prospective contract
Authority: `research/cevns_real_nucleus_solar_optimization_prereg.md`.
The frozen contract required the no-Helm Ar-40 dominant-Be7 calculation to reproduce iteration 0042 at 10, 20 and 40 eV within 1%, while prospectively using the broad-scan mass convention `M=A m_u`.

## What failed
Baseline CI run `34051556950`, job `101535983266`, raw full-suite result: `1 failed, 267 passed`.
The single failing prospective regression was the 40-eV Ar-40 dominant-Be7 no-Helm rate:

- iteration-0042 exact-isotope-mass authority: `3.973604373087567e-08 events/(kg day)`;
- 0044 `M=40 u` approximation: `2.7813779481704556e-08 events/(kg day)`.

Ratio `0044/0042 ≈ 0.700`, i.e. roughly a 30% endpoint-rate shift, far outside the frozen 1% criterion.

The dedicated 0044 workflow run `34051573524`, job `101536027748`, also stopped at this frozen regression before the full solar ranking, so no target ranking from this version is scientifically valid.

## Why this is a scientific approximation failure rather than a criterion to relax
At 40 eV the Ar-40 dominant-Be7 rate is sourced from a tiny recoil phase-space sliver. The difference between `A=40` and the physical atomic mass `39.9623831237 u` is small in fractional mass, but moves the recoil endpoint enough to change that tiny surviving phase-space fraction by order tens of percent.

Thus the prospective endpoint control did exactly what it was meant to do: it falsified the assumption that integer `A m_u` masses are harmless for the full threshold grid.

The 1% criterion is **not changed** and the failed result is retained.

## Corrective action fixed after FAIL
A new prospective iteration must:
1. use independently sourced exact isotopic atomic masses for every frozen candidate nucleus;
2. freeze those masses locally in the repository with provenance;
3. use exact atomic mass both for recoil kinematics and targets/kg;
4. retain the same physical source set, weak-charge convention, Helm response and 1% Ar-40/iteration-0042 endpoint regression;
5. not inspect or publish a full target ranking until the corrected prospective regression passes.

NIST Atomic Weights and Isotopic Compositions is selected as the mass authority for the corrected iteration. The correction is physically motivated by the failed endpoint sensitivity; it is not a post-hoc relaxation of the gate.

## Readiness accounting
No scientific-readiness credit is awarded for this failed pilot. The failure improves methodology/provenance but `NMIR_READINESS` remains **73%** until a corrected prospective real-nucleus optimization closes.
