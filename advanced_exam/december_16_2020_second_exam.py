def matrix_from_input(size: int) -> [[int]]:
    return [[s for s in input()] for _ in range(size)]


def find_start_player_position(matrix: [[str]], size: int, player_symbol: str) -> tuple:
    for row_index in range(size):
        for col_index in range(size):
            if matrix[row_index][col_index] == player_symbol:
                return row_index, col_index


def next_position(position: tuple, given_command: str) -> tuple:
    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    return tuple(sum(pair) for pair in zip(position, moves[given_command]))


def valid_indexes(position: tuple, size) -> bool:
    row_index, col_index = position
    return 0 <= row_index < size and 0 <= col_index < size


def get_punished(letters: list) -> list:
    letters.pop()
    return letters


def next_position_is_letter(matrix: [[str]], position: tuple, empty_symbol: str, player_symbol: str) -> bool:
    row_index, col_index = position
    return matrix[row_index][col_index] != empty_symbol and matrix[row_index][col_index] != player_symbol


def move_player(current_pos: tuple, next_pos: tuple, matrix: [[str]], player_symbol: str, empty_symbol: str) -> [[str]]:
    current_row_index, current_col_index = current_pos
    next_row_index, next_col_index = next_pos
    matrix[current_row_index][current_col_index] = empty_symbol
    matrix[next_row_index][next_col_index] = player_symbol
    return matrix


def get_letter(position: tuple, matrix: [[str]], letters: list) -> list:
    row_index, col_index = position
    letter = matrix[row_index][col_index]
    letters.append(letter)
    return letters


PLAYER_SYMBOL = "P"
EMPTY_SYMBOL = "-"

initial_letters = [letter for letter in input()]
matrix_size = int(input())
matrix_input = matrix_from_input(matrix_size)
commands_count = int(input())
player_position = find_start_player_position(matrix_input, matrix_size, PLAYER_SYMBOL)

for _ in range(commands_count):
    current_position = player_position
    command = input()
    next_possible_position = next_position(current_position, command)

    if not valid_indexes(next_possible_position, matrix_size):
        if initial_letters:
            get_punished(initial_letters)
        next_possible_position = current_position

    if next_position_is_letter(matrix_input, next_possible_position, EMPTY_SYMBOL, PLAYER_SYMBOL):
        get_letter(next_possible_position, matrix_input, initial_letters)

    move_player(current_position, next_possible_position, matrix_input, PLAYER_SYMBOL, EMPTY_SYMBOL)
    player_position = next_possible_position

print("".join(initial_letters))
print("\n".join("".join(row) for row in matrix_input))
