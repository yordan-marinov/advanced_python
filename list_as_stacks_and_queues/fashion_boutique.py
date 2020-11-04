""""
You own a fashion boutique and you receive a delivery once a month in a huge box,
which is full of clothes.
You must arrange them in your store, so you take the box and
start from the last piece of clothing
on the top of the pile to the first one at the bottom.
Use a stack for the purpose.
Each piece of clothing has its value (an integer).
You must sum their values, while you take them out of the box.
You will be given an integer representing the capacity of a rack.
While the sum of the clothes is less than the capacity, keep summing them.
If the sum becomes equal to the capacity you must take a new rack for the next clothes,
if there are any left in the box.
If it becomes greater than the capacity,
don't add the piece of clothing to the current rack and take a new one.
In the end,
print how many racks you have used to hang must the clothes.

"""

clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack = 0
rack_numbers = 0

while len(clothes) > 0:
    current_clothe = clothes.pop()
    current_rack += current_clothe

    if current_rack == rack_capacity:
        rack_numbers += 1
        current_rack = 0

    elif current_rack > rack_capacity:
        rack_numbers += 1
        clothes.append(current_clothe)
        current_rack = 0

    elif current_rack < rack_capacity and not clothes:
        rack_numbers += 1

print(rack_numbers)
