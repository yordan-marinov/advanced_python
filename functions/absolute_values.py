def absolute_values(lst: list):
    return [abs(i) for i in lst]


numbers = [float(n) for n in input().split()]

print(absolute_values(numbers))
