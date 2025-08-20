## Jour 2 — Vibe coding: passer de l’idée à un premier écran

Objectif du jour: transformer une idée simple en un début d’application visible, en avançant par petites boucles.

### Les 4 étapes clés

#### 1) Contexte (dites ce que vous voulez)
Posez le cadre en 5–7 phrases maximum:
- Qui est l’utilisateur et quel problème veut-il résoudre ?
- Le scénario d’usage principal (en une minute chrono)
- Le résultat attendu (qu’est-ce que l’on voit/peut faire à la fin ?)
- Les contraintes (mobile/desktop, langue, ton, simplicité…)
- Les “non‑objectifs” (ce qu’on ne fera pas aujourd’hui)

Modèle prêt à copier:
```text
Contexte
- Public: …
- Problème: …
- Scénario principal: …
- Résultat attendu aujourd’hui: …
- Contraintes: …
- Hors scope: …
```

#### 2) Demander à ChatGPT d’améliorer votre idée
Collez votre contexte et demandez 3 choses: clarification, plan minimal, et idées d’UI.

Prompt prêt à l’emploi:
```text
Voici le contexte de mon app. Améliore-le en:
1) Reformulant les objectifs en 3–5 points clairs
2) Proposant 5–8 user stories très simples (format: en tant que…, je veux…, afin de…)
3) Suggérant une structure d’écran d’accueil (sections, boutons) et 3 prochaines étapes concrètes

Contexte:
<votre texte>
```

Astuce: demandez des versions encore plus simples si la proposition vous paraît trop ambitieuse.

#### 3) Construire avec Cursor (pas besoin d’être technique)
- Ouvrez votre dossier de projet dans Cursor
- Collez le plan proposé et demandez: “crée l’écran d’accueil minimal et un README pour le lancer”
- Laissez Cursor proposer des edits, acceptez/ajustez
- Ouvrez l’aperçu/preview et vérifiez que l’écran s’affiche
- Restez sur des micro‑ajouts (texte, bouton, navigation simple)

Exemples de demandes utiles à Cursor:
- “Ajoute un bouton ‘Commencer’ qui mène à une page vide ‘/start’”
- “Affiche une liste d’éléments factices (3 items) avec un bouton ‘Voir’ pour chacun”
- “Ajoute un message d’erreur lisible quand la liste est vide”

#### 4) Itérez en petites boucles
Boucle type (5–10 minutes):
- Tester rapidement → Noter la friction principale
- Demander une toute petite amélioration → Accepter/ajuster
- Re‑tester → Passer à la prochaine micro‑tâche

Critères de réussite du jour:
- Un premier écran visible et utilisable (même très simple)
- 5–8 user stories triées par priorité
- 3 prochaines étapes notées pour le Jour 3

### Livrables attendus
- Un écran d’accueil minimal de l’app
- Un `README` ou une note qui indique “comment lancer”
- Une courte liste de user stories (copiée depuis ChatGPT et adaptée)

### Conseils pratiques
- Petit et palpable > grand et théorique
- Nommez vos sections/boutons avec des mots clairs
- Gardez une trace de vos prompts utiles pour les réutiliser

Référence du dépôt: [natachanj/GENAIExpress](https://github.com/natachanj/GENAIExpress.git)

