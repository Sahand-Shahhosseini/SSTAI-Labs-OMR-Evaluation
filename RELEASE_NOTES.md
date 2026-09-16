# Release Notes

## SSTAI OMR Eval7 — Current App Professor Installer

Release tag: `v0.1.0-eval.7-current-professor`

This is an **evaluation candidate** and supersedes Eval6 for current professor delivery.

### What changed

- Restored a real installer-based delivery flow.
- Bound delivery to the newer current application state `b138c02...` rather than the older Eval3 dashboard.
- Rebuilt and hardened the current-source batch processor.
- Preserved current UI/resources and university evaluation assets.
- Added exact identity checks showing the installed dashboard is not byte-identical to the historical Eval3 dashboard.
- Published the professor package as a public GitHub Release asset rather than a Gmail executable attachment.

### Producer-executed engineering results

The publisher-controlled Windows build lane reports the following bounded results:

- current dashboard identity comparison: PASS;
- hardened current-source batch-processor build: PASS;
- MFP cross-session dedup regression: PASS;
- Unicode-path regression for Persian/CJK/emoji: PASS;
- installer compilation: PASS;
- Microsoft Defender final-installer scan: no new detections reported by the test environment;
- isolated install: PASS;
- dashboard self-test: PASS;
- installed-payload Defender scan: no new detections reported by the test environment;
- uninstall: PASS;
- reinstall: PASS;
- exact installed dashboard and batch-processor hash readback: PASS;
- cleanup uninstall: PASS;
- final ZIP hash readback: PASS;
- GitHub release-asset digest observed as the same ZIP identity: PASS.

These results are publisher-executed and are **not represented as independent third-party validation**. See `TEST_REPORT_EVAL7.md` and `PROVENANCE.md`.

### Distribution

Release page:

`https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/releases/tag/v0.1.0-eval.7-current-professor`

Professor-facing package:

`OMR_Current_Eval7_Professor_Installable.zip`

SHA-256:

`e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`

Direct asset:

`https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/releases/download/v0.1.0-eval.7-current-professor/OMR_Current_Eval7_Professor_Installable.zip`

### Known limitations

- Evaluation candidate only; not institutionally approved.
- Trusted Authenticode signing is not claimed.
- SmartScreen or third-party antivirus reputation is not universally guaranteed.
- No production/Pilot or official-grading authorization is implied.
- No public claim of physical-paper/camera OMR accuracy is made.
- Institutional MFP/scanner calibration remains a separate acceptance gate.
- No real student data should be used for this evaluation.
- Public source-to-binary reproducibility is not currently provided; source linkage is publisher-attested and documented in `BUILD_PROVENANCE.md`.
