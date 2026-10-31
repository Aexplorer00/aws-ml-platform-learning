# DevOps / SRE + AI Infrastructure Track

**Career priority:** DevOps, SRE, Cloud / Platform Engineering. **AI/ML is an applied specialization, not a mandatory role switch.**

**Pace:** 2-hour sessions whenever available. A six-hour week can fit three sessions, but there are no calendar deadlines. Advance only after acceptance criteria pass.

## What we keep

- Existing `src/ml_platform` synthetic ML baseline, inference CLI, and tests.
- GitHub Actions CI, infrastructure, monitoring, runbooks, learning logs, and architecture docs.
- `docs/ROADMAP.md` remains an **optional deep MLOps specialization** for later.

## Skill allocation and guardrails

- **60%** production engineering for AI workloads: deployment, reliability, security, performance, IaC, AWS.
- **25%** applied AI/ML literacy: model artifacts, inference, evaluation, drift, LLM API behavior.
- **15%** portfolio / documentation / interview prep.
- Skip beginner Linux, Git, Docker, Terraform, and Kubernetes tutorials unless they cause a real blocker.
- Default to local workloads. Use AWS in short, cost-guarded labs; never leave an EKS cluster or inference endpoint running unattended.

## Milestones: 12 flexible modules, three 2-hour sessions each

Every module has three sessions: **A concept + design**, **B build + test**, **C operate + document**. The module is done only when its evidence is committed.

| Module | Theme | Build outcome | Evidence / gate |
| --- | --- | --- | --- |
| 01 | Baseline and model-serving boundaries | Run existing train/predict code; document lifecycle, artifact and deployment risks | Tests pass; baseline outputs + architecture note |
| 02 | Inference API | FastAPI wrapper with `/predict`, `/health`, structured errors | Contract tests; request examples |
| 03 | Container hardening | Minimal non-root Docker image, scans, reproducible build | CI image build + scan report |
| 04 | Kubernetes operations | Deployment, probes, resource limits, HPA load-test experiment | Load test + failure/rollout notes |
| 05 | AWS deployment choices | Compare ECS/Fargate, EKS, SageMaker inference for workload | ADR with cost, operations, lock-in tradeoffs |
| 06 | AWS IAM + CI release | OIDC trust model, least privilege, Terraform plan and workflow | IAM policy review; safe deployment checklist |
| 07 | Observability + SLOs | Request rate, errors, p95 latency, model version, logs and traces | Grafana panel screenshots + example alert |
| 08 | Reliability engineering | Canary rollout, backward-compatible schema, rollback and incident drill | Incident runbook + rollback demo |
| 09 | AI/ML literacy | MLflow experiments, model registry, data/model version distinction | 2 reproducible model versions |
| 10 | LLM-backed API operations | Optional external LLM API adapter with mocks; rate limits, retry budget, timeouts | Tests using mocks; no credentials in Git |
| 11 | Cost, security, governance | Model provenance, IAM, PII-safe logs, request budgets, cleanup | Threat model + cost checklist |
| 12 | Internal developer platform | Declarative onboarding of a second inference workload | Golden-path template + end-to-end demo |

**Estimate:** 36 sessions = 72 hands-on hours, or ~12 weeks at 6 hours/week. Extend or repeat modules as needed. This is a first specialization track, not a claim of full expertise.

## Each 2-hour session

1. **0–15 min:** recap; pick one verifiable outcome.
2. **15–35 min:** only the concepts that unblock it.
3. **35–105 min:** pair-program/build/debug.
4. **105–120 min:** test, write a learning log, commit and choose next session.

## Session 01 — Run and assess what already exists (2 hours)

- **0–15:** `git pull`; inspect README, current tests, dependencies.
- **15–35:** sketch boundary: data generation → training → artifact → inference; identify which parts DevOps owns.
- **35–65:** create a virtualenv, install requirements, run `python -m pytest -q`.
- **65–95:** run `python -m ml_platform.train` and `python -m ml_platform.predict --age 4 --distance 8 --hour 9`; record outputs.
- **95–110:** identify 3 operational failure modes (missing model, incompatible schema, insufficient capacity).
- **110–120:** copy `learning-log/TEMPLATE.md` to `learning-log/session-01.md`; add commands/results/issues; commit.

**Acceptance:** tests pass, training and prediction work, and the learning log names three operational risks.

## Future interview themes

- Operating an inference workload differs from a stateless web service in what ways?
- ECS/Fargate vs EKS vs SageMaker: when does each fit?
- What changes in latency/error SLOs when model loading is slow?
- How do you safely roll back a model and application version?
- What should be monitored beyond CPU, memory and HTTP status?
- How do you handle third-party model API throttling and cost spikes?
- What IAM boundaries protect inference and model artifacts?
- How would you build a self-service golden path for model teams?

## Curated references

- [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) — selected applied ML modules
- [MLflow](https://github.com/mlflow/mlflow) — model artifacts and tracking
- [KServe](https://github.com/kserve/kserve) — Kubernetes-native serving concepts
- [Evidently](https://github.com/evidentlyai/evidently) — data and model quality
- [AWS SageMaker samples](https://github.com/aws-samples/amazon-sagemaker-from-idea-to-production) — managed ML platform reference
- [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-demo) — reference instrumentation patterns
