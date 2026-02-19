import pandas as pd
from src.day4_pipeline import load_config, compute_mean


def test_load_config():
    config = load_config("config.yaml")
    assert "data_path" in config
    assert "column" in config


def test_compute_mean():
    df = pd.DataFrame({"value": [10, 20, 30]})
    result = compute_mean(df, "value")
    assert result == 20
