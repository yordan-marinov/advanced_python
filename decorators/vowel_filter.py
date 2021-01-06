def vowel_filter(function):
    def is_vowel(letter):
        vowels = {"a", "e", "o", "i", "u", "y"}
        return letter.lower() in vowels

    def wrapper():
        result = function()
        return [r for r in result if is_vowel(r)]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())  # ["a", "e"]
