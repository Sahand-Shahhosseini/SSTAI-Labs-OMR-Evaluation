# Release Notes

## SSTAI OMR Eval7 — Current App Professor Installer

Release tag: `v0.1.0-eval.7-current-professor`

This evaluation candidate supersedes Eval6 for current professor delivery.

### What changed

- Restored a real installer-based delivery flow.
- Bound delivery to the newer current application state `b138c02...` rather than the older Eval3 dashboard.
- Rebuilt and hardened the current-source batch processor.
- Preserved current UI/resources and university evaluation assets.
- Added exact identity checks proving the installed dashboard is not the old Eval3 dashboard.
- Published the professor package as a public GitHub Release asset rather than a Gmail executable attachment.

### Verification

PASS:

- current dashboard identity differs from Eval3;
- hardened current-source batch-processor build;
- MFP cross-session dedup regression;
- Unicode-path regression for Persian/CJK/emoji;
- installer compilation;
- Microsoft Defender final installer scan with no new detections;
- isolated install;
- dashboard self-test;
- installed-payload Defender scan with no new detections;
- uninstall;
- reinstall;
- exact installed dashboard and batch-processor hash readback;
- cleanup uninstall;
- final ZIP hash readback;
- public GitHub Release asset digest recorded as the same frozen ZIP identity.

### Distribution

Release page:

`https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/releases/tag/v0.1.0-eval.7-current-professor`

Official professor-facing package:

`OMR_Current_Eval7_Professor_Installable.zip`

SHA-256:

`e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`

Direct asset:

`https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/releases/download/v0.1.0-eval.7-current-professor/OMR_Current_Eval7_Professor_Installable.zip`

The release also contains `FINAL_RECEIPT.txt` with build-specific delivery details.

### Known limitations

- Evaluation candidate only.
- Trusted Authenticode signing is not claimed.
- SmartScreen or third-party antivirus reputation is not universally guaranteed.
- No production/Pilot authorization is implied.
- Real physical paper/camera accuracy and institutional MFP calibration remain separate acceptance gates.
- No real student data should be used for this evaluation.
