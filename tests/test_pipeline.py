import pytest
import pandas as pd
from src.day4_pipeline import load_config, load_data, compute_mean


# -----------------------------
# Core Function Tests
# -----------------------------

def test_load_config():
    """Ensure config.yaml loads correctly and contains required keys."""
    config = load_config("config.yaml")
    assert "data_path" in config
    assert "column" in config


def test_load_data():
    """Ensure sample CSV loads into a non-empty DataFrame."""
    df = load_data("data/sample_data.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_compute_mean():
    """Ensure compute_mean returns the correct average."""
    df = pd.DataFrame({"value": [10, 20, 30]})
    result = compute_mean(df, "value")
    assert result == 20.0


# -----------------------------
# Error Handling Tests
# -----------------------------

def test_missing_file():
    """Ensure load_data raises FileNotFoundError for missing files."""
    with pytest.raises(FileNotFoundError):
        load_data("data/does_not_exist.csv")
