def even_numbers(function):
    def is_even(number):
        return number % 2 == 0

    def wrapper(numbers):
        function_result = function(numbers)
        return [n for n in function_result if is_even(n)]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))  # [2, 4]
