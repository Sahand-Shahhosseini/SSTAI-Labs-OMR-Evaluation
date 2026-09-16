# Build Provenance — Eval7 Public-Safe Attestation

## Purpose

This document records the **publisher's source/build/artifact linkage** for Eval7. It is a public-safe attestation, not an independent reproducible-build certificate.

## Declared source identity

- Private engineering repository: `Sahand-Shahhosseini/SSTAI-OMR`
- Source commit: `b138c02ac6e611d8178e86b57aff545420403439`
- Source tree: `a202de98201e20f08d54d73c759cecc691c5dd23`

The source repository is private. An evaluator without access cannot independently reconstruct the source tree from this public repository.

## Build execution identity

- Primary Eval7 build run: `35098173989`
- Primary job: `104800725260`
- Runner: `AENS-CANARY-SSTAI-OMR-01`
- Host: `SSTAI-DESKTOP-1`
- Runner version: `2.337.0`
- Installer compiler observed: Inno Setup `6.7.3`
- Build date: `2026-09-16`

## Output identities

- Public release asset: `OMR_Current_Eval7_Professor_Installable.zip`
- Public release asset ID: `568003218`
- Asset size: `5,136,381` bytes
- ZIP SHA-256: `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`
- Current dashboard SHA-256: `5da42d925991c4d600db59f7f2ea395c03e970ff90d4759311046d8c15996431`
- Hardened current-source batch processor SHA-256: `6d456f7b7754c5d9ebfdaeb5037a38effb0cf545860f97d6eceafb009ada4767`

## Public distribution identity

- Public repository: `Sahand-Shahhosseini/SSTAI-Labs-OMR-Evaluation`
- Release ID: `389939118`
- Release tag: `v0.1.0-eval.7-current-professor`
- Tag ref currently points directly to public repository commit: `74db0baec0ec5523ac49ae84af0443f71d27563a`
- Tag type observed: lightweight ref to commit
- Release asset digest reported by GitHub: `sha256:e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`

## What this attestation establishes

The publisher states that the public Eval7 artifact is the output of the current b138 application build lineage and records exact build/run/output identities for audit and later independent checking.

## What this attestation does not establish

It does not independently prove:

- that the private source commit contains any particular implementation;
- that a third party can reproduce the same binary from the private source;
- that all build dependencies are independently verified;
- that the build host was uncompromised;
- that the package is malware-free under all analysis methods;
- that OMR accuracy is validated;
- that the tag or commits are cryptographically signed.

## Required next provenance upgrades

1. Generate and publish an exact package-content manifest with file hashes, sizes, architectures and signing status.
2. Publish a machine-readable build attestation with source, recipe, toolchain and output identities.
3. Add a public component inventory / SBOM and dependency versions.
4. Introduce cryptographic signing for release manifests and, when available, Authenticode signing for Windows binaries.
5. Use new versioned release tags for changed artifacts; do not overwrite an existing release asset.
