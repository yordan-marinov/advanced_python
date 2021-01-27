def args_length(*args):
    return len(args)


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))


# =========== Recursively solved ========================
def args_length(*args):
    if args == ():
        return 0

    return 1 + args_length(*args[1:])


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))