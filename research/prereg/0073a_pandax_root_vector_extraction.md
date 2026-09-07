# Iteration 0073a — PandaX ROOT-vector source extraction

Status: PROSPECTIVE / frozen before any numerical Fig.1 efficiency or Fig.3 per-bin values are extracted.
Date frozen: 2026-09-07.
Parent: 0073 `PARTIAL_PASS_PANDAX_INPUTS_NEED_ONE_NAMED_COMPONENT`.

## Question
Do the primary arXiv source assets `Fig1EffAndXsec.pdf` and `Fig3_bestFit_gpu.pdf` contain deterministic vector primitives from which the required PandaX efficiency and Fig.3 observed/background bin values can be reconstructed reproducibly without raster/manual digitization?

## Frozen provenance
Primary source archive: arXiv:2206.02339v3. Hosted source audit must hash-pin the archive and figure assets before extraction. Only the primary PDF vector content is authority; rendered screenshots are visual cross-check only.

## Frozen permitted method
1. Require zero embedded raster images in each target PDF and a deterministic vector/content stream.
2. Decode PDF content streams programmatically.
3. Identify plot frame/tick geometry from vector/text primitives, not hand-picked pixel coordinates.
4. Calibrate x/y axes using at least three labeled major ticks per linear axis; linear least-squares residual must be <= 0.02 axis units for Fig.3 x and <= 0.25 events/keV for Fig.3 y, and <= 0.002 in absolute efficiency for Fig.1 right axis. If text encoding prevents deterministic tick association, classify BLOCKED rather than infer by eye.
5. Fig.3 observed counts: accept only if a unique marker family corresponding to `Data` can be identified from the same vector style used by the legend and yields one marker per published 1-keV bin over the fitted range. Values must be quantized consistently with integer observed counts under the paper's 1-keV bins; if multiple vector families fit the legend identity, fail closed.
6. Fig.3 backgrounds: each component required by the De-Romeri likelihood may be accepted only when its legend style/color is deterministically mapped to one vector path/histogram family. Aggregate `All backgrounds` alone is insufficient for a full PASS.
7. Fig.1 efficiency: accept only when the efficiency central curve can be deterministically mapped from the right-axis legend/style and extracted as a monotone piecewise/vector curve over the fit range. The uncertainty band may be stored separately but is not a substitute for the central efficiency.
8. All extracted arrays must round-trip back to PDF user-space coordinates with <= 0.25 pt RMS and <= 0.75 pt max error for path vertices/marker centers used in the extraction.

## Frozen classifications
- `PASS_PANDAX_VECTOR_INPUTS_EXTRACTED`: exact observed 1-keV-bin data, every needed background component, and efficiency central curve are deterministically extracted and hash-frozen; next prospectively preregister SM/background benchmark reproduction.
- `PARTIAL_PASS_VECTOR_DATA_EFFICIENCY_ONLY`: observed data and efficiency are extractable, but one or more explicitly named background component arrays are not uniquely recoverable; no likelihood calculation permitted.
- `BLOCKED_PRIMARY_LIKELIHOOD_INPUTS`: controlling observed/background/efficiency information cannot be uniquely recovered under the frozen deterministic vector criteria.
- `SCIENTIFIC_FAIL_VECTOR_CALIBRATION`: vector/text primitives exist but fail the frozen calibration/round-trip tolerances.
- `INFRASTRUCTURE_FAIL`: parser/runtime/source transport fails before scientific assessment.

## Guards
No raster/manual digitization. No value selection by visual proximity. No Asimov substitution. No use of aggregate background in place of component arrays for a full likelihood PASS. No post-result tolerance relaxation. No B-L contour in 0073a.
