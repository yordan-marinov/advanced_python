def getting_elements(n: int):
    elements = set()
    for _ in range(n):
        current_elements = set(
            [items for items in input().split()]
        )
        elements |= current_elements
    return elements


number = int(input())
print("\n".join([str(e) for e in getting_elements(number)]))
