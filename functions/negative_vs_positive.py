def input_numbers() -> [int]:
    return [int(n) for n in input().split()]


def positive_numbers_only(numbers) -> int:
    def is_positive(num):
        return num > 0

    return sum([n for n in numbers if is_positive(n)])


def negative_numbers_only(numbers) -> int:
    def is_negative(num):
        return num < 0

    return sum([n for n in numbers if is_negative(n)])


def compare_abs_of_negative_with_positive_numbers_sum(negative_sum, positive_sum, numbers) -> str:
    if abs(negative_sum(numbers)) > positive_sum(numbers):
        return f"The negatives are stronger than the positives"
    return f"The positives are stronger than the negatives"


def final_required_results(negative, positive, compared_result, numbers) -> print:
    return f"""
{negative(numbers)}
{positive(numbers)}
{compared_result(negative, positive, numbers)}
"""


print(
    final_required_results(
        negative_numbers_only,
        positive_numbers_only,
        compare_abs_of_negative_with_positive_numbers_sum,
        input_numbers())
)
