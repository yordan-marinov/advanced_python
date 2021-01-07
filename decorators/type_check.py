def type_check(given_type):
    def decorator(fn):
        def wrapper(character):
            if not isinstance(character, given_type):
                return "Bad Type"

            return fn(character)

        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))  # 4
print(times2('Not A Number'))  # Bad Type


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))  # H
print(first_letter(['Not', 'A', 'String']))  # Bad Type
