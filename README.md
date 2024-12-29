# Performance-Forecaster

## Projet 2024-25 : Visualiser et prédire la forme des meilleurs joueurs de PL

### 📖 Description

---

Idée : en récupérant un maximum de données sur une liste de dix joueurs que nous avons établie, à savoir les dix joueurs les mieux notés de ligue anglaise (Premier League), nous cherchons à visualiser leurs performance, et établir une évolution possible (probable) de leurs performances.

Moyens : pour récolter les données, utiliser un API (Sofascore) et en scrappant éventuellement des informations sur d’autres sites (Flashscore, Twitter, L’Équipe,...). En ce qui concerne leur visualisation, réaliser des heatmaps de leur déplacement sur le terrain, des graphes montrant leurs goal contributions (buts + p/d) et enfin récupérer la liste de leurs précédents et futurs adversaires pour estimer la représentativité de leurs dernières performances.

---

## 📂 Structure du projet

Voici la structure des dossiers :

Premier-League-Simulation/
│
├── src/
│   ├── data/
│   │   ├── descriptive_data/   # Données générées et CSV des joueurs
│   ├── notebooks/              # Notebooks Jupyter pour analyse et visualisation
│   ├── scripts/                # Scripts Python pour automatiser des tâches
│
├── README.md                   # Documentation du projet
├── requirements.txt            # Liste des dépendances
└── ...
