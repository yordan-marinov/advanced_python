def enter_car(car_number, parking_lot):
    return parking_lot.add(car_number)


def leave_car(number, parking_lot):
    return parking_lot.remove(number)


def car_park(n: int):
    parking = set()
    for _ in range(n):
        direction, reg_number = input().split(", ")
        directions[direction](reg_number, parking)
    return parking


def print_statement(collection):
    if not collection:
        print("Parking Lot is Empty")
    for i in collection:
        print(i)


number_commands = int(input())

directions = {
    "IN": enter_car,
    "OUT": leave_car,
}

print_statement(car_park(number_commands))
