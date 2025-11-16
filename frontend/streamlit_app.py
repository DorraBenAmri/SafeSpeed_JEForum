import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:5000"

st.set_page_config(
    page_title="SafeSpeed",
    page_icon="🚘",
    layout="centered"
)

st.title("🚘 SafeSpeed – Vitesse Recommandée Dynamique")
st.markdown(
    "SafeSpeed recommande une **vitesse optimale personnalisée** "
    "en fonction de votre état, des conditions routières et du véhicule."
)

st.sidebar.header("⚙️ Paramètres d'entrée")

# Inputs côté conducteur
st.sidebar.subheader("Conducteur")
fatigue_level = st.sidebar.slider(
    "Niveau de fatigue (0 = reposé, 10 = épuisé)",
    min_value=0.0,
    max_value=10.0,
    value=3.0,
    step=0.5,
)

# Inputs côté route
st.sidebar.subheader("Route & météo")
weather_risk = st.sidebar.slider(
    "Risque météo (0 = idéal, 10 = dangereux)",
    min_value=0.0,
    max_value=10.0,
    value=2.0,
    step=0.5,
)

road_risk = st.sidebar.slider(
    "Qualité de la route (0 = parfaite, 10 = très dégradée)",
    min_value=0.0,
    max_value=10.0,
    value=3.0,
    step=0.5,
)

# Inputs côté véhicule
st.sidebar.subheader("Véhicule")
current_speed = st.sidebar.slider(
    "Vitesse actuelle (km/h)",
    min_value=0,
    max_value=140,
    value=80,
    step=5,
)

base_speed_limit = st.sidebar.slider(
    "Limitation de vitesse officielle (km/h)",
    min_value=30,
    max_value=130,
    value=90,
    step=10,
)

st.markdown("### 🎯 Simulation SafeSpeed")

if st.button("Calculer la vitesse recommandée"):
    try:
        payload = {
            "fatigue_level": fatigue_level,
            "weather_risk": weather_risk,
            "road_risk": road_risk,
            "current_speed": current_speed,
            "base_speed_limit": base_speed_limit,
        }
        response = requests.post(f"{BACKEND_URL}/api/recommend_speed", json=payload, timeout=5)
        response.raise_for_status()
        data = response.json()

        st.success("Recommandation calculée avec succès ✅")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Vitesse actuelle", f"{current_speed} km/h")
            st.metric("Limite officielle", f"{base_speed_limit} km/h")
        with col2:
            st.metric("Vitesse recommandée SafeSpeed", f"{data['recommended_speed']} km/h")
            st.metric("Score de vigilance", f"{data['vigilance_score']:.2f} / 1.00")

        st.markdown("### 🧠 Détails de l'analyse")
        st.write(f"**Score de risque global :** {data['risk_score']:.2f} / 1.00")
        st.write(f"**Commentaire IA :** {data['explanation']}")

    except requests.exceptions.RequestException as e:
        st.error("❌ Impossible de contacter le backend Flask. Vérifie qu'il est lancé sur http://127.0.0.1:5000")
        st.error(str(e))

st.markdown("---")
st.caption("Prototype SafeSpeed – Hack For Good 4.0 (INSAT x Lloyd Assurance)")
