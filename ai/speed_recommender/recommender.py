def recommend_speed(base_speed_limit: float, risk_score: float, current_speed: float) -> float:
    """
    Recommande une vitesse en fonction :
    - de la limitation officielle (base_speed_limit)
    - du score de risque (0 = aucun risque, 1 = risque max)
    - de la vitesse actuelle (current_speed)

    Logique simple pour le prototype :
    - plus le risque est grand, plus on réduit la vitesse
    - réduction max de 40% de la vitesse limite
    """

    base_speed_limit = max(20.0, min(130.0, base_speed_limit))
    risk_score = max(0.0, min(1.0, risk_score))

    # Réduction max de 40% de la limite en cas de risque = 1
    max_reduction_ratio = 0.4
    reduction = max_reduction_ratio * risk_score

    recommended_speed = base_speed_limit * (1.0 - reduction)

    # Option : éviter les changements trop extrêmes par rapport à la vitesse actuelle
    # ici on autorise un écart max de ±30 km/h
    max_delta = 30.0
    if current_speed > 0:
        lower_bound = max(20.0, current_speed - max_delta)
        upper_bound = min(base_speed_limit, current_speed + max_delta)
        recommended_speed = max(lower_bound, min(upper_bound, recommended_speed))

    return round(recommended_speed)
