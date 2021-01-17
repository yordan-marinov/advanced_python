def int_to_list_from_input(separator=" "):
    return [int(i) for i in input().split(separator)]


rows, columns = int_to_list_from_input(", ")

matrix = [
    int_to_list_from_input()
    for _ in range(rows)
]

for col_index in range(cols):
    col_sum = 0
    for row in matrix:
        col_sum += row[col_index]

    print(col_sum)

# =======================================================

for columns in zip(*matrix):
    print(columns)
