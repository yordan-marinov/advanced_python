def logged(fn):
    def wrapper(*args):
        name_function = f"you called {fn.__name__}{args}\n"
        result_function = f"it returned {fn(*args)}"
        return name_function + result_function

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
