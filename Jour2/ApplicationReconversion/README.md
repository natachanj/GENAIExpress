# 🚀 Assistant de Reconversion Data

Une application Streamlit intelligente qui aide les personnes à se reconvertir dans les métiers de la data science et de l'analyse de données.

## ✨ Fonctionnalités

- **🎯 Analyse Personnalisée** : Évaluation de votre profil avec recommandations de métiers data adaptés
- **📊 Comparatif Métiers** : Visualisation des salaires, durées de formation et difficultés
- **📚 Ressources** : Cours en ligne, documentation, projets pratiques et certifications
- **🤖 IA OpenAI** : Recommandations personnalisées basées sur votre profil
- **💻 Interface Moderne** : Design responsive et intuitif avec Streamlit

## 🛠️ Installation

### Prérequis
- Python 3.8 ou supérieur
- Clé API OpenAI

### Étapes d'installation

1. **Cloner le projet**
```bash
git clone <votre-repo>
cd ApplicationReconversion
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configuration de l'API OpenAI**
```bash
# Copier le fichier d'exemple
cp env_example.txt .env

# Éditer le fichier .env et ajouter votre clé API
OPENAI_API_KEY=votre_vraie_cle_api_ici
```

## 🚀 Lancement

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : `http://localhost:8501`

## 📱 Utilisation

### 1. **Accueil**
- Vue d'ensemble des opportunités dans la data
- Statistiques du marché
- Guide de démarrage

### 2. **Analyse Personnalisée**
- Remplissez le formulaire avec votre profil actuel
- L'IA analyse vos compétences et expérience
- Recevez des recommandations personnalisées de métiers data
- Obtenez un plan de formation adapté

### 3. **Ressources**
- **Cours en ligne** : Plateformes recommandées (Coursera, edX, Udemy, DataCamp)
- **Documentation** : Ressources officielles Python, SQL, visualisation
- **Projets pratiques** : Idées de projets pour développer vos compétences
- **Certifications** : Certifications reconnues par secteur

### 4. **Comparatif Métiers**
- Visualisations interactives des salaires et durées de formation
- Détails complets sur chaque métier data
- Comparaison des niveaux de difficulté

## 🎯 Métiers Data Couverts

| Métier | Description | Durée Formation | Salaire Junior | Salaire Senior |
|--------|-------------|-----------------|----------------|----------------|
| **Data Analyst** | Analyse de données business | 3-6 mois | 35k-45k€ | 55k-75k€ |
| **Data Scientist** | Modèles prédictifs et ML | 6-12 mois | 45k-60k€ | 70k-100k€ |
| **Data Engineer** | Infrastructures de données | 6-9 mois | 40k-55k€ | 65k-90k€ |
| **Business Intelligence** | Tableaux de bord business | 4-7 mois | 35k-45k€ | 55k-75k€ |
| **ML Engineer** | Déploiement de modèles ML | 8-12 mois | 50k-65k€ | 75k-110k€ |

## 🔧 Configuration

### Variables d'environnement
- `OPENAI_API_KEY` : Votre clé API OpenAI (obligatoire)

### Personnalisation
Vous pouvez modifier le dictionnaire `METIERS_DATA` dans `app.py` pour :
- Ajouter de nouveaux métiers
- Modifier les salaires et durées
- Ajuster les compétences requises

## 🚨 Sécurité

- **Jamais** de clé API exposée dans l'interface
- Utilisation de variables d'environnement
- Validation des entrées utilisateur
- Gestion d'erreurs robuste

## 📊 Technologies Utilisées

- **Frontend** : Streamlit
- **IA** : OpenAI GPT-3.5-turbo
- **Visualisation** : Plotly
- **Données** : Pandas
- **Interface** : streamlit-option-menu

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter de nouveaux métiers ou ressources
- Améliorer la documentation

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🆘 Support

Si vous rencontrez des problèmes :
1. Vérifiez que votre clé API OpenAI est correcte
2. Assurez-vous d'avoir installé toutes les dépendances
3. Consultez la documentation Streamlit
4. Ouvrez une issue sur le repository

## 🎉 Remerciements

- Streamlit pour l'interface
- OpenAI pour l'IA
- La communauté data science française
- Tous les contributeurs du projet

---

**🚀 Prêt à transformer votre carrière ? Lancez l'application et commencez votre parcours de reconversion data !**
