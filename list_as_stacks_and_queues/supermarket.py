from collections import deque

people = deque()

while True:
    command = input()
    if command == "Paid":
        while len(people) > 0:
            print(people.popleft())

    elif command == "End":
        break

    else:
        name = command
        people.append(name)


print(f"{len(people)} people remaining.")
