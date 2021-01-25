# def sort():
#     return sorted([int(i) for i in input().split()])
#
#
# print(sort())

def sort_numbers_increasing(func):
    def inner(numbers):
        return sorted(func(numbers))

    return inner


@sort_numbers_increasing
def input_numbers(numbers):
    return numbers


numbers = [int(n) for n in input().split()]
print(input_numbers(numbers))
