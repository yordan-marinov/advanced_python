def invited_guests(n: int):
    invited_set = set(
        [input() for _ in range(n)]
    )
    return invited_set


def visited_guests():
    visited_set = set()
    while True:
        guest = input()
        if guest == "END":
            break
        visited_set.add(guest)
    return visited_set


def not_turn_up(num: int):
    return invited_guests(num) - visited_guests()


def print_statement(collection):
    print(len(collection))
    for i in sorted(collection):
        print(i)


reservation_number = int(input())

print_statement(not_turn_up(reservation_number))
