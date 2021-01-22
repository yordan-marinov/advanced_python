heroes = {name: {} for name in input().split(", ")}

while True:
    data = input()
    if data == "End":
        break

    name, item, value = data.split("-")
    value = int(value)
    if item not in heroes[name]:
        heroes[name][item] = value

[print(f"{key} -> Items: {len(heroes[key])}, Cost: {sum(heroes[key].values())}") for key in heroes]
