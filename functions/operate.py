from functools import reduce


# def sumic(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
#
# def subtract(*args):
#     result = args[0]
#     for i in args[1:]:
#         result -= i
#     return result
#
#
# def multiply(*args):
#     result = args[0]
#     for i in args[1:]:
#         result *= i
#     return result
#
#
# def divide(*args):
#     result = args[0]
#     for i in args[1:]:
#         result /= i
#     return result
#
#
# def operate(operator, *args):
#     operators = {
#         "+": sumic,
#         "-": subtract,
#         "*": multiply,
#         "/": divide,
#     }
#     return operators[operator](*args)
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))


def operate(operator, *args):
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: a / b,
        "*": lambda a, b: a * b,
    }

    return reduce(operations[operator], args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
