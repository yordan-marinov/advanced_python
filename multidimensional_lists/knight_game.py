def matrix_from_input(size):
    return [list(input()) for _ in range(size)]


def all_possible_knights_hits_counter(current_row_col_indices: tuple, mat_rix: [list], knight_symbol: str) -> int:
    def valid_positions_with_knight_in_matrix() -> bool:
        return (
                0 <= row_index < len(mat_rix) and
                0 <= col_index < len(mat_rix) and
                matrix[row_index][col_index] == knight_symbol
        )

    moves_indices = [(1, 2), (2, 1), (-1, -2), (-2, -1), (1, -2), (-2, 1), (-1, 2), (2, -1)]

    knight_hits_counter = 0
    for move in moves_indices:
        row_index = current_row_col_indices[0] + move[0]
        col_index = current_row_col_indices[1] + move[1]
        if valid_positions_with_knight_in_matrix():
            knight_hits_counter += 1

    return knight_hits_counter


KNIGHT = "K"
EMPTY_SPACE = "0"

size_side = int(input())
matrix = matrix_from_input(size_side)

knights_counter = 0
while True:
    current_knight_hits_counter: int = 0
    current_knight_position = None

    for row in range(len(matrix)):
        for col in range(len(matrix)):

            if not matrix[row][col] == KNIGHT:
                continue

            current_knight_counter = all_possible_knights_hits_counter((row, col), matrix, KNIGHT)
            if current_knight_counter > current_knight_hits_counter:
                current_knight_hits_counter = current_knight_counter
                current_knight_position = row, col

    if not current_knight_hits_counter:
        break

    r, c = current_knight_position
    matrix[r][c] = EMPTY_SPACE
    knights_counter += 1

print(knights_counter)

#      0    1    2    3    4
#  0 ['0', 'K', '0', 'K', '0'],
#  1 ['K', '0', '0', '0', 'K'],
#  2 ['0', '0', 'K', '0', '0'],
#  3 ['K', '0', '0', '0', 'K'],
#  4 ['0', 'K', '0', 'K', '0']
# ]
