# Daily DevOps / SRE + AI Infrastructure Schedule

**Start any day you are available.** Each numbered day is a **2-hour session**, not a fixed calendar date. Target **3 study days/week** if you have 6 hours weekly: approximately **12 weeks / 36 sessions / 72 hours**. If you miss a day, resume the next unchecked day—no catch-up required.

**Primary goal:** DevOps, SRE and cloud/platform career development with practical AI workload operations. The [original 52-week MLOps path](ROADMAP.md) stays optional.

## Daily rhythm (every 2-hour study day)

- **00–15 min:** recap last commit, set today's acceptance test.
- **15–35 min:** targeted reading / concept.
- **35–105 min:** implement, run and troubleshoot.
- **105–120 min:** tests, evidence, learning-log note and git commit.

**Rule:** a day is complete only with verified output or documented blocker. Use `learning-log/TEMPLATE.md` and name notes `day-01.md`, `day-02.md`, etc. Where work exceeds two hours, keep the same day open. Do not commit keys, credentials, sensitive datasets, or generated model binaries.

## Day-by-day checklist

### Module 01 — ML workload baseline

- [ ] **Day 01 (2h):** Run tests and record existing repo structure. **Evidence:** `learning-log/day-01.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 02 (2h):** Run training and prediction; document artifact lifecycle. **Evidence:** `learning-log/day-02.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 03 (2h):** Failure review: missing model, bad inputs, version mismatch. **Evidence:** `learning-log/day-03.md` + tests/output/ADR as applicable + Git commit.

### Module 02 — Inference service

- [ ] **Day 04 (2h):** Implement FastAPI /health and /predict. **Evidence:** `learning-log/day-04.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 05 (2h):** Add schema validation and API tests. **Evidence:** `learning-log/day-05.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 06 (2h):** Add startup failure tests, API docs and demo requests. **Evidence:** `learning-log/day-06.md` + tests/output/ADR as applicable + Git commit.

### Module 03 — Container security

- [ ] **Day 07 (2h):** Dockerize prediction service with pinned dependencies. **Evidence:** `learning-log/day-07.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 08 (2h):** Run non-root and add Docker smoke tests. **Evidence:** `learning-log/day-08.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 09 (2h):** Add GitHub Actions build, basic scan and image notes. **Evidence:** `learning-log/day-09.md` + tests/output/ADR as applicable + Git commit.

### Module 04 — Kubernetes serving

- [ ] **Day 10 (2h):** Write deployment/service/probe manifests for local kind. **Evidence:** `learning-log/day-10.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 11 (2h):** Load test, resource requests/limits, graceful shutdown. **Evidence:** `learning-log/day-11.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 12 (2h):** Test rollout and pod-failure recovery; document findings. **Evidence:** `learning-log/day-12.md` + tests/output/ADR as applicable + Git commit.

### Module 05 — AWS architecture

- [ ] **Day 13 (2h):** Compare ECS/Fargate, EKS, SageMaker inference. **Evidence:** `learning-log/day-13.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 14 (2h):** Draft AWS deployment diagram, IAM/S3/data paths. **Evidence:** `learning-log/day-14.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 15 (2h):** Write architecture decision record and cost estimate. **Evidence:** `learning-log/day-15.md` + tests/output/ADR as applicable + Git commit.

### Module 06 — Secure delivery

- [ ] **Day 16 (2h):** Create Terraform example: S3/IAM, avoid deploying yet. **Evidence:** `learning-log/day-16.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 17 (2h):** Design GitHub OIDC least-privilege roles and threat review. **Evidence:** `learning-log/day-17.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 18 (2h):** Implement safe plan/validation CI; document manual deployment. **Evidence:** `learning-log/day-18.md` + tests/output/ADR as applicable + Git commit.

### Module 07 — Inference observability

- [ ] **Day 19 (2h):** Instrument request count, errors, duration and model version. **Evidence:** `learning-log/day-19.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 20 (2h):** Add Prometheus/Grafana config for local run. **Evidence:** `learning-log/day-20.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 21 (2h):** Draft SLO, alert rules and dashboard evidence. **Evidence:** `learning-log/day-21.md` + tests/output/ADR as applicable + Git commit.

### Module 08 — Release reliability

- [ ] **Day 22 (2h):** Define immutable model/artifact IDs and deployment contract. **Evidence:** `learning-log/day-22.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 23 (2h):** Implement model rollback or canary in local environment. **Evidence:** `learning-log/day-23.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 24 (2h):** Run failure injection; write incident runbook. **Evidence:** `learning-log/day-24.md` + tests/output/ADR as applicable + Git commit.

### Module 09 — MLOps literacy

- [ ] **Day 25 (2h):** Add MLflow local tracking of training runs. **Evidence:** `learning-log/day-25.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 26 (2h):** Log dataset/code/model versions and compare two runs. **Evidence:** `learning-log/day-26.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 27 (2h):** Write model promotion policy and reproducibility note. **Evidence:** `learning-log/day-27.md` + tests/output/ADR as applicable + Git commit.

### Module 10 — LLM API operations

- [ ] **Day 28 (2h):** Create optional mocked LLM provider adapter (no secret needed). **Evidence:** `learning-log/day-28.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 29 (2h):** Implement timeouts, retries, rate limits and error mapping. **Evidence:** `learning-log/day-29.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 30 (2h):** Test mock outages and add token/cost telemetry design. **Evidence:** `learning-log/day-30.md` + tests/output/ADR as applicable + Git commit.

### Module 11 — Security + cost

- [ ] **Day 31 (2h):** Review artifact provenance, IAM and sensitive logging. **Evidence:** `learning-log/day-31.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 32 (2h):** Add AWS budget/teardown checklist and resource tags plan. **Evidence:** `learning-log/day-32.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 33 (2h):** Write security + cost runbook; run tabletop incident. **Evidence:** `learning-log/day-33.md` + tests/output/ADR as applicable + Git commit.

### Module 12 — Platform golden path

- [ ] **Day 34 (2h):** Define onboarding YAML contract for second inference model. **Evidence:** `learning-log/day-34.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 35 (2h):** Add template/CLI or script for second model. **Evidence:** `learning-log/day-35.md` + tests/output/ADR as applicable + Git commit.
- [ ] **Day 36 (2h):** End-to-end test, README polish and portfolio demo. **Evidence:** `learning-log/day-36.md` + tests/output/ADR as applicable + Git commit.

## Checkpoints

- **Day 03:** baseline training + prediction verified; 3 failure scenarios documented.
- **Day 09:** usable inference API, tested container and secure image pipeline.
- **Day 18:** locally operated inference deployment plus an AWS architecture and secure delivery plan.
- **Day 24:** dashboards, SLOs, failure drill and rollback demonstration.
- **Day 30:** understand model tracking and operational LLM API patterns.
- **Day 36:** self-service second-model onboarding and interview-ready demonstration.

## Commands to start Day 01

```bash
git pull origin main
python -m venv .venv
source .venv/bin/activate  # PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m ml_platform.train
python -m ml_platform.predict --age 4 --distance 8 --hour 9
```

**Day 01 definition of done:** record test results, training metrics, prediction output, and an architecture observation in `learning-log/day-01.md`. Then commit only your learning notes and source changes (not generated artifacts).

## Daily git workflow

```bash
git checkout main
git pull origin main
# work on today's task
python -m pytest -q
git add <specific-files>
git commit -m "day-01: verify baseline ml workload"
git push origin main
```

Replace the commit day and summary per session. Prefer a feature branch and PR if a task involves risky infrastructure modifications. AWS labs must include explicit cost guardrails and teardown; avoid leaving billable resources running.
