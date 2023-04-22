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


def combo_button():
    global combos
    all_combos = []
    for item in combos:
        all_combos.append(item)

    return all_combos




choices_ = combo_button()
msg_ = "What combo do you want to edit"
combo_name = eg.buttonbox(title="Editing", msg= msg_, choices=choices_)
combo_dictionary = combos[combo_name]
print(combo_dictionary)
enterlist = [combo_name]
for item in combo_dictionary:
    print(item)
    print(combo_dictionary[item])
    enterlist.append(item)
    enterlist.append(f"{combo_dictionary[item]:.2f}")
    

msg_ = "Edit combo info"
fields_ = ["Enter combo name",
            "Enter item 1 name", "Enter item 1 price",
              "Enter item 2 name", "Enter item 2 price",
                "Enter item 3 name", "Enter item 3 price"]
eg.multenterbox(msg=msg_, fields=fields_, values= enterlist)



