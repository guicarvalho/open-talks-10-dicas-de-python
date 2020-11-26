from itertools import permutations

numbers = [1, 2, 3]

print(len(list((permutations(numbers)))))

for i in permutations(numbers):
    print(f"{i}")
