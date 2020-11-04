def numbers():
    return [int(i) for i in input().split()]


nums = numbers()


print(f"The minimum number is {min(nums)}")
print(f"The maximum number is {max(nums)}")
print(f"The sum number is: {sum(nums)}")
