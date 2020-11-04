from collections import defaultdict


def count_symbols(text):
    symbols_count = defaultdict(int)
    for char in text:
        symbols_count[char] += 1
    return symbols_count


def print_statement(collection: dict):
    for key, value in sorted(collection.items()):
        print(f"{key}: {value} time/s")


t = input()
print_statement(count_symbols(t))
