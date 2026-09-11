# 0105a6q5f1 — validated arXiv source archive structure locator

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5F1`
Classification: `PASS_0105A6Q5F1_ARXIV_SOURCE_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY`
Scope: archive member metadata only; NONDISCOVERY.

## Prospective chain

- q5f validated source-byte PASS record: `bb9910e91b833e26c6560f3ac878855acfe380e0`
- preregistration: `37847bf0d915208910b3eced72d8a40e541c6326`
- implementation: `f0fd6b7c31b6554dc700ac5530a597ee3ecee4fa`
- guards: `8813cbc10993f674997a062bbf07b34429b2adc1`
- execution head: `44bb09ad7b6e33897d75957f61770fc9b12b20eb`

## Hosted validation

- run/job/artifact: `34549346624/103108772174/10180197873`
- provider artifact ZIP SHA256: `2382db3992b1f7df1d7886512b40a619d8f1ae363d1d5cb86639a7a77ba5c048`
- independently downloaded ZIP SHA256: `2382db3992b1f7df1d7886512b40a619d8f1ae363d1d5cb86639a7a77ba5c048`
- independent inner `result.json` SHA256: `23f1ceb8fd56839e205786b0d05122e81b35907107e907249b86013661ae24e2`
- revalidated source SHA256: `5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde`, bytes `23805`

The archive contains 7 members. Under the prospectively frozen suffix rule, the complete source-text candidate set is exactly:

1. `authors_els.tex` — 4985 bytes
2. `CENNS10DataReleaseCompanion.bbl` — 1308 bytes
3. `CENNS10DataReleaseCompanion.bib` — 1274 bytes
4. `CENNS10DataReleaseCompanion.tex` — 27656 bytes

The q5f1 artifact explicitly records `member_content_read=false` and `source_text_inspected=false`. No candidate payload was read by this gate. No likelihood, pseudo-data, systematic Monte Carlo, nuisance fit or observed BSM residual was executed or inspected.

Green CI was not treated as scientific PASS; raw job/result and artifact bytes were checked against the frozen gate.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact continuation rule

PASS permits only a separately prospectively frozen semantic-evidence gate over all four candidates above, without ranking or pruning. The next gate may seek only explicit additional authority for the q5e-unresolved F1/F4/F6/F7 implementation semantics; absence or ambiguity must remain BLOCKED and cannot be filled by RooFit defaults, generic HEP convention, assumed nuisance independence, invented morphing/interpolation, or post-hoc precedence.