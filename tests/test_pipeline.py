import math
import pytest
from ml_platform.data import FEATURES, make_dataset
from ml_platform.train import train
from ml_platform.predict import predict


def test_dataset_reproducible():
    x1, y1 = make_dataset(seed=42)
    x2, y2 = make_dataset(seed=42)
    assert x1.shape == (500, len(FEATURES))
    assert (x1 == x2).all()
    assert (y1 == y2).all()


def test_training_and_prediction(tmp_path):
    path = str(tmp_path / "baseline.joblib")
    metrics = train(output=path)
    assert metrics["mae"] >= 0
    assert metrics["rmse"] >= metrics["mae"]
    result = predict(path, distance=8, hour=9, age=4)
    assert math.isfinite(result) and result > 0


def test_bad_input(tmp_path):
    with pytest.raises(ValueError):
        predict(str(tmp_path / "x.joblib"), distance=-1, hour=9, age=4)
