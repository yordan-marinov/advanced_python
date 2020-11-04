from collections import defaultdict

count_values = defaultdict(int)
values = [float(n) for n in input().split()]

for value in values:
    count_values[value] += 1

for key, value in count_values.items():
    print(f"{key} - {value} times")
