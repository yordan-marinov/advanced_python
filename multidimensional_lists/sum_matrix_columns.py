"""
3, 3
1 2 3
4 5 6
7 8 9

"""


def int_to_list_from_input(separator=" "):
    return [int(i) for i in input().split(separator)]

#
# def columns_sums(mtrx, row, col):
#     sums = []
#     for j in range(col):
#         col_sum = 0
#         for i in range(row):
#             col_sum += mtrx[i][j]
#         sums.append(col_sum)
#     return sums


rows_count, columns_count = int_to_list_from_input(", ")

matrix = [
    int_to_list_from_input()
    for _ in range(rows_count)
]
# for c in columns_sums(matrix, rows_count, columns_count):
#     print(c)



# matrix = []
# for _ in range(rows_count):
#     matrix.append(
#         int_to_list_from_input()
#     )


# column_sum = [0] * columns_count
#
# for row in range(len(matrix)):
#     for column in range(len(matrix[row])):
#         column_sum[column] += matrix[row][column]
#
for columns in zip(*matrix):
    print(columns)
