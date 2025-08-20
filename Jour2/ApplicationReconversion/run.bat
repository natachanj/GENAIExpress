@echo off
echo 🚀 Lancement de l'Assistant de Reconversion Data...

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

REM Vérifier la configuration
if not exist ".env" (
    echo ⚠️  Fichier .env non trouvé !
    echo 📝 Copiez env_example.txt vers .env et ajoutez votre clé API OpenAI
    echo copy env_example.txt .env
    pause
    exit /b 1
)

REM Lancer l'application
echo 🌟 Lancement de l'application...
streamlit run app.py
pause
