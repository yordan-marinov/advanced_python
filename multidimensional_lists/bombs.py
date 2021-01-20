def input_matrix() -> [[int]]:
    square_matrix_size = int(input())
    return [
        [int(n) for n in input().split()]
        for _ in range(square_matrix_size)
    ]


def coordinates_to_tuple_of_ints():
    return [
        tuple(int(n) for n in numbers.split(','))
        for numbers in input().split()
    ]


def bomb_explosion(matrix, row_index, column_index, value, exploded_value):
    possible_indexes = [
        (1, 0), (1, -1), (0, -1), (-1, -1),
        (-1, 0), (-1, 1), (0, 1), (1, 1)
    ]

    for possible_index in possible_indexes:
        r_index = row_index + possible_index[0]
        c_index = column_index + possible_index[1]

        if not (
                0 <= r_index < len(matrix) and
                0 <= c_index < len(matrix)
        ):
            continue

        matrix[row_index][column_index] = exploded_value
        if matrix[r_index][c_index] > exploded_value:
            matrix[r_index][c_index] -= value

    return matrix


def all_positive_numbers_in_final_matrix(matrix, exploded_value):
    result = []
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix)):
            if matrix[row_index][col_index] > exploded_value:
                result.append(matrix[row_index][col_index])

    return f"Alive cells: {len(result)}\nSum: {sum(result)}"


matrix_from_input = input_matrix()
bombs_coordinates = coordinates_to_tuple_of_ints()
EXPLODED_VALUE = 0

for bomb_coordinate in bombs_coordinates:
    row, col = bomb_coordinate
    bomb_value = matrix_from_input[row][col]
    bomb_explosion(matrix_from_input, row, col, bomb_value, EXPLODED_VALUE)


print(all_positive_numbers_in_final_matrix(matrix_from_input, EXPLODED_VALUE))
print("\n".join(" ".join(str(n) for n in r) for r in matrix_from_input))
