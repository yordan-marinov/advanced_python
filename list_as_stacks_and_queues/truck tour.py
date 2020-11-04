"""
Suppose there is a circle.
There are N petrol pumps on that circle.
Petrol pumps are numbered 0 to (N−1) (both inclusive).
You have two pieces of information corresponding to each of the petrol pump:
(1) the amount of petrol that petrol pump will give, and
(2) the distance from that petrol pump to the next petrol pump (kilometers).
Initially, you have a tank of infinite capacity carrying no petrol.
You can start the tour at any of the petrol pumps.
Calculate the first point from where the truck will be able to complete the circle.
Consider that the truck will stop at each of the petrol pumps.
The truck will move one kilometer for each liter of the petrol.

"""
from collections import deque

count_pumps = int(input())

pumps = deque(
    [
        [int(i) for i in input().split()]
        for _ in range(count_pumps)
    ]
)


for pump in range(count_pumps):

    is_valid = True
    fuel = 0
    for _ in range(count_pumps):
        current = pumps.popleft()
        fuel += current[0] - current[1]

        if fuel < 0:
            is_valid = False

        pumps.append(current)

    if is_valid:
        print(pump)
        break

    pumps.append(pumps.popleft())
