"""
    3, 6  # rows_length, columns_length
    7, 1, 3, 3, 2, 1  #
    1, 3, 9, 8, 5, 6  # matrix
    4, 6, 7, 9, 1, 0  #
"""
rows_length, columns_length = [int(i) for i in input().split(", ")]

matrix = []
for _ in range(rows_length):
    row = [int(i) for i in input().split(", ")]
    matrix.append(row)

# matrix = [
#     [int(i) for i in input().split(", ")]
#     for _ in range(rows_length)
# ]

matrix_sum = 0
for i in range(len(matrix)):
    print(matrix[i])
    matrix_sum += sum(matrix[i])

print(matrix_sum)
print(matrix)


