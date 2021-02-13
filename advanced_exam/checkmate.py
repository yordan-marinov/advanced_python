# EMPTY_CELL = "."
# QUEEN_SYMBOL = "Q"
# KING_SYMBOL = "K"
# BOARD_SIZE = 8
#
#
# def checkmate_board(size=BOARD_SIZE) -> [[str]]:
#     return [input().split(" ") for _ in range(size)]
#
#
# def find_all_queens(matrix: [[str]], queen=QUEEN_SYMBOL) -> [tuple]:
#     queens_positions_list = []
#     for row in range(len(matrix)):
#         for col in range(len(matrix)):
#             if matrix[row][col] == queen:
#                 queens_positions_list.append((row, col))
#     return queens_positions_list
#
#
# def valid_index(position: tuple, size=BOARD_SIZE) -> bool:
#     row, col = position
#     return 0 <= row < size and 0 <= col < size
#
#
# def next_move(current_position: tuple, next_position: tuple) -> tuple:
#     return tuple(sum(pair) for pair in zip(current_position, next_position))
#
#
# def king_is_captured(current_queen: tuple, matrix: [[str]], king=KING_SYMBOL, queen=QUEEN_SYMBOL) -> bool:
#     def is_symbol(symbol, position):
#         return matrix[position[0]][position[1]] == symbol
#
#     all_queen_directions = [
#         (-1, 0), (-1, 1), (0, 1), (1, 1),
#         (1, 0), (1, -1), (0, -1), (-1, -1),
#     ]
#
#     for direction in all_queen_directions:
#         next_position = next_move(current_queen, direction)
#         while valid_index(next_position) and not is_symbol(queen, next_position):
#             if is_symbol(king, next_position):
#                 return True
#             next_position = next_move(next_position, direction)
#
#
# def play_checkmate(matrix: [[str]]) -> list:
#     queens = find_all_queens(matrix)
#     queens_capturing_king = []
#     for queen in queens:
#         if king_is_captured(queen, matrix):
#             queens_capturing_king.append(list(queen))
#     return queens_capturing_king
#
#
# def print_queens_capturing_the_king(list_of_queens: [tuple]) -> print:
#     if not list_of_queens:
#         print("The king is safe!")
#     else:
#         print(*list_of_queens, sep="\n")
#
#
# board = checkmate_board()
# print_queens_capturing_the_king(play_checkmate(board))

# ==== The code above goes through all queens the one below through the king only ============

BOARD_SIZE = 8
EMPTY_SYMBOL = "."
QUEEN = "Q"
KING = "K"


def get_board(size=BOARD_SIZE):
    return [input().split() for _ in range(size)]


def find_position(matrix, searched_symbol) -> tuple:
    side = len(matrix)
    for row in range(side):
        for col in range(side):
            if matrix[row][col] == searched_symbol:
                return row, col


def find_queens_reaching_king(matrix, king):
    def next_move(current_position: tuple, next_position: tuple) -> tuple:
        return tuple(sum(pair) for pair in zip(current_position, next_position))

    def valid_positions() -> bool:
        return (
                0 <= row_index < len(matrix) and
                0 <= col_index < len(matrix)
        )

    directions = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1),
    ]
    all_queens = []
    for direction in directions:
        row_index, col_index = next_move(king, direction)
        while True:
            if not valid_positions():
                break
            if matrix[row_index][col_index] == QUEEN:
                all_queens.append([row_index, col_index])
                break
            row_index, col_index = next_move((row_index, col_index), direction)

    return all_queens


board = get_board()
king_position = find_position(board, KING)

queens = find_queens_reaching_king(board, king_position)

if not queens:
    print("The king is safe!")
else:
    for queen in queens:
        print(queen)
