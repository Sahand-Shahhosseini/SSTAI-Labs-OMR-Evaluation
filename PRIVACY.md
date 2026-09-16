# Privacy and Evaluation Data Handling — Eval7

## Evaluation data boundary

This release is for bounded technical evaluation only. **Do not use real student data, official examination records, credentials, or institutional production data.**

Use synthetic or otherwise explicitly authorized non-PII test material.

## Local storage

The application may create local evaluation/runtime data under:

`%LOCALAPPDATA%\SSTAI-OMR`

This may include exam definitions, sessions, imported images, processing outputs, review data, deduplication state, validation evidence, and draft institution/form profiles.

The installer itself is per-user. Removing the application does not imply that all runtime/evaluation data has been securely deleted.

## Network behavior

The current product includes local browser/phone capture functionality and may expose a bounded host-side HTTP receiver for local evaluation workflows. The public repository does not currently provide a complete independently audited network-endpoint inventory.

Therefore, for evaluation:

- use a controlled test network;
- do not expose the receiver directly to the public Internet;
- do not transmit real student data;
- do not assume that university IT/security approval has been granted;
- record unexpected outbound connections or authentication prompts as a finding.

## Telemetry and external services

No claim of a complete independent telemetry audit is made in this repository. Evaluators should treat telemetry/network behavior as an explicit review item rather than assume absence.

## Logs and screenshots

Before sharing logs or screenshots publicly, remove:

- student names or IDs;
- real answer-sheet images;
- credentials/tokens;
- local usernames when unnecessary;
- internal institutional paths or hostnames;
- private source or architecture details.

## Retention and deletion

For an evaluation run:

1. Define the test-data retention period before use.
2. Keep only evidence needed for the evaluation.
3. Remove test data from `%LOCALAPPDATA%\SSTAI-OMR` after the evaluation when preservation is not required.
4. Do not interpret application uninstall as a secure wipe.

## Current privacy claim ceiling

This document is an evaluation policy, not a completed institutional privacy assessment. Data-controller authority, retention approval, role-based access, incident response, and real-student-data authorization remain separate institutional gates.
