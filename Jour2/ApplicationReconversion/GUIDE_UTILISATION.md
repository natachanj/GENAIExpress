# 📖 Guide d'Utilisation - Assistant de Reconversion Data

## 🚀 Démarrage Rapide

### Option 1 : Version Complète (avec IA OpenAI)
```bash
# Sur macOS/Linux
./run.sh

# Sur Windows
run.bat
```

### Option 2 : Version Démo (sans IA)
```bash
# Sur macOS/Linux
./run_demo.sh

# Sur Windows
run_demo.bat
```

## 🎯 Utilisation de l'Application

### 1. **Page d'Accueil**
- Vue d'ensemble du marché de la data
- Statistiques et opportunités
- Guide de démarrage

### 2. **Analyse Personnalisée** ⭐ **FONCTIONNALITÉ PRINCIPALE**

#### Remplir le Formulaire
1. **Profil Actuel**
   - Métier actuel (ex: Commercial, Enseignant, Comptable)
   - Secteur d'activité
   - Années d'expérience
   - Niveau d'études

2. **Compétences**
   - **Techniques** : Excel, SQL, Python, R, PowerBI, etc.
   - **Transversales** : Analyse, Communication, Gestion de projet

3. **Motivation et Temps**
   - Motivation principale
   - Temps disponible pour la formation

#### Résultats de l'Analyse
- **Métiers Recommandés** : Top 3 avec scores de compatibilité
- **Analyse du Profil** : Forces et points d'amélioration
- **Plan de Formation** : Programme personnalisé en 3 phases
- **Conseils** : Recommandations spécifiques

### 3. **Ressources de Formation**
- **Cours en Ligne** : Plateformes recommandées
- **Documentation** : Ressources officielles
- **Projets Pratiques** : Idées de projets par domaine
- **Certifications** : Certifications reconnues par secteur

### 4. **Comparatif Métiers**
- **Visualisations** : Graphiques interactifs des salaires et durées
- **Détails** : Informations complètes sur chaque métier
- **Comparaisons** : Salaires, difficulté, compétences requises

## 🔧 Configuration

### Variables d'Environnement
```bash
# Créer le fichier .env
cp env_example.txt .env

# Éditer .env et ajouter votre clé API
OPENAI_API_KEY=votre_vraie_cle_api_ici
```

### Ports par Défaut
- **Version Complète** : `http://localhost:8501`
- **Version Démo** : `http://localhost:8502`

## 📱 Interface Utilisateur

### Navigation
- **Onglets horizontaux** pour naviguer entre les sections
- **Sidebar** avec informations utiles et conseils
- **Design responsive** adapté à tous les écrans

### Fonctionnalités Interactives
- **Formulaires** avec validation
- **Graphiques** Plotly interactifs
- **Expandeurs** pour organiser l'information
- **Métriques** en temps réel

## 🎨 Personnalisation

### Thème
Modifiez `.streamlit/config.toml` :
```toml
[theme]
primaryColor = "#FF6B6B"      # Couleur principale
backgroundColor = "#FFFFFF"    # Arrière-plan
secondaryBackgroundColor = "#F0F2F6"  # Arrière-plan secondaire
textColor = "#262730"         # Couleur du texte
```

### Métiers Data
Ajoutez/modifiez des métiers dans `app.py` :
```python
METIERS_DATA = {
    "Nouveau Métier": {
        "description": "Description du métier",
        "salaire_junior": "40k-50k€",
        "salaire_senior": "60k-80k€",
        "duree_formation": "6-9 mois",
        "niveau_difficulte": "Moyen",
        "competences_requises": ["Comp1", "Comp2", "Comp3"]
    }
}
```

## 🚨 Dépannage

### Problèmes Courants

#### 1. **Clé API OpenAI manquante**
```
⚠️ Clé API OpenAI non trouvée. Veuillez créer un fichier .env avec votre clé API.
```
**Solution** : Créer le fichier `.env` avec votre clé API

#### 2. **Port déjà utilisé**
```
Address already in use
```
**Solution** : Changer le port dans la commande
```bash
streamlit run app.py --server.port 8503
```

#### 3. **Dépendances manquantes**
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solution** : Réinstaller les dépendances
```bash
pip install -r requirements.txt
```

#### 4. **Erreur de version Python**
```
Python version 3.8+ required
```
**Solution** : Utiliser Python 3.8 ou supérieur

### Logs et Debug
```bash
# Mode verbose
streamlit run app.py --logger.level debug

# Vérifier les processus
lsof -i :8501  # macOS/Linux
netstat -an | findstr 8501  # Windows
```

## 📊 Métriques et Performance

### Temps de Chargement
- **Page d'accueil** : < 2 secondes
- **Analyse IA** : 5-15 secondes (selon la complexité)
- **Graphiques** : < 1 seconde

### Utilisation Mémoire
- **Base** : ~100 MB
- **Avec analyse IA** : ~150 MB
- **Graphiques** : +50 MB

## 🔒 Sécurité

### Bonnes Pratiques
- ✅ **Jamais** exposer la clé API dans l'interface
- ✅ Utiliser des variables d'environnement
- ✅ Valider toutes les entrées utilisateur
- ✅ Gérer les erreurs gracieusement

### Variables Sensibles
```bash
# ❌ Ne jamais faire
OPENAI_API_KEY=sk-123...  # Dans le code

# ✅ Toujours faire
OPENAI_API_KEY=${OPENAI_API_KEY}  # Variable d'environnement
```

## 🚀 Déploiement

### Local
```bash
streamlit run app.py
```

### Serveur
```bash
nohup streamlit run app.py --server.headless true &
```

### Docker (optionnel)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.headless", "true"]
```

## 📚 Ressources Supplémentaires

### Documentation Officielle
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [Plotly Python](https://plotly.com/python/)

### Communautés
- [Streamlit Community](https://discuss.streamlit.io/)
- [OpenAI Community](https://community.openai.com/)
- [Data Science France](https://www.datascience-fr.com/)

## 🤝 Support

### Signaler un Bug
1. Vérifiez la section dépannage
2. Consultez les logs d'erreur
3. Ouvrez une issue avec :
   - Description du problème
   - Étapes pour reproduire
   - Version de Python/OS
   - Logs d'erreur

### Demander une Fonctionnalité
1. Décrivez le besoin
2. Expliquez l'utilité
3. Proposez une implémentation

---

**🎉 Vous êtes maintenant prêt à utiliser l'Assistant de Reconversion Data !**

Commencez par l'onglet "Analyse Personnalisée" pour recevoir vos premières recommandations.
