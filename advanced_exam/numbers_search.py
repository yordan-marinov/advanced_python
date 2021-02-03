def numbers_searching(*args):

    full_sequence = [n for n in range(min(args), max(args) + 1)]
    duplicates = list(set(n for n in args if args.count(n) > 1))
    missing_nums = [n for n in full_sequence if n not in args]

    return [*missing_nums, sorted(duplicates)]


print(numbers_searching(1, 2, 4, 2, 5, 4, 7))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
