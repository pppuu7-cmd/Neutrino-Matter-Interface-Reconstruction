# 0105a6q5f — validated exact arXiv:2006.12659 source byte acquisition

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5F`
Classification: `PASS_0105A6Q5F_ARXIV_2006_12659_SOURCE_BYTES_ACQUIRED_NONDISCOVERY`
Scope: provenance-qualified source-byte acquisition only; NONDISCOVERY.

## Prospective chain

- parent q5e BLOCKED record: `04d63cf5a8a34b97a47668bcaf4d6eff3d090f07`
- preregistration: `cc4a01a55bb8232325a82df48b0ac220a7a0bef5`
- implementation: `4526dfa1de89da5b4e0ce43f92f93c7ef1caf363`
- guards: `0154f7b8613ee611dc4798f9431fa5597d46bad0`
- execution head: `57a04d9d71f3373a202acde98af5477d7a724372`

## Hosted validation

- run/job/artifact: `34549094920/103107997103/10180111003`
- dedicated guards: `7 passed`
- provider artifact ZIP SHA256: `37561e8555d663baf8be161462ca2ee247a3fba0a7abb1fbabcea93fcaecde23`
- independently downloaded ZIP SHA256: `37561e8555d663baf8be161462ca2ee247a3fba0a7abb1fbabcea93fcaecde23`
- independent inner `result.json` SHA256: `5701d951003c06c5356ba79e8f9e10f96f86342aec26b3a4ec1c0c2699c537cb`

Green Actions success was not treated as scientific PASS; raw job and artifact bytes were checked against the frozen q5f gate.

## Exact source identity

- requested endpoint: `https://arxiv.org/e-print/2006.12659`
- final URL: `https://arxiv.org/src/2006.12659`
- HTTP: `200`
- content type: `application/gzip`
- bytes: `23805`
- MD5: `517a5ba7cd5dc2b144c909e5b6543800`
- SHA256: `5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde`
- ETag: `CPqQ6MWYqPICEAE=`
- Last-Modified: `Wed, 11 Aug 2021 05:03:07 GMT`

The source archive was not extracted; source text was not inspected; no keyword search, likelihood evaluation, systematic MC or observed BSM residual inspection occurred.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact next allowed action

A separately prospectively frozen q5f1 archive-structure/member-name locator may reacquire the exact source bundle, require SHA256 `5d000befd41e44deece46f31e1bf3ee7305bc2e8c0357b524311962ddc9d3dde` before opening archive metadata, and inspect only member names/types/sizes. No member content may be read in q5f1.