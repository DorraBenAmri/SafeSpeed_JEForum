def compute_risk_context(vigilance_score: float, weather_risk: float, road_risk: float) -> float:
    """
    Calcule un score de risque global entre 0 et 1.

    - vigilance_score : 0 (aucune vigilance) à 1 (vigilance parfaite)
    - weather_risk : 0 (conditions idéales) à 10 (conditions très dangereuses)
    - road_risk : 0 (route parfaite) à 10 (route très dégradée)
    """

    # On inverse la vigilance pour la transformer en "risque lié au conducteur"
    driver_risk = 1.0 - max(0.0, min(1.0, vigilance_score))

    # Normalisation des risques météo/route
    weather_risk_norm = max(0.0, min(1.0, weather_risk / 10.0))
    road_risk_norm = max(0.0, min(1.0, road_risk / 10.0))

    # Poids simples pour un prototype
    driver_weight = 0.5
    weather_weight = 0.3
    road_weight = 0.2

    risk_score = (
        driver_weight * driver_risk
        + weather_weight * weather_risk_norm
        + road_weight * road_risk_norm
    )

    return round(max(0.0, min(1.0, risk_score)), 3)
