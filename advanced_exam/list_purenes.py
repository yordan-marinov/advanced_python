from collections import deque


def best_list_pureness(*args):
    def calculate_pureness(lst: deque):
        return sum((n * i) for i, n in enumerate(lst))

    def rotate_list(lst: deque):
        return lst.appendleft(lst.pop())

    current_list, rotations = args
    current_list = deque(current_list)

    max_pureness = None
    max_rotation = 0
    for rotation in range(rotations + 1):
        current_pureness = calculate_pureness(current_list)
        if max_pureness is None or current_pureness > max_pureness:
            max_pureness = current_pureness
            max_rotation = rotation
        rotate_list(current_list)

    return f"Best pureness {max_pureness} after {max_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
