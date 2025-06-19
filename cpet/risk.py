from typing import Dict


def assess_risk(biomarkers: Dict[str, float]) -> str:
    """Assess risk category based on biomarker thresholds."""
    vo2_max = biomarkers.get('VO2_max', 0)
    ve_vco2 = biomarkers.get('VE_VCO2_slope', 0)

    high_risk = vo2_max < 15 or ve_vco2 > 34
    if high_risk:
        return 'High'

    moderate_risk = vo2_max < 20 or ve_vco2 > 30
    if moderate_risk:
        return 'Moderate'

    return 'Low'
