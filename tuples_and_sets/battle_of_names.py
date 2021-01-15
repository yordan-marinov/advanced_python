def ascii_values_form_string(string: str, divisor: int) -> int:
    result = 0
    for letter in string:
        result += ord(letter)

    return result // divisor


def even_odd_sets(n: int) -> tuple:
    even_set = set()
    odd_set = set()
    for line_number in range(1, n + 1):
        name = input()
        ascii_value = ascii_values_form_string(name, line_number)

        if ascii_value % 2 == 0:
            even_set.add(ascii_value)
        else:
            odd_set.add(ascii_value)

    return even_set, odd_set


def battle_of_names(n: int):
    even_numbers_set, odd_numbers_set = even_odd_sets(n)
    if sum(even_numbers_set) == sum(odd_numbers_set):
        return f'{", ".join(str(e) for e in odd_numbers_set.union(even_numbers_set))}'

    elif sum(odd_numbers_set) > sum(even_numbers_set):
        return f'{", ".join(str(e) for e in odd_numbers_set.difference(even_numbers_set))}'

    else:
        return f'{", ".join(str(e) for e in odd_numbers_set.symmetric_difference(even_numbers_set))}'


count_people = int(input())
print(battle_of_names(count_people))
