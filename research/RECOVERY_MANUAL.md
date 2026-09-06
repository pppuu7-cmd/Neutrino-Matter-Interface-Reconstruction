# NMIR Recovery Manual — chat-independent reconstruction protocol

Last structural revision: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Purpose
This file is the operational manual for reconstructing and continuing NMIR without access to any development chat. Chat history is never scientific authority. The repository, frozen inputs, preregistrations, code, tests, validated Actions logs/artifacts, and chronological iteration notes are authority.

A new researcher or a new ChatGPT session must be able to resume by cloning/reading this repository only.

## Mandatory recovery order
1. Read this file completely.
2. Read `research/RECOVERY.md` for the latest compact scientific state, current readiness, exact open gates and authoritative run/artifact IDs.
3. Read `research/NMIR_FUNNEL.md` for the discovery-funnel logic and admissible gate ordering.
4. Read the newest files in `research/iterations/` in descending order until the current frontier and its immediate prerequisites are understood.
5. Read the preregistration/contract file named by the current iteration before inspecting or interpreting the corresponding result.
6. Inspect recent Git commits after the last `RECOVERY.md` reconciliation and reconcile any newer work before starting a new calculation.
7. Inspect relevant GitHub Actions runs. A green workflow is infrastructure success only until its raw benchmark/log/artifact is checked against the frozen prospective criterion.
8. Only then choose the highest-value OPEN funnel gate. Prefer a class-level bound/no-go/response theorem over another convenient isotope/material scan.

## Authoritative file map
- `research/RECOVERY_MANUAL.md` — how to recover and continue the project.
- `research/RECOVERY.md` — latest compact state of truth, gates, numbers, provenance, readiness, next steps.
- `research/NMIR_FUNNEL.md` — F0–F10 discovery funnel and anti-overclaim logic.
- `research/iterations/*.md` — immutable chronological scientific records; preserve negative results.
- `research/*_prereg.md` — prospective contracts; acceptance criteria must not be weakened after seeing the answer.
- `research/LITERATURE_LEDGER.md` — literature/provenance ledger.
- `research/sm_power_ledger.md` — validated Standard-Model target comparisons.
- `data/` — frozen numerical inputs and provenance manifests.
- `src/nmir/` — executable scientific formulas.
- `tests/` — regression/unit tests.
- `scripts/` — reproducible benchmark entry points producing machine-readable results.
- `.github/workflows/` — hosted reproducibility gates.

If two files disagree, prefer the newest validated immutable iteration + its preregistration and raw artifact; then repair `RECOVERY.md`. Never silently overwrite a historical scientific FAIL.

## Mission
Search the physically admissible space of neutrino↔matter/field interfaces and determine whether any mechanism can substantially improve one or more of:
1. state control / redirection / focusing;
2. probability of interaction or capture;
3. detector visibility of an interaction;
4. irreversible neutrino-sourced deposited energy.

These objectives are not interchangeable.

Frozen deposited-power accounting:

`P_dep = N_T ∫ dE_nu mu(E_nu,x) Phi(E_nu) sigma(E_nu) E_dep,nu(E_nu)`.

Always enforce

`0 <= E_dep,nu <= E_nu`.

Energy from daughter decay, target preparation, metastable free energy, external fields/pumping, cavity/mediator preparation, or extra thermalization belongs to its own source ledger and is never re-labelled as neutrino-supplied power.

## Core response formalism
For a general many-body target,

`Gamma = sum_ab ∫ d^3q dω K_ab(E_nu,q,ω) S_ab(q,ω)`.

Energy deposition carries an additional `ω` weighting. Candidate response functions must obey the applicable positivity, conservation laws, causality/Kramers–Kronig relations, detailed balance, sum rules, kinematic support and stability conditions.

The central inverse problem is not “which material sounds promising?” but

`S_target = argmax_{S in admissible set} score[S]`,

with the score explicitly labelled as interaction rate, detector rate, focusing gain or neutrino-sourced power.

## Funnel that every candidate must pass
F0 — classify objective: control / detect / focus / absorb / harvest neutrino energy.
F1 — identify the microscopic operator/channel: SM weak vector/axial, charged current, electromagnetic property, or explicitly labelled BSM.
F2 — when applicable, use production↔absorption/crossing to connect a known decay/production matrix element to inverse capture.
F3 — kinematics and source spectral overlap: thresholds, q, ω, linewidth, source profile, flavor/particle-vs-antiparticle.
F4 — microscopic strength: measured `ft`, `B(GT)`, response data, or a clearly bounded theoretical matrix element.
F5 — collective/resonant engineering: coherence, resonance, polarization, band/phonon/magnon/metastable response.
F6 — no-free-lunch gates: unitarity, integrated-strength/sum rules, Liouville, finite source, energy budget, stability, thermodynamic limit.
F7 — common quantitative score: cross section, optical depth, events/kg/day, and/or W/kg with units and source normalization.
F8 — external constraints and prior-art audit.
F9 — compose gains only after each factor has independently passed and is physically compatible with the same source/state/geometry.
F10 — classify `PASS`, `PASS-SURVIVOR`, `STRONG_NEGATIVE_SCOPED`, `SCIENTIFIC_FAIL`, `INFRASTRUCTURE_FAIL`, or `BLOCKED`.

## Frozen baseline formulas
Tree-level low-q weak charge:

`Q_W = N - (1 - 4 sin^2(theta_W)) Z`.

Ideal CEvNS normalization:

`sigma ~= G_F^2 Q_W^2 E_nu^2 / (4 pi)`.

Differential low-q CEvNS recoil response used for threshold studies:

`d sigma/dT = G_F^2 Q_W^2 M/(4 pi) * [1 - M T/(2 E_nu^2)]`,

with exact recoil endpoint

`T_max = 2 E_nu^2/(M + 2 E_nu)`

and inverse source threshold

`E_min(T) = 0.5 [T + sqrt(T^2 + 2 M T)]`.

For precision/high-q work, nuclear form factors/radiative corrections must be restored; never silently promote this low-q benchmark to a precision prediction.

Production↔absorption principle: the same weak matrix element (or Hermitian-conjugate/crossed amplitude, with the appropriate nuclear states and phase space) governs a decay/production channel and its allowed inverse channel. Measured `ft`/`B(GT)` data are preferred over guessed strengths.

Resonance rule: a high peak cross section is not sufficient. Track integrated entrance strength and physical source overlap. Narrowing a line alone must not be counted as newly created weak strength.

Metastable rule: a neutrino may trigger a macroscopic avalanche. That can be a detector `PASS-SURVIVOR`; released target free energy remains target energy, so it is not neutrino-energy gain.

## Already established broad guards
Do not reopen without a genuinely new assumption:
- naive macroscopic static `N^2` free gain;
- geometry-only staggered-layer ordering at fixed microscopic cross sections and fixed mass column;
- passive local density/phonon free superextensive energy-weighted gain;
- passive local spin/magnon free superextensive energy-weighted gain;
- extensive long-range pair interactions as a free superextensive gain;
- passive stable single- or finite-multimode linear mediator as a free gain once field energy is included;
- passive convex homogeneous nonlinear medium as a free gain once its free-energy budget is included;
- linewidth narrowing as a source of new integrated resonance strength.

Exact scopes and run IDs are in `research/RECOVERY.md`; the statements above are not universal no-go theorems outside their assumptions.

## Surviving research classes
The current funnel intentionally leaves open, subject to `RECOVERY.md` being newer:
- metastable/avalanche detector interfaces with real microscopic neutrino trigger rates and dark-count/reset constraints;
- source-profile-aware low-threshold CEvNS;
- target-specific true inverse resonances with independently evaluated entrance strength;
- genuine two-/higher-body nuclear-current residual not replaced by selected-nucleus anecdotes;
- distant-source gravitational focusing with finite-source/alignment/duty-cycle accounting;
- active/driven media with the pump energy explicitly separated;
- non-convex/multistable/higher-body many-body response not covered by previous theorems;
- BSM only after the principal SM loopholes are quantitatively bounded, except for maintaining a constraints ledger.

## Preregistration rule
Before every result-dependent calculation, freeze:
- scientific question and scope;
- exact input files/hashes or primary-source provenance;
- formulas/conventions/units;
- comparison/reference value if any;
- acceptance/failure thresholds;
- what would count as infrastructure failure versus scientific failure;
- exact next action on PASS/FAIL/BLOCKED.

Never relax an acceptance threshold after seeing the result. A failed approximation may be replaced only by a physically motivated new version with a new prospective contract; keep the old FAIL in chronology.

## Reproducibility/provenance rule
Every substantive numerical gate should leave:
1. code under `src/nmir/`;
2. dedicated tests under `tests/`;
3. a benchmark script under `scripts/` producing machine-readable output;
4. a hosted workflow when practical;
5. raw run/job/artifact IDs and artifact hash in the iteration note;
6. frozen external inputs copied into `data/` when licensing/size permits, plus original source repository/commit/blob SHA or primary citation;
7. a compact update in `research/RECOVERY.md`.

A workflow status by itself is never evidence of a scientific PASS.

## Recovery procedure after a chat crash or from a new session
Use the following exact prompt-independent algorithm:

1. Open repository default branch `main`.
2. Read `research/RECOVERY_MANUAL.md`.
3. Read `research/RECOVERY.md`; note `NMIR_READINESS`, latest numbered iteration, exact next gates and any queued/in-progress run.
4. Read `research/NMIR_FUNNEL.md`.
5. Read latest numbered iteration and its prereg file.
6. Inspect commits newer than the recovery reconciliation; if newer work exists, inspect its code/tests/workflows/results and reconcile recovery before new science.
7. Inspect current Actions. Do not duplicate queued/in-progress work.
8. For each newly terminal run, read raw log/artifact and classify it against the prereg contract.
9. Commit an immutable numbered iteration note.
10. Update `RECOVERY.md` and, if research architecture changed, this manual and/or `NMIR_FUNNEL.md`.
11. Select the highest-value OPEN class-level gate and preregister it before computation.
12. End the iteration with: `✅ closed`, `🟡 running/BLOCKED`, `❌ failed/open`, authoritative commit/run/artifact, exact next gate, and `NMIR_READINESS: XX%`.

## Readiness discipline
`NMIR_READINESS` is an audit estimate of funnel maturity, not probability that a revolutionary mechanism exists and not article acceptance probability. Increase it only when a reproducible scientific gate closes or a major uncertainty class is quantitatively bounded. More code/files alone earn no credit. Discovery of a new blocker may leave readiness unchanged or lower it.

## Anti-overclaim checklist
Before writing “new mechanism”, “enhancement”, “capture”, or “energy extraction”, answer all of:
- Is the effect rate, directionality, detectability or neutrino-sourced energy?
- Was the physical source spectrum integrated?
- Was the total final-state/angle phase space integrated where required?
- Is the gain still present at fixed target mass/column/energy budget?
- Does a sum rule or integrated-strength theorem merely redistribute spectral weight?
- Is external/stored energy separated?
- Are flavor and neutrino/antineutrino identities correct?
- Is the microscopic matrix element independently grounded?
- Are all multiplied gain factors individually validated and mutually compatible?
- Has prior art been searched before a novelty claim?

## Minimum information that must always remain recoverable in-repo
At all times `RECOVERY.md` + this manual + latest iteration must be sufficient to recover:
- mission and objective distinctions;
- governing formulas and units;
- source/data conventions;
- frozen negative/class-level results and their scopes;
- surviving branches;
- exact authoritative commits/runs/artifacts;
- current readiness;
- exact next funnel gate;
- which computations are currently running or blocked.

If any of these is missing after a substantive iteration, documentation recovery is itself the next mandatory gate before further branching.
