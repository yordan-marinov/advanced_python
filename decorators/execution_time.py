from time import perf_counter


def exec_time(fn):
    def wrapper(*args):
        start_function_time = perf_counter()
        fn(*args)
        end_function_time = perf_counter()

        return end_function_time - start_function_time

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
