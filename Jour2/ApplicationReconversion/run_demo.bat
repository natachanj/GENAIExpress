@echo off
echo 🚀 Lancement de l'Assistant de Reconversion Data - Version Démo...

REM Vérifier si l'environnement virtuel existe
if not exist "venv" (
    echo 📦 Création de l'environnement virtuel...
    python -m venv venv
)

REM Activer l'environnement virtuel
echo 🔧 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Installer les dépendances
echo 📚 Installation des dépendances...
pip install -r requirements.txt

REM Lancer l'application de démonstration
echo 🌟 Lancement de l'application de démonstration...
streamlit run test_app.py
pause
