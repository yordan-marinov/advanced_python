def cache(func):
    def wrapper(digit):
        result_func = func(digit)
        wrapper.log[digit] = result_func
        return result_func
    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)  # {1: 1, 0: 0, 2: 1, 3: 2}

fibonacci(4)
print(fibonacci.log)  # {1: 1, 0: 0, 2: 1, 3: 2, 4: 3}
