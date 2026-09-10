# 0105a6o — Ar Tier-B release-consistent numerical null reproduction preregistration

Status: **PREREGISTERED / NO NUMERICAL EXECUTION YET / NONDISCOVERY**

Parent architecture gate: `PASS_0105A6N_TWO_LAYER_RELEASE_CONSISTENT_NULL_ARCHITECTURE_NONDISCOVERY`.

## Scientific purpose

Prospectively freeze a reproducible **Tier-B release-consistent independent reproduction** of COHERENT CENNS-10 Analysis A before any likelihood minimization is evaluated.

This is not a claim to reconstruct the collaboration-internal RooFit implementation. Tier-A remains historically BLOCKED at 0105a6i.

No observed BSM/model-agnostic residual may be inspected in this gate or its numerical child gate.

## Stage 0 — exact input authority prerequisite

Numerical execution is forbidden unless a separate content-addressed transport gate reconstructs the exact official bytes of every required release file using the historical 0105a3 size+MD5+SHA256 identities.

Required central files:

- `datanobkgsub.txt`: SHA256 `dabf3d80f13959f4b94b77c9b56f7347a645105801e8cc177424e7ffcf7c7f66`;
- `cevnspdf.txt`: SHA256 `3b1d5b25749e8d8e1cfdf5c32e48f026ce4aafec0a80632b3a63273e6e0e1f37`;
- `brnpdf.txt`: SHA256 `02664ce6a84eca8c6146b6502497bc5d8165df945da132193622334ff4ff826f`;
- `delbrnpdf.txt`: SHA256 `ebccca6c1650b0ace71fdbaade7a80ea289a99ff3c120266ae6ecf0083df5c63`;
- `bkgpdf.txt`: SHA256 `36c89291dde3032a19ca7a8e64510d036d7b40c34b0805ce475a13ccfa739dd1`;
- `LArParametersAnlA.yaml`: SHA256 `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`.

Required shape-systematic files for the later external-excursion stage:

- `brnpdf+1sigBRNTimingMean.txt`: SHA256 `7f06099e1bba0d2e328555c61cb255bb290607a44202327d29eb3ae3e05c1cd5`;
- `brnpdf-1sigBRNTimingMean.txt`: SHA256 `b5c1c8d0cb8b2319d093d38418da5ac2ccda59108755fb23e7f4a559cfe154f8`;
- `brnpdf+1sigEnergy.txt`: SHA256 `fb6fdaf99c9941653d33e1a909d8000b81c1ee9bb8e8ad3bf31839561faf6661`;
- `brnpdf-1sigEnergy.txt`: SHA256 `20bcad29e716f3fb0f1e9eeb8ffb049b4b3d8b3b3a150800b9c8711e2b177be6`;
- `brnpdfBRNTimingWidthSyst.txt`: SHA256 `304dba1553989d7c0cd3f745df9731a5306ec07ecc1044c20efbe2952707b270`;
- `cevnspdf+1sigF90.txt`: SHA256 `308f78e19b7fb3e54399dc29c207bd2a89b91825df5309d48068a3495e1c92e2`;
- `cevnspdf-1sigF90.txt`: SHA256 `b4e8071f87aa22a562e0c00654a0989915251acf2c7e569068b9b78c3ae5ac35`;
- `cevnspdfCEvNSTimingMeanSyst.txt`: SHA256 `3170dafd4cf44df35bde0795e1245606d8144c05f3e50f015648c57bcdba97f5`.

No file whose exact official byte identity cannot be reconstructed is numerically usable.

## Stage 1 — parser and structural gates (before minimization)

All five central 3D arrays must parse as the same 960 coordinate tuples corresponding to 12 energy × 8 F90 × 10 trigger-time bins.

Frozen coordinates:

- energy centers: `5, 15, ..., 115` keVee;
- F90 centers: `0.525, 0.575, ..., 0.875`;
- trigger-time centers: `0.15, 0.65, ..., 4.65` μs.

The data fourth column is interpreted as observed on-beam count per bin. The signal/background fourth columns are released nominal expected-event contributions per bin, consistent with the provider statement that each PDF text file is normalized to its Analysis-A central-value prediction.

Required pre-fit checks:

1. all values finite; data and nominal template values non-negative;
2. all coordinate grids identical with no tolerance repair;
3. `sum(datanobkgsub) = 3752` within `1e-9` absolute parser tolerance;
4. each nominal template sum agrees with its frozen release central-value prediction to `<= 0.05` event absolute tolerance:
   - CEvNS 128;
   - prompt BRN 497;
   - delayed BRN 33;
   - steady-state branch-dependent nominal anchor handled below.

If a template total fails this structural criterion, numerical fitting is BLOCKED rather than silently renormalized from an unexplained file convention.

## Stage 2 — frozen central-value Tier-B likelihood

Each released template is converted to a unit-sum shape only after its Stage-1 nominal-total check passes:

`S_i = cevns_i / sum(cevns)`

`P_i = prompt_i / sum(prompt)`

`D_i = delayed_i / sum(delayed)`

`B_i = steady_i / sum(steady)`.

For event-count parameters `N_C, N_P, N_D, N_B`, the expected bin count is

`mu_i = N_C*S_i + N_P*P_i + N_D*D_i + N_B*B_i`.

The frozen objective (constant terms omitted) is

`Q = -2 ln L = 2 * sum_i [mu_i - n_i*ln(mu_i)] + ((N_P-497)/160)^2 + ((N_D-33)/33)^2 + ((N_B-B0)/25)^2`.

Conventions:

- bins with `n_i=0` contribute `2*mu_i`;
- any candidate with `mu_i <= 0` in a bin having `n_i>0` has `Q=+infinity`;
- `N_C >= 0`, `N_P >= 0`, `N_D >= 0`, `N_B >= 0`;
- CEvNS has no Gaussian penalty to its SM prediction in the fit;
- prompt, delayed and steady-state normalizations are profiled under the displayed Gaussian constraints.

This is explicitly a Tier-B binned extended likelihood chosen prospectively from the release-consistent architecture. It is not relabeled as the exact internal RooFit likelihood.

## Stage 3 — mandatory unresolved-steady-state dual-anchor fork

Two branches are executed with identical bytes, shapes, objective, bounds, starts, optimizer and tolerances. They differ only in the steady-state Gaussian center:

- `R3152`: `B0 = 3152`, `sigma_B = 25` (official release Table 2);
- `R3154`: `B0 = 3154`, `sigma_B = 25` (exact official release YAML; independently corroborated in the provenance-qualified thesis).

No branch may be selected after seeing the numerical result.

The steady-state template itself must pass a branch-independent shape-integrity test. If its raw total equals one of the provider anchors rather than both, the file is still converted to unit shape after the raw-total is recorded; the branch-specific event-count center is applied only through `N_B` and its Gaussian constraint. This avoids changing shape bytes between branches.

## Stage 4 — deterministic minimization

Primary minimizer: `scipy.optimize.minimize(method='L-BFGS-B')` with bounds `[0, +inf)` for all four normalizations.

Frozen settings:

- `ftol = 1e-12`;
- `gtol = 1e-9`;
- `maxiter = 20000`;
- no random initialization.

Run from all deterministic start vectors:

1. `[128, 497, 33, B0]`;
2. `[159, 553, 10, 3131]`;
3. `[0, 497, 33, B0]`;
4. `[256, 497, 33, B0]`.

Take the converged finite solution with minimum Q. All successful starts must agree in every fitted normalization within `1e-4` event and in Q within `1e-7`; otherwise classify optimizer instability BLOCKED.

Independent cross-check minimizer: `scipy.optimize.minimize(method='Powell')`, bounds `[0,+inf)`, `xtol=1e-10`, `ftol=1e-12`, `maxiter=50000`, initialized at the primary optimum. It must agree with the primary solution within `0.02` event per fitted normalization and `1e-5` in Q.

## Stage 5 — null and profile-statistical uncertainty

Best fit: all four normalizations profiled subject to Stage-2 rules.

Null fit: fix `N_C = 0` and profile `N_P,N_D,N_B` with identical constraints and numerical criteria.

Define

`q0 = Q_null - Q_best`, `Z_stat = sqrt(max(q0,0))`.

For the CEvNS 1σ statistical profile interval, fix `N_C` and profile all three backgrounds; solve the lower and upper crossings of

`Q_profile(N_C) - Q_best = 1`

using deterministic bracketing + Brent root solving with root tolerance `1e-6` event. If the lower crossing is below the physical boundary, report the boundary behavior explicitly rather than extrapolating through `N_C<0`.

## Stage 6 — central-fit publication targets

Each R3152/R3154 branch must independently satisfy all of:

- best-fit CEvNS: `|N_C - 159| <= 2.0` events;
- best-fit prompt BRN: `|N_P - 553| <= 3.0` events;
- best-fit delayed BRN: `|N_D - 10| <= 3.0` events;
- best-fit steady-state: `|N_B - 3131| <= 3.0` events;
- CEvNS profile 1σ half-width, defined as `(upper-lower)/2`: `|sigma_profile - 43| <= 2.0` events;
- `|Z_stat - 3.9| <= 0.15`.

These tolerances are frozen before numerical evaluation and are intentionally tighter than the scientific uncertainty but wider than printed rounding/numerical optimizer noise.

## Stage 7 — mandatory dual-anchor robustness thresholds

After both branches independently satisfy Stage 6, require between R3152 and R3154:

- `|ΔN_C| <= 1.0` event;
- `|ΔN_P| <= 1.0` event;
- `|ΔN_D| <= 1.0` event;
- `|ΔZ_stat| <= 0.05`;
- absolute difference in CEvNS profile 1σ half-width `<= 0.5` event.

If any robustness threshold fails, Tier-B reproduction remains BLOCKED pending provider clarification of 3152/3154. Post-result branch selection is forbidden.

## Stage 8 — shape-systematic reproduction is a separate child stage

The central/null reproduction may be classified independently of the later systematic-excursion reproduction. The latter must use the exact official ±1σ excursion bytes and the published two-layer procedure; it may not inject a continuous shape-morph nuisance into the central likelihood.

Before any pseudo-data generation, a separate child preregistration must freeze:

- each excursion-pair interpretation;
- exact pseudo-data generation law;
- deterministic PRNG algorithm and seeds;
- number of pseudo-experiments (publication method states 10,000 per excursion study);
- estimator of mean shift for each systematic source;
- rule for pairing one-sided/two-sided excursions;
- quadrature combination and acceptance target around the published `14` event systematic uncertainty.

Therefore a central-fit PASS does not yet imply the full systematic layer is reproduced.

## Numerical child classification

A future execution gate may classify:

- `PASS_0105A6O_TIERB_ARGON_CENTRAL_NULL_REPRODUCTION_NONDISCOVERY` only if Stage 0–7 all PASS;
- otherwise one of explicit `BLOCKED_*` classes for input authority, structural schema, optimizer consistency, publication-target mismatch, or dual-anchor sensitivity.

A central/null PASS permits preparation of the separate systematic-excursion gate only. It does **not** permit observed BSM residual inspection.

## Authority and discovery ceiling

Always:

- `tierA_exact_collaboration_internal_likelihood = BLOCKED`;
- Tier-B label = `release-consistent independent reproduction`;
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`;
- no BSM/model-family inference from a reproduction mismatch.
