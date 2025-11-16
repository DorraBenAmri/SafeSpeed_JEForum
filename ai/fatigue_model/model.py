def estimate_vigilance(fatigue_level: float) -> float:
    """
    Estime un score de vigilance entre 0 et 1 à partir d'un niveau de fatigue 0–10.

    0  = aucun fatigue -> vigilance ≈ 1.0
    10 = fatigue extrême -> vigilance ≈ 0.0
    """
    fatigue_level = max(0.0, min(10.0, fatigue_level))
    vigilance = 1.0 - (fatigue_level / 10.0)
    return round(vigilance, 3)
