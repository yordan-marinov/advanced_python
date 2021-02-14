from collections import deque

fireworks_effect = deque(int(n) for n in input().split(", "))
explosive_power = deque(int(n) for n in input().split(", ")[::-1])

Palm_Fireworks = 0
Willow_Fireworks = 0
Crossette_Fireworks = 0

is_full = False

while fireworks_effect and explosive_power:

    f_effect = fireworks_effect.popleft()
    if f_effect <= 0:
        continue
    e_power = explosive_power.popleft()
    if e_power <= 0:
        fireworks_effect.appendleft(f_effect)
        continue

    value = (f_effect + e_power)

    if value % 15 == 0:
        Crossette_Fireworks += 1

    elif value % 3 == 0:
        Palm_Fireworks += 1

    elif value % 5 == 0:
        Willow_Fireworks += 1

    else:
        fireworks_effect.append(f_effect - 1)
        explosive_power.appendleft(e_power)
        # continue

    if (Palm_Fireworks >= 3) and (Willow_Fireworks >= 3) and (Crossette_Fireworks >= 3):
        is_full = True
        break

if is_full:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
    if fireworks_effect:
        print(f"Firework Effects left: {', '.join(map(str, fireworks_effect))}")
    if explosive_power:
        print(f"Explosive Power left: {', '.join(map(str, reversed(explosive_power)))}")

print(f"Palm Fireworks: {Palm_Fireworks}")
print(f"Willow Fireworks: {Willow_Fireworks}")
print(f"Crossette Fireworks: {Crossette_Fireworks}")
