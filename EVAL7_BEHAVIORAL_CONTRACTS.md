# Eval7 Behavioral Contracts — Public-Safe Audit Summary

Source scope: frozen publisher-declared b138 source identity `b138c02ac6e611d8178e86b57aff545420403439` / tree `a202de98201e20f08d54d73c759cecc691c5dd23`.

This document summarizes externally relevant behavior supported by the frozen implementation/tests. It intentionally does not publish private source code and does not expand the claim beyond observed contracts.

## 1. MFP cross-session dedup contract

### Identity key

For the tested MFP batch flow, duplicate identity is based on an **exact SHA-256 content digest** recorded in a persistent ledger. The demonstrated behavior is therefore byte/content-hash deduplication, not semantic or perceptual physical-sheet identity.

### Session behavior

- A valid SHA-256 identity is a 64-character hexadecimal digest.
- Session identifiers are bounded and restricted to a conservative character set.
- The first accepted occurrence of a digest records the digest and its originating session.
- Re-processing the same digest in the **same session** is allowed by the tested contract.
- Seeing the same digest in a **different session** is classified as a prior-session duplicate and is blocked by default.
- A controlled reprocess can be authorized by supplying a bounded operator reason.
- An authorized reprocess creates a separate audit record linking the original session, reprocess session and reason.
- The original first-session provenance is preserved; an authorized reprocess does not replace the original origin record.

### Integration regression demonstrated in the frozen test

The frozen cross-session integration test exercises this sequence:

1. `SESSION_A` + payload A -> finalized.
2. `SESSION_A` + the same payload A -> finalized again; not treated as a prior-session duplicate.
3. `SESSION_B` + the same payload A -> classified as prior-session duplicate and not finalized.
4. `SESSION_B` + payload A + controlled operator reprocess reason -> finalized and one reprocess audit row is recorded.
5. `SESSION_C` + different payload B -> finalized.
6. The persistent first-origin ledger retains two identities: payload A -> `SESSION_A`, payload B -> `SESSION_C`.
7. Removing the reprocess override causes the cross-session duplicate to block again.

### Fail-closed property within this scope

Within this exact-content policy, a cross-session exact duplicate is not silently finalized unless the bounded controlled-reprocess path is explicitly used.

### Explicit limitations

This evidence does **not** establish:

- semantic deduplication of two different byte representations of the same physical sheet;
- reliable recognition that two independent scans/photos are the same sheet when their bytes differ;
- collision resistance beyond the cryptographic properties assumed for SHA-256;
- correctness under all concurrent-writer/race conditions;
- all crash/interruption/recovery interleavings;
- deduplication based on student identity, answer pattern, image similarity or perceptual hashing;
- institutional policy for when an operator should authorize a reprocess.

A broader dedup claim requires separate concurrency, crash, rescan, correction/version and physical-sheet-identity tests.

## 2. Windows Unicode/path contract

### Demonstrated synthetic coverage

The frozen Windows UTF-8 boundary test uses a path containing:

- Persian text;
- CJK text;
- emoji;
- spaces.

The synthetic example family includes a component equivalent to `کاربر 測試 📄`.

The test is bounded to Windows environments at or above Windows 10 build 18362 for the tested UTF-8 active-code-page contract.

### Manifest/build boundary

The test checks the expected UTF-8 active-code-page manifest behavior for the relevant Windows binary boundary.

### Operator/runtime boundary

In operator-mode coverage, binaries and synthetic input are staged through Unicode paths and the workflow checks:

- process execution through that path;
- grading/runtime flow;
- SQLite put/count/get operations;
- backup/reopen behavior;
- preservation/read-back of the Unicode path and stored bytes.

### Batch/CSV boundary

In the batch-mode test hook, synthetic non-photo input is processed through Unicode paths and the test verifies that CSV output preserves the exact Unicode input/work paths and can be reopened/read back. The frozen producer evidence reports terminal token:

`PASS_WINDOWS_UNICODE_BATCH_CSV_PATHS_TEST_HOOKS`

### Explicit limitations

This evidence does **not** establish universal Windows pathname compatibility. In particular, it does not by itself prove:

- all NFC/NFD or other Unicode normalization forms;
- all RTL/control-marker edge cases;
- all Windows locales/code-page configurations;
- UNC/network-share paths;
- Windows long-path boundary behavior;
- every non-ASCII username/profile/TEMP combination;
- every filesystem or institutional endpoint policy.

These cases remain successor test-matrix work.

## 3. Failure and review semantics supported by current evaluation evidence

The public Eval7 evidence supports a conservative interpretation:

- integrity/hash mismatch -> do not execute the package;
- cross-session exact duplicate without controlled override -> block that duplicate finalization in the tested batch contract;
- antivirus/security detection -> do not disable endpoint protection or force-run; capture the product/detection/hash and report it;
- unsupported/uncertain OMR conditions are not evidence of safe automatic grading and must remain bounded by the existing review/acceptance claim ceiling.

This document does not invent a complete production failure-state machine. Full corruption, storage exhaustion, power-loss, concurrency, institutional rollback and physical ambiguity semantics require additional test evidence and are tracked as open promotion gates.

## 4. Test-vs-validation boundary

Passing these regression contracts means the stated behaviors were observed in the publisher-controlled test lane for the frozen source/artifact lineage. It does **not** establish independent validation, physical OMR accuracy, malware absence, or institutional fitness for grading.
