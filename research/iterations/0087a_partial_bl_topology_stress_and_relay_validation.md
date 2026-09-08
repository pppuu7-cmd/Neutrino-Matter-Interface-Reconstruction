# NMIR iteration 0087a — partial B-L topology stress and constraint-relay validation

Date: 2026-09-08
Prospective validation contract: `research/prereg/0087a_partial_bl_topology_stress_and_relay_validation.md`, frozen commit `8f6cbfc0a8b6ecf6286b6bc7c59b07364dc46190` before stress/relay validation.
Final classification: **PASS_PARTIAL_B_L_TOPOLOGY_STABLE_RELAY_NOT_VALIDATED**.
`NMIR_READINESS: 98%`.

## Authoritative hosted execution
- workflow: `NMIR 0087a partial B-L topology relay validation`
- head commit: `d11068f40f615f23eb34d09213ac00d23d45ee09`
- run: `34178514608`
- job: `101912617239`
- artifact: `10038071270`
- artifact ZIP SHA256: `ae30c4327f0f782d2e277fc1c18181c20cbbf1da9ecce78042dd54193a5749f8`
- raw JSON SHA256: `4f5bc2fb1901a2af53d1b83b719ed93313aa36864f5c3c0856c96222a778cbe0`

All prospective regression tests, source reproductions, inward-window tests, leave-one-family-out tests, graph tests, and artifact upload passed. All area-closure checks passed.

## Result A — 0087 N1 fragmentation survives strong inward-window stress
Prospectively frozen y ceilings were `-2,-3,-4,-5` in `log10(g_BL)`, with x fixed to `-6..10` in `log10(m/eV)` and the lower y edge fixed at `-25`.

`WINDOW_STABLE_N1=true` in **all four** preserved scenario branches.

At the reference ceiling `y_max=-2`, every scenario has three qualifying permitted components. The smallest `0.4239535888152022 decade^2` component disappears when the ceiling is lowered to `-3`, but the topology does **not** reconnect: two qualifying components remain at every tested ceiling through `y_max=-5`.

Representative qualifying component areas at `y_max=-5`:
- Majorana + BODY_NATIVE: `235.37235681684487` and `14.59117977349949 decade^2`;
- Majorana + CONCLUSION_SUMMARY: `235.38014685981827` and `14.59117977349949`;
- Dirac + BODY_NATIVE: `233.95761584169608` and `14.59729681297028`;
- Dirac + CONCLUSION_SUMMARY: `233.96701462837117` and `14.59729681297028`.

Therefore the main 0087 disconnection is not a fine-tuned consequence of choosing the original `g_BL=1e-2` analysis ceiling. It survives an inward shift of that ceiling by three coupling decades.

This still does not establish a globally bounded physical island because the test only shrinks an existing finite window; it never extrapolates beyond source authority.

## Result B — leave-one-family-out identifies SN1987A as structurally necessary
At the original `y_max=-2` window, the preregistered leave-one-family-out diagnostic gives the same causal pattern in all four scenario branches:

- remove CMB -> N1 remains true, three qualifying components;
- remove Solar CEvNS -> N1 remains true, two qualifying components;
- remove Wagner -> N1 remains true, three qualifying components;
- **remove SN1987A -> N1 becomes false, exactly one qualifying permitted component**.

This is a new structural synthesis produced by NMIR: within the current authoritative partial family set, **SN1987A is necessary for the disconnected permitted topology**, whereas no other single included family is individually necessary.

The statement is scenario-stable across both CMB alternatives and both separately preserved Shin-Yun mass-endpoint semantics.

## Result C — stronger four-family relay hypothesis is rejected by its prospective test
At `y_max=-2,-3,-4`, the exact overlap graph passes the generated SN-articulation relay conditions in all four scenarios.

Typical positive-area edges at `y_max=-4` (Majorana BODY_NATIVE) are:
- CMB–SN: `25.351075 decade^2`;
- CMB–Solar: `2.085177`;
- SN–Solar: `1.042152`;
- SN–Wagner: `2.653329`.
Wagner has no >=0.01 direct edge to CMB or Solar, so deleting SN isolates the ultra-light Wagner node at these ceilings.

However the preregistered relay validation required this to remain true through `y_max=-5`.
At `y_max=-5`, only the CMB–SN and SN–Wagner >=0.01 edges remain; the Solar node no longer has a qualifying overlap edge. Therefore the full four-node graph is not connected and `RELAY_STABLE=false` in every scenario.

Accordingly the stronger classification `PASS_PARTIAL_B_L_TOPOLOGY_AND_RELAY_ROBUST` is correctly **not** awarded.

## Scientific interpretation
Accepted under the current partial-authority set:

1. **Robust partial B-L fragmentation:** the allowed complement remains disconnected under a three-decade inward coupling-ceiling stress and under all preserved CMB/SN semantic alternatives.
2. **SN1987A pivot:** SN1987A is the unique single-family removal that destroys the fragmentation at the reference window.
3. **No fully robust four-family relay:** the apparent Wagner→SN→CMB/Solar connected overlap network is real over `y_max=-2..-4` but does not satisfy the prospectively frozen `y_max=-5` requirement.

This is a cross-family structural result of NMIR. It is **not yet** a complete B-L allowed region, evidence of a new mediator, or a literature-priority claim.

## Mandatory next question
The useful next discovery/completeness gate is not to repeat the same topology. It is to determine which currently blocked/missing families are actually capable, by source-authorized **mass support alone**, of intersecting the robust low-mass fragmented components. A blocked high-mass family that is provably mass-disjoint cannot erase the candidate, while a mass-overlapping blocked family remains a genuine threat.

This threat-ranking gate must not invent missing y-coordinate geometry. In particular:
- use NA64 x-axis/mass support only where 0086c already has enough x anchors;
- do not infer its blocked g-axis;
- similarly treat BBN/Cerdeno/COHERENT only with exact source-authorized mass support;
- preserve fifth-force finite-mass blocker.

BSM response/enhancement remains locked until missing-family stability is sufficient for a separate unlock gate.
