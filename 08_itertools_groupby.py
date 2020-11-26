from itertools import groupby

items = [("car", "Ferrari"), ("car", "Renault"), ("country", "France"), ("country", "New Zealand"), ("fruit", "Kiwi")]

grouped_items = groupby(items, lambda x: x[0])

for category, group in grouped_items:

    print("=" * 30)
    print(f"{category.title()} Category")
    print("=" * 30)

    for item in group:
        print(f"{item[1]}")

    print()
