# Compatibility Matrix — Eval7

This matrix distinguishes **declared support**, **producer-tested scope**, and **not-yet-validated environments**.

| Environment / condition | Declared support | Producer-tested evidence | Current status |
|---|---:|---:|---|
| Windows 10 x64, build 18362+ | Yes | Yes, bounded publisher environment | Supported evaluation target |
| Windows 11 x64 | Expected from x64/MinVersion contract | Not independently documented here | Needs explicit test record |
| Standard non-admin user | Yes; installer uses per-user/lowest privileges | Producer install cycle reports PASS | Supported evaluation target |
| Administrator installation | Not required | Not a required gate | Not a support requirement |
| Persian/CJK/emoji local paths | Intended | Producer Unicode regression reports PASS | Bounded producer-tested |
| NFC/NFD normalization variants | Not fully specified | Not publicly evidenced | Open |
| Long-path edge cases | Not fully specified | Not publicly evidenced | Open |
| UNC/network-share installation | Not declared | Not publicly evidenced | Not supported by this claim |
| Offline evaluation | Partially intended | Runtime network requirements not fully audited publicly | Open |
| Domain-joined university endpoint | Not yet institutionally validated | No independent acceptance evidence | Open |
| Enterprise EDR/AV products | No universal guarantee | Defender only in producer test environment | Open |
| Windows ARM64 native | No | No | Not supported |
| Windows Server | No declared support | No | Not supported by current evidence |

## Installer contract observed from the private source

The publisher-declared current source uses these installer constraints:

- `ArchitecturesAllowed=x64compatible`
- `MinVersion=10.0.18362`
- `PrivilegesRequired=lowest`
- default installation under `%LOCALAPPDATA%\Programs\SSTAI\BRB001`

## Dependencies

The distributed product includes native Windows executables and resources. Publicly documented third-party components currently include Project Nayuki QR Code generator and ZXing-C++; see `SBOM_PUBLIC.md`.

A complete clean-machine prerequisite audit, including all system runtime/DLL assumptions, remains open until a public package manifest and independent clean-machine execution report are available.
