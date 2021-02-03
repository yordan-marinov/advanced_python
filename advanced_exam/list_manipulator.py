def adding(nums, *args):
    position, *numbers = args
    if position == "end":
        return nums + numbers
    return numbers + nums


def removing(nums, *args):
    position, *number = args
    if position == "end":
        if number:
            return nums[:-int(*number)]
        return nums[:-1]
    elif position == "beginning":
        if number:
            return nums[int(*number):]
        return nums[1:]


def list_manipulator(*args):
    numbers, command, *elements = args
    commands = {"add": adding, "remove": removing}
    return commands[command](numbers, *elements)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
