def get_unique_elements(n: int) -> str:
    elements_set = set()
    for _ in range(n):
        for element in input().split():
            elements_set.add(element)

    return "\n".join(elements_set)


n = int(input())

print(get_unique_elements(n))
