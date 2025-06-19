import matplotlib.pyplot as plt
import pandas as pd


def plot_wasserman(df: pd.DataFrame, output: str = None) -> None:
    """Create a simple Wasserman 9-panel plot from CPET data."""
    fig, axes = plt.subplots(3, 3, figsize=(12, 10))
    axes = axes.flatten()

    df = df.copy()
    df['RER'] = df['VCO2'] / df['VO2']
    df['O2Pulse'] = df['VO2'] / df['HeartRate']
    df['VE_VO2'] = df['VE'] / df['VO2']
    df['VE_VCO2'] = df['VE'] / df['VCO2']

    axes[0].plot(df['Time'], df['WorkRate'])
    axes[0].set_ylabel('Work Rate (W)')

    axes[1].plot(df['Time'], df['VO2'])
    axes[1].set_ylabel('VO2 (ml/min)')

    axes[2].plot(df['Time'], df['VCO2'])
    axes[2].set_ylabel('VCO2 (ml/min)')

    axes[3].plot(df['Time'], df['VE'])
    axes[3].set_ylabel('VE (L/min)')

    axes[4].plot(df['VCO2'], df['VE'])
    axes[4].set_xlabel('VCO2 (ml/min)')
    axes[4].set_ylabel('VE (L/min)')

    axes[5].plot(df['Time'], df['RER'])
    axes[5].set_ylabel('RER')

    axes[6].plot(df['Time'], df['HeartRate'])
    axes[6].set_ylabel('Heart Rate (bpm)')

    axes[7].plot(df['Time'], df['O2Pulse'])
    axes[7].set_ylabel('O2 Pulse (ml/beat)')

    axes[8].plot(df['Time'], df['VE_VO2'], label='VE/VO2')
    axes[8].plot(df['Time'], df['VE_VCO2'], label='VE/VCO2')
    axes[8].set_ylabel('Ventilatory Equivalents')
    axes[8].legend()

    for ax in axes:
        ax.set_xlabel('Time (s)')

    fig.tight_layout()
    if output:
        plt.savefig(output)
    else:
        plt.show()

    plt.close(fig)
