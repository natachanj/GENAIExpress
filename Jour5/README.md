# Jour 5 — Agent IA YouTube : Extraction et Analyse de Transcriptions

## 🎯 Objectif du Jour 5

Ce dernier jour du challenge GenAI Express vous permet de créer un **agent conversationnel intelligent** capable d'extraire automatiquement les transcriptions de vidéos YouTube et de les analyser en profondeur avec GPT-4o.

## 🚀 Fonctionnalités Principales

### ✨ Extraction Automatique de Transcriptions
- **Récupération intelligente** des sous-titres depuis n'importe quelle URL YouTube
- **Support multilingue** : français en priorité, puis anglais, avec fallback automatique
- **Gestion des erreurs** robuste pour les vidéos sans transcription disponible

### 🤖 Agent IA Conversationnel
- **Analyse contextuelle** du contenu des vidéos
- **Réponses naturelles** en langage français
- **Anti-hallucination** : l'agent ne fait jamais de suppositions sans source

### 📱 Génération de Contenu pour Réseaux Sociaux
- **Posts LinkedIn** (800-1200 caractères) : style professionnel et structuré
- **Posts Instagram** (300-600 caractères) : ton direct et percutant
- **Adaptation automatique** du style selon la plateforme cible

## 🛠️ Technologies Utilisées

| Composant | Description |
|-----------|-------------|
| **OpenAI Agents** | Framework pour créer des agents conversationnels intelligents |
| **GPT-4o** | Modèle de langage avancé pour l'analyse et la génération |
| **YouTube Transcript API** | Extraction automatique des sous-titres YouTube |
| **Gradio** | Interface web moderne et intuitive |
| **Python 3.11+** | Langage de programmation principal |

## 📁 Structure du Projet

```
Jour5/
├── 1_Créer_Un_Agent_IA_Youtube.ipynb    # Notebook d'apprentissage
├── app.py                                 # Application web Gradio
├── requirements.txt                       # Dépendances Python
└── README.md                             # Ce fichier
```

## 🚀 Installation et Configuration

### 1. Prérequis
- Python 3.11 ou supérieur
- Conda (recommandé) ou pip
- Clé API OpenAI valide

### 2. Installation des Dépendances

```bash
# Activer l'environnement conda (si utilisé)
conda activate rag-env

# Installer les packages requis
pip install -r requirements.txt
```

### 3. Configuration de l'API OpenAI

Créez un fichier `.env` à la racine du projet :

```env
OPENAI_API_KEY=votre_clé_api_openai_ici
```

## 💻 Utilisation

### Option 1 : Notebook Jupyter
1. Ouvrez `1_Créer_Un_Agent_IA_Youtube.ipynb`
2. Exécutez les cellules dans l'ordre
3. Testez l'agent avec vos URLs YouTube

### Option 2 : Application Web Gradio
1. Lancez l'application :
   ```bash
   python app.py
   ```
2. Ouvrez votre navigateur sur l'URL affichée
3. Collez une URL YouTube et posez vos questions !

## 🎬 Exemples d'Utilisation

### Scénario 1 : Analyse de Contenu
- **Entrée** : URL d'une vidéo YouTube
- **Question** : "De quoi parle cette vidéo ?"
- **Résultat** : Résumé détaillé basé sur la transcription

### Scénario 2 : Création de Contenu
- **Entrée** : URL d'une vidéo + demande de post LinkedIn
- **Résultat** : Post professionnel structuré avec accroche et call-to-action

### Scénario 3 : Questions Spécifiques
- **Entrée** : URL + question précise sur le contenu
- **Résultat** : Réponse contextuelle basée uniquement sur la transcription

## 🔧 Fonctionnalités Techniques

### Extraction d'ID Vidéo
- Support de tous les formats d'URL YouTube :
  - `youtube.com/watch?v=...`
  - `youtu.be/...`
  - `youtube.com/shorts/...`
  - `youtube.com/embed/...`

### Gestion des Transcriptions
- **Priorité 1** : Sous-titres français manuels
- **Priorité 2** : Sous-titres français générés automatiquement
- **Priorité 3** : Sous-titres anglais avec traduction
- **Fallback** : Message d'erreur informatif

### Sécurité et Performance
- **Anti-hallucination** strict
- **Gestion d'erreurs** complète
- **Interface asynchrone** pour une expérience fluide

## 🎓 Apprentissages Clés

Ce projet vous permet de maîtriser :
- ✅ **Création d'agents IA** avec OpenAI Agents
- ✅ **Intégration d'APIs externes** (YouTube)
- ✅ **Gestion de contextes longs** avec GPT-4o
- ✅ **Interfaces utilisateur** avec Gradio
- ✅ **Gestion d'erreurs** robuste en production
- ✅ **Génération de contenu** adaptatif

## 🚨 Dépannage

### Problème : "Transcription non disponible"
**Solution** : La vidéo n'a pas de sous-titres. L'agent vous proposera des alternatives.

### Problème : "Erreur d'API OpenAI"
**Solution** : Vérifiez votre clé API dans le fichier `.env`

### Problème : "URL invalide"
**Solution** : Assurez-vous que l'URL YouTube est complète et valide

## 🌟 Prochaines Étapes

Après ce jour 5, vous pourrez :
- **Personnaliser** l'agent selon vos besoins
- **Intégrer** d'autres sources de contenu
- **Déployer** votre application en production
- **Créer** d'autres types d'agents IA

---

**🎉 Félicitations ! Vous avez terminé le challenge GenAI Express !**

Vous maîtrisez maintenant les fondamentaux de l'IA générative et pouvez créer des applications intelligentes et utiles. Continuez à explorer et innover !


