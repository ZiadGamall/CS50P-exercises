# Nutrition Facts — Outputs the calorie count for a given fruit based on FDA data.

fruits = {"apple":130, "avocado":150, "banana": 110, "cherry":100}
item = input("Item: ").strip().lower()
calories = fruits.get(item)

if calories:
    print(f"Calories: {calories}")

