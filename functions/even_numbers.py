# def even_numbers(lst: list):
#     return [n for n in lst if n % 2 == 0]
#
#
# numbers = list(map(int, input().split()))
#
# print(even_numbers(numbers))

even_nums = list(filter(
    lambda x: x % 2 == 0, map(int, input().split())
))

print(even_nums)
