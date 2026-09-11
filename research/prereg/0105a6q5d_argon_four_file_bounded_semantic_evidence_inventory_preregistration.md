# 0105a6q5d — Argon four-file bounded semantic-evidence inventory preregistration

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5D`
Scope: authority/semantic evidence inventory only; NONDISCOVERY.

## Parent authorization

Parent q5c1 validated class: `PASS_0105A6Q5C1_ARGON_OFFICIAL_FOUR_SEMANTIC_FILES_BYTE_LOCKED_NONDISCOVERY`, immutable record commit `908038bcff4f6f1c6554dbb03c1ce339546d9173`.

q5d may inspect the complete set of four exact byte-locked files and no other release-file content. Before semantic inspection, the following evidence categories and extraction rules are frozen.

## Exact source identities

The same four q5c1 URLs and exact size+MD5+SHA256 identities are mandatory. Any identity mismatch is FAIL CLOSED and no semantic result may be emitted.

## Frozen evidence categories

Normalize text only by UTF-8 decode with replacement, Unicode NFKC and casefold. Preserve original line numbers and original line text in the evidence artifact. For every matching line retain a fixed ±2-line context window; overlapping windows may be merged but no hit may be dropped.

E1 — elementary likelihood/count-law vocabulary:
`poisson`, `multinomial`, `likelihood`, `extended`, `binned`, `unbinned`, `roofit`, `roorealvar`, `roodata`, `generate`, `pseudo`.

E2 — nuisance/constraint vocabulary:
`nuisance`, `constraint`, `gaussian`, `normalization`, `normalisation`, `uncertainty`, `parameter`, `prior`, `penalty`.

E3 — shape-systematic/morphing vocabulary:
`systematic`, `shape`, `morph`, `interpol`, `excursion`, `plus1`, `minus1`, `+1sigma`, `-1sigma`, `+1 sigma`, `-1 sigma`, `pdf`.

E4 — simultaneous/correlation vocabulary:
`simultaneous`, `correlation`, `correlated`, `covariance`, `independent`, `joint`, `profile`.

E5 — count-anchor/precedence vocabulary:
exact numeric strings `3152`, `3154`, plus `anchor`, `nominal`, `central`, `precedence`, `cevns`, `events`, `counts`.

E6 — efficiency/interpolation vocabulary:
`efficiency`, `acceptance`, `interpol`, `spline`, `linear`, `node`, `threshold`.

The inventory must report every hit by category and file and the complete fixed context windows. It must not rank or prune evidence after inspection.

## Frozen terminal classes

- `PASS_0105A6Q5D_BOUNDED_SEMANTIC_EVIDENCE_INVENTORY_COMPLETE_NONDISCOVERY` iff all four source byte identities pass and deterministic extraction completes.
- `FAIL_0105A6Q5D_SOURCE_BYTE_IDENTITY_MISMATCH` if any downloaded source differs from the frozen q5c1 identity.
- `BLOCKED_0105A6Q5D_SOURCE_TRANSPORT_OR_DECODE_FAILURE` if exact-source acquisition/processing cannot complete.

q5d PASS means only that the bounded evidence inventory is complete under the preregistered vocabulary. It does **not** by itself establish F1/F4/F6/F7 closure, authorize an elementary likelihood implementation, systematic MC, or observed residual fitting. Any semantic adjudication against those methodological questions must be separately prospectively specified before using the q5d evidence to make an implementation decision.

## Hard prohibitions

No event-data residual inspection; no pseudo-data generation; no likelihood evaluation; no fitting; no nuisance profiling; no BSM quantities; no systematic MC.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`