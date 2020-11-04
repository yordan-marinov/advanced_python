from collections import deque

food_quantity = int(input())

queue = deque([int(i) for i in input().split()])

print(max(queue))

while queue:
    current = queue.popleft()
    if food_quantity >= current:
        food_quantity -= current

    else:
        queue.appendleft(current)
        break

if any([x for x in queue]):
    print(f"Orders left: {' '.join([str(i) for i in queue])}")
else:
    print("Orders complete")
