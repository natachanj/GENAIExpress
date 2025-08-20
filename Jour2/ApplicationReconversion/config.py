# Configuration de l'application
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_MAX_TOKENS = 1000

# Configuration de l'application
APP_TITLE = "🚀 Assistant de Reconversion Data"
APP_ICON = "📊"
APP_LAYOUT = "wide"

# Configuration des métiers data
METIERS_DATA = {
    "Data Analyst": {
        "description": "Analyse des données pour prendre des décisions business",
        "salaire_junior": "35k-45k€",
        "salaire_senior": "55k-75k€",
        "duree_formation": "3-6 mois",
        "niveau_difficulte": "Facile",
        "competences_requises": ["SQL", "Excel", "Python", "Tableau/PowerBI", "Statistiques"]
    },
    "Data Scientist": {
        "description": "Création de modèles prédictifs et d'algorithmes ML",
        "salaire_junior": "45k-60k€",
        "salaire_senior": "70k-100k€",
        "duree_formation": "6-12 mois",
        "niveau_difficulte": "Difficile",
        "competences_requises": ["Python", "Machine Learning", "Mathématiques", "SQL", "Deep Learning"]
    },
    "Data Engineer": {
        "description": "Construction et maintenance des infrastructures de données",
        "salaire_junior": "40k-55k€",
        "salaire_senior": "65k-90k€",
        "duree_formation": "6-9 mois",
        "niveau_difficulte": "Moyen",
        "competences_requises": ["Python", "SQL", "Cloud (AWS/Azure)", "Big Data", "DevOps"]
    },
    "Business Intelligence": {
        "description": "Création de tableaux de bord et rapports business",
        "salaire_junior": "35k-45k€",
        "salaire_senior": "55k-75k€",
        "duree_formation": "4-7 mois",
        "niveau_difficulte": "Facile",
        "competences_requises": ["SQL", "PowerBI/Tableau", "Excel", "Business", "SQL Server"]
    },
    "Machine Learning Engineer": {
        "description": "Déploiement et productionisation de modèles ML",
        "salaire_junior": "50k-65k€",
        "salaire_senior": "75k-110k€",
        "duree_formation": "8-12 mois",
        "niveau_difficulte": "Très difficile",
        "competences_requises": ["Python", "ML/DL", "DevOps", "Cloud", "Docker/Kubernetes"]
    }
}

# Options pour les formulaires
SECTEURS_ACTIVITE = [
    "Commerce/Retail", "Finance/Banque", "Santé", "Éducation", 
    "Industrie", "Services", "Autre"
]

NIVEAUX_ETUDES = [
    "Bac", "Bac+2", "Bac+3", "Bac+4", "Bac+5", "Doctorat"
]

COMPETENCES_TECH = [
    "Excel", "SQL", "Python", "R", "PowerBI", "Tableau", 
    "JavaScript", "HTML/CSS", "Git", "Aucune"
]

COMPETENCES_SOFT = [
    "Analyse", "Communication", "Gestion de projet", 
    "Résolution de problèmes", "Travail en équipe", "Autonomie"
]

MOTIVATIONS = [
    "Changement de carrière", "Évolution dans mon domaine", 
    "Intérêt pour la tech", "Salaire plus attractif", "Autre"
]

TEMPS_DISPONIBLE = [
    "2-5h/semaine", "5-10h/semaine", "10-15h/semaine", "15h+/semaine"
]

# Configuration des couleurs et thème
THEME_CONFIG = {
    "primaryColor": "#FF6B6B",
    "backgroundColor": "#FFFFFF",
    "secondaryBackgroundColor": "#F0F2F6",
    "textColor": "#262730",
    "font": "sans serif"
}

# Messages d'erreur et d'information
MESSAGES = {
    "no_api_key": "⚠️ Clé API OpenAI non trouvée. Veuillez créer un fichier .env avec votre clé API.",
    "api_key_help": "Copiez le contenu de env_example.txt vers un fichier .env et ajoutez votre vraie clé API.",
    "analysis_success": "✅ Analyse terminée !",
    "analysis_error": "Erreur lors de l'analyse :",
    "json_error": "Erreur dans l'analyse. Voici la réponse brute :",
    "use_manual_info": "Utilisez les informations des métiers disponibles dans l'onglet 'Comparatif Métiers'"
}

# Configuration des ressources
RESSOURCES = {
    "cours_platformes": {
        "Coursera": [
            "Data Science Specialization (Johns Hopkins)",
            "Machine Learning (Stanford)",
            "Python for Everybody"
        ],
        "edX": [
            "Data Science MicroMasters (UC San Diego)",
            "Introduction to Python Programming",
            "Data Analysis with Python"
        ],
        "Udemy": [
            "Python for Data Science Bootcamp",
            "SQL Bootcamp",
            "Tableau A-Z"
        ],
        "DataCamp": [
            "Data Analyst with Python",
            "Data Scientist with Python",
            "Machine Learning Fundamentals"
        ]
    },
    "documentation": {
        "Python": [
            ("Documentation officielle Python", "https://docs.python.org/"),
            ("Pandas User Guide", "https://pandas.pydata.org/docs/"),
            ("NumPy Reference", "https://numpy.org/doc/")
        ],
        "SQL": [
            ("SQL Tutorial", "https://www.w3schools.com/sql/"),
            ("PostgreSQL Documentation", "https://www.postgresql.org/docs/")
        ],
        "Visualisation": [
            ("Matplotlib Tutorial", "https://matplotlib.org/stable/tutorials/"),
            ("Plotly Documentation", "https://plotly.com/python/"),
            ("Seaborn Guide", "https://seaborn.pydata.org/tutorial.html")
        ]
    }
}
