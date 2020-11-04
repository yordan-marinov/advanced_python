def rounding_numbers(lst: list):
    return [round(i) for i in lst]


numbers = [float(n) for n in input().split()]

print(rounding_numbers(numbers))
