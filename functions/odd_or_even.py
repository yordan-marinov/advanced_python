def odd_numbers(numbers: list) -> [int]:
    def is_odd(n):
        return n % 2 != 0

    return [n for n in numbers if is_odd(n)]


def even_number(numbers: list) -> [int]:
    def is_even(n):
        return n % 2 == 0

    return [n for n in numbers if is_even(n)]


def odd_or_even(command, numbers: list) -> int:
    commands = {
        "Odd": odd_numbers,
        "Even": even_number,
    }
    return sum(commands[command](numbers)) * len(numbers)


command = input()
numbers = [int(i) for i in input().split()]

print(odd_or_even(command, numbers))
