import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def compute_mean(df: pd.DataFrame, column: str) -> float:
    return df[column].mean()


def run_pipeline():
    df = load_data("data/day3_data.csv")
    mean_value = compute_mean(df, "value")
    print(f"MEAN VALUE IS: {mean_value}")


if __name__ == "__main__":
    run_pipeline()
