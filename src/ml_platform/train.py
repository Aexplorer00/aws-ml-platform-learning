"""Train and save baseline model with reproducible evaluation."""
import argparse
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from ml_platform.data import FEATURES, make_dataset


def train(output: str = "artifacts/model.joblib", seed: int = 42):
    X, y = make_dataset(seed=seed)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    model = RandomForestRegressor(n_estimators=60, max_depth=8, random_state=seed, n_jobs=1)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    metrics = {"mae": float(mean_absolute_error(y_test, predictions)),
               "rmse": float(mean_squared_error(y_test, predictions) ** 0.5)}
    target = Path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"model": model, "features": FEATURES, "seed": seed, "metrics": metrics}, target)
    print(f"Model saved: {target}")
    print(f"MAE: {metrics['mae']:.3f} min | RMSE: {metrics['rmse']:.3f} min")
    return metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/model.joblib")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    train(output=args.output, seed=args.seed)


if __name__ == "__main__":
    main()
