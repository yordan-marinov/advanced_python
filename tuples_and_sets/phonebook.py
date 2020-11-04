from collections import defaultdict


def adding_to_phonebook():
    phone_book = defaultdict(str)
    while True:
        token = input().split("-")
        if token[0].isdigit():
            n = int(token[0])
            break
        phone_book[token[0]] = token[1]
    return n, phone_book


def print_searching_names(num: int):
    for _ in range(num):
        name = input()
        if name not in phonebook:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phonebook[name]}")


search_number, phonebook = adding_to_phonebook()
print_searching_names(search_number)
