ROW_COUNT = 6
COLUMN_COUNT = 7
DEFAULT_EMPTY_SYMBOL = 0


def index_is_valid(matrix, index):
    return 0 <= index < len(matrix)


def is_possible_move(matrix, choice, empty_symbol):
    return (
            index_is_valid(matrix, choice) and
            matrix[0][choice] == empty_symbol
    )


def input_matrix_board(rows=ROW_COUNT, cols=COLUMN_COUNT):
    return [[0] * cols for _ in range(rows)]


def get_player_move(player):
    print(f"Player {player}, please choose a column")
    return int(input()) - 1


def get_next_possible_index(matrix, col_number, empty_symbol):
    # Next possible index will be the first index of symbol=0 in the reversed chosen column
    def current_column_reversed():
        return [r[col_number] for r in matrix][::-1]

    return (len(current_column_reversed()) - current_column_reversed().index(empty_symbol)) - 1


def move_player(matrix, col_index, player):
    next_possible_row_index = get_next_possible_index(matrix, col_index, DEFAULT_EMPTY_SYMBOL)
    matrix[next_possible_row_index][col_index] = player
    return next_possible_row_index, col_index


def current_player_won():
    pass


def print_board(matrix):
    for r in matrix:
        print(r)


def print_invalid_index_massage(player):
    print(f"Invalid range of choice of player {player}. Try again\n")


def print_winner_message(player):
    print(f"Player {player} won!")


def play_game(matrix, current_player=1):
    while True:
        try:
            player_choice = get_player_move(current_player)
        except ValueError:
            print(f"Player {current_player}, the choice must be integer. Choose again!")
            continue

        if not is_possible_move(matrix, player_choice, DEFAULT_EMPTY_SYMBOL):
            print_invalid_index_massage(current_player)
            continue

        move_player(matrix, player_choice, current_player)
        print_board(board)
        if current_player_won():
            print_winner_message(current_player)

        current_player = 2 if current_player == 1 else 1


board = input_matrix_board()
play_game(board)

"""
[
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0],
]
"""
# ======== This is the working sample of the code ================

# DEFAULT_ROWS_COUNT = 6
# DEFAULT_COLUMNS_COUNT = 7
# DEFAULT_WIN_CONDITION_COUNT = 4
#
#
# def get_player_choice_func(is_test=False):
#     def get_player_choice(player):
#         print(f'Player {player}, please choose a column')
#         return int(input()) - 1
#
#     # choices_for_test = [1, 2, 2, 3, 3, 4, 1, 5]  # horizontal win
#     # choices_for_test = [1, 2, 1, 2, 1, 2, 1]  # vertical win
#     # choices_for_test = [1, 2, 2, 3, 4, 7, 4, 4, 4, 3, 3]  # right to left
#     # choices_for_test = [1, 2, 2, 3, 4, 4, 4, 1, 4, 3, 3]  # left to right
#     choices_for_test_index = 0
#
#     def get_player_choice_for_test(player):
#         nonlocal choices_for_test_index
#         print(f'Player {player}, please choose a column')
#         choice = choices_for_test[choices_for_test_index]
#         print(choice)
#         choices_for_test_index += 1
#         return choice - 1
#
#     if is_test:
#         return get_player_choice_for_test
#     else:
#         return get_player_choice
#
#
# def get_lowest_free_row_index_func():
#     rows_on_column_count = []
#
#     def get_lowest_free_row_index(board, column_index):
#         while len(rows_on_column_count) < column_index + 1:
#             rows_on_column_count.append(0)
#
#         row_index = len(board) - rows_on_column_count[column_index] - 1
#         rows_on_column_count[column_index] += 1
#         return row_index
#
#     return get_lowest_free_row_index
#
#
# def apply_player_choice(board, column_index, player):
#     row_index = get_lowest_free_row_index(board, column_index)
#     board[row_index][column_index] = player
#     return (row_index, column_index)
#
#
# def in_range(value, max_value):
#     return 0 <= value < max_value
#
#
# def is_win_condition_value(board, row_index, column_index, player, rows_count, columns_count):
#     return in_range(row_index, rows_count) \
#            and in_range(column_index, columns_count) \
#            and board[row_index][column_index] == player
#
#
# def get_sequence_length(board, row_index, column_index, row_delta, column_delta, max_possible_length,
#                         value):  # row_delta: 0, -1, 1
#     leftmost_row_index = row_index
#     rightmost_row_index = row_index
#     for i in range(max_possible_length):
#         current_row_index = row_index - row_delta * i
#         current_column_index = column_index - column_delta * i
#         if in_range(current_row_index, len(board)) \
#                 and in_range(current_column_index, len(board[0])) \
#                 and board[current_row_index][current_column_index] == value:
#             leftmost_row_index = current_row_index
#         else:
#             break
#     for i in range(max_possible_length):
#         current_row_index = row_index + row_delta * i
#         current_column_index = column_index + column_delta * i
#         if in_range(current_row_index, len(board)) \
#                 and in_range(current_column_index, len(board[0])) \
#                 and board[current_row_index][current_column_index] == value:
#             rightmost_row_index = current_row_index
#         else:
#             break
#
#     return abs(rightmost_row_index - leftmost_row_index + 1)
#
#
# def has_horizontal_win_condition(board, player, row_index, column_index, win_condition_count):
#     return win_condition_count <= get_sequence_length(board, row_index, column_index, 0, 1, win_condition_count, player)
#
#
# def has_vertical_win_condition(board, player, row_index, column_index, win_condition_count):
#     return win_condition_count <= get_sequence_length(board, row_index, column_index, 1, 0, win_condition_count, player)
#
#
# def has_left_to_right_diagonal_win_condition(board, player, row_index, column_index, win_condition_count):
#     return win_condition_count <= get_sequence_length(board, row_index, column_index, 1, 1, win_condition_count, player)
#
#
# def has_right_to_left_diagonal_win_condition(board, player, row_index, column_index, win_condition_count):
#     result = win_condition_count <= get_sequence_length(board, row_index, column_index, 1, -1, win_condition_count,
#                                                         player)
#
#     return result
#
#
# def has_win_condition(board, player, row_index, column_index, win_condition_count=DEFAULT_WIN_CONDITION_COUNT):
#     return any([
#         has_horizontal_win_condition(board, player, row_index, column_index, win_condition_count),
#         has_vertical_win_condition(board, player, row_index, column_index, win_condition_count),
#         has_left_to_right_diagonal_win_condition(board, player, row_index, column_index, win_condition_count),
#         has_right_to_left_diagonal_win_condition(board, player, row_index, column_index, win_condition_count),
#     ])
#
#
# def is_choice_valid(board, choice):
#     return in_range(choice, len(board[0])) and board[0][choice] == 0
#
#
# def print_board(board):
#     for row in board:
#         print(row)
#
#
# def print_winner_message(player):
#     print(f'The winner is player {player}')
#
#
# def print_invalid_choice_message(player):
#     print(f'Invalid choice by player {player}. Try again')
#
#
# def play(board, player=1):
#     player_choice = get_player_choice(player)
#     if not is_choice_valid(board, player_choice):
#         print_invalid_choice_message(player)
#         return play(board, player)
#
#     (row_index, column_index) = apply_player_choice(board, player_choice, player)
#     print_board(board)
#     if has_win_condition(board, player, row_index, column_index):
#         return print_winner_message(player)
#     else:
#         return play(board, 2 if player == 1 else 1)
#
#
# def create_board(rows_count=DEFAULT_ROWS_COUNT, columns_count=DEFAULT_COLUMNS_COUNT):
#     return [[0] * columns_count for _ in range(rows_count)]
#
#
# get_player_choice = get_player_choice_func(is_test=True)
# get_lowest_free_row_index = get_lowest_free_row_index_func()
#
# board = create_board()
# play(board)