def collect_data_as_list_of_tuples(count_bombs: int) -> list:
    def convert_to_tuple_of_ints(data) -> tuple:
        data = data[1:][:-1].split(', ')
        return tuple(int(n) for n in data)

    return [convert_to_tuple_of_ints(input()) for _ in range(count_bombs)]


def add_bombs_to_field(size, bombs: list, bomb: str):
    matrix = []
    for row in range(size):
        current_row = []
        for col in range(size):
            if (row, col) in bombs:
                current_row.append(bomb)
            else:
                current_row.append(0)
        matrix.append(current_row)
    return matrix


def bombs_counter(matrix: [[]], current_position: tuple, bomb: str) -> int:
    def valid_indexes(position, size) -> bool:
        index_row, index_col = position
        return 0 <= index_row < size and 0 <= index_col < size

    def next_possible_position(current_pos, possible_pos) -> tuple:
        return tuple(sum(pair) for pair in zip(current_pos, possible_pos))

    possible_pairs_indexes = [
        (1, 0), (1, -1), (0, -1), (-1, -1),
        (-1, 0), (-1, 1), (0, 1), (1, 1)
    ]
    counter = 0
    for possible_pair_indexes in possible_pairs_indexes:
        around_position = next_possible_position(current_position, possible_pair_indexes)
        if valid_indexes(around_position, len(matrix)) and matrix[around_position[0]][around_position[1]] == bomb:
            counter += 1

    return counter


matrix_size = int(input())
bombs_count = int(input())

BOMB_SYMBOL = "*"


positions_of_bombs = collect_data_as_list_of_tuples(bombs_count)
matrix_input = add_bombs_to_field(matrix_size, positions_of_bombs, BOMB_SYMBOL)

for row in range(len(matrix_input)):
    for col in range(len(matrix_input)):
        if matrix_input[row][col] != BOMB_SYMBOL:
            matrix_input[row][col] += bombs_counter(matrix_input, (row, col), BOMB_SYMBOL)

print("\n".join(" ".join(map(str, row)) for row in matrix_input))
