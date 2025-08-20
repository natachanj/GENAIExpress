#!/usr/bin/env python3
"""
Script de test pour vérifier la connexion OpenAI
"""

import os
import openai
from dotenv import load_dotenv

def test_openai_connection():
    """Test de la connexion à l'API OpenAI"""
    
    # Charger les variables d'environnement
    load_dotenv()
    
    # Vérifier la clé API
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Erreur : Clé API OpenAI non trouvée")
        print("📝 Créez un fichier .env avec votre clé API")
        return False
    
    if api_key.startswith("sk-test"):
        print("⚠️  Attention : Clé API de test détectée")
        print("🔑 Remplacez par votre vraie clé API pour utiliser l'application")
        return False
    
    try:
        # Tester la connexion
        print("🔌 Test de connexion à l'API OpenAI...")
        
        client = openai.OpenAI(api_key=api_key)
        
        # Test simple avec un prompt court
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Dis-moi bonjour en français"}],
            max_tokens=50
        )
        
        print("✅ Connexion réussie !")
        print(f"🤖 Réponse : {response.choices[0].message.content}")
        return True
        
    except openai.AuthenticationError:
        print("❌ Erreur d'authentification")
        print("🔑 Vérifiez que votre clé API est correcte")
        return False
        
    except openai.RateLimitError:
        print("❌ Limite de taux dépassée")
        print("⏳ Attendez un moment avant de réessayer")
        return False
        
    except openai.APIError as e:
        print(f"❌ Erreur API : {e}")
        return False
        
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
        return False

def test_configuration():
    """Test de la configuration de l'application"""
    
    print("\n🔧 Test de la configuration...")
    
    # Vérifier les fichiers requis
    required_files = [
        "app.py",
        "requirements.txt",
        ".env",
        "config.py"
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} - Présent")
        else:
            print(f"❌ {file} - Manquant")
    
    # Vérifier les dépendances
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__} - Installé")
    except ImportError:
        print("❌ Streamlit - Non installé")
    
    try:
        import pandas
        print(f"✅ Pandas {pandas.__version__} - Installé")
    except ImportError:
        print("❌ Pandas - Non installé")
    
    try:
        import plotly
        print(f"✅ Plotly {plotly.__version__} - Installé")
    except ImportError:
        print("❌ Plotly - Non installé")

if __name__ == "__main__":
    print("🚀 Test de l'Assistant de Reconversion Data")
    print("=" * 50)
    
    # Test de la configuration
    test_configuration()
    
    # Test de la connexion OpenAI
    print("\n" + "=" * 50)
    test_openai_connection()
    
    print("\n" + "=" * 50)
    print("📋 Résumé des tests terminé")
    print("💡 Pour lancer l'application : streamlit run app.py")
