# NMIR-BENCHMARK-0100C1D — restricted mapping-evidence pass

Frozen: 2026-09-09

## Purpose

Prospectively define the only permitted content-level inspection of the six filename/role-selected text members frozen by `research/locks/0100c1c_presn_auxiliary_manifest_lock.json`. The pass asks one narrow authority question: does the released Kato/Nagakura auxiliary MESA package contain an explicit, reproducible relation that is sufficient to map an emission-side spectrum/lightcurve step or time-to-core-bounce to a unique stellar model/profile/snapshot identifier?

This is an authority/provenance gate. It is not an oscillation calculation and may not select a convenient stellar profile from a physics result.

## Frozen parent identities

The pass MUST verify the already-frozen auxiliary archive before reading any candidate text:

- DOI / record: `10.5281/zenodo.20822085` / `20822085`
- file: `pre_sn_neutrino.tar.gz`
- size: `17344435` bytes
- MD5: `e7282d0a7241b60a602e82d5e0e9f47f`
- SHA-256: `2aca20c46ab7fb0f7d2253da13a224d24453970b19470acc3e69df84909edc1b`
- archive member count: `44`
- frozen manifest SHA-256: `93fc56ec08c47aeb98c74434ba9a02eabe8001e079d72bdce67d4bb26a656a45`

Only these exact six members may be read:

1. `pre_sn_neutrino/README.rst` — 1726 bytes — SHA-256 `a97e371db4c82ed9cb5b1a2c5a7c1e43166db0037394df46461eb76b8861007f`
2. `pre_sn_neutrino/history_columns.list` — 33551 bytes — SHA-256 `987dd88721f7751a17876541126854431448f150aa434a5077809fd06fefa232`
3. `pre_sn_neutrino/profile_columns.list` — 29301 bytes — SHA-256 `1174c3591d72453fc1f54895003ecfbaeec2f7d0e4b682d65aaebab388122147`
4. `pre_sn_neutrino/inlist_common` — 13204 bytes — SHA-256 `de5aa4ccb5a31b9f6b41b4367f0ed30991075e3d0e03facc6a66f1fb1714be92`
5. `pre_sn_neutrino/inlist_to_cc` — 3391 bytes — SHA-256 `be7e528c6a5643d56c5a67e4e702c05a3a53c59da465b4e852a344d8a8a0e759`
6. `pre_sn_neutrino/src/run_star_extras.f90` — 7730 bytes — SHA-256 `e13aba921d975be80e7a3c8046a1d31050dc3f2ddc01f3ba0fa2e777c87dbecd`

No other member of the auxiliary archive may be read in 0100c1d. Expansion requires a new prospective amendment based on a filename/role rule stated before the new content is inspected.

## Already-established emission-side relation

The authors' public `massivestar-neutrino-data` README is treated only as emission-side authority: `spectrum*.dat` is indexed by the lightcurve step, and the lightcurve supplies time relative to core bounce. This establishes `spectrum index -> lightcurve step -> emission time`. It does **not** establish a stellar snapshot/profile mapping by itself.

## Frozen machine search

For every one of the six permitted members, the implementation SHALL decode text deterministically and report all fixed ±5-line windows around matches from the following token families (case-insensitive):

- emission/time tokens: `spectrum`, `lightcurve`, `core bounce`, `core_bounce`, `time to bounce`, `pre_sn`, `presn`, `neutrino`
- snapshot tokens: `profile_number`, `profile number`, `model_number`, `model number`, `star_age`, `star age`, `profile`, `save_model`, `saved model`
- relation tokens: `step`, `index`, `time`, `number`, `write`, `save`, `history`, `when`

A `machine_candidate_window` exists only when one fixed ±5-line window contains at least one emission/time token, at least one snapshot token, and at least one relation token. Every candidate window must be emitted; none may be manually omitted.

## Frozen classification rule

The mapping gate can close positively only if a machine-candidate window contains an **explicit relation** sufficient, from released information alone, to determine a unique stellar snapshot/profile/model identifier from the already-authorized emission step/time. Examples of sufficient relation forms are an assignment, table/column definition, or deterministic write/save rule that includes both sides of the relation. Mere co-occurrence of words, a generic MESA output setting, the existence of `star_age`, or a profile-saving cadence is not sufficient unless it provides the required crosswalk to the emission step/time.

Classification is frozen as follows:

- If there are zero `machine_candidate_window`s: `BLOCKED_0100C_MAPPING_AUTHORITY_UNRESOLVED_AFTER_RESTRICTED_READ`.
- If one or more candidate windows exist but none contains the explicit crosswalk defined above: `BLOCKED_0100C_MAPPING_AUTHORITY_UNRESOLVED_AFTER_RESTRICTED_READ`.
- If a candidate window contains a potentially explicit crosswalk but uniqueness cannot be established mechanically from the released rule: `REVIEW_REQUIRED_0100C_EXPLICIT_MAPPING_CANDIDATE_NONTERMINAL`; no snapshot may be selected.
- Only an unambiguous released deterministic crosswalk may yield `PASS_0100C_MAPPING_AUTHORITY_CLOSED_NONTERMINAL`. Even then, this pass may record the mapping rule but may not run terminal MSW or select a different rule after seeing a physics result.

## Allowed next step if blocked

If this restricted pass is blocked, the only next stellar-profile action is a separately prospectively frozen **structural inventory** of the already-authorized 25 Msun stellar archive. That inventory may expose filename/header/time/model-number metadata but may not choose the nearest/convenient profile unless a mapping rule is prospectively defined from authority available before the choice.

## Prohibitions

- No oscillation probabilities are calculated in this gate.
- No `rho(r), Ye(r)` profile is selected here.
- No nearest-time matching is permitted merely because timestamps appear numerically close.
- No candidate list, token family, window width, or pass criterion may be changed after the six contents are inspected to rescue a preferred outcome.
- A missing mapping is an authority BLOCK, never a failure of standard three-flavor MSW physics.

Status at freeze: `PREREGISTERED_0100C1D_RESTRICTED_MAPPING_EVIDENCE_UNRUN`.
