def find_cycles(dd: dict, searched_index: int) -> int:
    cycles = 0
    for index, number in sorted(dd.items(), key=lambda x: x[1]):
        cycles += number
        if index == searched_index:
            return cycles


indexes_numbers_dict = {index: int(number) for index, number in enumerate(input().split(", "))}
task_index = int(input())

print(find_cycles(indexes_numbers_dict, task_index))
