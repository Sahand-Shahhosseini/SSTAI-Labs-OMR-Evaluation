# Release Freeze and Supersession Policy

## Objective

Keep professor/university evaluation artifacts identifiable, non-ambiguous and auditable over time.

## No-overwrite rule

Once a release asset has been published and referenced externally, its bytes must not be silently replaced under the same release identity.

If package bytes change:

1. produce a new version/tag or explicit revision;
2. publish a new SHA-256;
3. state which prior release is superseded;
4. preserve historical release metadata unless a security/legal reason requires withdrawal;
5. never claim old test evidence ran on new bytes without an explicit evidence-freshness justification.

## Current Eval7 release

- Tag: `v0.1.0-eval.7-current-professor`
- Release ID: `389939118`
- Tag target commit: `74db0baec0ec5523ac49ae84af0443f71d27563a`
- ZIP asset ID: `568003218`
- ZIP SHA-256: `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23`

The tag is currently observed as a lightweight ref to a commit, not an annotated/signed tag.

## Platform immutability

GitHub release metadata previously reported `immutable: false`. This repository therefore does not rely on platform immutability as its only control. The governance control is:

- versioned release identity;
- published SHA-256;
- no-overwrite policy;
- explicit supersession;
- preserved release IDs/asset IDs;
- future cryptographic signing where available.

## Prerelease semantics

This package is an evaluation candidate and should be treated as prerelease/evaluation-only even if a GitHub metadata field is temporarily inconsistent. Release metadata should be corrected to prerelease status where supported; the textual claim ceiling remains authoritative for use.

## Revocation

If a release is revoked, the repository should publish a visible notice containing:

- revoked tag/version;
- reason;
- date;
- replacement release if any;
- affected SHA-256;
- required evaluator action.

## Future signing

Preferred future hardening:

- signed annotated release tags;
- signed checksum/manifest;
- Authenticode-signed Windows binaries/installer when a trusted code-signing certificate is available;
- verifiable build attestation.
