# Preregistration 0080 — B-L cosmology CMB/BBN source-asset authority audit

Date frozen: 2026-09-07
Parent state: 0079a `PASS_FIFTH_FORCE_B_L_ASYMPTOTIC_MATERIALIZATION`; 0078c `PASS_PARTIAL_B_L_EXTERNAL_ENVELOPE`.

## Scientific question
Does the primary Esseili–Kribs cosmology analysis provide a machine-reproducible source asset for the published gauged U(1)_{B-L} CMB/BBN constraint geometry, sufficient to authorize a later calibrated contour/materialization gate without manual raster reading?

## Frozen primary source
H. Esseili and G. D. Kribs, *Cosmological Implications of Gauged U(1)_{B-L} on Delta N_eff in the CMB and BBN*, JCAP 05 (2024) 110, arXiv:2308.07955v2.
Source URL: `https://export.arxiv.org/e-print/2308.07955v2`.

The primary abstract states the audited mass scope is approximately `1 eV <= m_X <= 100 MeV`; it treats distinct Majorana and Dirac neutrino scenarios. The audit must preserve this scenario distinction and must not combine their contours.

## Frozen audit procedure
1. Download the exact v2 arXiv source archive and SHA256-pin the bytes.
2. Enumerate every archive member with size and extension.
3. Identify TeX source files and locate all `includegraphics` / `includegraphics*` references plus nearby figure captions/labels.
4. Resolve graphic references to archive members without adding guessed filenames except TeX-standard extension completion (`.pdf`, `.eps`, `.svg`, `.png`, `.jpg`, `.jpeg`).
5. Identify the assets associated with published Figs. 5 and 6 (CMB/Delta N_eff Majorana/Dirac) and Figs. 7 and 8 (BBN Y_p Majorana/Dirac) only from source order/captions/labels.
6. Classify each resolved asset as vector-primary (`pdf`, `eps`, `svg`) or raster-primary (`png`, `jpg`, `jpeg`).
7. Record whether the source contains numerical tables/data/code files plausibly encoding the contour coordinates (`csv`, `tsv`, `dat`, `txt`, `npy`, `npz`, `json`, `py`) but do not interpret them in this gate.

## Forbidden
- no manual reading of contour values from any figure;
- no raster digitization;
- no calibration of plot axes;
- no selection of a stronger Majorana/Dirac scenario after seeing the shapes;
- no conversion of a Delta N_eff contour into an observed exclusion until the primary observational threshold and contour semantics are separately frozen;
- no union with 0078c or 0079a in this gate.

## Classification
- `PASS_COSMOLOGY_B_L_VECTOR_ASSET_AUTHORITY` if the relevant primary cosmology figures resolve unambiguously and at least the CMB constraint figures 5/6 are genuine vector assets suitable for a later integrity/calibration audit.
- `PASS_COSMOLOGY_B_L_NUMERICAL_ASSET_AUTHORITY` if a source numerical asset directly encoding the relevant contour geometry is found and source-linked.
- `PARTIAL_COSMOLOGY_B_L_RASTER_ONLY` if relevant figures resolve but only to raster assets and no linked numerical geometry exists.
- `BLOCKED_COSMOLOGY_B_L_SOURCE_SEMANTICS` if relevant figure/source mapping is ambiguous.
- `INFRASTRUCTURE_FAIL` if exact source bytes cannot be acquired or decoded.

A PASS authorizes only a separately preregistered 0080a integrity/semantics gate. It does not itself materialize a cosmological exclusion region.
