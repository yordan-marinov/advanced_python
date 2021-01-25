# def numbers():
#     return [int(i) for i in input().split()]
#
#
# nums = numbers()
#
#
# print(f"The minimum number is {min(nums)}")
# print(f"The maximum number is {max(nums)}")
# print(f"The sum number is: {sum(nums)}")
def min_max_and_sum_of_numbers():
    numbers = [int(n) for n in input().split()]
    return f"""The minimum number is {min(numbers)}
The maximum number is {max(numbers)}
The sum number is: {sum(numbers)}
"""


print(min_max_and_sum_of_numbers())
