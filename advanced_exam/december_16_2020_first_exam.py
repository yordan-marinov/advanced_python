from collections import deque


def current_person(current_que: deque) -> int:
    return current_que.popleft()


def is_equal_or_below_zero(number: int) -> bool:
    return number <= 0


def special_case_modulus_25(number: int) -> bool:
    return number % 25 == 0


def both_values_matched(male: int, female: int) -> bool:
    return male == female


def add_person_back_to_que(que: deque, person: int):
    return que.appendleft(person)


males = deque([int(male) for male in input().split()][::-1])
females = deque([int(female) for female in input().split()])

matches_count = 0
while males and females:
    current_male = current_person(males)
    if is_equal_or_below_zero(current_male):
        continue

    current_female = current_person(females)
    if is_equal_or_below_zero(current_female):
        add_person_back_to_que(males, current_male)
        continue

    if special_case_modulus_25(current_male):
        current_person(males)
        add_person_back_to_que(females, current_female)
        continue

    if special_case_modulus_25(current_female):
        current_person(females)
        add_person_back_to_que(males, current_male)
        continue

    if not both_values_matched(current_male, current_female):
        add_person_back_to_que(males, current_male - 2)
    else:
        matches_count += 1

print(f"Matches: {matches_count}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(map(str, males))}")

if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(map(str, females))}")
