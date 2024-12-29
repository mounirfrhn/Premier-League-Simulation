# Projet **Prédiction de performance pour les top joueurs de Premier League**

## Description
Ce projet vise à prédire les performances de certains joueurs de Premier League à l'aide d'algorithmes de ML, mais aussi et surtout à comprendre les facteurs qui font de ces joueurs les éléments clefs de leur équipe. En exploitant des données historiques sur les joueurs, leurs équipes, et leurs performances passées, le modèle tente de fournir des prévisions précises pour les futures rencontres.

---

## Structure du projet

    Premier-League-Simulation/
    │
    ├── src/
    │   ├── data/
    │   │   ├── descriptive_data/   # Données générées et CSV des joueurs
    │   │   ├── model_data/         # Données pour entrainer les modèles
    │   ├── notebooks/              # Notebooks Jupyter pour analyse et visualisation
    │   ├── scripts/                # Scripts Python pour automatiser des tâches (scrapping)
    │
    ├── README.md                   # Documentation du projet
    ├── requirements.txt            # Liste des dépendances
    └── main.ipynb                  # Notebook final

---

## Comment exécuter le projet

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/mounirfrhn/Premier-League-Simulation
   cd Premier-League-Simulation
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python -m venv .venv
   source venv/bin/activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Installer les dépendances** :
   - sélectionner 'venv' au moment de choisir le Kernel du notebook main.ipynb

NB : Si vous souhaitez scrapper vous-même les données, il est nécessaire de récuperer une clé API sur rapidAPI et de changer celle dans le fichier src/scripts/get_descriptive_data.py

---

## Scrapping
L'API utilisé est totalement gratuit.
Dans le fichier `main.ipynb`, le scrapping est effectué principalement en utilisant une API dédiée aux statistiques sportives. Les principales étapes incluent :

1. **Requête API** : Envoi de requêtes HTTP pour récupérer des données structurées sur les performances des joueurs, les résultats des matchs, et d'autres statistiques pertinentes.
   - Bibliothèque utilisée : **requests**.
   - Documentation de l'API : La documentation de l'API a été consultée pour comprendre les points d'accès disponibles et les paramètres requis.
2. **Extraction et validation** : Vérification des réponses de l'API pour s'assurer qu'elles contiennent les informations attendues, suivie d'un nettoyage des données.
   - Exemple : Retrait des doublons, correction des formats de date.
3. **Stockage local** : Sauvegarde des données dans des fichiers CSV pour un accès rapide et une utilisation dans les étapes ultérieures du pipeline.

Ces données constituent la base des analyses et des modèles présentés dans les sections suivantes.

---

## Data Visualisation
Une analyse approfondie des données est entreprise pour répondre à deux objectifs principaux :

1. **Établir le profil des joueurs** : Identifier les points forts et faibles des joueurs individuels, tels que leurs contributions offensives et défensives.
   - Visualisations : Graphiques en barres et histogrammes illustrant les statistiques moyennes des joueurs (par exemple, buts marqués, passes décisives).

2. **Déterminer les facteurs clés de performance** : Identifier les variables qui influencent significativement les résultats des matchs et les performances des joueurs.
   - Approche : Analyse de corrélation entre diverses métriques, comme le nombre de passes réussies ou les kilomètres parcourus, et les performances globales.
   - Outils : **matplotlib** pour les visualisations statiques et **seaborn** pour les analyses approfondies (comme les heatmaps de corrélation).

Ces visualisations fournissent des insights précieux pour orienter la phase de modélisation.

---

## Modélisation
La phase de modélisation, détaillée dans `main.ipynb`, vise à prédire les performances futures des joueurs. Les étapes clés incluent :

1. **Préparation des données** :
   - Division en ensembles d'entraînement (80%) et de test (20%).
   - Normalisation des valeurs pour garantir une échelle homogène entre les différentes variables.

2. **Entraînement des modèles** :
   - Modèles implémentés :
     - Régression linéaire pour des prédictions basées sur des relations linéaires.
     - Forêts aléatoires pour capturer des interactions complexes entre les variables.
     - LSTM pour capturer les relations temporelles entre les matchs

Les résultats montrent que les forêts aléatoires obtiennent une meilleure performance globale, en particulier sur des données riches en variables interactives.

---

## Objectifs futurs
- Améliorer la prédiction des modèles en utilisant les ranks des équipes qui se rencontrent
- Développer une interface utilisateur intuitive pour permettre aux utilisateurs d'entrer des données et de visualiser les prédictions.
