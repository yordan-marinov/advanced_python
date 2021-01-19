from itertools import chain


def matrix_from_input(separator=" "):
    rows, cols = [int(n) for n in input().split(separator)]
    matrix = [
        [n for n in input().split(separator)]
        for _ in range(rows)
    ]
    return rows, cols, matrix


def find_number_equal_matrices(row, col, matrix) -> int:
    counter = 0
    for i in range(row - 1):
        for j in range(col - 1):
            square = [
                [matrix[i][j], matrix[i][j + 1]],
                [matrix[i + 1][j], matrix[i + 1][j + 1]],
            ]

            if len(set(chain(*square))) == 1:
                counter += 1

    return counter


row, col, input_matrix = matrix_from_input()
print(find_number_equal_matrices(row, col, input_matrix))

# [
#   ['A', 'B', 'B', 'D'],
#   ['E', 'B', 'B', 'B'],
#   ['I', 'J', 'B', 'B']
# ]

# [
#   [
#       ['A', 'B'],
#       ['E', 'B']
#   ],
#   [
#       ['B', 'B'],
#       ['B', 'B']
#   ],
#   [
#       ['B', 'D'],
#       ['B', 'B']
#   ],
#   [
#       ['E', 'B'],
#       ['I', 'J']
#   ],
#   [
#       ['B', 'B'],
#       ['J', 'B']
#   ],
#   [
#       ['B', 'B'],
#       ['B', 'B']
#   ]
# ]
