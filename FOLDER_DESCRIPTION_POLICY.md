# Folder Description Policy v0.1

Every tracked directory must have a bounded description. Source-owned directories require a folder-local `README.md`. Generated/vendor/build/cache/environment/package-metadata directories use an explicit non-empty `MANIFEST_EXEMPT` entry in `FOLDER_DESCRIPTIONS.json`. Existing non-empty READMEs are preserved. Every new directory must be described in the same change.
