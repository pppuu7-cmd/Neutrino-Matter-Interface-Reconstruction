# NMIR amendment 0087d-r2 — exact B-L semantic parser conformance

Date: 2026-09-08

## Trigger
The 0087d-r1 hosted artifact successfully repaired starred `includegraphics`, but its diagnostic candidate list contained assets from all five source figure environments (rate plots, universal-model plots, B-L plots and L_mu-L_tau plots).

The infrastructure-only exact-source semantic diagnostic had already shown the source captions separately. Only the source figure labelled `fig:B-L_limits` has the explicit caption semantics:

`Excluded regions in the M_{Z'}-g_{Z'} plane for the B-L model ...`

with source assets:
- `Coherent_Results_B-L.pdf`
- `Comparison_B-L.pdf`.

The base `bl_context()` regular expression was over-broad and could accidentally match ordinary letters/punctuation in non-B-L captions. Therefore r1's multi-figure candidate set is a parser-semantic conformance failure, not a scientific ambiguity among multiple B-L figures.

## Allowed repair
Only B-L lexical-semantic recognition may change:
- accept explicit source-native forms such as `B-L`, `$B-L$`, `B\! - \!L`, `B\!-\!L`, and whitespace/TeX-spacing variants around the literal hyphen/minus;
- require an actual literal hyphen/minus relation between B and L after harmless TeX spacing-command normalization;
- do not accept generic `B ... L` adjacency without the B-minus-L token;
- reuse the already-authorized starred/unstarred includegraphics support from r1.

No source bytes, figure-coordinate logic, x-axis tick count, ≥2-decade span, residual tolerance, frame tolerance, cross-route consistency threshold, target interval, threat rule, PASS/BLOCKED/FAIL consequence or guard changes.

No new figure-axis numerical coordinates were inspected in deciding this repair. The repair is determined solely from source caption semantics and false-positive figure membership.

## Reclassification
The 0087d-r1 result is not authoritative science and is classified:

`INFRASTRUCTURE_FAIL_BL_SEMANTIC_PARSER_CONFORMANCE`

A new r2 hosted run must evaluate the unchanged frozen scientific contract on only semantically exact B-L figure environments.
