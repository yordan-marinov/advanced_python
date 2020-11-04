start = int(input())
end = int(input())

result = [
    number
    for number in range(start, end + 1)
    if any([number % j == 0 for j in range(2, 11)])
]


print(result)
