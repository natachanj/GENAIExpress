#!/bin/bash

echo "🚀 Lancement de l'Assistant de Reconversion Data - Version Démo..."

# Vérifier si l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances
echo "📚 Installation des dépendances..."
pip install -r requirements.txt

# Lancer l'application de démonstration
echo "🌟 Lancement de l'application de démonstration..."
streamlit run test_app.py
