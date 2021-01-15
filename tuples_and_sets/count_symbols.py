# from collections import defaultdict
#
#
# def count_symbols(text):
#     symbols_count = defaultdict(int)
#     for char in text:
#         symbols_count[char] += 1
#     return symbols_count
#
#
# def print_statement(collection: dict):
#     for key, value in sorted(collection.items()):
#         print(f"{key}: {value} time/s")
#
#
# t = input()
# print_statement(count_symbols(t))
#
#===================================================

from collections import defaultdict


def count_symbols(text: str) -> str:
    def sort_symbols_alphabetical(dct: dict):
        return sorted(dct.items(), key=lambda pair: pair[0])

    def printing_line(elements):
        return f"{elements[0]}: {elements[1]} time/s"

    symbols = defaultdict(int)
    for symbol in text:
        symbols[symbol] += 1

    return "\n".join(
        printing_line(e)
        for e in sort_symbols_alphabetical(symbols)
    )


string = input()
print(count_symbols(string))
