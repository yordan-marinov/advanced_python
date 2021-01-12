# numbers = input().split()
#
# reversed_stack = []
# for _ in range(len(numbers)):
#     num = numbers.pop()
#     reversed_stack.append(num)
#
#
# print(" ".join(reversed_stack))


def reverse_numbers(numbers: list):
    if not numbers:
        return numbers

    return reverse_numbers(numbers[1:]) + numbers[:1]


print(*reverse_numbers(input().split()))
