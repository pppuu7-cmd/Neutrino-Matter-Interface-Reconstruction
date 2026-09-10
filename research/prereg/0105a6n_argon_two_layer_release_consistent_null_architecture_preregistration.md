# 0105a6n — Ar two-layer release-consistent null-architecture gate

Status: **PREREGISTERED / NONDISCOVERY / NO FIT / TIER-B ARCHITECTURE ONLY**

## Purpose

Test whether the already-frozen COHERENT Ar public-release evidence supports a prospectively defined **Tier-B release-consistent reproduction architecture** that is distinct from the still-BLOCKED Tier-A exact collaboration-internal likelihood contract.

The specific hypothesis to test is:

> Analysis A can be represented for publication-benchmark reproduction as a two-layer procedure: (1) a central-value three-dimensional extended binned likelihood with normalization constraints and CEvNS profiling; followed by (2) discrete, separate systematic-excursion studies whose effects are treated as uncorrelated and combined after the statistical fit, rather than by an undocumented simultaneous continuous shape-morphing likelihood.

This gate performs no numerical likelihood evaluation and inspects no observed BSM residual.

## Frozen evidence scope

Primary/provider evidence:

1. exact COHERENT Ar measurement source `arXiv:2003.10630v7`, source payload SHA256 `2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114`;
2. exact official Ar data-release source `arXiv:2006.12659v2`, source payload SHA256 `5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde`;
3. 0105a3 exact 24-file Ar Zenodo byte-lock manifest SHA256 `5ccaea9ae1b59cb60d0db0a28b98a334d8fb32fb39a436301126a32fcd523091`;
4. exact-byte official-equivalent `LArParametersAnlA.yaml`, SHA256 `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`;
5. exact-byte official-equivalent `CENNS10AnlAEfficiency.txt`, SHA256 `21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2`.

Secondary corroboration only:

6. 0105a6m bounded evidence from the exact Zettlemoyer institutional dissertation, artifact `10160137826`, artifact ZIP SHA256 `df11b8726e52b3b1662509d3130bfab39c45bd298e5d21995a0613a375fa7d6b`, inner evidence SHA256 `672b8e5ec68e01395250e97fbafcbda956f8ffc51b52773d6379588b1fb87364`.

No other implementation or third-party likelihood source is allowed.

## Frozen architecture fields

### A1 — central statistical layer

PASS requires the evidence union to establish all of:

- three-dimensional Analysis-A fit in reconstructed energy, F90 and trigger time;
- binned likelihood semantics;
- extended maximum-likelihood semantics;
- central-value signal/background PDFs/templates;
- CEvNS normalization/profile parameter is not Gaussian-constrained to the SM prediction.

The elementary mathematical law may be supported by the provenance-qualified secondary-author dissertation, but this must be labelled secondary corroboration rather than official release authority.

### A2 — normalization-constraint layer

PASS requires explicit identification of the normalization treatment for the steady-state background, prompt BRN and delayed BRN, including which quantities carry Gaussian constraints and which signal quantity floats/profiles.

No missing normalization treatment may be inferred from RooFit defaults.

### A3 — shape-systematic architecture

PASS requires affirmative evidence that the published Analysis-A systematic treatment can be represented as **discrete excursion/alternative-fit studies outside the central-value likelihood**, rather than requiring an unknown simultaneous interpolation rule for the central fit.

Evidence must establish at least:

- provider release supplies systematic excursion/alternate PDFs or equivalent ±1σ shape variants;
- the variants are used in separate fits/studies rather than an undocumented simultaneous continuous nuisance morph;
- the resulting shape-systematic contributions are treated as independent/uncorrelated or otherwise have an explicit combination rule.

If the evidence instead requires continuous simultaneous morphing but does not document that morphing, A3 FAILS CLOSED.

### A4 — published statistic layer

PASS requires an explicit published statistical target chain sufficient for a future benchmark:

- best-fit CEvNS normalization/rate;
- profile/null statistic convention;
- statistical-only uncertainty/significance target;
- rule for incorporating the externally evaluated systematic error into the reported combined uncertainty/significance.

This gate does not test those numbers; it only establishes that the target definitions are unambiguous enough to freeze prospectively in the next numerical preregistration.

### A5 — `3152 ± 25` versus `3154 ± 25` conflict containment

This gate does **not** attempt to invent a precedence rule.

PASS requires that a future Tier-B reproduction can be made analyst-choice-free despite the conflict by freezing a **dual-anchor robustness fork** before numerical execution:

- branch R3152 uses steady-state prediction/constraint center `3152` with width `25` from the official release table;
- branch R3154 uses center `3154` with width `25` from the exact official release YAML / provenance-qualified secondary corroboration;
- identical data, templates, objective, nuisance rules, optimizer, tolerances and seeds are used in both branches;
- publication-benchmark closure is permitted only if both branches individually satisfy the same preregistered reproduction tolerances **and** their between-branch change in the benchmark quantities is below a prospectively frozen robustness threshold.

If the future result depends materially on choosing one anchor, Tier-B null reproduction must remain BLOCKED pending provider clarification. No post-result branch selection is permitted.

### A6 — authority separation

PASS requires explicit preservation of both statements:

- Tier-A exact collaboration-internal implementation remains `BLOCKED_0105A6I_ARGON_LIKELIHOOD_IMPLEMENTATION_AUTHORITY_INCOMPLETE`;
- any later Tier-B numerical result must be labelled `release-consistent independent reproduction`, not `exact collaboration likelihood reproduction`.

## Classification

`PASS_0105A6N_TWO_LAYER_RELEASE_CONSISTENT_NULL_ARCHITECTURE_NONDISCOVERY` only if A1–A6 all PASS.

Otherwise:

`BLOCKED_0105A6N_TWO_LAYER_RELEASE_CONSISTENT_NULL_ARCHITECTURE_INCOMPLETE`.

## Permission semantics

A PASS does **not** run a fit. It only sets:

- `TIERB_ARGON_NULL_PREREGISTRATION_PERMISSION_PERCENT = 100`

and leaves:

- `TIERA_EXACT_SM_NULL_REPRODUCTION_PERMISSION_PERCENT = 0`
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`.

A separate 0105a6o-style preregistration must freeze the exact Tier-B objective, data/template identities, nuisance parameters, dual-anchor robustness fork, optimizer, numerical tolerances and published-target acceptance criteria before any numerical evaluation.

## Hard prohibitions

- No observed residual or BSM/model-family scan.
- No numerical minimization or fit in this gate.
- No claim that lack of simultaneous morphing documentation is BSM evidence.
- No retroactive modification of 0105a6i, 0105a6l or 0105a6m.
- No selecting 3152 or 3154 after seeing numerical behavior.
- No third-party likelihood implementation as authority.
