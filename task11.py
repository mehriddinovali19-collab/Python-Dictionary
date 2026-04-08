config = {}

for i in range(3):
    key = input(f" {i+1} - setting uchun kalitni kiriting: ")
    value = input(f" {i+1} - qitmatni kiriting: ")
    config[key] = value

print(config)