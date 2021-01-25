# def age_assignment(*args, **kwargs):
#     names_age = {}
#     for name in args:
#         if name[0] in kwargs.keys():
#             names_age[name] = kwargs[name[0]]
#     return names_age
#
#
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


def age_assignment(*args, **kwargs):
    def first_letter(word) -> str:
        return word[0]

    names = args
    symbol_age = kwargs
    return {
        name: symbol_age[first_letter(name)]
        for name in names
        if first_letter(name) in symbol_age
    }


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
