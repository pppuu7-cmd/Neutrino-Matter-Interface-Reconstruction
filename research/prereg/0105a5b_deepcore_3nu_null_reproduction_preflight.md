# 0105a5b — DeepCore B4RITM standard-3nu/null reproduction preflight

Date frozen: 2026-09-10
Parent authority gate: 0105a4d
Scope: standard three-flavor atmospheric-neutrino reproduction only
Result dependence at freeze: no B4RITM scientific payload content has been parsed under this gate; only authority hashes and the public IceCube publication have been used to define this contract.

## Question

Can the exact byte-locked IceCube DeepCore `10.7910/DVN/B4RITM` release reproduce the collaboration's published standard three-flavor/null analysis behavior without any BSM term, post-result bin selection, nuisance deletion, ad-hoc normalization, or residual-guided tuning?

A PASS is a prerequisite for later residual work. A PASS is not evidence for BSM physics.

## Frozen authority hierarchy

1. Exact consumed bytes must match the 0105a4d byte ledger before scientific parsing.
2. The B4RITM `readme.md`, `example.ipynb` and byte-locked machine-readable files are computational authority for release-specific column meanings, weights, response functions, priors and intended reproduction procedure.
3. IceCube Collaboration, Phys. Rev. D 108, 012014 (2023), DOI `10.1103/PhysRevD.108.012014`, is authority for the published analysis definition and benchmark values.
4. If release documentation and publication differ in a material numerical convention and the difference cannot be resolved by an explicit release mapping, classify `BLOCKED_0105A5B_AUTHORITY_CONVENTION_CONFLICT`; do not silently choose the convention that fits better.
5. `10.7910/DVN/QKL28Z` remains forbidden as a substitute dataset.

## Frozen byte identities required before parsing

The 0105a4d manifest must reproduce exactly:

- dataset `10.7910/DVN/B4RITM`, release `1.0`, `RELEASED`;
- 11 consumed files;
- exactly 9 Saved Original CSV representations and 2 direct files;
- manifest SHA256 `e0c1d4d88234160b7ee443cea3d38979c84d4f9c3ac50dc12f815c60f7fdda1c`;
- 11 SHA256 values recorded in `research/iterations/0105a4d_deepcore_b4ritm_original_representation_byte_lock_result.md`.

Any hash mismatch is `BLOCKED_0105A5B_BYTE_AUTHORITY_MISMATCH` before a physics calculation.

## Frozen published analysis structure

Use all 200 published analysis bins:

- 10 reconstructed-energy bins, logarithmically spaced over 6.31–158.49 GeV, with the publication's wider last-bin convention;
- 10 reconstructed cosine-zenith bins over `[-1, 0.1]`;
- 2 PID bins: mixed (`0.55 <= PID < 0.75`) and track (`0.75 <= PID <= 1.0`) according to release boundary semantics.

No bin may be removed because it worsens agreement. No rebinning is permitted in the primary gate.

The publication's observed total is frozen as:

`N_observed = 21914`.

The publication's best-fit expected component totals are frozen as diagnostics:

- `nu_mu + anti-nu_mu CC = 17656`;
- `nu_e + anti-nu_e CC = 1820`;
- `nu_tau + anti-nu_tau CC = 603`;
- all-flavor NC = `1222`;
- atmospheric muons = `711`;
- total best-fit expectation = `22012`.

## Frozen objective

The primary fit uses the publication's modified chi-square over all bins,

\[
\chi^2_{\rm mod}
=\sum_i\frac{(N_i^{\rm exp}-N_i^{\rm obs})^2}
{N_i^{\rm exp}+(\sigma_i^{\rm sim})^2}
+\sum_j\frac{(s_j-\hat s_j)^2}{\sigma_{s_j}^2},
\]

with

\[
N_i^{\rm exp}=\sum_{e\in i}w_e,
\qquad
(\sigma_i^{\rm sim})^2=\sum_{e\in i}w_e^2+(\sigma_i^\mu)^2,
\]

and with release-authorized non-Gaussian/unconstrained treatment where the publication/release specifies no Gaussian penalty.

Do not replace this objective with a Poisson likelihood, Pearson chi-square, covariance chi-square, or generic least-squares objective in the primary reproduction gate.

## Frozen standard-3nu physics semantics

- normal mass ordering;
- three-flavor coherent matter propagation through Earth;
- 12-layer PREM approximation if a propagation calculation is required by the release workflow;
- electron-to-nucleon fraction `0.4656` in inner/outer core and `0.4957` in mantle;
- `delta_CP = 0`;
- `theta23` and atmospheric mass splitting are fit physics parameters;
- `theta12`, solar mass splitting and `theta13` are fixed exactly to the values encoded by the byte-locked release's intended reproduction implementation. The paper values are a cross-check. A release/paper discrepancy is not resolved post hoc by choosing whichever produces the closer best fit.

No NSI, sterile, magnetic-moment/spin-flavor, decay, decoherence or light-mediator term is permitted.

## Frozen nuisance scope

The primary fit must retain the publication/release nuisance directions corresponding to:

- 5 detector/calibration directions: DOM efficiency, relative optical-efficiency `p0`, relative optical-efficiency `p1`, ice absorption, ice scattering;
- 7 atmospheric-flux directions: spectral-index shift and the six retained meson-yield directions;
- 4 interaction/cross-section directions: CCQE axial-mass, CCRES axial-mass, NC/CC ratio and DIS-CSMS interpolation;
- atmospheric-muon scale;
- global effective-area/neutrino-rate scale.

That is 18 nuisance directions in addition to the two fitted atmospheric oscillation parameters, unless the byte-locked release explicitly documents an equivalent reparameterization. An equivalent release mapping must be recorded before minimization and may not change effective nuisance rank.

No nuisance direction may be deleted because it is inconvenient, weakly constrained or degenerates with the physics parameters.

## Frozen execution sequence

### R0 — byte re-verification
Re-fetch or materialize consumed release assets and verify every consumed SHA256 against 0105a4d before parsing.

### R1 — release-structure audit
After R0 PASS only, parse release documentation and schemas. Record exact columns, units, event-category encoding, systematic-response encoding, priors/bounds, weight construction and any release-provided reference output. Any missing quantity required for the frozen objective yields `BLOCKED_0105A5B_RELEASE_SEMANTICS_INCOMPLETE`.

### R2 — deterministic no-fit structural reproduction
Before minimization, reproduce:

- exactly 200 populated/defined analysis bins under the frozen binning;
- exactly `21914` observed events/counts;
- finite nonnegative nominal expectations and simulation-variance terms in all used bins;
- the complete frozen nuisance design/rank or an explicitly documented release-equivalent parameterization.

Failure here stops before optimization.

### R3 — standard-3nu profiled best-fit reproduction
Only after R2 PASS, minimize the frozen `chi2_mod` over the two atmospheric oscillation parameters and all authorized nuisance parameters.

The publication benchmark is:

\[
\sin^2\theta_{23}=0.51\pm0.05,
\qquad
\Delta m^2_{32}=(2.41\pm0.07)\times10^{-3}\ {\rm eV}^2.
\]

Primary predeclared best-fit acceptance windows are one-half of the published 68% half-widths:

- `abs(sin2_theta23_fit - 0.51) <= 0.025`;
- `abs(dm2_32_fit - 2.41e-3) <= 0.035e-3 eV^2`.

The total best-fit expectation must satisfy:

- `abs(N_expected_total - 22012) / 22012 <= 0.005`.

Component-total diagnostics must each agree within 2% for the four neutrino interaction groups and within 5% for atmospheric muons. Component diagnostics are required for PASS unless the release explicitly demonstrates that a published category is not reconstructible from the public machine-readable encoding; in that case the gate is BLOCKED rather than silently dropping the diagnostic.

The minimizer must converge from at least three deterministic, prospectively fixed starting points spanning both theta23 octants and the central region. All successful starts must reach objective values agreeing within `Delta chi2_mod <= 0.05`; otherwise classify `BLOCKED_0105A5B_OPTIMIZER_NONUNIQUENESS` and do not choose the most convenient minimum.

## Confidence-interval boundary

This gate does not claim reproduction of the collaboration's 68% confidence intervals merely from Wilks' theorem. The publication uses Feldman-Cousins for the quoted 68% intervals and reports a pseudo-experiment goodness-of-fit p-value of 26.1% based on 1000 trials.

If R3 passes, confidence-interval / pseudo-experiment calibration becomes a separate prospective child gate. A Wilks contour may be recorded only as a diagnostic and may not be called a collaboration-equivalent 68% interval.

## PASS / BLOCK / FAIL semantics

`PASS_0105A5B_DEEPCORE_3NU_NULL_REPRODUCTION_NONDISCOVERY` requires R0, R1, R2 and R3 all to pass exactly under this contract.

Use `BLOCKED` for missing release authority, representation/convention conflict, optimizer nonuniqueness, transport, or inability of the public release to reconstruct a required frozen quantity. Use `FAIL` only for a genuine numerical/scientific mismatch under a complete and correctly implemented frozen public-release authority. Infrastructure failures are not scientific FAILs.

## Explicit prohibitions

Before terminal classification of this gate:

- do not compute, plot, inspect or rank a BSM/model-agnostic residual;
- do not add an NSI or mediator parameter;
- do not remove a high-energy or otherwise inconvenient bin;
- do not rescale the observed or expected sample outside the frozen nuisance model;
- do not tune priors, bounds, starting points or acceptance tolerances after seeing the fit result;
- do not use `QKL28Z` to repair B4RITM;
- do not interpret a successful null reproduction as evidence against or for BSM.

`observed_residual_execution_allowed = false` throughout 0105a5b.
