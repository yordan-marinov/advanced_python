def input_matrix() -> [[int]]:
    size = int(input())
    return [[int(n) for n in input().split()] for _ in range(size)]


def valid_index(index, matrix) -> bool:
    return 0 <= index < len(matrix)


def valid_indexes_in_square_matrix(row_index, col_index, matrix) -> bool:
    return valid_index(row_index, matrix) and valid_index(col_index, matrix)


def add_to_one_matrix_element(matrix, *args) -> [[int]]:
    row, col, value = args

    if not valid_indexes_in_square_matrix(row, col, matrix):
        return "Invalid coordinates"

    matrix[row][col] += value
    return matrix


def subtract_from_one_matrix_element(matrix, *args) -> [[int]]:
    row, col, value = args

    if not valid_indexes_in_square_matrix(row, col, matrix):
        return "Invalid coordinates"

    matrix[row][col] -= value
    return matrix


def all_allowed_commands() -> dict:
    return {
        "Add": add_to_one_matrix_element,
        "Subtract": subtract_from_one_matrix_element,
    }


def print_matrix_as_string(matrix) -> str:
    print(f"\n".join(" ".join(str(e) for e in row) for row in matrix))


matrix = input_matrix()
while True:
    data = input()

    if data == "END":
        print_matrix_as_string(matrix)
        break

    data = data.split()
    command = data.pop(0)
    coordinates = list(map(int, data))
    result = all_allowed_commands()[command](matrix, *coordinates)
    if isinstance(result, str):
        print(result)
