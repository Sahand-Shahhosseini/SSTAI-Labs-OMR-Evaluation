# SSTAI Labs — OMR University Evaluation

Official public **evaluation-distribution surface** for SSTAI OMR / BRB-001.

This repository is intentionally separated from the private engineering repositories. It exists only to distribute bounded professor/university evaluation packages, checksums, provenance, release notes, and public-safe documentation.

## Current evaluation candidate

**SSTAI OMR — Eval7 Current App Professor Installer**

- Evaluation class: professor / university technical evaluation candidate
- Platform: Windows x64 application payload
- Current product source identity: `b138c02ac6e611d8178e86b57aff545420403439`
- Current product tree: `a202de98201e20f08d54d73c759cecc691c5dd23`
- Current dashboard SHA-256: `5da42d925991c4d600db59f7f2ea395c03e970ff90d4759311046d8c15996431`
- Hardened current-source batch processor SHA-256: `6d456f7b7754c5d9ebfdaeb5037a38effb0cf545860f97d6eceafb009ada4767`
- Published professor-delivery ZIP SHA-256: `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`

## Official download

**Release:** [SSTAI OMR Eval7 — Current App Professor Evaluation](https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/releases/tag/v0.1.0-eval.7-current-professor)

**Direct ZIP:** [OMR_Current_Eval7_Professor_Installable.zip](https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/releases/download/v0.1.0-eval.7-current-professor/OMR_Current_Eval7_Professor_Installable.zip)

The binary package is distributed as a **GitHub Release asset**, not committed into source history.

## Verification already performed

The current Eval7 delivery was built from the verified newer `b138c02...` application state rather than the older Eval3 dashboard. The current dashboard hash is different from the historical Eval3 dashboard hash.

Bounded verification completed on Windows includes:

- hardened batch processor rebuild from current product source;
- MFP cross-session dedup regression;
- Persian / CJK / emoji Unicode-path regression;
- installer compilation;
- Microsoft Defender scan of installer and installed payload with no new detections;
- install → dashboard self-test → uninstall → reinstall → exact hash readback → cleanup uninstall;
- final package publication as a public GitHub Release asset with GitHub-reported SHA-256 digest.

## Important scope limits

This repository and its releases are **evaluation artifacts**, not a declaration of:

- institutional acceptance;
- production authorization;
- real-student-data authorization;
- guaranteed physical-camera or physical-paper accuracy;
- completed university MFP/scanner calibration;
- trusted Authenticode/code-signing reputation;
- source-code transfer or open-source licensing.

## Intellectual property boundary

The private source code, algorithms, internal architecture, datasets, research material, operational control plane, and other proprietary SSTAI intellectual property are **not included** in this repository.

Public access to this repository does not grant an open-source license. See [`LICENSE.md`](LICENSE.md) and [`SECURITY.md`](SECURITY.md).

## Integrity

Verify the downloaded release ZIP against [`SHA256SUMS.txt`](SHA256SUMS.txt). The release also contains `FINAL_RECEIPT.txt` as a public build/delivery receipt.

---

Copyright © 2026 Sahand Shahhosseini. All rights reserved.
