first, second = ("apple", "orange")
print(f"{first}, {second}")

first, second, *others = ("apple", "orange", "lemon", "pineapple")
print(f"{first}, {second}, {others}")

first, second, *_ = ("apple", "orange", "lemon", "pineapple")
print(f"{first}, {second}")

first, *_, last = ("apple", "orange", "lemon", "pineapple")
print(f"{first}, {last}")
