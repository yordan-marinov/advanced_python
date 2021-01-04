def reverse_text(string: str):
    for character in string[::-1]:
        yield character


for char in reverse_text("step"):
    print(char, end="")
