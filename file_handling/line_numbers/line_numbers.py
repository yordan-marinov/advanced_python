from string import punctuation
from string import ascii_letters
from collections import Counter

LETTERS = ascii_letters
PUNCTUATIONS = punctuation


def modify_line(string, line_number, letters, punctuations):
    def count_letters_and_punctuations() -> str:
        letters_count = sum(Counter(letter for letter in string if letter in letters).values())
        punctuations_count = sum(Counter(symbol for symbol in string if symbol in punctuations).values())

        return f" ({letters_count})({punctuations_count})"

    def count_lines() -> str:
        return f"Line {line_number}: "

    return count_lines() + string + count_letters_and_punctuations() + "\n"


with open("text.txt", "r") as rf:
    with open("text_copy.txt", "w") as wf:
        for line_index, line in enumerate(rf, 1):
            final_line = modify_line(line.rstrip(), line_index, LETTERS, PUNCTUATIONS)
            wf.write(final_line)
