players = [
    {"player": "Pelé", "nationality": "Brazilian", "number_goals": 1282},
    {"player": "Maradona", "nationality": "Argentine", "number_goals": 446},
    {"player": "Cruyff", "nationality": "Dutch", "number_goals": 392},
]

verify_using_all_func = all([player_info["number_goals"] > 400 for player_info in players])
verify_using_any_func = any([player_info["number_goals"] <= 400 for player_info in players])

print(f"All: {verify_using_all_func}")
print(f"Any: {verify_using_any_func}")
