# NMIR — Neutrino–Matter Interface Reconstruction

NMIR is a model-agnostic research program for reconstructing and optimizing the physical interface between neutrinos and organized matter.

## Resume / recover the research

**Do not reconstruct NMIR from chat history.** The repository is the scientific source of truth.

A new researcher or a new ChatGPT session must start in this order:

1. `research/RECOVERY_MANUAL.md` — chat-independent operational reconstruction protocol;
2. `research/RECOVERY.md` — latest scientific state, authoritative results, run/artifact provenance, readiness and exact next gates;
3. `research/NMIR_FUNNEL.md` — F0–F10 discovery funnel and anti-overclaim rules;
4. newest `research/iterations/*.md` plus the associated prospective preregistration;
5. recent commits and raw GitHub Actions results newer than the latest recovery reconciliation.

If recovery documentation is stale relative to a validated result, documentation must be reconciled before a new research branch is started.

## Central question

> What is the strongest neutrino↔matter coupling, energy-transfer channel, state-control, focusing or detector-amplification mechanism allowed by known physics and current observations, and what additional microphysics would be required to exceed it?

NMIR does **not** assume that a useful neutrino absorber exists. A rigorous no-go/upper-bound result is an acceptable scientific outcome.

## Core decomposition

We separate four physically different objectives:

1. **State control / focusing** — flavor/spin conversion or redirection without necessarily depositing energy.
2. **Interaction/capture** — increasing the microscopic probability of scattering or absorption.
3. **Detection/event amplification** — making a rare microscopic interaction macroscopically visible, including metastable/avalanche interfaces.
4. **Energy capture** — irreversible deposition of neutrino-supplied energy.

A mechanism is never promoted between these categories without an explicit quantitative accounting. Stored target energy, pump energy and reset work are not neutrino energy.

## Model-independent interface

At low energy, candidate microscopic couplings are mapped onto medium response functions,

\[
\Gamma_\nu \sim \int d^3q\,d\omega\; L_{ab}(q,\omega)\,S^{ab}(q,\omega),
\]

where the leptonic/operator kernel `L_ab` contains the neutrino interaction and `S_ab` (or equivalently a retarded susceptibility) contains the many-body material physics.

The inverse problem is

\[
S_{\rm target}(q,\omega)=\arg\max_{S\in\mathcal A}\; {\rm score}[S]
\]

with the score explicitly labelled as interaction rate, detector rate, focusing gain or neutrino-sourced deposited power, and subject to causality, unitarity, sum rules, conservation laws, stability and applicable experimental constraints.

## Operator / mechanism basis

NMIR includes or tests:

- Standard Model charged-current and neutral-current weak interactions;
- coherent elastic neutrino–nucleus scattering (CEvNS);
- neutrino–electron scattering;
- production↔absorption / inverse weak transitions grounded by measured `ft` or `B(GT)` when possible;
- electromagnetic neutrino properties;
- matter potentials and spin-polarized media;
- density, spin, current, phonon, magnon and other collective response;
- true resonances with integrated-strength/source-profile accounting;
- metastable/avalanche detector media with a separate stored-energy ledger;
- gravitational focusing with finite-source/Liouville/geometry constraints;
- structured/staggered/multi-isotope media under fixed-mass controls;
- NSI/light-mediator/other BSM hypotheses only after the principal Standard-Model loopholes are quantitatively bounded.

## Research gates

- **G0 — normalization/reproducibility**
- **G1 — static/macroscopic coherence**
- **G2 — many-body response, engineered detection and deposited-energy channels**
- **G3 — Standard-Model solar-neutrino power ceiling**
- **G4 — engineered resonance/polarization/periodicity**
- **G5 — minimal BSM residual**
- **G6 — global BSM consistency**
- **G7 — production/decay → inverse capture**
- **G8 — resonance integrated-strength/bandwidth/source-profile gate**
- **G9 — gravitational focusing**
- **G10 — staggered/multi-isotope/fixed-column structured matter**

The detailed F0–F10 discovery funnel is authoritative in `research/NMIR_FUNNEL.md`.

## Non-negotiable scientific rules

- Repository state, frozen inputs, preregistrations, code, tests, raw validated Actions results and immutable iteration notes are authoritative; chat text is not.
- Freeze a prospective acceptance/failure contract before inspecting a substantive numerical result.
- A green workflow is infrastructure success, not automatically a scientific PASS.
- Distinguish amplitude/directional coherence from total-rate enhancement.
- Distinguish lower detector threshold from larger microscopic cross section.
- Distinguish event amplification from neutrino-sourced energy gain.
- Track integrated resonance strength and physical source overlap, not peak cross section alone.
- Keep stored target energy, external pumping and reset work in separate ledgers.
- Do not multiply gains until each factor is independently validated and compatible with the same source/state/geometry.
- Negative gates and no-go results are retained in chronology.
- Any numerical claim intended for a paper must retain code, inputs, units, assumptions, tests and provenance.

## Current status

**2026-09-06 — reconciled through iteration 0043.**

`NMIR_READINESS: 73%` — audit estimate of funnel maturity, not probability that a revolutionary mechanism exists and not publication probability.

Latest class-level inverse-design result: at fixed detector mass, in the low-q continuous-`A` envelope with approximately fixed weak charge per nucleon, CEvNS target selection has an interior optimum

\[
A_* = \frac{2E_\nu^2}{3m_uT_{\rm thr}},
\]

equivalently `T_max(A*) ≈ 3 T_thr`. Hosted exact-endpoint validation passes by far inside the preregistered 1% tolerance. For Be7-like neutrinos the design center moves from `A≈13.3` at 40 eV to `A≈26.6` at 20 eV and `A≈53.3` at 10 eV. The next required gate replaces this continuous envelope by real nuclei and the full frozen solar spectrum.

The preceding physical Be7-profile result remains important: an Ar-40 40-eV threshold is technically open but retains only about `4.91e-6` of the dominant-line CEvNS cross section, so kinematic opening alone is not useful sensitivity.

See `research/RECOVERY.md` for the exact source-of-truth state and `research/RECOVERY_MANUAL.md` for recovery/continuation instructions.
