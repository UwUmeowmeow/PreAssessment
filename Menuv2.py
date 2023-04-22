
combos = {
    "Value": {
        "Beef burger": 5.69, 
        "Fries": 1.00,
        "Fizzy drink" : 1.00
    },
    "Cheezy": {
        "Cheeseburger": 6.69,
        "Fries": 1.00,
        "Fizzy drink": 1.00
    },
        "Super": {
        "Cheeseburger": 6.69,
        "Large Fries": 2.00,
        "Smoothie": 2.00
        }
}
for combo_name, combo_items in combos.items():
    print(f"Combo Name: {combo_name}")
    for food_item, price in combo_items.items():
        print(f"{food_item}: {price}")