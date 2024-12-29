import pandas as pd
import requests
import os

api_key = "dc0d9b5d1bmshdf521e95eed7ecbp153cb0jsn2db0c659e7b6"

# Récupérer les meilleurs attaquants de la Premier League
def get_top_players(premier_league_id, season_id="61627"):
    url = "https://sofascore.p.rapidapi.com/tournaments/get-top-players"
    querystring = {"tournamentId": premier_league_id, "seasonId": season_id}
    headers = {
        "x-rapidapi-key": api_key,  # Remplacez par votre clé RapidAPI
        "x-rapidapi-host": "sofascore.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    players = data['topPlayers']['rating']
    
    # Trier les joueurs par note moyenne (rating) et ne sélectionner que les attaquants (position = 'F')
    top_10_players = sorted(players, key=lambda x: x['statistics']['rating'], reverse=True)
    top_10_premier_league = [
        {
            "name": player['player']['name'],
            "rating": player['statistics']['rating'],
            "appearances": player['statistics']['appearances'],
            "team": player['team']['name'],
            "position": player['player']['position'],
            "id": player['player']['id']
        }
        for player in top_10_players if player['player']['position'] == 'F'
    ][:10]
    return top_10_premier_league

# Fonction pour récupérer les statistiques d'un joueur pour un match donné
def get_stats_player(player_id, match_id):
    url = "https://sofascore.p.rapidapi.com/matches/get-player-statistics"
    querystring = {"matchId": match_id, "playerId": player_id}
    headers = {
        "x-rapidapi-key": api_key,  # Remplacez par votre clé RapidAPI
        "x-rapidapi-host": "sofascore.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        player_info = data.get('player', {})
        player_stats = data.get('statistics', {})

        stats = []
        if player_info and player_stats:
            player_name = player_info.get('name', 'N/A')
            goals = player_stats.get('goals', 0)
            goal_assists = player_stats.get('goalAssist', 0)
            shots_on_target = player_stats.get('onTargetScoringAttempt', 0)
            shots_off_target = player_stats.get('shotOffTarget', 0)
            big_chance_created = player_stats.get('bigChanceCreated', 0)
            big_chance_missed = player_stats.get('bigChanceMissed', 0)
            key_passes = player_stats.get('keyPass', 0)
            touches = player_stats.get('touches', 0)
            duels_won = player_stats.get('duelWon', 0)
            duels_lost = player_stats.get('duelLost', 0)
            expected_goals = player_stats.get('expectedGoals', 0)
            expected_assists = player_stats.get('expectedAssists', 0)

            game_stats = [
                player_name, goals, goal_assists, shots_on_target, shots_off_target,
                big_chance_created, big_chance_missed, key_passes, touches,
                duels_won, duels_lost, expected_goals, expected_assists
            ]
            stats.append(game_stats)
        return stats
    else:
        print(f"Erreur: Impossible de récupérer les statistiques, code de statut {response.status_code}")
        return []

# Fonction pour récupérer les notes des derniers matchs d'un joueur
def get_ratings_player(player_id):
    url = "https://sofascore.p.rapidapi.com/players/get-last-ratings"
    querystring = {"playerId": player_id, "tournamentId": "17", "seasonId": "61627"}
    headers = {
        "x-rapidapi-key": api_key,  # Remplacez par votre clé RapidAPI
        "x-rapidapi-host": "sofascore.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    last_ratings = data.get('lastRatings', [])
    five_last_games = []
    if last_ratings:
        for rating_data in last_ratings[:5]:
            match = rating_data.get('event', {})
            home_team = match.get('homeTeam', {}).get('name', 'N/A')
            away_team = match.get('awayTeam', {}).get('name', 'N/A')
            rating = rating_data.get('rating', 'N/A')
            home_score = match.get('homeScore', {}).get('current', 'N/A')
            away_score = match.get('awayScore', {}).get('current', 'N/A')
            match_id = match.get('id', 'N/A')
            game = [match_id, home_team, away_team, home_score, away_score, rating]
            five_last_games.append(game)
    else:
        print("No ratings found.")
    return five_last_games

# Fonction principale pour générer un DataFrame des statistiques des joueurs
def generate_player_stats_dataframe(player_id):
    last_games = get_ratings_player(player_id)
    player_stats_list = []

    for game in last_games:
        match_id, home_team, away_team, home_score, away_score, rating = game
        stats = get_stats_player(player_id, match_id)

        if stats:
            (player_name, goals, assists, shots_on_target, shots_off_target,
             big_chance_created, big_chance_missed, key_passes, touches,
             duels_won, duels_lost, expected_goals, expected_assists) = stats[0]

            player_stats_list.append({
                "Match ID": match_id,
                "Home Team": home_team,
                "Away Team": away_team,
                "Home Score": home_score,
                "Away Score": away_score,
                "Player Rating": rating,
                "Goals": goals,
                "Assists": assists,
                "Shots on Target": shots_on_target,
                "Shots off Target": shots_off_target,
                "Big Chances Created": big_chance_created,
                "Big Chances Missed": big_chance_missed,
                "Key Passes": key_passes,
                "Touches": touches,
                "Duels Won": duels_won,
                "Duels Lost": duels_lost,
                "xG": expected_goals,
                "xA": expected_assists
            })
    return pd.DataFrame(player_stats_list)

# ID de la Premier League (à spécifier si nécessaire)
premier_league_id = "17"

# Obtenir les 10 meilleurs attaquants
top_10_premier_league = get_top_players(premier_league_id)

# Génération des fichiers CSV pour les 10 meilleurs attaquants
output_path_root = '/home/onyxia/work/Premier-League-Simulation/src/data/descriptive_data'

for player in top_10_premier_league:
    player_id = player["id"]
    stats_df = generate_player_stats_dataframe(player_id)
    file_name = f"statsheet_{player['name'].replace(' ', '_')}.csv"
    file_path = os.path.join(output_path_root, file_name)
    stats_df.to_csv(file_path, index=False)
    print(f"Fichier {file_name} exporté avec succès.")
