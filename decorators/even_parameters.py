def even_parameters(fn):
    def is_even(*args):
        even_numbers = []
        for item in args:
            if not isinstance(item, int):
                break
            if item % 2 == 0:
                even_numbers.append(item)

        return len(args) == len(even_numbers)

    def wrapper(*args):
        if not is_even(*args):
            return "Please use only even numbers!"

        return fn(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))  # 6
print(add("Peter", 1))  # Please use only even numbers!


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))  # 384
print(multiply(2, 4, 9, 8))  # Please use only even numbers!
