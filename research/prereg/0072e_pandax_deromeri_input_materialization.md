# NMIR 0072e preregistration — PandaX-4T / De Romeri primary-input materialization audit

Date frozen: 2026-09-07
Parent: 0072 B-L primary-contour materialization.
Trigger: 0072d preserved Wagner as a partial primary materialization but scientifically failed to resolve the EW/EW94/EW99 blue identities under the prospectively frozen rule. The frozen decision tree therefore switches to the independent PandaX-4T likelihood-reproduction route.

## Scientific question
Can the PandaX-4T-only B-L analysis of De Romeri, Papoulias & Ternes, JHEP 05 (2024) 165 (arXiv:2402.05506), be reproduced without manual plot reading and without silently substituting later PandaX data?

This gate audits/materializes the exact inputs only. It does **not** fit or scan `g_BL` and cannot produce an exclusion contour.

## Frozen primary authorities
1. Analysis formalism: De Romeri, Papoulias & Ternes, JHEP 05 (2024) 165, arXiv:2402.05506.
2. PandaX dataset/detector/background authority used by that paper: PandaX Collaboration, *Search for Light Fermionic Dark Matter Absorption on Electrons in PandaX-4T*, PRL 129 (2022) 161804, arXiv:2206.02339 (`Ref. [11]`).
3. Atomic-xenon ionization/effective-electron authority named by De Romeri: Chen, Chi, Liu & Wu, Phys. Lett. B 774 (2017) 656, arXiv:1610.04177 (`Ref. [73]`).
4. Solar-flux uncertainty authority: Villante & Serenelli, Front. Astron. Space Sci. 7 (2021) 112, arXiv:2101.03077 (`Ref. [78]`), together with the already-frozen NMIR solar-spectrum authority where the same source component is used.

## Frozen interpretation of the De Romeri reference-order typo
JHEP lines corresponding to eq. (3.3) say backgrounds are extracted from refs. `[6,11,84]` for `LZ, XENONnT, PandaX-4T, respectively`. This cannot be literal: ref. [6] is XENONnT, ref. [11] is PandaX-4T and ref. [84] is LZ background determination. The immediately following nuisance statement explicitly assigns ref. [84] Table VI to LZ and ref. [11] Table I to PandaX-4T.

For **PandaX-only 0072e**, the frozen authority is therefore ref. [11] for PandaX data, detector response, component backgrounds and Table-I nuisance normalizations. Ref. [84] is forbidden as a PandaX input. This is a provenance correction, not a numerical choice.

## Frozen PandaX analysis facts from De Romeri
- exposure `E = 0.63 tonne*year` for PandaX-4T;
- analysis threshold `1 keV`, with detector efficiency becoming sizable only around a few keV;
- reconstructed data are taken from **Figure 3 of ref. [11]**;
- PandaX detector efficiency and energy resolution are taken from **ref. [11]**;
- PandaX background-normalization uncertainties are taken from **Table I of ref. [11]**;
- low-statistics likelihood is the Poisson deviance in eq. (3.4), with background normalization nuisances `alpha_i` and solar-flux nuisances `beta_i`;
- only pp and 7Be solar components enter the present-experiment E-nu-ES fold;
- for B-L, `Q_e=Q_nu=-1`, so `Q_e Q_nu = +1` in the tree-level vector shift of eq. (2.3);
- `sin^2(theta_W)=0.23857`; `sin^2(theta_23)=0.5` is used for the mu/tau split.

## Required materialized package for PASS
A `PASS_PANDAX_DEROMERI_INPUTS_MATERIALIZED` requires **all** of the following from primary-authority files/text, with hashes and provenance:

### A. Experimental bins/data
- exact Figure-3 PandaX reconstructed-energy bin edges over the range actually used by De Romeri;
- exact observed `D_k` per bin, recovered from an author numerical table/data release **or** a calibrated vector source asset. Raster/manual point reading is forbidden.

### B. Background spectra
- per-bin shapes/yields sufficient to construct every PandaX background component entering `R_k` in the De Romeri reproduction;
- Table-I nominal normalizations and fractional uncertainties for the corresponding components;
- components marked `Float` must remain unpenalized/free exactly as in the primary analysis.
A total-background curve alone is insufficient if De Romeri's nuisance treatment requires individually floating/penalized components.

### C. Efficiency and resolution
- detector efficiency `A(T_e)` from primary numerical data or a calibrated primary vector asset;
- energy-resolution function sufficient for the convolution. The explicit approximate `1 sigma` polynomial stated in ref. [11] is admissible if its units/variable convention are recovered exactly; no fitted replacement curve is allowed.

### D. Atomic response
- a reproducible xenon `Z_eff(T_e)` / equivalent step-response or atomic-ionization factor consistent with the quantity actually used in De Romeri eq. (2.1), with primary provenance to ref. [73] or an author-supplied numerical product. A plotted RRPA total rate is **not** automatically equivalent to `Z_eff(T_e)`.

### E. Solar/nuisance inputs
- pp and 7Be spectral/line inputs and the flux-normalization uncertainties used for the `beta_i` penalties, with an explicit map to the existing NMIR solar authority or ref. [78].

### F. Conventions
- exact PandaX energy variable convention for Figure 3 / efficiency / resolution;
- B-L charge convention and mediator denominator `2 m_e T_e + m_Z'^2`;
- exact exposure normalization and xenon target normalization.

## Allowed materialization routes
In priority order:
1. official/author machine-readable tables or data release matching the 2022 0.63 t yr dataset;
2. arXiv/APS/SCOAP source archive author data files;
3. calibrated vector extraction from an original author EPS/PDF/PS figure asset under a separately frozen coordinate-calibration contract;
4. analytic formulas/numerical tables printed in the primary article.

Raster digitization, secondary recreated curves, later PandaX datasets and hand-read plot values are forbidden scientific inputs.

## Prospective classifications
- `PASS_PANDAX_DEROMERI_INPUTS_MATERIALIZED`: all A-F are independently recoverable; next action is a **new preregistered** PandaX-only B-L likelihood reproduction and 90% CL contour validation.
- `PARTIAL_PASS_PANDAX_INPUTS`: a useful proper subset is primary/reproducible, but at least one indispensable A-F item is missing; no likelihood scan authorized.
- `BLOCKED_PANDAX_PRIMARY_DATA`: the necessary item exists only as a non-vector raster/plot or unreleased model product after allowed source routes are exhausted.
- `FAIL_INPUT_CONVENTION_MISMATCH`: primary products exist but cannot be mapped consistently to the De Romeri observable/likelihood without an additional unstated model assumption.
- `INFRASTRUCTURE_FAIL`: source archive/download/parser/runtime failure before the scientific availability question can be evaluated.

## First deterministic audit
Before any numerical extraction, inspect the arXiv source archives for `2206.02339`, `2402.05506`, and `1610.04177` and freeze:
- archive hashes;
- full member lists relevant to figures/data;
- asset formats and hashes;
- whether Figure 1 / Figure 3 of PandaX and the atomic-response figures/tables have vector or numerical source representations.
Also record whether the official PandaX public Data Release page exposes a dataset explicitly corresponding to PRL 129 (2022) 161804; do not infer equivalence from a later release.

## Guards
- 0072d negative result remains immutable; do not invent a post-hoc Wagner rescue.
- Green CI is infrastructure validation, not PASS.
- A newer PandaX public CSV package may motivate a later **updated-constraint** gate, but cannot substitute for the 2022 De Romeri reproduction in this gate.
- No B-L NMIR response/enhancement calculation until 0072 obtains enough primary constraint families to freeze an allowed region.
