# 0105a6q5d — validated Argon four-file bounded semantic-evidence inventory

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5D`
Classification: `PASS_0105A6Q5D_BOUNDED_SEMANTIC_EVIDENCE_INVENTORY_COMPLETE_NONDISCOVERY`
Scope: deterministic authority/semantic evidence inventory only; NONDISCOVERY.

## Prospective chain

- parent q5c1 byte-lock PASS record: `908038bcff4f6f1c6554dbb03c1ce339546d9173`
- preregistration: `b0d5a15e8bcba061fc2c3000fff0e299828caf72`
- implementation: `f5fd0cca01b070ab7f54814fc46c0e1539a50718`
- guards: `7093f04fb3076f8a693bed8a55737540e65a0d4b`
- execution head: `36fd99270bf11aec076849c6560a4315c3a4a72f`

## Hosted validation

- run/job/artifact: `34548694721/103106794490/10179973686`
- dedicated guards: `8 passed`
- provider artifact ZIP SHA256: `269ff3984ff40b7010f35b755b4f1ef5207ba82ae285d08ef035b29b1d30a178`
- independently downloaded ZIP SHA256: `269ff3984ff40b7010f35b755b4f1ef5207ba82ae285d08ef035b29b1d30a178`
- independent inner `result.json` SHA256: `0c45f7cbba28c5a3a21222d45ff3bd6260ad9849629e71c3be9c82ddc875a324`

Green Actions success was not treated as scientific PASS; the raw job, source identities and artifact bytes were checked against the frozen q5d gate.

All four official source payloads again matched q5c1 exact size + MD5 + SHA256 identities before any evidence extraction.

## Frozen evidence hit counts

- `CENNS10AnlAEfficiency.txt`: E1=0, E2=0, E3=0, E4=0, E5=0, E6=0.
- `LArParametersAnlA.yaml`: E1=8, E2=45, E3=9, E4=1, E5=9, E6=4.
- `PlotExtractedData.C`: E1=0, E2=0, E3=7, E4=0, E5=60, E6=0.
- `readYAMLParameters.py`: E1=0, E2=13, E3=0, E4=0, E5=0, E6=0.

Notable inventory facts only (not yet implementation adjudication): YAML lines 54/62/70/78/86/94/102/112 mention normalizations before/after a 3D likelihood fit; YAML line 108 contains `3154`; `PlotExtractedData.C` line 169 contains `double cvss = 3152.0;`. The frozen q5e semantic adjudication criteria were committed at `7e414409b9f79da0a24090ef5ce3583d67a30e09` **before this hosted q5d evidence artifact was inspected**.

q5d itself performs no likelihood, fitting, nuisance profiling, pseudo-data generation, systematic MC or observed residual inspection.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact next allowed action

Execute q5e only against the complete q5d E1–E6 evidence inventory under its already-frozen F1/F4/F6/F7 criteria. If any required contract remains absent or ambiguous, q5e must be BLOCKED rather than filled by convention.