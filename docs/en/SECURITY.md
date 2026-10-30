# Security and data-handling policy

## Classification: research prototype / not production hardened
**Critical trust boundary:** `joblib` uses pickle; loading untrusted artifacts can execute code. Use only verified local Kaggle outputs. The API model path is allowlisted by known target name; preserve this invariant. Verify provenance and hashes of models before distribution and deployment.

## Threats and mitigations
| Risk | Current control | Required before public deployment |
|---|---|---|
| Arbitrary model deserialization | Fixed registry paths / known target enumeration | Model signing, artifact registry, immutable release versions, permissions, malware/code review |
| CSV abuse | 10 MiB / 2,000-row bounds, `.csv` extension, exact finite-numeric schema | Rate limits, auth, request timeout, CSV parser fuzzing, resource monitoring |
| Model misuse | Condition-class and anomaly disclaimer | Explicit uncertainty/operational policies and human review |
| CORS/exposure | Localhost allowed origins by default | Explicit production origin list and strict reverse proxy |
| Secrets in Git | `.gitignore` should exclude `.env`, keys, tokens and caches | Secret scan in CI, credential rotation if ever pushed |
| User/plant data privacy | Client uploads local CSV to backend | Privacy classification, encryption, access control, retention/deletion and audit policy |
| Mismatched dependencies | Python packages declared in `backend/requirements.txt` | Full version pinning, reproducible builds, compatibility tests |
| Supply-chain dependencies | npm + pip packages | Dependency scanning, lockfiles, update governance |

## Handling rules
Never commit raw industrial telemetry, private organizational datasets, access tokens, model files from unknown provenance, Kaggle credentials or authentication session data. Do not write full uploaded CSV content to ordinary logs. Images used as evidence must be genuine screenshots/plots, stripped of secrets and personal information.

## Vulnerability reporting
Use private communication with the repository owner (GitHub private vulnerability reporting if enabled); avoid publishing exploit details before remediation. No contact address is asserted here. A fixed user interface or passing Pytest test suite does not constitute a penetration test or a security certification.
