class store_results:
    def __init__(self, fn):
        self._fn = fn

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as file:
            file.write(
                f"Function '{self._fn.__name__}' was called. "
                f"Result: {self._fn(*args, **kwargs)}\n"
            )


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)  # Function 'add' was called. Result: 4
mult(6, 4)  # Function 'mult' was called. Result: 24
