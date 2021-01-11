s = list(input())


stack = []
while len(s) > 0:
    stack.append(s.pop())

print(*stack, sep='')
