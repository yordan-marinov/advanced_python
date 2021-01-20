def field_as_input_matrix(n) -> [[str]]:
    return [input().split() for _ in range(n)]


def starting_position(matrix, start_symbol) -> tuple:
    side = len(matrix)
    for row in range(side):
        for col in range(side):
            if matrix[row][col] == start_symbol:
                return row, col


def all_coals_on_field(matrix, coal_symbol) -> int:
    total = 0
    for row in range(len(matrix)):
        total += matrix[row].count(coal_symbol)

    return total


def next_move(current_pos, current_command) -> tuple:
    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    return tuple(sum(pair) for pair in zip(current_pos, moves[current_command]))


def valid_indexes(matrix, position) -> bool:
    r, c = position
    return 0 <= r < len(matrix) and 0 <= c < len(matrix)


def move_symbol(matrix, current_pos, next_pos, miner_symbol) -> [[str]]:
    regular_position_symbol = "*"
    matrix[current_pos[0]][current_pos[1]] = regular_position_symbol
    matrix[next_pos[0]][next_position[1]] = miner_symbol

    return matrix


REGULAR_POSITION = "*"
ROUTE_END = "e"
COAL = "c"
MINER_SYMBOL = "s"

field_size = int(input())
list_of_commands = input().split()
field = field_as_input_matrix(field_size)
miner_position = starting_position(field, MINER_SYMBOL)
total_coals_on_field = all_coals_on_field(field, COAL)

coal_counter = 0
game_over = False
for command in list_of_commands:
    current_position = miner_position
    next_position = next_move(current_position, command)

    if not valid_indexes(field, next_position):
        continue

    if field[next_position[0]][next_position[1]] == COAL:
        coal_counter += 1
        if coal_counter == total_coals_on_field:
            print(f"You collected all coals! {next_position[0], next_position[1]}")
            game_over = True
            break
        move_symbol(field, current_position, next_position, MINER_SYMBOL)

    elif field[next_position[0]][next_position[1]] == ROUTE_END:
        print(f"Game over! {next_position[0], next_position[1]}")
        game_over = True
        break

    else:
        move_symbol(field, current_position, next_position, MINER_SYMBOL)

    miner_position = next_position

# print("\n".join(" ".join(row) for row in field))
if not game_over:
    print(f"{total_coals_on_field - coal_counter} coals left. {miner_position[0], miner_position[1]}")
