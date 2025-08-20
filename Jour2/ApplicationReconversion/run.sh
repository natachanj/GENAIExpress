#!/bin/bash

echo "🚀 Lancement de l'Assistant de Reconversion Data..."

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

# Vérifier la configuration
if [ ! -f ".env" ]; then
    echo "⚠️  Fichier .env non trouvé !"
    echo "📝 Copiez env_example.txt vers .env et ajoutez votre clé API OpenAI"
    echo "cp env_example.txt .env"
    exit 1
fi

# Lancer l'application
echo "🌟 Lancement de l'application..."
streamlit run app.py
