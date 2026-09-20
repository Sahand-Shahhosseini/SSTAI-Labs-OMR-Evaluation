# SSTAI Labs — OMR University Evaluation

Publisher-hosted public **evaluation-distribution surface** for SSTAI OMR / BRB-001.

This repository is intentionally separated from the private engineering repositories. It distributes bounded professor/university evaluation artifacts, checksums, public-safe provenance, release notes, test reports and operational documentation. It is **not** an institutional approval surface and is **not** the source-of-truth for private engineering source code.

## Published evaluation package — frozen

**SSTAI OMR — Eval7 Current App Professor Installer**

- Evaluation class: professor / university technical evaluation candidate
- Platform: Windows x64 application payload
- Publisher-declared private source identity: `b138c02ac6e611d8178e86b57aff545420403439`
- Publisher-declared private source tree: `a202de98201e20f08d54d73c759cecc691c5dd23`
- Current dashboard SHA-256: `5da42d925991c4d600db59f7f2ea395c03e970ff90d4759311046d8c15996431`
- Hardened current-source batch processor SHA-256: `6d456f7b7754c5d9ebfdaeb5037a38effb0cf545860f97d6eceafb009ada4767`
- Published professor-delivery ZIP SHA-256: `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`

**Eval7 is frozen as historical evaluation evidence. It must not be silently overwritten. Any byte-changing remediation requires a successor candidate/version.**

## Successor engineering candidate — not released

Observed state: **2026-09-20**

- Successor family: **Eval8**
- Engineering review surface: private `SSTAI-OMR` PR #171
- Current candidate head: `18000a57cc5cbf739ac02229233d88cbab3d8de9`
- State: **UNRELEASED / ENGINEERING SOURCE INTEGRATED TO PRIVATE MAIN / POST-INTEGRATION VALIDATION EXECUTING**
- Validated hardening PR: private `SSTAI-OMR` PR #171 — merged
- Controlled mainline integration PR: private `SSTAI-OMR` PR #174 — merged
- Private engineering `main`: `1241861442d29a68844265936656d0ddd6b0d039`
- Integrated tree: `bec21c7da5cd808580cb7e0ba049f30256edcf7e`
- Exact product hardening head `18000a57cc5cbf739ac02229233d88cbab3d8de9` has a successful Windows x64 publisher-controlled evidence run: `SSTAI-CHATGPT-SKILLS#35487292516` (2/2 targeted dedup; 33/33 full product-shell; CycloneDX validation; bounded OSV exact-commit review).
- Controlled union proof showed all 642 validated product-line blobs preserved exactly, all current-main-only blobs preserved except the intentional README resolution, 729/729 expected union paths, and zero unexpected paths.
- Post-union exact-tree validation run `SSTAI-CHATGPT-SKILLS#35500421896` is additional confirmation and is still executing at this documented checkpoint.
- Eval8 is **not** downloadable from this repository and source integration into private `main` is **not** a public release, production authorization, institutional acceptance, physical-accuracy validation, or grading authorization.
- The current validation lane materializes the exact candidate source outside the volatile self-hosted runner workspace and records source identity, build/test evidence, SBOM/OSV evidence and validation receipts separately from runner-health observations.
- Any future head change invalidates promotion use of earlier-head test results unless the affected scope is explicitly revalidated.

The latest published downloadable package remains frozen Eval7 until a successor candidate passes its required engineering and release gates.

## Download

**Publisher release page:** [SSTAI OMR Eval7 — Current App Professor Evaluation](https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/releases/tag/v0.1.0-eval.7-current-professor)

**Direct ZIP:** [OMR_Current_Eval7_Professor_Installable.zip](https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/releases/download/v0.1.0-eval.7-current-professor/OMR_Current_Eval7_Professor_Installable.zip)

The binary package is distributed as a GitHub Release asset, not committed into source history.

## Evidence model

The public repository distinguishes three evidence classes:

1. **GitHub-observed identity evidence** — release/tag/asset metadata and SHA-256 digest reported by GitHub.
2. **Publisher-executed engineering evidence** — build/regression/install/security checks executed on publisher-controlled Windows infrastructure and referenced by exact run IDs.
3. **Independent validation** — not yet complete unless explicitly identified as independent.

See [`TEST_REPORT_EVAL7.md`](TEST_REPORT_EVAL7.md), [`BUILD_PROVENANCE.md`](BUILD_PROVENANCE.md) and the live [`OMR_REMEDIATION_LEDGER.md`](OMR_REMEDIATION_LEDGER.md). Repeating `PASS` in documentation is not treated as multiple independent observations.

## Remediation / open promotion gates

The current audit ledger explicitly separates `CLOSED`, `PARTIAL`, `OPEN` and `BLOCKED_EXTERNAL` obligations. Major gates that remain open include trusted Authenticode signing, signed release lineage, complete SBOM/vulnerability review, independent clean-machine validation, physical paper/camera/MFP accuracy benchmarking, university IT/security acceptance, institutional grading authorization and real-student-data authorization.

Behavioral claims for deduplication and Unicode/path handling are bounded in [`EVAL7_BEHAVIORAL_CONTRACTS.md`](EVAL7_BEHAVIORAL_CONTRACTS.md). A partial machine-readable CycloneDX inventory is available at [`SBOM_EVAL7_PARTIAL.cdx.json`](SBOM_EVAL7_PARTIAL.cdx.json); it is intentionally **not** presented as a complete transitive SBOM or vulnerability-clearance attestation.

## Accuracy claim ceiling

**This repository does not provide evidence of OMR accuracy on physical paper, real phone-camera captures or an institution-approved corpus, and must not be cited as an accuracy-validation report.**

It also does not establish:

- institutional acceptance;
- production or Pilot authorization;
- official grading authorization;
- real-student-data authorization;
- completed university MFP/scanner calibration;
- universal antivirus or SmartScreen reputation;
- trusted Authenticode signing;
- source-code transfer or open-source licensing.

## Integrity verification

Expected ZIP SHA-256:

```text
e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23
```

Windows PowerShell:

```powershell
Get-FileHash .\OMR_Current_Eval7_Professor_Installable.zip -Algorithm SHA256
```

Windows CMD:

```cmd
certutil -hashfile OMR_Current_Eval7_Professor_Installable.zip SHA256
```

Linux / Git Bash:

```bash
sha256sum OMR_Current_Eval7_Professor_Installable.zip
```

macOS:

```bash
shasum -a 256 OMR_Current_Eval7_Professor_Installable.zip
```

If the computed hash differs, **do not run the package**. Re-download it from the release page and report the mismatch.

## Documentation

- [`OMR_REMEDIATION_LEDGER.md`](OMR_REMEDIATION_LEDGER.md) — live CLOSED/PARTIAL/OPEN/BLOCKED remediation state
- [`EVAL7_BEHAVIORAL_CONTRACTS.md`](EVAL7_BEHAVIORAL_CONTRACTS.md) — bounded dedup/Unicode/failure contracts and limitations
- [`PROVENANCE.md`](PROVENANCE.md) — public-safe provenance and claim ceiling
- [`TEST_REPORT_EVAL7.md`](TEST_REPORT_EVAL7.md) — producer-executed evidence with exact run references
- [`BUILD_PROVENANCE.md`](BUILD_PROVENANCE.md) — source/build/artifact linkage and unresolved trust boundaries
- [`BUILD_ATTESTATION_EVAL7.json`](BUILD_ATTESTATION_EVAL7.json) — publisher machine-readable build attestation
- [`PACKAGE_MANIFEST_EVAL7.json`](PACKAGE_MANIFEST_EVAL7.json) — release package manifest
- [`SBOM_EVAL7_PARTIAL.cdx.json`](SBOM_EVAL7_PARTIAL.cdx.json) — partial machine-readable CycloneDX inventory
- [`INSTALLATION.md`](INSTALLATION.md) — installation, removal and recovery procedure
- [`COMPATIBILITY.md`](COMPATIBILITY.md) — supported/tested environment boundaries
- [`PRIVACY.md`](PRIVACY.md) — evaluation data-handling rules
- [`SUPPORT.md`](SUPPORT.md) — support and release-lifecycle policy
- [`VERSIONING.md`](VERSIONING.md) — version and supersession model
- [`RELEASE_POLICY.md`](RELEASE_POLICY.md) — no-overwrite and release-freeze policy
- [`SBOM_PUBLIC.md`](SBOM_PUBLIC.md) — human-readable partial component/dependency inventory
- [`LICENSE.md`](LICENSE.md) — proprietary evaluation terms
- [`SECURITY.md`](SECURITY.md) — security reporting and antivirus policy

## Intellectual-property boundary

The private source code, algorithms, internal architecture, non-public datasets, research material and operational control plane are not included in this repository. Public access does not grant an open-source license.

---

Copyright © 2026 Sahand Shahhosseini. All rights reserved.
