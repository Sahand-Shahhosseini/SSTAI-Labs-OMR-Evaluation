# Security Policy

## Evaluation-only distribution

The software distributed from this repository is an evaluation candidate. It is not production-authorized and must not be used with real student data unless separately approved.

## Antivirus and operating-system warnings

Do **not** disable Microsoft Defender, SmartScreen, or another endpoint-security product in order to run an evaluation package.

If a security product reports a detection:

1. Do not force-run the file.
2. Record the exact detection family/name, affected filename, product/version, and screenshot when possible.
3. Verify the package SHA-256 against `SHA256SUMS.txt`.
4. Report the observation to the repository owner before continuing.

A warning that includes the term `Win32` is not, by itself, evidence that the installed OMR application payload is 32-bit. The current OMR application payload is Windows x64; installer/bootstrap technology can have a different executable format.

## Current bounded verification

The current Eval7 candidate has undergone bounded local Windows verification including:

- Microsoft Defender scan of the final installer with no new detections;
- Microsoft Defender scan of the installed payload with no new detections;
- install / uninstall / reinstall cycle;
- dashboard self-test;
- exact file-hash readback;
- hardened batch-processor regression tests including Unicode-path and MFP dedup cases.

These checks do not constitute a universal malware guarantee, code-signing reputation, institutional acceptance, or validation on every endpoint-security product.

## Reporting a security issue

Do not disclose private SSTAI source, credentials, keys, internal datasets, or non-public architecture in a public issue.

For a binary/security observation, report only the minimum necessary public-safe information: release version, SHA-256, operating system, security-product name, exact detection name, affected filename, and reproduction steps.
