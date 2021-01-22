def number_classification(separated_by=", ") -> str:
    input_numbers = [int(n) for n in input().split(separated_by)]

    def positive_numbers(numbers) -> [int]:
        return [n for n in numbers if n >= 0]

    def negative_numbers(numbers) -> [int]:
        return [n for n in numbers if n < 0]

    def even_numbers(numbers) -> [int]:
        return [n for n in numbers if n % 2 == 0]

    def odd_numbers(numbers) -> [int]:
        return [n for n in numbers if n % 2 == 1]

    classifications = {
        "Positive": positive_numbers,
        "Negative": negative_numbers,
        "Even": even_numbers,
        "Odd": odd_numbers,
    }

    return "\n".join(f"{key}: {', '.join(str(v) for v in values(input_numbers))}" for key, values in classifications.items())


print(number_classification())
