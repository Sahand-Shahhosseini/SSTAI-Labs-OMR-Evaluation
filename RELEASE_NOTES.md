# Release Notes

## SSTAI OMR Eval7 — Current App Professor Installer

Release label: `0.1.0-eval.7-current-professor`

This evaluation candidate replaces the earlier Eval6 professor handoff for current delivery.

### What changed

- Restored a real installer-based delivery flow.
- Bound delivery to the newer current application state `b138c02...` rather than the older Eval3 dashboard.
- Rebuilt and hardened the current-source batch processor.
- Preserved current UI/resources and university evaluation assets.
- Added exact identity checks proving the installed dashboard is not the old Eval3 dashboard.

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
- final ZIP hash readback.

### Distribution files

Official professor-facing package:

`OMR_Current_Eval7_Professor_Installable.zip`

Expected SHA-256:

`e3bd44eab6b9528f219d89dde9afd76aabdba435d7a92e9ca99aa05734e5a98b`

Inside the ZIP, the installer is:

`OMR_Current_Eval7_Setup.exe`

Expected installer SHA-256:

`98f17786a210598c85b150a07c102ec1200d9866c698fc8d270985f18f17f720`

### Known limitations

- Evaluation candidate only.
- Trusted Authenticode signing is not claimed.
- SmartScreen or third-party antivirus reputation is not universally guaranteed.
- No production/Pilot authorization is implied.
- Real physical paper/camera accuracy and institutional MFP calibration remain separate acceptance gates.
- No real student data should be used for this evaluation.
