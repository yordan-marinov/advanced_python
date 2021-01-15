def set_constructor(start, end):
    return {n for n in range(start, end + 1)}


def split_pair_of_sets(lst: list):
    all_elements = []
    for element in lst:
        (start, end) = [int(e) for e in element.split(",")]
        all_elements.append((start, end))

    return all_elements


def longest_intersection(n):
    max_intersection = []
    for _ in range(n):
        token = input().split("-")
        data = split_pair_of_sets(token)

        set_1 = set_constructor(data[0][0], data[0][1])
        set_2 = set_constructor(data[1][0], data[1][1])

        current_intersection = set_1.intersection(set_2)

        if len(current_intersection) > len(max_intersection):
            max_intersection = current_intersection

    return (
        f"Longest intersection is {list(max_intersection)} "
        f"with length {len(max_intersection)}"
    )


print(longest_intersection(int(input())))
