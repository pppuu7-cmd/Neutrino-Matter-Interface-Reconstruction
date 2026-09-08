# Iteration 0092b-a1 r1 — GONG parser infrastructure failure

Date: 2026-09-08
Classification: `INFRASTRUCTURE_FAIL_G9_0092B_A1`

Parent prereg: `research/prereg/0092b_g9_ccsn_mev_solar_transmission_authority.md` (`66341d7eb7322e958a52dc30fb24d4e2b3e44647`).
Composition-authority amendment: `research/amendments/0092b_a1_model_s_gong_composition_authority.md` (`8e7466013f0e978be9c036ec9ca10f4aa005cb66`).

Execution head: `d788ab953ff226a801889d2471dac152a5958d59`.
Run/job: `34277408907 / 102233717306`.
Artifact: `10076251763`.

Dedicated conformance tests passed (`3 passed`). All three official source files downloaded successfully. The scientific composition calculation did not begin because the parser assumed the GONG integer header was at zero-based line index 3; the official file contains a blank record before the integer header, so `lines[3]` was blank and `parse_fgong` raised `ValueError: unexpected integer header`.

This is an implementation failure before any H/He/Z chord result. It is not `BLOCKED_G9_0092B_SOLAR_COMPOSITION_AUTHORITY`, not `BLOCKED_G9_0092B_COMPOSITION_NUMERICS`, and provides no composition scientific classification.

Raw hosted hashes:
- limited Model-S: `65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc`;
- extensive GONG Model-S: `a30c31b9f6af2e5918f49d3808c0dade54f9946133b679b86949fc73625c2393`;
- official GONG format PDF: `9614e18f6eed3f7121352539651c502ae84b7b13bb308b091a66157b45a597b5`.

The artifact was downloaded independently. Independent artifact ZIP SHA256:
`506c1c5d662180e6415510400bc645df8b4dadd7b76a28c8829d93a925d04de8`.

Independent hashes of all three inner source files exactly match the hosted values above. No result JSON exists because execution failed before result construction.

Permitted repair: make parser locate the first valid four-integer GONG header record after the text header/blank records, then consume the subsequent numeric payload. This changes no scientific source, formula, ray, numerical resolution, threshold or classification rule.
