AFTER_EXPLOSION_VALUE = 0


def get_matrix(size):
    return [[int(n) for n in input().split()] for _ in range(size)]


def explosions(matrix, bomb_position, bomb_value):
    def next_move(current_position: tuple, next_position: tuple) -> tuple:
        return tuple(sum(pair) for pair in zip(current_position, next_position))

    def valid_positions_with_positive_value() -> bool:
        return (
                0 <= row_index < len(matrix) and
                0 <= col_index < len(matrix) and
                matrix[row_index][col_index] > AFTER_EXPLOSION_VALUE
        )

    directions = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1),
    ]
    for direction in directions:
        row_index, col_index = next_move(bomb_position, direction)
        if valid_positions_with_positive_value():
            matrix[row_index][col_index] -= bomb_value

    return matrix


def explode_bombs(matrix, bombs):
    for bomb in bombs:
        value = matrix[bomb[0]][bomb[1]]
        if value > AFTER_EXPLOSION_VALUE:
            matrix[bomb[0]][bomb[1]] = AFTER_EXPLOSION_VALUE
            explosions(matrix, bomb, value)

    return matrix


def get_alive_and_sum_bombs(matrix):
    all_alive = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] > 0:
                all_alive.append(matrix[row][col])
    return all_alive


def print_results(matrix, left_alive):
    print(f"Alive cells: {len(left_alive)}")
    print(f"Sum: {sum(left_alive)}")
    print('\n'.join(' '.join(map(str, row)) for row in matrix))


size_matrix = int(input())
matrix_input = get_matrix(size_matrix)
bombs_input = [tuple(int(i) for i in element.split(",")) for element in input().split(" ")]

matrix_after_explosions = explode_bombs(matrix_input, bombs_input)
alive = get_alive_and_sum_bombs(matrix_after_explosions)
print_results(matrix_after_explosions, alive)
