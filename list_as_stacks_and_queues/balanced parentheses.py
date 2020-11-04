"""
Given a sequence consisting of parentheses,
determine whether the expression is balanced.
A sequence of parentheses is balanced
if every open parenthesis can be paired uniquely with a closed parenthesis
that occurs after the former.
Also, the interval between them must be balanced.
You will be given three types of parentheses:
(, {, and [.

{[()]} - This is a balanced parenthesis.
{[(])} - This is not a balanced parenthesis.
"""

brackets = input()

stack = []
for bracket in brackets:
    if bracket in ["(", "[", "{"]:
        stack.append(bracket)
        continue

    is_balanced = stack and (
        (bracket == ")" and stack[-1] == "(") or
        (bracket == "]" and stack[-1] == "[") or
        (bracket == "}" and stack[-1] == "{")
    )

    if is_balanced:
        stack.pop()
    else:
        break

if is_balanced:
    print("YES")
else:
    print("NO")
 