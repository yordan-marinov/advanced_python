# def even_only(num):
#     return num % 2 == 0
#
#
# def even_numbers():
#     return list(filter(even_only, map(int, input().split())))
#
#
# print(even_numbers())

def even_numbers_only(func):
    def is_even_number(n):
        return n % 2 == 0

    def inner(numbers):
        return [n for n in func(numbers) if is_even_number(n)]

    return inner


@even_numbers_only
def input_numbers(numbers):
    return numbers


numbers = [int(n) for n in input().split()]
print(input_numbers(numbers))
