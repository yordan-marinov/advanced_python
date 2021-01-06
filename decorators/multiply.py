def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            function_result = function(*args, *kwargs)
            result = function_result * times
            return result
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))  # 39


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))  # 80
