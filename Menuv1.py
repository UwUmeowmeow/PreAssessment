# Define a list of meal combos with their corresponding items and prices
meal_combos = [
    ["value", ["beef burger", 5.69], ["Fries", 1.00], ["Fizzy drink", 1.00]],
    ["Cheezy", ["Cheeseburger", 6.69], ["Fries", 1.00], ["Fizzy drink", 1.00]],
    ["Super", ["Cheeseburger", 6.69], ["Large Fries", 2.00], ["Smoothie", 2.00]]
]

# Loop through each combo in the list
for combo in meal_combos:
    # Print the name of the combo
    print(f"Combo Name: {combo[0]}")
    # Loop through each item in the combo (starting at the second element)
    for food_item in combo[1:]:
        # Print the name of the item and its price
        print(f"{food_item[0]} : {food_item[1]}")
