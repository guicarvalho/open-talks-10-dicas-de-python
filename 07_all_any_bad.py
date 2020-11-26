players = [
    {"player": "Pelé", "nationality": "Brazilian", "number_goals": 1282},
    {"player": "Maradona", "nationality": "Argentine", "number_goals": 446},
    {"player": "Cruyff", "nationality": "Dutch", "number_goals": 392},
]

all_players_scored_more_than_400_goals = True

for player_info in players:
    if player_info["number_goals"] <= 400:
        all_players_scored_more_than_400_goals = False
        break

if all_players_scored_more_than_400_goals:
    print("Yes, all players scored more than 400 goals.")
else:
    print("No, some players did not score more than 400 goals.")
