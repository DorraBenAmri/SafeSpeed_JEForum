from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Permet les imports depuis le dossier parent (ai/)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)

from ai.fatigue_model.model import estimate_vigilance
from ai.fusion.fusion_logic import compute_risk_context
from ai.speed_recommender.recommender import recommend_speed

app = Flask(__name__)
CORS(app)  # autorise les requêtes depuis Streamlit

@app.route("/api/recommend_speed", methods=["POST"])
def api_recommend_speed():
    data = request.get_json(force=True)

    fatigue_level = float(data.get("fatigue_level", 0))
    weather_risk = float(data.get("weather_risk", 0))
    road_risk = float(data.get("road_risk", 0))
    current_speed = float(data.get("current_speed", 0))
    base_speed_limit = float(data.get("base_speed_limit", 90))

    vigilance_score = estimate_vigilance(fatigue_level)
    risk_score = compute_risk_context(vigilance_score, weather_risk, road_risk)
    recommended_speed = recommend_speed(
        base_speed_limit=base_speed_limit,
        risk_score=risk_score,
        current_speed=current_speed,
    )

    explanation = (
        f"Vitesse adaptée en fonction d'une vigilance de {vigilance_score:.2f}, "
        f"d'un risque météo/route de {risk_score:.2f} et d'une limite officielle de {base_speed_limit:.0f} km/h."
    )

    return jsonify(
        {
            "recommended_speed": int(recommended_speed),
            "vigilance_score": vigilance_score,
            "risk_score": risk_score,
            "explanation": explanation,
        }
    )


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "SafeSpeed backend is running"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
