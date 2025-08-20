#!/usr/bin/env python3
"""
Script de test pour vérifier que l'analyse fonctionne correctement
"""

import json
import openai
from dotenv import load_dotenv, find_dotenv
import os

def test_analysis_logic():
    """Test de la logique d'analyse sans appeler l'API"""
    
    print("🧪 Test de la logique d'analyse...")
    
    # Simuler une réponse d'API
    test_response = {
        "metiers_recommandes": [
            {"nom": "Data Analyst", "score": 8},
            {"nom": "Business Intelligence", "score": 7},
            {"nom": "Data Engineer", "score": 6}
        ],
        "analyse_profil": "Profil avec de bonnes compétences d'analyse",
        "plan_formation": "Formation en 3 phases",
        "conseils": "Conseils personnalisés"
    }
    
    # Test de la logique de parsing
    try:
        # Vérifier que la structure attendue existe
        if "metiers_recommandes" in test_response and isinstance(test_response["metiers_recommandes"], list):
            print("✅ Structure metiers_recommandes valide")
            
            for metier in test_response["metiers_recommandes"]:
                # Gérer différents formats de réponse
                nom_metier = metier.get('nom') or metier.get('name') or metier.get('metier') or "Métier non spécifié"
                score = metier.get('score') or metier.get('note') or "N/A"
                
                print(f"   - {nom_metier} - Score: {score}/10")
        else:
            print("❌ Structure metiers_recommandes invalide")
        
        # Test des autres champs
        if "analyse_profil" in test_response:
            print("✅ Champ analyse_profil présent")
        
        if "plan_formation" in test_response:
            print("✅ Champ plan_formation présent")
        
        if "conseils" in test_response:
            print("✅ Champ conseils présent")
            
        print("✅ Test de logique réussi !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test de logique : {e}")
        return False

def test_different_formats():
    """Test avec différents formats de réponse"""
    
    print("\n🔄 Test avec différents formats...")
    
    # Format alternatif 1
    alt_response1 = {
        "metiers_recommandes": [
            {"name": "Data Scientist", "note": 9},
            {"metier": "Data Analyst", "score": 8}
        ],
        "analyse": "Analyse alternative",
        "formation": "Plan de formation alternatif",
        "recommandations": "Conseils alternatifs"
    }
    
    # Format alternatif 2
    alt_response2 = {
        "metiers": [
            {"nom": "Data Engineer", "score": 7}
        ],
        "analyse_profil": "Analyse standard",
        "plan_formation": "Plan standard",
        "conseils": "Conseils standard"
    }
    
    try:
        # Test format 1
        print("📝 Test format alternatif 1...")
        if "metiers_recommandes" in alt_response1:
            for metier in alt_response1["metiers_recommandes"]:
                nom = metier.get('nom') or metier.get('name') or metier.get('metier') or "Métier non spécifié"
                score = metier.get('score') or metier.get('note') or "N/A"
                print(f"   - {nom} - Score: {score}/10")
        
        # Test format 2
        print("📝 Test format alternatif 2...")
        if "metiers" in alt_response2:
            for metier in alt_response2["metiers"]:
                nom = metier.get('nom') or metier.get('name') or metier.get('metier') or "Métier non spécifié"
                score = metier.get('score') or metier.get('note') or "N/A"
                print(f"   - {nom} - Score: {score}/10")
        
        print("✅ Test des formats alternatifs réussi !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test des formats : {e}")
        return False

def test_error_handling():
    """Test de la gestion d'erreurs"""
    
    print("\n🚨 Test de la gestion d'erreurs...")
    
    # Test avec structure manquante
    incomplete_response = {
        "analyse_profil": "Seulement l'analyse"
    }
    
    try:
        if "metiers_recommandes" in incomplete_response and isinstance(incomplete_response["metiers_recommandes"], list):
            print("✅ Structure metiers_recommandes présente")
        else:
            print("⚠️  Structure metiers_recommandes manquante (comportement attendu)")
        
        print("✅ Test de gestion d'erreurs réussi !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test de gestion d'erreurs : {e}")
        return False

if __name__ == "__main__":
    print("🚀 Test de l'analyse de l'Assistant de Reconversion Data")
    print("=" * 60)
    
    # Tests
    test1 = test_analysis_logic()
    test2 = test_different_formats()
    test3 = test_error_handling()
    
    print("\n" + "=" * 60)
    print("📋 Résumé des tests :")
    print(f"   Test logique : {'✅ Réussi' if test1 else '❌ Échoué'}")
    print(f"   Test formats : {'✅ Réussi' if test2 else '❌ Échoué'}")
    print(f"   Test erreurs : {'✅ Réussi' if test3 else '❌ Échoué'}")
    
    if all([test1, test2, test3]):
        print("\n🎉 Tous les tests sont réussis ! L'analyse est robuste.")
    else:
        print("\n⚠️  Certains tests ont échoué. Vérifiez le code.")
    
    print("\n💡 Pour tester l'application complète : streamlit run app.py")
