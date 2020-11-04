def multiply_numbers(num1, num2):
    return num1 * num2


def sum_numbers(num1, num2):
    return num1 + num2


def func_executor(*args):
    sum_pair = args[0][1]
    multiply_pair = args[1][1]
    return [
        sum_numbers(*sum_pair),
        multiply_numbers(*multiply_pair),
    ]


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))