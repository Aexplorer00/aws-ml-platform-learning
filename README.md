# AWS ML Platform Learning — DevOps/SRE first, AI-ready

**Primary goal:** strengthen DevOps / SRE / Cloud Platform Engineering while learning how to deploy, secure, observe, and operate AI/ML workloads. A full MLOps transition is optional.

**Start here:** [DevOps + AI Infrastructure track](docs/DEVOPS_AI_PLATFORM_TRACK.md) — 12 modules, each with three flexible 2-hour sessions (72 hours of hands-on study). Learn when available; no fixed deadlines.

**Preserved material:** the existing runnable ML baseline, CI, tests, infrastructure skeleton, learning-log template, and [original 52-week deep MLOps roadmap](docs/ROADMAP.md) are unchanged. The original roadmap is now an optional specialization, not the default plan.

## Original MLOps starter and reference

One evolving, portfolio-ready project. **52 weeks · 6 hours/week · flexible 2-hour sessions**. Start locally, add AWS services only after the ML lifecycle is understood.

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m ml_platform.train
python -m ml_platform.predict --age 4 --distance 8 --hour 9
```

Training uses **synthetic taxi-like data** generated locally (no external dataset, cloud charges, or credentials). It writes a model to `artifacts/` (gitignored). This is an engineering starter, not a realistic production ML benchmark. Replace it with a real dataset in subsequent sessions.

## The next 2-hour session (Session 01)

1. **0–20 min:** clone/unzip, create virtual environment, install deps, run tests.
2. **20–55 min:** inspect `src/ml_platform/data.py` and `train.py` — identify features, label, train/test split, leakage risk.
3. **55–95 min:** run training, record MAE and RMSE, change a feature or model parameter and compare.
4. **95–120 min:** run prediction, record observations in `learning-log/session-01.md`, commit your changes.

**Done when:** tests pass, training produces a model, predict returns a numeric result, and your learning log has at least one observation and one question.

## Roadmap

- Weeks 1–8: ML foundations, preprocessing, API and model quality tests
- Weeks 9–16: MLflow, versioning, lineage and model registry
- Weeks 17–24: orchestration, ML-specific CI, evaluation gates and CT
- Weeks 25–32: AWS S3, IAM, SageMaker pipelines and Terraform
- Weeks 33–40: Kubernetes/KServe serving and reusable model-onboarding contract
- Weeks 41–46: reliability, drift, monitoring, security, cost
- Weeks 47–52: integration, incident drills, documentation and interviews

See [the weekly checklist](docs/ROADMAP.md), [platform architecture](docs/ARCHITECTURE.md), and [session template](learning-log/TEMPLATE.md).

## Repo layout

```
.github/workflows/     - CI
src/ml_platform/       - reproducible ML baseline and inference CLI
tests/                 - training and prediction tests
training/              - future orchestration / MLflow integrations
serving/               - future FastAPI and KServe services
infrastructure/        - Terraform, Kubernetes, AWS examples (added progressively)
monitoring/            - drift, metrics and dashboards (added progressively)
learning-log/          - progress and learning notes
runbooks/              - failure and rollback documentation
```

## Learning references

- [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp)
- [Made With ML](https://github.com/GokuMohandas/Made-With-ML)
- [MLflow](https://github.com/mlflow/mlflow)
- [DVC](https://github.com/iterative/dvc)
- [AWS: SageMaker from Idea to Production](https://github.com/aws-samples/amazon-sagemaker-from-idea-to-production)
- [KServe](https://github.com/kserve/kserve)
- [Evidently](https://github.com/evidentlyai/evidently)

## Safety and cost

Never commit AWS keys or sensitive data. Later AWS labs should use scoped IAM roles / GitHub OIDC, budgets, resource tags, and explicit teardown. Do not create EKS or always-on SageMaker endpoints as part of this initial starter.
