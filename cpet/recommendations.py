from typing import Dict, List


def doctor_recommendations(risk: str) -> List[str]:
    """Generate doctor recommendations based on risk."""
    recs = []
    if risk == 'High':
        recs.append('Patient exhibits high risk markers. Consider full cardiological evaluation.')
    elif risk == 'Moderate':
        recs.append('Patient shows moderate risk. Follow up testing recommended.')
    else:
        recs.append('Patient is low risk. Routine monitoring.')
    return recs


def coach_plan(volume_hours: float, tid: str = 'polarized') -> Dict[str, List[float]]:
    """Generate a simple 3-week training plan with 2 loading and 1 deloading cycle."""
    volume_hours = max(0.0, min(volume_hours, 10.0))

    # volumes for three weeks (two loading then deload)
    weeks = [volume_hours * 0.9, volume_hours, volume_hours * 0.6]

    if tid == 'polarized':
        dist = {'low': 0.8, 'moderate': 0.0, 'high': 0.2}
    else:  # pyramidal
        dist = {'low': 0.7, 'moderate': 0.2, 'high': 0.1}

    plan = {
        'weeks': weeks,
        'distribution': dist,
    }
    return plan
