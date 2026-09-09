# 0100c — Kato/Nagakura 25 Msun coherent source+profile control

Date frozen: 2026-09-09
Parent benchmark: `NMIR-BENCHMARK-0100`
State: PREREGISTERED_AUTHORITY_PINNING_ONLY

## Purpose

Create a second standard-3-flavor+MSW control in which the stellar structure and emitted neutrino spectra come from the **same published Kato/Nagakura model series**, rather than combining a Farmer 25 Msun density/Ye profile with an unrelated source spectrum.

This benchmark is additive. It does **not** replace or rewrite the already frozen Farmer control `0100a/0100b`.

## Frozen external authorities

### Neutrino emission data

Kato, Nagakura, Ito, Hirai, Furusawa, Yoshida, Akaho, *Comprehensive Neutrino Light Curves and Spectra: From Pre-supernova Evolution to Early Supernova Phase* data release.

- original Zenodo record: `10.5281/zenodo.18886215`;
- the record explicitly directs users who need individual progenitor models to version 1.1: `10.5281/zenodo.20618971`;
- data include luminosities, mean energies, and spectra for all neutrino flavors;
- progenitor masses span 10–40 Msun and include MESA models.

Only the v1.1 individual-progenitor release may be used for 0100c. The earlier monolithic v1 archive must not silently replace it.

### Stellar evolution models

Companion model dataset:

- Zenodo DOI: `10.5281/zenodo.20822085`;
- MESA version: `r24.08.1`;
- MESA SDK: `x84_64-linux-24.7.1`;
- OS: AlmaLinux 9.8;
- published 25 Msun archive: `25msun.tar.gz`;
- published MD5: `b34c9573c929638afac89cec43ae7203`;
- dataset description states `XXmsun.tar.gz` bundles profile and history files for an `XX` solar-mass star with no mass loss.

The exact 25 Msun archive identity above is frozen before any parser sees its contents.

## Control-model identity

0100c is restricted to:

- stellar-evolution family: `MESA`;
- ZAMS mass: `25 Msun`;
- Kato/Nagakura 2026 model series;
- no mass loss, as documented for the companion stellar archive;
- standard 0100 NO and IO PMNS branches unchanged.

This is a **control benchmark environment**, not a claim that Betelgeuse is a 25 Msun no-mass-loss progenitor.

## Coherence gate

A terminal 0100c calculation is forbidden unless a deterministic parser establishes from released metadata/files that the selected spectrum/light-curve object and the selected `rho(r), Ye(r)` profile belong to the same MESA 25 Msun model and can be tied to a common evolutionary time/snapshot.

Required proof fields include, where present in the release:

- model family/name;
- ZAMS mass;
- evolutionary time or time-to-bounce;
- model/profile number or other snapshot identity;
- source-spectrum step number;
- any mapping table supplied by the authors.

If no released metadata supports an unambiguous spectrum-to-profile snapshot mapping, the correct status is

`BLOCKED_0100C_SPECTRUM_PROFILE_SNAPSHOT_MAPPING_UNPINNED`

and no nearest-neighbour time match may be invented after inspecting the physics result.

## Deterministic selection rule

The future pinning workflow must:

1. download only the prospectively named 25 Msun MESA source/model assets;
2. verify every published top-level checksum available from Zenodo;
3. enumerate candidate spectrum/light-curve members and stellar profile/history members without using the resulting oscillation probabilities;
4. retain only members whose released metadata identify `MESA` and `25 Msun`;
5. construct all candidate spectrum↔profile correspondences from explicit released time/snapshot identifiers;
6. require exactly one correspondence for each frozen terminal evaluation snapshot, or return BLOCKED;
7. hash every selected internal member and every normalized derivative table;
8. write a non-terminal discovery artifact;
9. freeze exact member paths/hashes, normalization rules, snapshot mapping and the terminal energy/time grid in a later immutable lock **before** the MSW terminal run.

No member may be selected because it produces a stronger/weaker NMIR result.

## Energy-grid rule

The terminal energy grid must be taken directly from the selected released Kato/Nagakura spectrum file. No plot digitization, analytic refit, hand smoothing, or replacement by an arbitrary log grid is allowed.

Interpolation is allowed only after the native grid has been frozen and only through a prospectively specified deterministic rule. Native-grid results must remain available as the authority result.

## Source-spectrum semantics

The released source spectra are source-emission inputs. Standard 0100 MSW propagation may redistribute flavors through the frozen Hamiltonian, but 0100c may not add:

- neutrino self-interaction / collective conversion;
- NSI;
- sterile states;
- spin-flavor conversion;
- detector response or cross-section changes;
- G9 ray refitting.

Those belong to other benchmark slots.

## Relation to 0100b Farmer control

The two controls answer different questions:

- `0100b Farmer`: independently authoritative `rho(r), Ye(r)` profile for standard MSW propagation; source-spectrum authority remains separate.
- `0100c Kato/Nagakura`: attempts a same-series stellar-profile + neutrino-spectrum control with explicit snapshot coherence.

Neither may be tuned to agree with the other. A discrepancy must be reported as model/source-environment dependence unless a reproducible implementation error is identified.

## Terminal ceiling before exact asset lock

Until the v1.1 25 Msun MESA neutrino-emission member(s), the 25 Msun stellar member(s), their hashes, and an unambiguous snapshot mapping are frozen, the maximum status is

`BLOCKED_0100C_COHERENT_SOURCE_ASSET_LOCK_UNPINNED`.

A future successful pinning step may create a lock provisionally named

`research/locks/0100d_kato_nagakura_25msun_coherent_source_lock.json`.

Even after that lock, detector-level event predictions remain separately subject to the interaction/transport authority gates inherited from 0100.

## Interpretation

A successful 0100c standard-MSW control would provide a self-consistent published 25 Msun source environment for comparing flavor transfer against the independent Farmer profile control. It would not validate either stellar model as a Betelgeuse progenitor and would not by itself establish detector-level observability.
