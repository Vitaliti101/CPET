import pandas as pd
import numpy as np
from typing import Dict


def compute_biomarkers(df: pd.DataFrame) -> Dict[str, float]:
    """Compute basic CPET biomarkers from raw data."""
    biomarkers: Dict[str, float] = {}

    if 'VO2' in df.columns:
        biomarkers['VO2_max'] = df['VO2'].max()

    if {'VE', 'VCO2'}.issubset(df.columns):
        # Simple linear regression VE vs VCO2
        slope = np.polyfit(df['VCO2'], df['VE'], 1)[0]
        biomarkers['VE_VCO2_slope'] = slope

    if {'VO2', 'HeartRate'}.issubset(df.columns):
        df['O2Pulse'] = df['VO2'] / df['HeartRate'].replace(0, np.nan)
        biomarkers['O2_pulse_max'] = df['O2Pulse'].max()

    return biomarkers
