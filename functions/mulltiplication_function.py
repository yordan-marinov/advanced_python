def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result


print(multiply(2, 0, 1000, 5000))
