# Security Policy

## Evaluation-only distribution

The software distributed from this repository is an evaluation candidate. It is not production-authorized and must not be used with real student data unless separately approved.

## Antivirus and operating-system warnings

Do **not** disable Microsoft Defender, SmartScreen or another endpoint-security product in order to run an evaluation package.

If a security product reports a detection:

1. Do not force-run the file.
2. Record the exact detection family/name, affected filename, product/version and screenshot when possible.
3. Verify the package SHA-256 against `SHA256SUMS.txt`.
4. Report the observation before continuing.

A warning that includes the term `Win32` is not, by itself, evidence that the installed OMR application payload is 32-bit. The current application payload is Windows x64; installer/bootstrap technology can have a different executable format.

## Current producer-executed security checks

The current Eval7 build procedure reports bounded Windows checks including:

- Microsoft Defender scan of the final installer with no new detections;
- Microsoft Defender scan of the installed payload with no new detections;
- install / uninstall / reinstall cycle;
- dashboard self-test;
- exact file-hash readback;
- hardened batch-processor regression tests including Unicode-path and MFP dedup cases.

These are **publisher-executed observations**, not a universal malware guarantee, penetration test, independent security audit, code-signing reputation or institutional approval.

## Private vulnerability reporting

Preferred private route: GitHub Private Vulnerability Reporting / Security Advisories for this repository:

`https://github.com/Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation/security/advisories/new`

If GitHub does not present a private-reporting form for the repository, **do not post sensitive details in a public issue**. Contact the repository owner through the GitHub profile first and request a private reporting channel.

A private report should include, when safe:

- release tag and ZIP SHA-256;
- affected filename and file hash;
- Windows version/build and architecture;
- security-product name/version and exact detection name;
- minimal reproduction steps;
- observed impact;
- redacted logs or screenshots.

Do not include real student data, credentials, keys, private source, internal datasets or non-public architecture.

## Public-safe issue reports

Public issues may be used for non-sensitive installation failures, checksum mismatches, Unicode-path failures, crashes without sensitive dumps, and evaluation feedback. Use the repository issue templates where available.

## Current open security gates

The following are **not** claimed closed:

- trusted Authenticode signing and timestamping;
- independent malware analysis / sandbox review;
- third-party antivirus reputation;
- complete public SBOM/transitive dependency validation;
- independent vulnerability assessment;
- professor/university endpoint acceptance.
