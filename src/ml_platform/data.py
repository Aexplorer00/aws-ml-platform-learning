"""Deterministic synthetic taxi-like regression data for local learning.

This is NOT real NYC taxi data. Replace it later to study real-world drift/leakage.
"""
import numpy as np

FEATURES = ["trip_distance_km", "pickup_hour", "vehicle_age_years"]


def make_dataset(n_samples: int = 500, seed: int = 42):
    if n_samples < 10:
        raise ValueError("n_samples must be at least 10")
    rng = np.random.default_rng(seed)
    distance = rng.uniform(0.5, 25.0, n_samples)
    hour = rng.integers(0, 24, n_samples)
    age = rng.integers(0, 14, n_samples)
    rush_hour = ((hour >= 7) & (hour <= 9)) | ((hour >= 16) & (hour <= 19))
    duration_minutes = 4.0 + 2.8 * distance + 5.5 * rush_hour + 0.09 * age
    duration_minutes += rng.normal(0, 3, n_samples)
    X = np.column_stack([distance, hour, age]).astype(float)
    y = np.maximum(duration_minutes, 1.0)
    return X, y
