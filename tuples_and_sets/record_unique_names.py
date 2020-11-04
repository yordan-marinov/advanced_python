def adding_to_set(num):
    names = set()
    for _ in range(num):
        name = input()
        names.add(name)
    return names


def print_statement(collection):
    for c in collection:
        print(c)


number_names = int(input())

print_statement(adding_to_set(number_names))
