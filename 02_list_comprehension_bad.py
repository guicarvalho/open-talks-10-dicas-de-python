numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pair_numbers = []

for number in numbers:
    if number % 2 == 0:
        pair_numbers.append(number)

print(pair_numbers)
