from collections import defaultdict


def average_grade(values: list):
    return sum(values) / len(values)


def students_dict(number: int):
    students = defaultdict(list)
    for _ in range(number):
        name, grade = input().split()
        students[name].append(float(grade))
    return students


def print_statement(collection: dict):
    for key, value in collection.items():
        print(
            f"{key} -> {' '.join(f'{x:.2f}' for x in value)}"
            f" (avg: {average_grade(value):.2f})"
        )


number_students = int(input())

print_statement(
    students_dict
    (
        number_students
    )
)
