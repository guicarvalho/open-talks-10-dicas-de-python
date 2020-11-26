def add(x, y):
    return x + y


add_2 = lambda x, y: x + y  # noqa

print(add(2, 2))
print(add_2(2, 2))


players = ["Pelé", "Maradona", "Cruyff"]
print(sorted(players))


def order_by_nationality(player_info):
    return player_info[1]


players = [("Pelé", "Brazilian"), ("Maradona", "Argentine"), ("Cruyff", "Dutch")]
print(sorted(players, key=order_by_nationality))

players = [("Pelé", "Brazilian"), ("Maradona", "Argentine"), ("Cruyff", "Dutch")]
print(sorted(players, key=order_by_nationality))
