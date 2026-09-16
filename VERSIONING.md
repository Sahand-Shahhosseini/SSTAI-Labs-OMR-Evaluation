# Versioning and Identity Model

The public evaluation repository uses several different identifiers. They are not interchangeable.

| Identifier | Meaning | Example |
|---|---|---|
| Product family | Logical project/product identity | `SSTAI OMR / BRB-001` |
| Evaluation generation | Human-readable evaluation generation | `Eval7` |
| Public release tag | GitHub release identity | `v0.1.0-eval.7-current-professor` |
| Public release ID | GitHub native release identity | `389939118` |
| Public tag target commit | Commit in this public distribution repo | `74db0baec0ec5523ac49ae84af0443f71d27563a` |
| Private source commit | Publisher-declared engineering source identity | `b138c02ac6e611d8178e86b57aff545420403439` |
| Private source tree | Publisher-declared source-tree identity | `a202de98201e20f08d54d73c759cecc691c5dd23` |
| Release asset hash | Exact distributed ZIP identity | `e97eb321b15efd3068a9b10b9f3e399cb8b1a2495e33d8b5d82cb792ba347a23` |

## Rules

1. A change to release ZIP bytes requires a new checksum and must not be silently treated as the old artifact.
2. A change to application binaries requires a new evaluation revision/generation or explicit supersession record.
3. Source commit identity is not a substitute for release-asset identity.
4. Release-asset hash identity is not a substitute for functional validation.
5. Different executable hashes prove only byte-level difference unless additional evidence establishes semantic change.
6. Historical releases remain distinguishable; they must not be relabeled as the current release.

## Current lineage

- Eval3: historical evaluation lineage; not the current professor handoff.
- Eval6: historical/superseded professor handoff; do not use for current delivery.
- Eval7: current professor/university evaluation generation.
- Current public release: `v0.1.0-eval.7-current-professor`.

## Future release naming

If Eval7 package bytes must change after publication, use a new version such as:

- `v0.1.0-eval.7.1-current-professor`, or
- a new evaluation generation such as `Eval8` when behavior/scope materially changes.

Do not overwrite an existing asset while retaining the same version identity.
