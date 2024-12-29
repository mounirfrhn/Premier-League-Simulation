# Performance-Forecaster

## Projet 2024-25 : Visualiser et prédire la forme des meilleurs joueurs de PL

### 📖 Description

---

Idée : en récupérant un maximum de données sur une liste de dix joueurs que nous avons établie, à savoir les dix joueurs les mieux notés de ligue anglaise (Premier League), nous cherchons à visualiser leurs performance, et établir une évolution possible (probable) de leurs performances.

Moyens : pour récolter les données, utiliser un API (Sofascore) et en scrappant éventuellement des informations sur d’autres sites (Flashscore, Twitter, L’Équipe,...). En ce qui concerne leur visualisation, réaliser des heatmaps de leur déplacement sur le terrain, des graphes montrant leurs goal contributions (buts + p/d) et enfin récupérer la liste de leurs précédents et futurs adversaires pour estimer la représentativité de leurs dernières performances.

---

## 📂 Structure du projet

Voici la structure des dossiers :

    ├── build                   # Compiled files (alternatively `dist`)
    ├── docs                    # Documentation files (alternatively `doc`)
    ├── src                     # Source files (alternatively `lib` or `app`)
    ├── test                    # Automated tests (alternatively `spec` or `tests`)
    ├── tools                   # Tools and utilities
    ├── LICENSE
    └── README.md


---

## 🏗️ Installation
Suivez ces étapes pour configurer l'environnement et exécuter le projet :

### 1. Cloner le dépôt
Cloner le projet localement :
git clone https://github.com/mounirfrhn/Premier-League-Simulation.git
cd Premier-League-Simulation

### 2. Créer un environnement virtuel
Créez un environnement virtuel pour isoler les dépendances :
python -m venv env

### 3. Activer l'environnement virtuel
Activez l'environnement virtuel :
Linux/Mac :
source env/bin/activate
Windows :
env\Scripts\activate

### 4. Installer les dépendances
Installez toutes les bibliothèques nécessaires à partir du fichier requirements.txt :
pip install -r requirements.txt
