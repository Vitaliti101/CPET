import pandas as pd
from pathlib import Path


def load_csv(path: str) -> pd.DataFrame:
    """Load CPET raw data from a CSV file."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")
    df = pd.read_csv(file_path)
    return df
