import argparse
import logging
from logging import config
import yaml
import pandas as pd


def load_config(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def compute_mean(df: pd.DataFrame, column: str) -> float:
    return df[column].mean()


def run_pipeline(config_path: str):
    # Load config
    config = load_config(config_path)

    # Configure logging
    logging.basicConfig(level=config.get("log_level", "INFO"))
    logging.info("Pipeline started")

    # Load data
    df = load_data(config["data_path"])
    logging.info(f"Loaded data from {config['data_path']}")

    # Compute mean
    mean_value = compute_mean(df, config["column"])
    logging.info(f"Mean value for column '{config['column']}': {mean_value}")

    # Save output to file (if configured)
    if "output_path" in config:
        with open(config["output_path"], "w") as f:
            f.write(str(mean_value))
        logging.info(f"Saved mean value to {config['output_path']}")

    logging.info("Pipeline finished successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 4 MLOps pipeline")
    parser.add_argument("--config", type=str, required=True,
                        help="Path to config file")
    args = parser.parse_args()

    run_pipeline(args.config)
