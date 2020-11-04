from collections import deque

liters_in_dispenser = int(input())
people = deque()

while True:
    command = input()
    if command == "Start":
        break
    else:
        people.append(command)


while True:
    commands = input()
    if commands == "End":
        break

    if commands.isdigit():
        name = people.popleft()
        if int(commands) <= liters_in_dispenser:
            liters_in_dispenser -= int(commands)
            print(f"{name} got water")
        else:
            print(f"{name} must wait")

    elif commands.startswith("refill "):
        liters_to_refill = int(commands.split()[-1])
        liters_in_dispenser += liters_to_refill

print(f"{liters_in_dispenser} liters left")
