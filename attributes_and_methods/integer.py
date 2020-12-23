class Integer:
    def __init__(self, value: int):
        self.value: int = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"

        instance = cls(int(value))
        return instance

    @classmethod
    def from_roman(cls, value):
        roman_symbols_to_digits = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000, 'IV': 4, 'IX': 9,
            'XL': 40, 'XC': 90,
            'CD': 400, 'CM': 900
        }
        roman_single_symbol = 0
        num = 0
        while roman_single_symbol < len(value):
            if (
                    roman_single_symbol + 1 < len(value) and
                    value[roman_single_symbol:roman_single_symbol + 2] in roman_symbols_to_digits
            ):
                num += roman_symbols_to_digits[value[roman_single_symbol:roman_single_symbol + 2]]
                roman_single_symbol += 2
            else:
                num += roman_symbols_to_digits[value[roman_single_symbol]]
                roman_single_symbol += 1
        return cls(int(num))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str) or not value.isdigit():
            return "wrong type"

        return cls(int(value))

    def add(self, number):
        if not isinstance(number, Integer):
            return "number should be an Integer instance"

        return self.value + number.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))
