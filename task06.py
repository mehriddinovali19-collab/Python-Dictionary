key = input("Enter a key: ")
car = {"brand": "Chevrolet", "model": "Cobalt", "color": "white"}
if key in car:
    print(car[key])
else:
    print("Key not found")