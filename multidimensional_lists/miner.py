REGULAR_POSITION = "*"
END_ROUTE = "e"
COAL = "c"
MINER_START_POSITION = 's'


def get_field(size) -> [[str]]:
    return [input().split() for _ in range(size)]


def get_position(matrix, searched_symbol) -> tuple:
    side = len(matrix)
    for row in range(side):
        for col in range(side):
            if matrix[row][col] == searched_symbol:
                return row, col


def all_coals_on_field(matrix, coal_symbol=COAL) -> int:
    total = 0
    for row in range(len(matrix)):
        total += matrix[row].count(coal_symbol)

    return total


def dig_coals(matrix, miner, commands_list, all_coals_count) -> str:
    def next_move(current_pos, current_command) -> tuple:
        moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        return tuple(sum(pair) for pair in zip(current_pos, moves[current_command]))

    def valid_positions() -> bool:
        return (
                0 <= row_index < len(matrix) and
                0 <= col_index < len(matrix)
        )

    coal_counter = 0
    for command in commands_list:
        row_index, col_index = next_move(miner, command)
        if not valid_positions():
            continue

        if matrix[row_index][col_index] == COAL:
            coal_counter += 1
            if coal_counter == all_coals_count:
                return f"You collected all coals! ({row_index}, {col_index})"
            matrix[row_index][col_index] = REGULAR_POSITION

        if matrix[row_index][col_index] == END_ROUTE:
            return f"Game over! ({row_index}, {col_index})"

        miner = (row_index, col_index)

    return f"{all_coals_count - coal_counter} coals left. {miner}"


field_size = int(input())
commands = input().split()
field = get_field(field_size)
miner_position = get_position(field, MINER_START_POSITION)
all_coals = all_coals_on_field(field)

print(dig_coals(field, miner_position, commands, all_coals))
