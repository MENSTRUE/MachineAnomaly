# Scripts and operational helpers

This folder is reserved for small, reproducible maintenance helpers **within the existing standard repository structure**. No executables or scripts are assumed to exist just because this README does.

Future script candidates (not implemented): a bounded engineered-feature CSV sample exporter, SHA-256 evidence manifest verifier, model-compatibility check, dataset-provenance audit and non-sensitive project integrity checker. Prefer adding these only when they are needed and tested.

Example **manual** verification from root:
```powershell
Get-ChildItem models -Recurse -Filter *.joblib | Select-Object FullName,Length
Get-ChildItem assets/plots -Recurse -Filter *.png | Select-Object Name,Length
git status
```

Never add scripts that automatically download entire third-party datasets, remove user data, rewrite research metrics, silently push to GitHub or deserialize untrusted artifacts. Raw experimental data is handled separately from repo source control.
