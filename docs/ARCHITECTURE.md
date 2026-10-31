# Architecture evolution

**Now:** synthetic data → scikit-learn training → serialized artifact → local prediction CLI → pytest/GitHub Actions.

**Next:** MLflow experiment tracking and model registry; DVC lineage; orchestrated training; quality gates.

**Later:** AWS S3 + SageMaker Training/Pipelines/Registry; Terraform + GitHub OIDC; Kubernetes inference; monitoring and incident drills.

## Design decisions

1. Local-first to avoid cloud cost and reduce infrastructure distraction.
2. Training and inference are separate modules to mirror actual ML lifecycle boundaries.
3. Synthetic data is explicitly labeled; real dataset and leakage checks come next.
4. Model files are not committed to Git. Only load artifacts from trusted sources.
