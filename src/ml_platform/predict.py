"""Load an artifact and run single-row inference."""
import argparse
from pathlib import Path
import joblib
import numpy as np


def predict(model_path: str, distance: float, hour: int, age: int) -> float:
    if distance <= 0 or not 0 <= hour <= 23 or age < 0:
        raise ValueError("distance must be positive; hour 0–23; age nonnegative")
    path = Path(model_path)
    if not path.is_file():
        raise FileNotFoundError(f"No trained model found at {path}. Run python -m ml_platform.train first")
    # Only load trusted local model artifacts; joblib uses pickle underneath.
    artifact = joblib.load(path)
    sample = np.array([[distance, hour, age]], dtype=float)
    return float(artifact["model"].predict(sample)[0])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="artifacts/model.joblib")
    parser.add_argument("--distance", type=float, required=True, help="trip distance in km")
    parser.add_argument("--hour", type=int, required=True, help="pickup hour 0–23")
    parser.add_argument("--age", type=int, required=True, help="vehicle age in years")
    args = parser.parse_args()
    result = predict(args.model, args.distance, args.hour, args.age)
    print(f"Predicted duration: {result:.2f} minutes")


if __name__ == "__main__":
    main()
