PLAYER = "P"
WALL = "X"


def input_matrix(size):
    matrix = []
    for row in range(size):
        current_row = []
        for e in input().split():
            if e.isdigit():
                current_row.append(int(e))
            else:
                current_row.append(e)
        matrix.append(current_row)
    return matrix


def find_position(matrix, searched_symbol) -> tuple:
    side = len(matrix)
    for row in range(side):
        for col in range(side):
            if matrix[row][col] == searched_symbol:
                return row, col


def next_move(current_pos, current_command) -> tuple:
    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    return tuple(sum(pair) for pair in zip(current_pos, moves[current_command]))


def valid_indexes_and_wall(matrix, position, wall=WALL) -> bool:
    r, c = position
    return 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] != wall


size_matrix = int(input())
field = input_matrix(size_matrix)
player = find_position(field, PLAYER)

coins = 0
path = []
while True:
    command = input()
    if command not in ("up", "down", "left", "right"):
        continue
    next_position = next_move(player, command)
    if not valid_indexes_and_wall(field, next_position):
        coins = coins // 2
        print(f"Game over! You've collected {coins} coins.")
        break

    row, col = next_position
    path.append([row, col])
    coins += field[row][col]
    player = (row, col)
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

print(f"Your path:")
for p in path:
    print(f"{p}")
