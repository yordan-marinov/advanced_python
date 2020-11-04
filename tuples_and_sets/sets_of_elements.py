def adding_to_set(number_length: int):
    result = set(
        [input() for _ in range(number_length)]
    )
    return result


def sets_of_elements():
    return adding_to_set(first_set_len).\
        intersection(adding_to_set(second_set_len))


first_set_len, second_set_len = tuple(map(int, input().split()))

print("\n".join([str(x) for x in sets_of_elements()]))
