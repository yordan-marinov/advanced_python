class vowels:
    ALL_VOWELS = ("a", "e", "i", "u", "y", "o")

    def __init__(self, text_string: str):
        self.text_string: str = text_string
        self.index = 0

    @staticmethod
    def is_vowel(character):
        return character.lower() in vowels.ALL_VOWELS

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text_string):
            current_character = self.text_string[self.index]
            self.index += 1

            if not vowels.is_vowel(current_character):
                continue

            return current_character

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
