def input_numbers() -> [int]:
    return [int(n) for n in input().split()]


def sum_of_positive_numbers_only(numbers) -> int:
    def is_positive(num):
        return num > 0

    return sum([n for n in numbers if is_positive(n)])


def sum_of_negative_numbers_only(numbers) -> int:
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
        sum_of_negative_numbers_only,
        sum_of_positive_numbers_only,
        compare_abs_of_negative_with_positive_numbers_sum,
        input_numbers())
)

# ============= Recursively solved ===============================
numbers = [int(n) for n in input().split()]


def negative_vs_positive(nums, positive=[], negative=[]):
    def is_positive(n):
        return n > 0

    if not nums:
        print(sum(negative))
        print(sum(positive))

        if abs(sum(negative)) > sum(positive):
            return f"The negatives are stronger than the positives"

        return f"The positives are stronger than the negatives"

    if is_positive(nums[0]):
        positive.append(nums[0])
        nums.remove(nums[0])
        return negative_vs_positive(nums, positive, negative)

    negative.append(nums[0])
    nums.remove(nums[0])
    return negative_vs_positive(nums, positive, negative)


print(negative_vs_positive(numbers))
