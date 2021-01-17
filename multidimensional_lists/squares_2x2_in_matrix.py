from itertools import chain


def matrix_from_input(separator=" "):
    rows, cols = [int(n) for n in input().split(separator)]
    matrix = [
        [n for n in input().split(separator)]
        for _ in range(rows)
    ]
    return matrix


def find_number_equal_matrices(matrix) -> int:
    def list_of_matrices_two_by_two():
        list_of_squares = []
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[i]) - 1):
                square = [
                    [matrix[i][j], matrix[i][j + 1]],
                    [matrix[i + 1][j], matrix[i + 1][j + 1]],
                ]
                list_of_squares.append(square)

        return list_of_squares

    counter = 0
    for matrix in list_of_matrices_two_by_two():
        matrix_as_line = list(chain(*matrix))
        if all(matrix_as_line[0] == letter for letter in matrix_as_line):
            counter += 1
    return counter


input_matrix = matrix_from_input()
print(find_number_equal_matrices(input_matrix))

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
