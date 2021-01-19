from itertools import chain


def matrix_from_input(rows) -> [list]:
    return [[int(n) for n in input().split()] for _ in range(rows)]


def sum_of_matrix(matrix) -> int:
    return sum(chain(*matrix))


def matrix_3x3_with_biggest_sum(r, c, matrix: [list]) -> [list]:
    biggest_matrix = None
    biggest_sum = None
    for i in range(r - 2):
        for j in range(c - 2):
            square = [
                [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]],
            ]
            if biggest_sum is None or sum_of_matrix(square) > biggest_sum:
                biggest_sum = sum_of_matrix(square)
                biggest_matrix = square
            # all_matrices.append(square)

    return biggest_matrix


rows, cols = [int(n) for n in input().split()]
matrix_with_biggest_sum = matrix_3x3_with_biggest_sum(rows, cols, matrix_from_input(rows))
print(f"Sum = {sum_of_matrix(matrix_with_biggest_sum)}")
print("\n".join([" ".join(str(number) for number in row) for row in matrix_with_biggest_sum]))

# [    0  1  2  3  4
#  0  [1, 5, 5, 2, 4],
#  1  [2, 1, 4, 14, 3],
#  2  [3, 7, 11, 2, 8],
#  3  [4, 8, 12, 16, 4],
# ]
