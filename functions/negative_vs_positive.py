def negative_positive_pair(lst: list):
    return [
        [n for n in lst if n < 0],
        [n for n in lst if n > 0],
    ]


numbers = [int(i) for i in input().split()]

negative = sum(negative_positive_pair(numbers)[0])
positive = sum(negative_positive_pair(numbers)[1])

print(negative)
print(positive)

if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than negatives")
