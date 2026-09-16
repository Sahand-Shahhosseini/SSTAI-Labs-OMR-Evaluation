# Eval7 Test Report — Public-Safe Evidence Summary

## Evidence class

This report summarizes **publisher-executed** engineering evidence for the current Eval7 evaluation package. It is intended to make the producer's PASS claims auditable at the level of exact run IDs, artifact hashes and observed terminal outputs. It is **not** an independent third-party validation report.

## Artifact under test

- Release tag: `v0.1.0-eval.7-current-professor`
- Release asset: `OMR_Current_Eval7_Professor_Installable.zip`
- Published SHA-256: `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`
- Release asset ID: `568003218`
- Publisher-declared private source commit: `b138c02ac6e611d8178e86b57aff545420403439`
- Publisher-declared private source tree: `a202de98201e20f08d54d73c759cecc691c5dd23`

## Primary build / verification execution

- GitHub Actions run: `35098173989`
- Job: `104800725260`
- Runner: `AENS-CANARY-SSTAI-OMR-01`
- Host: `SSTAI-DESKTOP-1`
- Runner version observed in job log: `2.337.0`
- Inno Setup compiler observed in job log: `6.7.3`
- Execution date: `2026-09-16`

Run URL:

`https://github.com/Sahand-Shahhosseini/SSTAI-OMR/actions/runs/35098173989`

The engineering repository is private; an external reviewer without repository access may not be able to open that run. The exact run ID is nevertheless published here as the producer evidence pointer.

## Observed terminal evidence

The producer-controlled run log contained the following explicit terminal observations:

| Test ID | Purpose | Expected result | Observed result | Public status |
|---|---|---|---|---|
| E7-BP-01 | Apply hardened batch-processor patch with UTF-8 path boundary | patch applied before build | `BRB001_BATCH_PROCESSOR_HARDENING_PATCH=APPLIED_WITH_UTF8_PATH_BOUNDARY` | PRODUCER-OBSERVED PASS |
| E7-DEDUP-01 | Cross-session MFP duplicate/reprocess regression | regression completes without duplicate-policy failure | `BRB001 MFP cross-session dedup + controlled reprocess integration: PASS` | PRODUCER-OBSERVED PASS |
| E7-UNICODE-01 | Windows Unicode batch/CSV path regression | Persian/CJK/emoji path cases complete | `PASS_WINDOWS_UNICODE_BATCH_CSV_PATHS_TEST_HOOKS` | PRODUCER-OBSERVED PASS |
| E7-BP-02 | Hardened current-source batch processor build | binary produced and hardening build gate passes | `BRB001_BATCH_PROCESSOR_HARDENING_BUILD=PASS` | PRODUCER-OBSERVED PASS |
| E7-INSTALLER-01 | Compile installer | Inno compiler returns successful setup build | `Successful compile`; Inno Setup `6.7.3` | PRODUCER-OBSERVED PASS |
| E7-PACKAGE-01 | Complete current-app package build | fail-closed builder emits terminal package PASS | `OMR_EVAL7_CURRENT_APP_INSTALLER=PASS` | PRODUCER-OBSERVED PASS |
| E7-HASH-01 | Bind final package identity | terminal ZIP hash equals published release digest | `ZIP_SHA256=e97eb321...` | PRODUCER-OBSERVED PASS + GitHub asset digest match |
| E7-HASH-02 | Bind current dashboard identity | terminal dashboard hash equals documented current dashboard | `DASHBOARD_SHA256=5da42d9259...` | PRODUCER-OBSERVED PASS |

Current hardened batch-processor SHA-256 reported by the same build:

`6d456f7b7754c5d9ebfdaeb5037a38effb0cf545860f97d6eceafb009ada4767`

## Scripted gates reported by the fail-closed builder

The build procedure also reports completion of these gates before emitting terminal package PASS:

- Microsoft Defender scan of the installer;
- install to a bounded evaluation location;
- dashboard self-test;
- Microsoft Defender scan of installed payload;
- uninstall;
- reinstall;
- exact installed dashboard hash readback;
- exact installed hardened batch-processor hash readback;
- cleanup uninstall.

For public audit purposes these are classified as **producer-executed / self-attested until raw per-gate evidence is independently mirrored or reproduced**. The public repository must not present them as independent validation.

## Definitions / safety properties

### Dedup regression

The current batch-processor implementation uses an MFP persistent hash ledger and records dedup lineage. The regression is intended to verify that an input previously registered under another import session is identified as a prior-session duplicate while same-session reprocessing remains controlled. A complete independent dedup validation still requires a public test matrix covering same-content/different-file, re-scan, restart/crash and false-positive cases.

### Unicode regression

The regression specifically covers Windows file/path handling through UTF-16/UTF-8 boundaries and includes Persian, CJK and emoji path cases. This does not yet constitute a complete Unicode compatibility claim for every normalization form, UNC/network path, long-path configuration or locale.

## Independent validation still open

This report does **not** close:

- clean independent professor-machine install acceptance;
- independent security/malware analysis;
- trusted Authenticode verification;
- physical paper/camera OMR accuracy;
- institution-approved scanner/MFP calibration;
- real-student-data authorization;
- third-party reproduction of the private source-to-binary build.

## Failure rule

If a future package has a different release-asset digest, installer identity, dashboard identity or current-source batch-processor identity, these results must not be silently carried forward. A new versioned test report and exact artifact binding are required.
