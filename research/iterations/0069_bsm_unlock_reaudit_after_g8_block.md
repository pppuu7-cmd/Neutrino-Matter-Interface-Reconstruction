# NMIR iteration 0069 — BSM unlock re-audit after G8 normalization-authority block

Date: 2026-09-07
Prospective contract: `research/prereg/0069_bsm_unlock_reaudit_after_g8_block.md`, commit `cb02acc5ed6f7dd9463c0d06353b6ca6d6f5ee56`.

## Classification
**`PASS_UNLOCK_BSM_CONSTRAINT_LEDGER_ONLY`**.

This is an architecture/readiness classification only. It is **not** a BSM mechanism PASS, not evidence for a new force, and not permission to tune a coupling to NMIR before external constraints are frozen.

## Why 0066 failed but 0069 passes
The unlock criterion did not change.

Iteration 0066 failed because G8/Cu63 was both quantitatively unbounded and immediately actionable: the exact-state target package existed and the thermal-solar source overlap/rate chain could be executed from available primary inputs.

Iterations 0067 and 0068 changed only the evidence state:
- 0067 materialized the Standard-Model thermal-solar anti-nu_e source tail at `162.496486 keV`;
- 0068 then found that the exact primary continuous-spectrum RIOEC normalization package could not be independently materialized under the frozen primary-only rule and classified `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`.

Therefore G8 is no longer an immediately executable numerical SM branch under the existing reproducibility rules. No acceptance criterion was relaxed.

## Survivor-by-survivor audit
- **G2 — `BLOCKED_NOT_ACTIONABLE`.** Iteration 0063 still lacks a public same-configuration sub-keV measured rejection × bulk-NR acceptance pair. No cross-detector multiplication is allowed.
- **G3 — `OPEN_NOT_CURRENTLY_ACTIONABLE`.** The absolute short-range/contact-current coefficient residual remains physically OPEN. Iterations 0059, 0062 and 0065 retire three different coefficient-independent universal-ceiling routes. No new theorem or physical assumption has been identified that can presently execute a harder bound. This residual is not counted as closed.
- **G8 — `BLOCKED_NOT_ACTIONABLE`.** Source tail is frozen by 0067, but 0068 blocks the primary continuous-spectrum RIOEC normalization package. Secondary summaries cannot supply the missing normalization.
- **G9 — `STRONG_NEGATIVE_SCOPED`.** Iteration 0061 closes the frozen 10-kpc Galactic CCSN transparent-Sun solar-lens utility benchmark after finite-source/alignment/duty accounting.
- **G4/G10 broad passive guards — `STRONG_NEGATIVE_SCOPED`** in their frozen assumptions.

The frozen 0069 criterion asks whether any principal SM branch is both quantitatively unbounded **and immediately actionable with presently available primary inputs**. The answer is no.

Machine-readable ledger: `data/bsm_unlock_readiness_0069.json`, commit `76434353545f5aa70f19c770b9286b4d24955740`.

## Allowed new branch state
BSM/light mediator changes from `LOCKED` to:

**`UNLOCKED_FOR_CONSTRAINT_LEDGER_ONLY`**.

The first allowed BSM action is a primary-source external constraints ledger covering at minimum mediator mass, coupling normalization/operator structure, and applicable laboratory, stellar/astrophysical and cosmological exclusions/limits.

## Still forbidden
- no NMIR BSM enhancement scan before the constraints ledger is frozen;
- no choosing a mediator/coupling because it produces a large NMIR effect before external limits are applied;
- no multiplying a BSM factor by unresolved G2/G3/G8 gains;
- no relabeling metastable/target/pump energy as neutrino-supplied energy;
- no `BSM_PASS` claim from this architecture audit.

## Exact next gate
Prospectively freeze iteration 0070: a **primary external BSM constraints-ledger gate**. The gate must define operator basis and coupling conventions before collecting limits, then freeze primary laboratory, astrophysical/stellar and cosmological constraints with provenance. Only parameter space surviving that ledger can later enter an NMIR response calculation under a separate prospective contract.

## Readiness
Branch-status reclassification alone earns no scientific readiness credit. `NMIR_READINESS` remains **89%**.
