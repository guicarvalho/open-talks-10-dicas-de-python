numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# like filter
pair_numbers = [number for number in numbers if number % 2 == 0]
print(pair_numbers)

# like map
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# remove duplicated
numbers = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9]
print(set(numbers))

# nested comprehensions
matrix_3_x_3 = [[i for j in range(3)] for i in range(3)]
print(matrix_3_x_3)
"""
for i in range(3):
    matrix_3_x_3.append([])

    for j in range(3):
        matrix_3_x_3[i].append(j)

print(matrix_3_x_3)
"""
