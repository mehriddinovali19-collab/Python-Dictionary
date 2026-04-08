inventory = {"apple": 10,
              "banana": 20,
                "orange": 15
}
input_key = input("Enter a fruit name: ")
if input_key not in inventory:
    inventory[input_key] = 0

print(inventory)