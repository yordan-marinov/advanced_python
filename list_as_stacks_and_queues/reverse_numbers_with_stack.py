numbers = input().split()

reversed_stack = []
for _ in range(len(numbers)):
    num = numbers.pop()
    reversed_stack.append(num)


print(" ".join(reversed_stack))
