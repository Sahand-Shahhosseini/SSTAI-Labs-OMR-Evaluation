# Public-Safe Provenance — SSTAI OMR Eval7

## Evidence classification

This document is a **publisher provenance record**. It records declared identities, GitHub-observed release metadata, and producer-executed engineering results. It is not an independent third-party attestation.

## Delivery identity

- Product: SSTAI OMR / BRB-001
- Delivery class: Professor / University Evaluation Candidate
- Release tag: `v0.1.0-eval.7-current-professor`
- Release ID: `389939118`
- Release-tag target commit in this public repository: `74db0baec0ec5523ac49ae84af0443f71d27563a`
- Tag object type observed through GitHub API: direct `commit` ref (lightweight tag)
- Delivery ZIP: `OMR_Current_Eval7_Professor_Installable.zip`
- Release asset ID: `568003218`
- Published ZIP size: `5,136,381` bytes
- Published ZIP SHA-256: `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`
- Public release: `https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/releases/tag/v0.1.0-eval.7-current-professor`

GitHub currently reports the asset digest above. This establishes the identity of the release asset as observed on GitHub; it is distinct from an independent recomputation performed by an external evaluator.

## Publisher-declared private source identity

- Private engineering repository: `Sahand-Shahhosseini/SSTAI-OMR`
- Declared source commit: `b138c02ac6e611d8178e86b57aff545420403439`
- Declared source tree: `a202de98201e20f08d54d73c759cecc691c5dd23`
- Current dashboard SHA-256: `5da42d925991c4d600db59f7f2ea395c03e970ff90d4759311046d8c15996431`
- Historical Eval3 dashboard SHA-256: `1d6ca57966ff6bff51414e37430054b53ef8ab52dceeaa34833f39f4e81117a0`
- Current hardened batch-processor SHA-256: `6d456f7b7754c5d9ebfdaeb5037a38effb0cf545860f97d6eceafb009ada4767`

The different dashboard hashes establish only that the two files are not byte-identical. They do **not**, by themselves, prove a functional difference or source-to-binary lineage. Source-to-artifact linkage is therefore treated here as a publisher attestation supported by build-run pointers, not as an independently reproduced public build.

## Producer-executed build evidence

Primary current build run:

- GitHub Actions run: `35098173989`
- Job: `104800725260`
- Runner: `AENS-CANARY-SSTAI-OMR-01`
- Host: `SSTAI-DESKTOP-1`
- Runner version observed in logs: `2.337.0`
- Inno Setup compiler observed in logs: `6.7.3`

Observable terminal/log evidence from that run includes:

- `BRB001_BATCH_PROCESSOR_HARDENING_PATCH=APPLIED_WITH_UTF8_PATH_BOUNDARY`
- `BRB001 MFP cross-session dedup + controlled reprocess integration: PASS`
- `PASS_WINDOWS_UNICODE_BATCH_CSV_PATHS_TEST_HOOKS`
- `HARDENED_BATCH_PROCESSOR_SHA256=6d456f7b7754c5d9ebfdaeb5037a38effb0cf545860f97d6eceafb009ada4767`
- `BRB001_BATCH_PROCESSOR_HARDENING_BUILD=PASS`
- successful Inno Setup compilation
- terminal package status `OMR_EVAL7_CURRENT_APP_INSTALLER=PASS`
- terminal ZIP SHA-256 `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`
- terminal dashboard SHA-256 `5da42d925991c4d600db59f7f2ea395c03e970ff90d4759311046d8c15996431`

Additional producer-controlled gates reported by the build procedure include Microsoft Defender checks, install/self-test/uninstall/reinstall and exact installed-file hash readback. These are **publisher-executed results**. See [`TEST_REPORT_EVAL7.md`](TEST_REPORT_EVAL7.md) for the evidence class and current public audit boundary.

## What is not independently established here

This public provenance does not independently establish:

- reproducibility of the private source build by an external party;
- the semantic difference between Eval3 and Eval7 solely from hashes;
- OMR accuracy on physical answer sheets or real phone-camera captures;
- institutional acceptance or grading authorization;
- absence of malware under all security products;
- trusted Authenticode publisher identity;
- release immutability at the GitHub platform level;
- signed commit/tag provenance.

## Claim ceiling

This record **documents** the identities and producer-executed observations listed above. It does not claim that those execution results have been independently reproduced or institutionally validated.
