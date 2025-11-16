# SafeSpeed — Vitesse Recommandée Dynamique et Personnalisée par l’IA
**Optimisez votre vitesse, améliorez votre sécurité.**

Projet développé dans le cadre du **Hack For Good 4.0 – INSAT x Lloyd Assurance**  
Équipe : *Code4Impact*  
Repository : **SafeSpeed_JEForum**

---

# 1. Problématique

Les limitations de vitesse actuelles sont **statiques**, uniformes et déconnectées :
- du **conducteur** (fatigue, vigilance, habitudes),
- de la **route** (météo, luminosité, état du revêtement),
- du **véhicule** (freinage, réponse moteur, dynamique).

Elles ne reflètent pas la réalité dynamique du trafic et ne permettent pas une adaptation intelligente.

=> SafeSpeed répond à ce besoin en fournissant une vitesse optimale, personnalisée et évolutive.

---

# 2. Notre Solution : SafeSpeed

SafeSpeed est une application intelligente qui recommande en temps réel une **vitesse optimale personnalisée**, basée sur trois sources de données :

### 🔹 Données du Conducteur
- Détection de fatigue
- Détection de distraction
- Score de vigilance

### 🔹 Données de la Route
- Météo
- Visibilité
- Luminosité
- Conditions routières

### 🔹 Données du Véhicule
- Vitesse
- Accélération
- Freinage
- Consommation

Ces données sont fusionnées grâce à l’IA pour ajuster continuellement une **vitesse recommandée dynamique**.
---

# 3. Rôle de l’IA

### 🔸 Computer Vision (Fatigue & Distraction)
Analyse du visage pour détecter :
- clignements anormaux  
- yeux fermés  
- signes de somnolence  
- distraction

### 🔸 Fusion de Données & Machine Learning
Combinaison des informations :
- conducteur  
- environnement  
- véhicule  

### 🔸 Recommandation de Vitesse
Un modèle analyse en continu le contexte pour proposer une **vitesse optimale**, plus sécurisée et plus écologique.

---

# 4. Architecture Technique

```
SafeSpeed System
│
├── Streamlit Frontend (Prototype UI)
│   ├── Dashboard temps réel
│   ├── Vitesse recommandée
│   └── Alertes fatigue
│
├── Flask Backend
│   ├── /predict_speed
│   ├── /driver_state
│   └── Fusion & logique métier
│
└── IA Module (Python)
    ├── fatigue_model.py
    ├── risk_fusion.py
    └── speed_recommender.py
```

✔ Architecture simple, adaptée à un prototype de hackathon  
✔ Pas de base de données en Phase 1 (dataset local)  
✔ Communication Streamlit ↔ Flask  

---

# 5. Structure du Repository

```
SafeSpeed_JEForum/
│
├── README.md
│
├── frontend/
│   └── streamlit_app.py
│
├── backend/
│   └── app.py
│
├── ai/
│   ├── fatigue_model/
│   ├── fusion/
│   └── speed_recommender/
│
├── data/
│   └── simulated_dataset.csv
│
└── docs/
    ├── phase1_slides.pdf
    └── architecture_diagram.png
```

---

# 6. Dimension RSE

### 🌱 Environnemental
- Réduction de consommation carburant  
- Diminution des émissions CO₂ grâce à une vitesse optimisée  

### 👥 Social
- Réduction des accidents  
- Aide aux conducteurs vulnérables  
- Conseils proactive en temps réel  

### 🤝 Éthique
- Encouragement d’une conduite responsable  
- Technologie au service du bien commun  
- Transparence et explicabilité des recommandations IA

---
# 7. Roadmap — Alignée Hack For Good 4.0

### Phase 1 — Idéation & Développement (EN COURS)
- Définition du concept SafeSpeed  
- Architecture préliminaire  
- Interface prototype (Streamlit)  
- Détection fatigue (prototype simple)  
- Recommandation vitesse v0.1  
- Mise en place du repo GitHub  
- Vidéo de présentation 1–2 minutes  

### Phase 2 — Accompagnement & Perfectionnement
- Prototype IA plus stable  
- Intégration complète Flask ↔ Streamlit  
- Démo fonctionnelle  
- Stratégie RSE avancée  
- Présentation PPTX + pitch  

### Phase 3 — Finalisation & Pitch Final
- Prototype final complet  
- Vidéo démo intégrée au PPTX  
- BMC + stratégie marketing  
- Pitch final devant jury et public  
- Version stable du repo  

---

# 8. Contact
Équipe Code4Impact — SafeSpeed :
Dorra Ben El Amri Bettaieb: dorra.benelamribettaieb@esprit.tn
Anas Nguira: anas.nguira@esprit.tn
Louay Ben Amar: benamarlouay6@gmail.com
Eya Fetni: eyafetni60@gmail.com


