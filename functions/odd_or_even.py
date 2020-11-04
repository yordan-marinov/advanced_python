def odd_numbers(lst: list):
    return [n for n in lst if n % 2 != 0]


def even_number(lst: list):
    return [n for n in lst if n % 2 == 0]


def odd_or_even_command(commander, lst: list):
    result = {
        "Odd": odd_numbers,
        "Even": even_number,
    }
    return sum(result[commander](lst)) * len(nums)


command = input()
nums = [int(i) for i in input().split()]

print(odd_or_even_command(command, nums))
