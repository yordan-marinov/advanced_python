# expression = input()
# stack = []
#
# for char in expression:
#     if char == "(":
#         stack.append("")
#
#     for i in range(len(stack)):
#         stack[i] += char
#
#     if char == ")":
#         sub_expression = stack.pop()
#         print(sub_expression)

expression = input()
stack = []

for index, char in enumerate(expression):
    if char == "(":
        stack.append(index)
    elif char == ")":
        start_index = stack.pop()
        end_index = index
        print(expression[start_index: end_index + 1])
