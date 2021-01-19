# def read_list_integers(separate=" "):
#     return [int(n) for n in input().split(separate)]
#
#
# def primary_diagonal_sum(size_n: int, mat_rix):
#     result = 0
#     for i in range(size_n):
#         result += mat_rix[i][i]
#     return result
#
#
# size = int(input())
#
# matrix = [
#     read_list_integers()
#     for _ in range(size)
# ]
#
# print(primary_diagonal_sum(size, matrix))

# ===================================================
rows = int(input())

matrix_input = [[int(n) for n in input().split()] for _ in range(rows)]


# [   0   1  2
#  0 [11, 2, 4],
#  1 [4, 5, 6],
#  2 [10, 8, -12]
# ]

def sum_of_primary_diagonal_matrix(matrix) -> int:
    return sum([matrix[i][i] for i in range(len(matrix[0]))])


print(sum_of_primer_diagonal_matrix(matrix_input))


def sum_of_non_primary_diagonal_matrix(matrix) -> int:
    side_length = len(matrix) - 1
    return sum([matrix[i][side_length - i] for i in range(len(matrix))])


print(sum_of_non_primer_diagonal_matrix(matrix_input))
