def odd_numbers(numbers: list) -> [int]:
    def is_odd(n):
        return n % 2 != 0

    return [n for n in numbers if is_odd(n)]


def even_numbers(numbers: list) -> [int]:
    def is_even(n):
        return n % 2 == 0

    return [n for n in numbers if is_even(n)]


def even_odd(*args):
    command = args[-1]
    commands = {
        "even": even_numbers,
        "odd": odd_numbers,
    }
    return commands[command](args[:-1])


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
