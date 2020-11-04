n = int(input())

stack = []

for _ in range(n):
    token = input().split()
    command = int(token[0])

    if command == 1:
        stack.append(int(token[1]))

    if stack:
        if command == 2:
            stack.pop()

        elif command == 3:
            print(max(stack))

        elif command == 4:
            print(min(stack))


print(", ".join([str(i) for i in reversed(stack)]))
