def lair_as_input_matrix(n) -> [[str]]:
    return [[c for c in input()] for _ in range(n)]


def valid_indexes(row_index, col_index, row, col) -> bool:
    return 0 <= row_index < row and 0 <= col_index < col


def player_first_position(row, col, player_symbol, matrix) -> tuple:
    for r_index in range(row):
        for c_index in range(col):
            if matrix[r_index][c_index] == player_symbol:
                return r_index, c_index


def next_possible_position(current_pos, current_command) -> tuple:
    moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    return tuple(sum(pair) for pair in zip(current_pos, moves[current_command]))


def move_player(matrix, current_position, next_position, player_symbol, free_space_symbol, bunny_symbol) -> [[str]]:
    if matrix[next_position[0]][next_position[1]] == bunny_symbol:
        next_position = current_position

    matrix[next_position[0]][next_position[1]] = player_symbol
    matrix[current_position[0]][current_position[1]] = free_space_symbol

    return matrix


def list_of_all_current_bunnies(row, col, bunny_symbol, matrix) -> list:
    all_current_bunnies = []
    for r_index in range(row):
        for c_index in range(col):
            if valid_indexes(r_index, c_index, row, col) and matrix[r_index][c_index] == bunny_symbol:
                all_current_bunnies.append((r_index, c_index))

    return all_current_bunnies


def spread_bunny(bunny_position, bunny_symbol, matrix, player_symbol, rows_len, cols_len) -> [[str]]:
    r_index, c_index = bunny_position
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    global is_player_out_or_dead
    for move in moves:
        r, c = tuple(sum(pair) for pair in zip((r_index, c_index), move))
        if valid_indexes(r, c, rows_len, cols_len):
            if matrix[r][c] == player_symbol:
                is_player_out_or_dead = True
            matrix[r][c] = bunny_symbol

    return matrix


def bunny_on_next_index(matrix, next_position, bunny_symbol) -> bool:
    return matrix[next_position[0]][next_position[1]] == bunny_symbol


rows, cols = [int(i) for i in input().split()]
lair = lair_as_input_matrix(rows)
list_of_commands = [c for c in input()]

PLAYER = "P"
BUNNY = "B"
FREE_SPACE = "."

player_position = player_first_position(rows, cols, PLAYER, lair)
is_player_out_or_dead = None

for command in list_of_commands:
    current_player_position = player_position
    next_player_position = next_possible_position(current_player_position, command)

    if not valid_indexes(next_player_position[0], next_player_position[1], rows, cols):
        next_player_position = player_position
        is_player_out_or_dead = False

    if bunny_on_next_index(lair, next_player_position, BUNNY):
        is_player_out_or_dead = True

    move_player(lair, current_player_position, next_player_position, PLAYER, FREE_SPACE, BUNNY)
    player_position = next_player_position

    for current_bunny in list_of_all_current_bunnies(rows, cols, BUNNY, lair):
        spread_bunny(current_bunny, BUNNY, lair, PLAYER, rows, cols)

    if is_player_out_or_dead is not None:
        break

print("\n".join("".join(row) for row in lair))
if is_player_out_or_dead:
    print(f"dead: {player_position[0]} {player_position[1]}")
else:
    print(f"won: {player_position[0]} {player_position[1]}")
