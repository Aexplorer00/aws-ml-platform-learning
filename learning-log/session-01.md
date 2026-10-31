# Session 01 — First training baseline

## Goal
Run the included reproducible toy regression baseline; understand features, labels, and train/test split.

## Commands
```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m ml_platform.train
python -m ml_platform.predict --distance 8 --hour 9 --age 4
```

## Record after running
- MAE:
- RMSE:
- Prediction for 8 km, 9 AM, vehicle age 4:
- One change I tried:
- One question for next time:
