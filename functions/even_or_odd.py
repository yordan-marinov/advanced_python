def even_odd(*args):
    command = args[-1]
    commands = {
        "even": [i for i in args[:-1] if i % 2 == 0],
        "odd": [i for i in args[:-1] if i % 2 != 0],
    }
    return commands[command]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
