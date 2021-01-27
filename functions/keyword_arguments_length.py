def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))


# =========== Recursively solved ==================
def kwargs_length(**kwargs):
    if kwargs == {}:
        return 0

    kwargs.popitem()
    return 1 + kwargs_length(**kwargs)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
