def input_matrix(size):
    return [[e for e in input()] for _ in range(size)]


def find_position(matrix, searched_symbol) -> tuple:
    side = len(matrix)
    for row in range(side):
        for col in range(side):
            if matrix[row][col] == searched_symbol:
                return row, col


def next_move(current_pos, current_command) -> tuple:
    moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    return tuple(sum(pair) for pair in zip(current_pos, moves[current_command]))


def valid_indexes(matrix, position) -> bool:
    r, c = position
    return 0 <= r < len(matrix) and 0 <= c < len(matrix)


def move_snake(matrix, current_pos, next_pos, snake_symbol, tail_symbol) -> [[str]]:
    matrix[current_pos[0]][current_pos[1]] = tail_symbol
    matrix[next_pos[0]][next_pos[1]] = snake_symbol

    return matrix


size_matrix = int(input())
snake_field = input_matrix(size_matrix)

SNAKE = "S"
FOOD = "*"
EMPTY_POSITION = "-"
BURROW = "B"
TRAIL = "."
MAX_FOOD = 10

snake_position = find_position(snake_field, SNAKE)

food_counter = 0
while True:
    command = input().strip()
    current_position = snake_position
    next_position = next_move(current_position, command)

    if not valid_indexes(snake_field, next_position):
        print("Game over!")
        snake_field[current_position[0]][current_position[1]] = TRAIL
        break

    next_symbol = snake_field[next_position[0]][next_position[1]]

    if next_symbol == FOOD:
        food_counter += 1

    if next_symbol == BURROW:
        snake_field[next_position[0]][next_position[1]] = TRAIL
        next_position = find_position(snake_field, BURROW)

    move_snake(snake_field, current_position, next_position, SNAKE, TRAIL)
    snake_position = next_position

    if food_counter == MAX_FOOD:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food_counter}")
print("\n".join("".join(row) for row in snake_field))
