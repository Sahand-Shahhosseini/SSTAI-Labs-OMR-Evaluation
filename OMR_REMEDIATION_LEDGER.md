# OMR Eval7 Remediation Ledger

Audit state refreshed: 2026-09-20

This ledger separates documentation closure, publisher-observed engineering evidence, independent validation, and external/institutional acceptance. A status of `CLOSED` means the stated narrow obligation has evidence in the public distribution surface; it does **not** promote the whole product to independently validated or production-authorized status.

## Frozen identities

- Public distribution repository: `Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation`
- Evaluation tag: `v0.1.0-eval.7-current-professor`
- Tag target observed during this audit: `74db0baec0ec5523ac49ae84af0443f71d27563a`
- Public repository verification commit: `4102019affd9fffdb729e5b4115187ccc4a55acb`
- Latest public verifier run: `35487329493` — SUCCESS
- Publisher-declared private source commit: `b138c02ac6e611d8178e86b57aff545420403439`
- Publisher-declared private source tree: `a202de98201e20f08d54d73c759cecc691c5dd23`
- Public professor ZIP SHA-256: `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`
- Public ZIP release asset ID: `568003218`
- Public release ID: `389939118`

Eval7 is frozen as historical evaluation evidence. Byte-changing remediation must be published under a successor candidate/version (for example Eval8); the Eval7 asset must not be silently overwritten.

## Status vocabulary

- `CLOSED` — the narrow obligation, version/scope, acceptance criterion, evidence pointer, evidence class, and reopen condition are all stated or linked; it does not close neighboring product or institutional obligations.
- `CLOSED_DOC` — documentation obligation is closed, but the external mechanism it describes may still require independent verification.
- `PARTIAL` — useful evidence exists, but the obligation is not fully closed.
- `OPEN` — evidence or implementation is still required.
- `BLOCKED_EXTERNAL` — requires an administrative, institutional, credential, hardware, or third-party action not established by this repository.

## Remediation matrix

| Finding / obligation | Status | Current evidence / limitation | Promotion gate |
|---|---|---|---|
| Eval7 presented as evaluation candidate rather than stable production | CLOSED | GitHub Release is marked prerelease and repository claim ceiling is explicit. | Keep successor evaluation releases as prereleases until promotion criteria change. |
| Public release-byte identity | CLOSED | Release asset metadata and published SHA-256 are consistent. | New version requires a new immutable identity/hash. |
| Public Eval7 byte/manifest/receipt verification | CLOSED | GitHub-hosted workflow run `35487329493` SUCCESS: pinned checkout action; public ZIP download + SHA-256/size recompute; every ZIP member path/size/SHA checked against `PACKAGE_MANIFEST_EVAL7.json`; release metadata/asset digest/tag target checked; `FINAL_RECEIPT.txt` independently downloaded/rehashed. Evidence class: GitHub-hosted public distribution-integrity verification. | Reopen on release asset/tag/manifest/receipt drift or verifier failure. This does not validate OMR correctness or Eval8. |
| PASS wording separated from independent validation | CLOSED | `TEST_REPORT_EVAL7.md` labels producer results as `PRODUCER-OBSERVED PASS`; README separates GitHub-observed, publisher-executed, and independent evidence. | Do not relabel producer evidence as third-party validation. |
| Checksum verification instructions | CLOSED | README provides PowerShell, CMD and sha256sum instructions and fail-closed behavior on mismatch. | Keep expected digest synchronized with each new release. |
| Evaluation/review rights clarity | CLOSED | Proprietary evaluation terms allow bounded evaluation, backups, screenshots/log excerpts, black-box/dynamic review, independent benchmark execution and publication of technical findings. | Legal review if institutional contract terms supersede repository terms. |
| Private security-reporting documentation | CLOSED_DOC | `SECURITY.md` documents private vulnerability reporting through GitHub security reporting/advisory mechanisms and a fallback contact route. | Verify repository private-vulnerability-reporting setting operationally when admin access is available. |
| Package outer manifest | CLOSED | `PACKAGE_MANIFEST_EVAL7.json` binds package members/identity to the published ZIP and records installer architecture/signing state. | Regenerate for every byte-changing release. |
| Publisher source/build/artifact linkage | PARTIAL | `BUILD_ATTESTATION_EVAL7.json` binds declared source identity, build run/job, toolchain observations and output hashes. It is publisher self-attestation, not independent reproduction. | Signed provenance and/or controlled independent rebuild/source audit. |
| Raw/structured test evidence public auditability | PARTIAL | `TEST_REPORT_EVAL7.md` exposes run/job/runner and observed gates; not all raw logs/environment evidence are mirrored as immutable public artifacts. | Publish sanitized raw logs/receipts tied to exact artifact SHA and test IDs. |
| Dedup behavioral contract | CLOSED | Public-safe contract is documented in `EVAL7_BEHAVIORAL_CONTRACTS.md` from the frozen b138 implementation/test evidence. Scope is exact SHA-256 cross-session dedup only. | Add concurrency/crash/rescan/semantic-identity tests before broader claims. |
| Unicode/path behavioral contract | CLOSED | Public-safe coverage/limits are documented in `EVAL7_BEHAVIORAL_CONTRACTS.md`; synthetic Persian/CJK/emoji-space path coverage is bounded and explicit. | Add NFC/NFD, UNC/network, long-path and locale matrix before broader claims. |
| Complete machine-readable SBOM | PARTIAL | `SBOM_EVAL7_PARTIAL.cdx.json` and `SBOM_PUBLIC.md` record a partial public component inventory. | Enumerate all bundled/static/dynamic components, versions, hashes, licenses and vulnerability review. |
| Authenticode trusted publisher identity | OPEN | Current installer is documented as `NotSigned`. | Acquire trusted code-signing certificate; sign/timestamp installer and relevant binaries; publish certificate fingerprint. |
| Signed commits / signed release tag | OPEN | Audited public main commit and frozen private source commit were observed unsigned; Eval7 tag is a lightweight commit ref. | Use signed commits/tags for successor release lineage without rewriting Eval7 history. |
| Repository rulesets / protected release governance | OPEN | GitHub rulesets endpoint returned no rulesets during this audit. | Add rules/protected tags/main governance through repository administration. |
| Main branch protection read-back | BLOCKED_EXTERNAL | Branch-protection API returned `403 Resource not accessible by integration`; this connector cannot establish the admin setting. | Owner/admin must configure and provide read-back evidence. |
| GitHub Release immutability | OPEN | Release metadata reports `immutable: false`. No asset mutation is inferred from this fact. | Enable platform immutability if available, or preserve no-overwrite + new-tag supersession policy with external signatures/transparency. |
| Independent clean-machine install/runtime validation | OPEN | Publisher install/uninstall/reinstall evidence exists; independent clean-machine execution has not been established. | Independent Windows test host/VM executes documented protocol against exact `e97...` bytes. |
| Complete security/malware assessment | OPEN | Defender producer scan is bounded evidence only and is not a malware-free proof. | Independent sandbox/static/dynamic review and signed supply-chain evidence as appropriate. |
| Physical paper / camera / MFP OMR benchmark | OPEN | Repository explicitly disclaims physical accuracy validation. | Ground-truthed printed-paper/scanner/camera corpus with predefined metrics and thresholds. |
| Independent source reproduction | OPEN | Private source identity is declared and exists, but public reproducible build is not provided. | Independent confidential source/build audit or signed trusted-builder provenance/rebuild. |
| University IT/security acceptance | BLOCKED_EXTERNAL | Institutional acceptance is outside publisher-only evidence. | University IT/security review and recorded acceptance/rejection. |
| Institutional grading authorization | BLOCKED_EXTERNAL | No institutional approval is claimed. | Formal institution authorization. |
| Real-student-data authorization | BLOCKED_EXTERNAL | Evaluation policy excludes real student data without authorization. | Institutional privacy/legal/data-controller approval. |
| Real phone/browser/camera LAN acceptance | OPEN | Remains an external acceptance gate in the BRB-001 delivery program. | Execute real-device LAN protocol and retain evidence. |
| Unaided nontechnical operator E2E acceptance | OPEN | Not established by public Eval7 evidence. | Independent operator executes end-to-end workflow without developer intervention. |

## Successor Eval8 validation state

- Candidate: **Eval8 — UNRELEASED**
- Private engineering PR: `SSTAI-OMR #171`
- Exact OMR candidate head: `18000a57cc5cbf739ac02229233d88cbab3d8de9`
- Exact source tree: `66024803d6bb2586a9210918aca473bb0e275c59`
- Validation class: publisher-controlled Windows engineering validation, separate from runner-health observations and separate from external/institutional acceptance.
- Current validation workflows materialize the exact OMR commit and exact pinned third-party dependency sources before build.
- Current secondary validation run: `35487292516`
- Current release-runner validation run: `35487295216`
- Promotion rule: no prior-head result is promoted to a changed OMR head. Eval8 remains unreleased until a current-head receipt/readback closes the applicable engineering and installer-lifecycle gates.

## Authority boundary

The public repository is a distribution/evaluation evidence surface. It does not supersede the private engineering authority in `SSTAI-OMR`, nor does it by itself supersede the university full-project acceptance state in `BRB-001-OMR`.

The frozen b138 software lane remains distinct from external acceptance. An external demonstrated product defect must create a successor candidate rather than silently changing the frozen Eval7 artifact.

## Current promotion ceiling

The strongest defensible description is:

> Eval7 is a publisher-hosted Windows evaluation candidate with a pinned public release identity, public integrity checks, publisher-executed engineering evidence, and partially auditable provenance. It is not yet independently validated for university grading, physical OMR accuracy, institutional deployment, or real-student-data use.
