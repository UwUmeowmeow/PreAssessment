import easygui as eg
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


msg_ = "Enter combo info"
fields_ = ["Enter combo name",
            "Enter item 1 name", "Enter item 1 price",
              "Enter item 2 name", "Enter item 2 price",
                "Enter item 3 name", "Enter item 3 price"]
info = eg.multenterbox(msg=msg_, fields=fields_)
print(info)
info_dictionary = {}
for i in range(1, len(info), 2):
    info_dictionary[info[i]] = info[i + 1]
print(f"Combo name: {info[0]}")

print(info_dictionary)
combos[info[0]] = info_dictionary
print(combos)