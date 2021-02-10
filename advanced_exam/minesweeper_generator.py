BOMB_SYMBOL = "*"
SURROUNDING_POSITIONS = (
    (1, 0), (1, -1), (0, -1), (-1, -1),
    (-1, 0), (-1, 1), (0, 1), (1, 1)
)


def get_all_bombs_positions(count) -> list:
    def get_position(string_input):
        numbers = string_input[1:-1].split(", ")
        return tuple(int(n) for n in numbers)

    all_bombs = []
    for _ in range(count):
        position = get_position(input())
        all_bombs.append(position)
    return all_bombs


def minesweeper_generator(size, bombs, all_surroundings=SURROUNDING_POSITIONS, bomb=BOMB_SYMBOL):
    def valid_index(position):
        return 0 <= position[0] < size and 0 <= position[1] < size

    def is_bomb(position):
        return position in bombs

    def get_position_value(current_position):
        value = 0
        for surrounding in all_surroundings:
            possible_pos = tuple(sum(pair) for pair in zip(current_position, surrounding))
            if valid_index(possible_pos) and is_bomb(possible_pos):
                value += 1
        return value

    matrix = []
    for row_index in range(size):
        row = []
        for col_index in range(size):
            if not is_bomb((row_index, col_index)):
                row.append(get_position_value((row_index, col_index)))
            else:
                row.append(bomb)
        matrix.append(row)

    return "\n".join(" ".join(map(str, row)) for row in matrix)


matrix_size = int(input())
bombs_count = int(input())
all_bombs_positions = get_all_bombs_positions(bombs_count)

print(minesweeper_generator(matrix_size, all_bombs_positions))
