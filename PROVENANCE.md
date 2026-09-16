# Public-Safe Provenance — SSTAI OMR Eval7

## Delivery identity

- Product: SSTAI OMR / BRB-001
- Delivery class: Professor / University Evaluation Candidate
- Release tag: `v0.1.0-eval.7-current-professor`
- Delivery ZIP: `OMR_Current_Eval7_Professor_Installable.zip`
- Published ZIP SHA-256: `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`
- Public release: `https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/releases/tag/v0.1.0-eval.7-current-professor`

The exact installer hash for each frozen package build is recorded inside the release asset `FINAL_RECEIPT.txt`; the public repository-level checksum file pins the outer delivery ZIP and the independently stable product identities below.

## Current application identity

- Current product source identity: `b138c02ac6e611d8178e86b57aff545420403439`
- Current product tree identity: `a202de98201e20f08d54d73c759cecc691c5dd23`
- Current dashboard SHA-256: `5da42d925991c4d600db59f7f2ea395c03e970ff90d4759311046d8c15996431`
- Historical Eval3 dashboard SHA-256: `1d6ca57966ff6bff51414e37430054b53ef8ab52dceeaa34833f39f4e81117a0`
- Dashboard identity comparison: **different binaries**

This distinction is important: Eval7 is the current `b138c02...` application delivery and is not a rename/repack of the older Eval3 dashboard.

## Hardened batch processor

- Hardened current-source batch processor SHA-256: `6d456f7b7754c5d9ebfdaeb5037a38effb0cf545860f97d6eceafb009ada4767`
- Hardened build/regression status: PASS
- MFP cross-session dedup regression: PASS
- Windows Unicode path regression (including Persian/CJK/emoji cases): PASS

## Local Windows verification

The Eval7 current-app package passed the following bounded gates on Windows:

- installer compilation: PASS;
- Microsoft Defender installer scan: PASS / no new detections;
- install: PASS;
- dashboard self-test: PASS;
- Microsoft Defender installed-payload scan: PASS / no new detections;
- uninstall: PASS;
- reinstall: PASS;
- installed dashboard exact-hash readback: PASS;
- installed hardened batch-processor exact-hash readback: PASS;
- cleanup uninstall: PASS;
- final ZIP hash readback: PASS.

The final public release asset is reported by GitHub with the same SHA-256 digest `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`.

## Public-release contents

The release contains:

- `OMR_Current_Eval7_Professor_Installable.zip`
- `FINAL_RECEIPT.txt`

The public release itself contains no private engineering source tree.

## Claim ceiling

This provenance record proves only the bounded identities and execution gates listed above. It does **not** establish institutional acceptance, production authorization, universal antivirus reputation, trusted Authenticode signing, physical phone/paper accuracy, real-student-data authorization, or completed university MFP calibration.
