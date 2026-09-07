# NMIR 0080e erratum — hosted artifact hash reconciliation

Date: 2026-09-08
Status: **AUTHORITY_HASH_ERRATUM; SCIENTIFIC_CLASSIFICATION_UNCHANGED**

## Scope
This erratum does not rerun or reinterpret the 0080e scientific gate. It reconciles a provenance error discovered by direct raw-log and artifact-byte inspection after `research/iterations/0080e_bl_cosmology_scenario_semantics.md` had already been committed as immutable.

The original immutable 0080e note is retained unchanged. Its scientific result remains `PASS_COSMOLOGY_B_L_SCENARIO_CONDITIONAL_AUTHORITY`, but the two hosted-output SHA256 values recorded there are superseded by this erratum and the corrected persistent ledger.

## Authoritative hosted identifiers
- run/job: `34164286854 / 101872133978`
- artifact: `10033631352`
- artifact name: `nmir-0080e-bl-cosmology-scenario-semantics`
- artifact size: `3052` bytes

## Correct hashes
Direct decoded job log printed:
- result JSON SHA256: `381c04707c1f9d29ce88ca1ff3b728a55e2de1b59b1ac256f6f4c580e451037f`
- uploaded artifact ZIP SHA256: `9a1f92cd70bad33a441ec5eac18ecdfc3311f36f6f48e877094ac6177282293e`

GitHub Actions artifact metadata independently reports digest:
`sha256:9a1f92cd70bad33a441ec5eac18ecdfc3311f36f6f48e877094ac6177282293e`.

The artifact ZIP was then downloaded independently. Local byte inspection reproduced:
- ZIP SHA256: `9a1f92cd70bad33a441ec5eac18ecdfc3311f36f6f48e877094ac6177282293e`
- inner `esseili_kribs_scenario_semantics_0080e.json` SHA256: `381c04707c1f9d29ce88ca1ff3b728a55e2de1b59b1ac256f6f4c580e451037f`

## Superseded incorrect values
The first persisted ledger and immutable note had recorded:
- raw JSON SHA256 `381c0470a03cf468df56601ca04cb9a1763676fe11d05a25b5e7c049e8d1037f`
- artifact ZIP SHA256 `21f3953dad41891087004cabdc613ba9903cc62d684dd69ceb80944146856820`

Those hashes do not match the authoritative job, GitHub artifact digest, or downloaded bytes and must not be cited as 0080e hosted authority.

## Scientific consequence
None. The downloaded JSON contains the same frozen-gate classification and checks observed in the raw log:
- `PASS_COSMOLOGY_B_L_SCENARIO_CONDITIONAL_AUTHORITY`
- Majorana and Dirac are explicit separate scenarios
- no primary-source common combination rule is detected
- scenario-independent union/intersection remains unauthorized.

Persistent corrected ledger: `data/esseili_kribs_scenario_semantics_0080e_authority.json`, correction commit `8b7edaa82124595c361d7a6fa18a923ad3b3f641`.

## Guard
Future recovery must prefer this erratum plus the corrected ledger over the two stale hash fields in the original immutable 0080e note. Scientific classification remains unchanged; only hosted provenance was repaired.
