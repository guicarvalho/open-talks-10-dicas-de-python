players = ["Pelé", "Maradona", "Cruyff"]
nationalities = ["Brazilian", "Argentine", "Dutch"]
goals = ["1282", "446", "392"]

for player, nationality, number_goals in zip(players, nationalities, goals):
    print(f"{player} is {nationality} and has scored {number_goals} in his career.")
