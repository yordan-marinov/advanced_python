from collections import deque, defaultdict


def counts_bombs_of_each_type(lst):
    return [n for n in lst if n >= 3]


BOMBS = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs",
}
bombs_counter = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}

bomb_effects = deque([int(n) for n in input().split(", ")])
bomb_casings = deque([int(n) for n in input().split(", ")][::-1])

is_pouch_full = False
while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.popleft()
    current_value = current_effect + current_casing
    if current_value not in BOMBS:
        bomb_effects.appendleft(current_effect)
        bomb_casings.appendleft(current_casing - 5)
        continue

    bombs_counter[BOMBS[current_value]] += 1

    if len(counts_bombs_of_each_type(bombs_counter.values())) == len(bombs_counter):
        is_pouch_full = True
        break

if not is_pouch_full:
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print(f"Bene! You have successfully filled the bomb pouch!")
if not bomb_effects:
    print(f"Bomb Effects: {'empty'}")
else:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
if not bomb_casings:
    print(f"Bomb Casings: {'empty'}")
else:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")

for bomb, count in sorted(bombs_counter.items()):
    print(f"{bomb}: {count}")
