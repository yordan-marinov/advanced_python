from itertools import chain


def matrix_from_input(separator=", "):
    rows, cols = [int(n) for n in input().split(separator)]
    mat_rix = [
        [int(n) for n in input().split(separator)]
        for _ in range(rows)
    ]
    return mat_rix


def sum_of_matrix(matrix) -> int:
    return sum(chain(*matrix))


def make_matrix_from_matrix_by_size(matrix):
    all_matrices = []

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            new_matrix = [
                [matrix[i][j], matrix[i][j + 1]],
                [matrix[i + 1][j], matrix[i + 1][j + 1]],
            ]
            all_matrices.append(new_matrix)

    return all_matrices


def matrix_with_max_sum():
    max_sum = None
    result = None
    for current_matrix in make_matrix_from_matrix_by_size(matrix_from_input()):
        if max_sum is None or sum_of_matrix(current_matrix) > max_sum:
            max_sum = sum_of_matrix(current_matrix)
            result = current_matrix

    return result


final_matrix = matrix_with_max_sum()
print('\n'.join([' '.join(str(e) for e in row) for row in final_matrix]))
print(sum_of_matrix(final_matrix))

# [
#   [7, 1, 3, 3, 2, 1],
#   [1, 3, 9, 8, 5, 6],
#   [4, 6, 7, 9, 1, 0],
# ]
