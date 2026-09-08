# NMIR iteration 0087 — authoritative partial B-L topology discovery

Date: 2026-09-08
Prospective contract: `research/prereg/0087_authoritative_partial_b_minus_l_topology_discovery.md`, frozen commit `b7c372013a52a11ba1c271c8df2c7cebe8c2722a` before the cross-family composition was executed.
Final classification: **PASS_PARTIAL_B_L_TOPOLOGY_CANDIDATE**.
`NMIR_READINESS: 98%` (discovery candidate found; completeness/stability not yet passed).

## Authoritative hosted execution
- workflow: `NMIR 0087 authoritative partial B-L topology discovery`
- head commit: `bbcc7e304fa90f785e348bce5ab1054873f993fd`
- run: `34178290574`
- job: `101911967827`
- artifact: `10037999116`
- artifact ZIP SHA256: `0c2cb177c5f509564c2f331f3c63566b3a0db5449f969ed8409b4341d236455a`
- raw JSON SHA256: `bc3bc145c044c156e4a5e58ba26b25c5a9d8e571db96ea339e34ee001c86f0f8`

All prospective regression tests, exact-source reproductions, composition, and artifact upload passed. Scientific classification is taken from the raw artifact, not workflow color.

## Reproduced authoritative inputs
0087 re-ran or reloaded only previously accepted numerical geometry:

- Solar CEvNS 0078c: area `12.519875455438353 decade^2` after exact `log10(m/GeV)+9 -> log10(m/eV)` coordinate shift; persisted data SHA256 `0339cfbcfd2ccc5689fdb82473082ffe9ebb26964ed255411952e98b72047ca5`.
- CMB Majorana 0080d: `48.332188584322665 decade^2`, exact source SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`.
- CMB Dirac 0080d: `45.129364149717375 decade^2`, same exact source archive; scenarios remain separate.
- SN1987A 0084b T+L same-variant union:
  - BODY_NATIVE: `58.474894853425305 decade^2`;
  - CONCLUSION_SUMMARY: `58.41749121763166 decade^2`.
- Wagner 0085-r1: exact active anonymous component remains `blue_3`; support `-6 <= log10(m/eV) <= -5.164592898649604`; excluded-above closure inside support gives `16.275568720525467 decade^2` in the 0087 analysis window. The object remains a pointwise strongest collection of individually published 95% CL upper limits, not a statistically combined 95% CL curve.

Blocked NA64/BBN/Cerdeno/COHERENT/finite fifth-force geometry was not approximated or inserted.

## Prospectively defined topology result
Frozen analysis window:
`-6 <= log10(m/eV) <= 10`, `-25 <= log10(g_BL) <= -2`, area exactly `368 decade^2`.

The preregistered N1 criterion required at least two permitted connected components of area `>=0.01 decade^2`.

**N1 passes in all four scenario-conditioned compositions. Every scenario has exactly three qualifying permitted components.**

### Majorana + SN BODY_NATIVE
- excluded union: `98.08268944829386 decade^2`
- permitted complement: `269.9173105517061 decade^2`
- components: `240.04319178159912`, `29.450165181291766`, `0.4239535888152022 decade^2`
- area closure relative error: `0.0`.

### Majorana + SN CONCLUSION_SUMMARY
- excluded union: `98.07489940532042`
- permitted: `269.9251005946795`
- components: `240.05098182457252`, `29.450165181291766`, `0.4239535888152022 decade^2`
- area closure relative error: `1.544658121217609e-16`.

### Dirac + SN BODY_NATIVE
- excluded union: `99.52865105557726`
- permitted: `268.4713489444227`
- components: `238.5911131348449`, `29.456282220762553`, `0.4239535888152022 decade^2`
- area closure relative error: `1.544658121217609e-16`.

### Dirac + SN CONCLUSION_SUMMARY
- excluded union: `99.51925226890216`
- permitted: `268.4807477310978`
- components: `238.60051192152`, `29.456282220762553`, `0.4239535888152022 decade^2`
- area closure relative error: `1.544658121217609e-16`.

Thus the N1 result is insensitive to both source-preserving CMB scenario choice and the two separately preserved Shin-Yun upper-mass semantics.

## Geometry of the two smaller components
The medium component is approximately bounded in x by:
- Majorana: `-5.164592898649604 <= x <= 0.0024224379083968017`;
- Dirac: `-5.164592898649604 <= x <= 0.14790331894229417`;
with y bounds reaching from `-7.823908740944319` to the analysis ceiling `-2`.

The smallest component is identical across all four branches:
- area `0.4239535888152022 decade^2`;
- bounds `3.079181246047625 <= x <= 4.0`, `-2.920818753952375 <= y <= -2.0`;
- its boundary is contributed by Solar CEvNS 0078c and SN1987A 0084b.

## Important falsification-oriented caveat
The preregistered N2 bounded-pocket criterion **does not pass**. Every permitted component, including both smaller ones, touches the finite analysis-window boundary. Therefore 0087 does **not** establish a physically bounded island or globally complete surviving corridor.

N3 also does not pass: among included objects, Wagner is the only source-authorized global upper-limit-type family. CMB/CEvNS filled polygons and SN excluded bands were correctly not reinterpreted as upper curves.

The current positive finding is narrower but real under the frozen contract: **independent accepted B-L exclusion families generate disconnected permitted topology inside the authoritative partial-analysis window in every preserved scenario branch**.

## Post-discovery structural observation to validate separately
The raw pairwise overlap matrix suggests an additional hypothesis: Wagner overlaps SN1987A (`~2.6533 decade^2`) but not CMB or Solar directly; SN overlaps both CMB (`~29.4`) and Solar (`~1.6245`), while CMB also overlaps Solar (`~5.386`). This suggests a cross-family exclusion relay in which SN1987A may act as an articulation bridge between the ultra-light Wagner regime and higher-mass CMB/solar constraints.

This **was not an 0087 preregistered novelty criterion** and therefore is recorded only as a hypothesis generated by 0087, not as an accepted discovery result. It requires a separate prospective validation gate.

## Exact next gate
Prospectively preregister 0087a to attack the candidate rather than merely repeat it:
1. inward analysis-window stress tests (no extrapolation), especially lowering the y ceiling within already-authorized support;
2. leave-one-family-out connectivity tests;
3. prospective validation or rejection of the generated `SN1987A articulation/constraint-relay` hypothesis;
4. preserve all Majorana/Dirac and BODY_NATIVE/CONCLUSION_SUMMARY alternatives.

Even if 0087a passes, missing-family stability against NA64/BBN/Cerdeno/COHERENT remains mandatory before any global allowed-region or BSM-response claim.
