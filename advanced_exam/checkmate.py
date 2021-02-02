def checkmate_board(size: int) -> [[str]]:
    return [input().split() for _ in range(size)]


def all_queens_positions(matrix: [[str]], queen_symbol: str) -> list:
    queens = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == queen_symbol:
                queens.append((row, col))

    return queens


def queen_capture_king(current_position: tuple, matrix: [[str]], queen: str, king: str) -> bool:
    def valid_indexes(position: tuple, size) -> bool:
        row_index, col_index = position
        return 0 <= row_index < size and 0 <= col_index < size

    def next_queen_position(position: tuple, next_position: tuple) -> tuple:
        return tuple(sum(pair) for pair in zip(position, next_position))

    def is_queen_next_symbol():
        return matrix[next_possible[0]][next_possible[1]] != queen

    def is_king_next_symbol() -> bool:
        return matrix[next_possible[0]][next_possible[1]] == king

    queens_moves = [
        (-1, -1), (-1, 0), (-1, 1), (0, 1),
        (1, 1), (1, 0), (1, -1), (0, -1)
    ]

    for queen_move in queens_moves:
        next_possible = next_queen_position(current_position, queen_move)

        while valid_indexes(next_possible, len(matrix)) and is_queen_next_symbol():
            if is_king_next_symbol():
                return True

            next_possible = next_queen_position(next_possible, queen_move)


BOARD_SIZE = 8
EMPTY_SYMBOL = "."
QUEEN = "Q"
KING = "K"

input_matrix = checkmate_board(BOARD_SIZE)

queens_that_captures_king = []
for queen_position in all_queens_positions(input_matrix, QUEEN):
    if queen_capture_king(queen_position, input_matrix, QUEEN, KING):
        queens_that_captures_king.append(list(queen_position))

if queens_that_captures_king:
    print(*queens_that_captures_king, sep="\n")
else:
    print("The king is safe!")

"""
   0 1 2 3 4 5 6 7
0  . . . . . . . .
1  Q . . . . . . .
2  . K . . . Q . .
3  . . . Q . . . .
4  Q . . . Q . . .
5  . Q . . . . . .
6  . . . . . . Q .
7  . Q . Q . . . .
"""
