players = ["Pelé", "Maradona", "Cruyff"]
nationalities = ["Brazilian", "Argentine", "Dutch"]
goals = ["1282", "446", "392"]

for index, player in enumerate(players):
    nationality = nationalities[index]
    number_goals = goals[index]

    print(f"{player} is {nationality} and has scored {number_goals} in his career.")
