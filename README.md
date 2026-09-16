# SSTAI Labs — OMR University Evaluation

Official public **evaluation-distribution surface** for SSTAI OMR / BRB-001.

This repository is intentionally separated from the private engineering repositories. It exists only to distribute bounded professor/university evaluation packages, checksums, provenance, release notes, and public-safe documentation.

## Current evaluation candidate

**SSTAI OMR — Eval7 Current App Professor Installer**

- Evaluation class: professor / university technical evaluation candidate
- Platform: Windows x64 application payload
- Current product source identity: `b138c02ac6e611d8178e86b57aff545420403439`
- Current dashboard SHA-256: `5da42d925991c4d600db59f7f2ea395c03e970ff90d4759311046d8c15996431`
- Hardened current-source batch processor SHA-256: `563891a8e5cf0fd7c09ff5f659b2c00b9d164df144407b25b64f935fa221f088`
- Installer SHA-256: `98f17786a210598c85b150a07c102ec1200d9866c698fc8d270985f18f17f720`
- Professor delivery ZIP SHA-256: `e3bd44eab6b9528f219d89dde9afd76aabdba435d7a92e9ca99aa05734e5a98b`

The binary package should be distributed through **GitHub Releases**, not committed into source history.

## Verification already performed

The current Eval7 delivery was built from the verified newer `b138c02...` application state rather than the older Eval3 dashboard. The current dashboard hash is different from the historical Eval3 dashboard hash.

Bounded verification completed on Windows includes:

- hardened batch processor rebuild from current product source;
- MFP cross-session dedup regression;
- Persian / CJK / emoji Unicode-path regression;
- installer compilation;
- Microsoft Defender scan of installer and installed payload with no new detections;
- install → dashboard self-test → uninstall → reinstall → exact hash readback → cleanup uninstall.

## Important scope limits

This repository and its releases are **evaluation artifacts**, not a declaration of:

- institutional acceptance;
- production authorization;
- real-student-data authorization;
- guaranteed physical-camera or physical-paper accuracy;
- completed university MFP/scanner calibration;
- source-code transfer or open-source licensing.

## Intellectual property boundary

The private source code, algorithms, internal architecture, datasets, research material, operational control plane, and other proprietary SSTAI intellectual property are **not included** in this repository.

Public access to this repository does not grant an open-source license. See [`LICENSE.md`](LICENSE.md) and [`SECURITY.md`](SECURITY.md).

## Downloads

Use the **Releases** section of this repository for official professor-facing downloads. Verify the downloaded file against [`SHA256SUMS.txt`](SHA256SUMS.txt) before use.

---

Copyright © 2026 Sahand Shahhosseini. All rights reserved.
