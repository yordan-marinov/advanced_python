def create_square_matrix(n: int) -> [[str]]:
    return [[e for e in input()] for _ in range(n)]


def valid_position(matrix_size: int, position: tuple) -> bool:
    row, col = position
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def get_player(side: int, matrix: [[str]], player: str) -> tuple:
    for r in range(side):
        for c in range(side):
            if matrix[r][c] == player:
                return r, c


def next_position(current: tuple, next_pos: tuple) -> tuple:
    return tuple(sum(pair) for pair in zip(current, next_pos))


def move_player(
        matrix: [[str]],
        curr_pos: tuple,
        next_pos: tuple,
        player: str,
        empty: str,
        initial_list: list
) -> tuple:
    if matrix[next_pos[0]][next_pos[1]] not in (player, empty):
        initial_list.append(matrix[next_pos[0]][next_pos[1]])

    matrix[curr_pos[0]][curr_pos[1]] = empty
    matrix[next_pos[0]][next_pos[1]] = player
    curr_pos = next_pos
    return curr_pos


def commands_position() -> dict:
    return {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }


def get_punish(lst: list) -> list:
    return lst.pop()


def concatenate_letters(count, current_pos):
    for _ in range(count):

        next_position_player = next_position(current_pos, commands_position()[input()])
        if not valid_position(size, next_position_player):
            get_punish(initial_string_as_list)
            continue

        current_pos = move_player(
            input_matrix,
            current_pos,
            next_position_player,
            PLAYER,
            EMPTY,
            initial_string_as_list
        )


PLAYER = "P"
EMPTY = "-"

initial_string_as_list = [e for e in input()]
size = int(input())
input_matrix = create_square_matrix(size)
commands_count = int(input())
current_position = get_player(size, input_matrix, PLAYER)

concatenate_letters(commands_count, current_position)

print(*initial_string_as_list, sep="")
print("\n".join("".join(row) for row in input_matrix))
