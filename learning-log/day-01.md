# Day 01 — First AI workload

## Environment
- Python: 3.12.10
- Tests: 3 passed

## Results
- Model artifact: artifacts/model.joblib
- MAE: 3.517 minutes
- RMSE: 4.512 minutes
- Inference result: 30.14 minutes

## DevOps / SRE learning
- ML inference needs a model artifact in addition to application code.
- A missing or invalid model should prevent readiness.
- Model versions and artifact availability need operational controls.

## Next session
Build a FastAPI inference service with health and readiness endpoints.
