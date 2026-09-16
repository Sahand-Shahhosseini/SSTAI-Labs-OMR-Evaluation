# Public-Safe Provenance — SSTAI OMR Eval7

## Delivery identity

- Product: SSTAI OMR / BRB-001
- Delivery class: Professor / University Evaluation Candidate
- Package label: `0.1.0-eval.7-current-professor`
- Delivery ZIP: `OMR_Current_Eval7_Professor_Installable.zip`
- ZIP SHA-256: `e3bd44eab6b9528f219d89dde9afd76aabdba435d7a92e9ca99aa05734e5a98b`
- Installer: `OMR_Current_Eval7_Setup.exe`
- Installer SHA-256: `98f17786a210598c85b150a07c102ec1200d9866c698fc8d270985f18f17f720`

## Current application identity

- Current product source identity: `b138c02ac6e611d8178e86b57aff545420403439`
- Current product tree identity: `a202de98201e20f08d54d73c759cecc691c5dd23`
- Current dashboard SHA-256: `5da42d925991c4d600db59f7f2ea395c03e970ff90d4759311046d8c15996431`
- Historical Eval3 dashboard SHA-256: `1d6ca57966ff6bff51414e37430054b53ef8ab52dceeaa34833f39f4e81117a0`
- Dashboard identity comparison: **different binaries**

This distinction is important: Eval7 is the current `b138c02...` application delivery and is not a rename/repack of the older Eval3 dashboard.

## Hardened batch processor

- Hardened current-source batch processor SHA-256: `563891a8e5cf0fd7c09ff5f659b2c00b9d164df144407b25b64f935fa221f088`
- Hardened build/regression status: PASS
- MFP cross-session dedup regression: PASS
- Windows Unicode path regression (including Persian/CJK/emoji cases): PASS

## Local Windows verification

The exact Eval7 package passed the following bounded gates on Windows:

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

Build evidence was recorded in SSTAI OMR execution run `35074940292`; exact chat-handoff readback/export was recorded in run `35075651480`.

## Claim ceiling

This provenance record proves only the bounded identities and execution gates listed above. It does **not** establish institutional acceptance, production authorization, universal antivirus reputation, trusted Authenticode signing, physical phone/paper accuracy, real-student-data authorization, or completed university MFP calibration.
