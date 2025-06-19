# CPET Analysis

This project provides a small tool to analyze Cardiopulmonary Exercise Test (CPET) data.

## Features

- Generate a Wasserman 9-panel plot from CPET raw data.
- Calculate simple biomarkers (VO2 max, VE/VCO2 slope, O2 pulse).
- Assess risk based on biomarkers.
- Provide recommendations for doctors and a training plan for coaches.

## Usage

```bash
python main.py sample_cpet.csv --tid polarized --volume 6 --plot output.png
```

The command prints the biomarker values, risk category, doctor recommendations, and a three-week training plan. If `--plot` is provided, the Wasserman plot is saved to the specified file.

## Sample Data

A small example dataset is included in `sample_cpet.csv`.
