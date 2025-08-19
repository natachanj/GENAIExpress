## GENAIExpress — Démarrer avec l’IA Générative en 5 jours

Un mini-parcours pour prendre en main les fondamentaux de l’IA générative en 5 jours, avec des notebooks Jupyter et des ressources pédagogiques.

- **Dépôt GitHub**: [natachanj/GENAIExpress](https://github.com/natachanj/GENAIExpress.git)

Note: le dépôt distant peut apparaître vide tant que le premier commit n’a pas été poussé depuis la machine locale.

### Prérequis

- Git installé
- Python 3.10+ et `pip`
- Jupyter (`pip install jupyter` ou `pip install jupyterlab`)

Si vous utilisez l’API OpenAI dans les notebooks, configurez votre clé :

```bash
export OPENAI_API_KEY="votre_clef_api_openai"
```

### Cloner le dépôt

```bash
git clone https://github.com/natachanj/GENAIExpress.git
cd GENAIExpress
```

### Publier ce dossier local vers GitHub (si le dépôt distant est vide)

Si vous partez des fichiers locaux de ce dossier et souhaitez les publier sur GitHub :

```bash
git init
git branch -M main
git remote add origin https://github.com/natachanj/GENAIExpress.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

### Installation rapide (environnement isolé recommandé)

```bash
python -m venv .venv
source .venv/bin/activate  # sous macOS/Linux
# .venv\Scripts\activate  # sous Windows PowerShell

pip install --upgrade pip
pip install jupyter jupyterlab
# Selon vos besoins dans les notebooks :
# pip install openai python-dotenv pandas numpy
```

### Lancer les notebooks

```bash
jupyter lab
# ou
jupyter notebook
```

Ouvrez ensuite les notebooks dans le dossier `Jour1/` (et suivants au fil du parcours).

### Structure du projet

```text
GENAIExpress/
  Jour1/
    01_Utiliser_API_OPENAI.ipynb
    Challenge-GenAI-Express-Demarrer-avec-lIA-Generative-en-5-Jours.pdf
    Template de cadrage – Projet IA Générative (MVP) 2.pdf
  Jour2/
  Jour3/
  Jour4/
  Jour5/
```

- **`Jour1/`**: premiers pas (utilisation de l’API OpenAI, cadrage MVP, ressources PDF).
- **`Jour2/` … `Jour5/`**: dossiers réservés aux étapes suivantes du programme.

### Ressources incluses

- Challenge et support de cours (PDF) pour guider la progression.
- Notebook d’exemple `01_Utiliser_API_OPENAI.ipynb` pour démarrer rapidement avec des appels d’API.

### Contribution

1) Créez une branche : `git checkout -b feature/ma-feature`
2) Commitez : `git commit -m "Ajoute ma feature"`
3) Poussez : `git push origin feature/ma-feature`
4) Ouvrez une Pull Request sur GitHub.

### Licence

Sauf indication contraire, le contenu est fourni tel quel à des fins pédagogiques. Ajoutez la licence de votre choix si nécessaire (ex. MIT).


