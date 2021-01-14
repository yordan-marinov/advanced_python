# def enter_car(car_number, parking_lot):
#     return parking_lot.add(car_number)
#
#
# def leave_car(number, parking_lot):
#     return parking_lot.remove(number)
#
#
# def car_park(n: int):
#     parking = set()
#     for _ in range(n):
#         direction, reg_number = input().split(", ")
#         directions[direction](reg_number, parking)
#     return parking
#
#
# def print_statement(collection):
#     if not collection:
#         print("Parking Lot is Empty")
#     for i in collection:
#         print(i)
#
#
# number_commands = int(input())
#
# directions = {
#     "IN": enter_car,
#     "OUT": leave_car,
# }
#
# print_statement(car_park(number_commands))
#
# =============================================================

def parking_lot(count_cars):
    def register_car(reg_number):
        parking.add(reg_number)

    def unregister_car(reg_number):
        if reg_number in parking:
            parking.remove(reg_number)

    commands = {"IN": register_car, "OUT": unregister_car, }
    parking = set()

    for _ in range(count_cars):
        command, reg_num = input().split(", ")
        commands[command](reg_num)

    if parking:
        return "\n".join(parking)
    return "Parking Lot is Empty"


print(parking_lot(int(input())))
