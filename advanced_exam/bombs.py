from collections import deque


bomb_effects = deque([int(i) for i in input().split(", ")])
bomb_casings = deque([int(i) for i in input().split(", ")])

bombs = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

bombs_counter = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0,
}

is_pouch = False
while len(bomb_effects) > 0 and len(bomb_casings) > 0:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()

    if not effect + casing in bombs:
        bomb_effects.appendleft(effect)
        casing -= 5
        bomb_casings.append(casing)
        continue

    bombs_counter[bombs[effect + casing]] += 1

    if len([e for e in bombs_counter.values() if e >= 3]) == 3:
        is_pouch = True
        break

if is_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(n) for n in bomb_effects)}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(n) for n in bomb_casings)}")

for k, v in sorted(bombs_counter.items()):
    print(f"{k}: {v}")
