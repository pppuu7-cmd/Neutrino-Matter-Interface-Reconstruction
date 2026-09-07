# Iteration 0073 — PandaX-4T / De Romeri B-L likelihood input materialization

Date: 2026-09-07
Classification: **`PARTIAL_PASS_PANDAX_INPUTS_NEED_ONE_NAMED_COMPONENT`**
Readiness credit: 0 percentage points.

## Prospective authority
Frozen before this audit in `research/prereg/0073_pandax_b_minus_l_likelihood_input_materialization.md`, commit `20ee0ab7cf4ab3d709c147a4826d4b24897cc83a`.

Primary/public authorities audited:
- De Romeri, Papoulias, Ternes, JHEP 05 (2024) 165, arXiv:2402.05506v2.
- PandaX Collaboration, D. Zhang et al., Phys. Rev. Lett. 129 (2022) 161804, arXiv:2206.02339v3.

## What is now independently materialized
De Romeri et al. explicitly define the current-experiment event-rate and statistical structure needed for a PandaX-only reproduction:

- PandaX exposure `0.63 ton*year`;
- solar E-nu-ES signal dominated by `pp` and `7Be` components in this analysis;
- reconstructed-bin rate Eq. (8), including efficiency, resolution, oscillated solar flux and the interaction cross section;
- total prediction Eq. (10) as signal plus individual backgrounds;
- PandaX observed spectrum taken from Fig. 3 of the PandaX primary paper;
- background-normalization uncertainties taken from PandaX Table I, with specified freely floating components;
- PandaX statistic Eq. (11), a Poisson least-squares profiled over background and solar-flux nuisance normalizations;
- published B-L constraints are 90% CL.

The PandaX primary HTML independently materializes the key Table-I nuisance inventory and several detector facts. It states 1058 selected data events, `1060 +- 46` total best-fit events, 30 one-keV bins for the displayed goodness-of-fit, and gives the approximate one-sigma reconstructed-energy resolution

`0.073 + 0.173 E_vis - 6.5e-3 E_vis^2 + 1.1e-4 E_vis^3`, with `E_vis` in keV,

with the additional instruction that the smeared spectrum must be corrected by the efficiency function in its Fig. 1.

Table-I entries relevant to the De-Romeri background-nuisance structure are persisted machine-readably in `data/pandax_likelihood_input_audit_0073.json`. In particular tritium is free-floating by data set; flat-ER has 9% normalization uncertainty; Xe136 16%; Xe127 L-shell 25%; accidental 20%; surface 25%; neutron 50%; B8 28%.

## Exact blocker remaining
The route is not yet executable fail-closed because the controlling **per-bin numerical spectrum information** has not yet been independently materialized. De Romeri et al. say they use the data from PandaX Fig. 3, but the accessible primary HTML exposes that figure as a figure rather than a numerical per-bin table. The audit has not yet established whether the arXiv source archive contains deterministic numerical/vector source arrays for:

1. observed per-bin counts;
2. per-bin background component spectra;
3. the efficiency curve used in the De-Romeri convolution.

A source-archive fetch attempted during this iteration failed at network/DNS transport before the archive could be inspected. That is infrastructure failure of the transport attempt, **not evidence that the primary numerical inputs do not exist**. Therefore the frozen `BLOCKED_PRIMARY_LIKELIHOOD_INPUTS` classification is not yet justified.

Additional later prerequisites remain: hash-pinned solar spectra/normalizations and nuisance uncertainties, exact executable B-L cross-section convention, and a separately frozen Delta-chi2 rule. These are not evaluated post hoc in this input audit.

## Scientific consequence
No PandaX likelihood was evaluated, no De-Romeri contour was digitized, and no B-L exclusion point was emitted. BSM remains `UNLOCKED_FOR_CONSTRAINT_LEDGER_ONLY`.

## Exact next action
Materialize the arXiv:2206.02339 source archive or an author/public numerical release and inspect the Fig. 3 / efficiency source assets. If deterministic numerical arrays exist, freeze/hash them and then prospectively preregister an SM/background benchmark reproduction. If the source-level audit establishes that controlling per-bin data/background/efficiency inputs are only obtainable by prohibited raster/manual reading, classify `BLOCKED_PRIMARY_LIKELIHOOD_INPUTS` and retire this route without weakening the gate.

## Authority
- prereg commit: `20ee0ab7cf4ab3d709c147a4826d4b24897cc83a`
- machine-readable audit ledger commit: `fd5f6fb92bee6c9390e462fe3358852ae4431ca0`
- no scientific run/artifact: documentary primary-input audit; no result-dependent numerical calculation was authorized or performed.
