# Support and Release Lifecycle

## Current supported evaluation release

Current professor-facing evaluation release:

`v0.1.0-eval.7-current-professor`

This release supersedes Eval6 for current delivery. Earlier packages remain historical evidence and should not be used for new professor/university evaluation unless explicitly re-authorized.

## Status vocabulary

- **Current Evaluation Candidate** — publisher-designated package for bounded review.
- **Superseded** — retained for history but not recommended for new evaluation.
- **Revoked** — must not be used because identity, security or correctness was invalidated.
- **Production/Pilot** — not authorized by the current release.

## Support scope

Supported questions for this public repository include:

- download and checksum verification;
- installation/uninstallation problems;
- antivirus/SmartScreen observations;
- crashes and reproducible failures using synthetic/non-PII data;
- Unicode/path handling;
- evaluation feedback;
- documentation inconsistencies.

## Out of scope without separate authorization

- official grading;
- real student data;
- production deployment;
- institutional procurement acceptance;
- public disclosure of private SSTAI source/architecture;
- guaranteed physical-paper/camera accuracy.

## Supersession policy

Changed executable/package bytes require a new versioned release or explicit revision identifier. Existing release assets should not be silently overwritten. A replacement release must identify what it supersedes and publish a new checksum.

## Revocation policy

A release should be marked revoked/superseded if any of the following is established:

- published asset hash does not match the documented identity;
- a security issue makes continued evaluation unsafe;
- package/source provenance is materially wrong;
- the installer deploys the wrong application lineage;
- a critical data-loss or integrity defect is confirmed.

## Response expectations

This repository currently provides best-effort research/evaluation support; no commercial SLA is promised. Security-sensitive reports should follow `SECURITY.md` rather than public issue discussion.
