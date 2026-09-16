# Public Component Inventory / SBOM Summary — Eval7

## Scope

This is a **public-safe component inventory**, not yet a claim of complete transitive binary SBOM coverage. It records third-party components directly observed in the publisher-declared current private source and distributed notices.

## SSTAI component

- Product: SSTAI OMR / BRB-001
- Evaluation generation: Eval7
- Private source commit: `b138c02ac6e611d8178e86b57aff545420403439`
- License for SSTAI evaluation binary: proprietary evaluation terms; see `LICENSE.md`

## Observed third-party components

### Project Nayuki — QR Code generator library (C++)

- Purpose: local/offline QR generation
- Upstream: `https://github.com/nayuki/QR-Code-generator`
- Pinned commit: `3c6d0b3cefb4e049dc337e82237c9644399716a8`
- License: MIT
- Runtime network dependency: none; compiled into Windows product shell

### ZXing-C++

- Purpose: decode opaque physical SheetIdentity QR from captured/scanned sheets; not the OMR recognizer/scorer
- Upstream: `https://github.com/zxing-cpp/zxing-cpp`
- Declared version: `3.1.1`
- Pinned commit: `287c85df6f961c8efbfb5ffd736cd9457b8b890e`
- License: Apache-2.0
- Build mode: readers enabled; writers/C API/examples/upstream tests disabled for the BRB001 product-shell dependency
- Runtime network dependency: none; compiled into Windows product shell
- Full third-party license is distributed with the product as `third_party/ZXing-C++-LICENSE.txt`

## Build tooling observed

- Inno Setup 6.7.3 — installer build tooling observed in producer run logs; this is build tooling, not represented here as a runtime library.

## Open SBOM work

The following remain required for a complete SBOM claim:

- enumerate all executable/DLL package members;
- identify all statically and dynamically linked third-party libraries;
- record exact versions/hashes/licenses for transitive components;
- distinguish Windows system libraries from bundled third-party libraries;
- publish SPDX or CycloneDX machine-readable output tied to the exact release-asset SHA-256;
- run vulnerability review against the resulting component set.

Until those steps are complete, this file must be described as a public component inventory / partial SBOM, not a complete software-bill-of-materials attestation.
