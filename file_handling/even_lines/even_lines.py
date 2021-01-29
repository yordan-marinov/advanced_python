"""
Write a program that reads a text file and
prints on the console its even lines.
Line numbers start from 0.
Before you print the result replace
{"-", ",", ".", "!", "?"} with "@" and
reverse the order of the words.

======== This below is the correct output! ==========

fault@ his wasn't it but him@ judge to quick was @I
safer@ is It here@ hide @Quick@
"""


def is_line_even(num: int) -> bool:
    return num % 2 == 0


def replace_symbols(line: str, given_symbol: str, searched_symbols: set) -> str:
    for symbol in searched_symbols:
        if symbol in line:
            line = line.replace(symbol, given_symbol)
    return line


def reverse_line(line: list) -> str:
    return " ".join(line[::-1])


SYMBOLS_TO_REPLACE = {"-", ",", ".", "!", "?"}
SYMBOL_TO_REPLACE_WITH = "@"

with open("text.txt", "r+") as f:
    for line_index, file_line in enumerate(f):
        if is_line_even(line_index):
            replaced_symbols = replace_symbols(file_line, SYMBOL_TO_REPLACE_WITH, SYMBOLS_TO_REPLACE)
            print(reverse_line(replaced_symbols.split()))
