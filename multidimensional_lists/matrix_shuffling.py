def matrix_from_input() -> [list]:
    rows, cols = [int(n) for n in input().split()]
    return [[n for n in input().split()] for _ in range(rows)]


def swap_elements(matrix: [list], coordinates: [int]):
    if len(coordinates) == 4 and all(coordinate <= len(matrix[0]) - 1 for coordinate in coordinates):
        row_1, col_1, row_2, col2 = coordinates
        matrix[row_1][col_1], matrix[row_2][col2] = matrix[row_2][col2], matrix[row_1][col_1]
        return matrix


def matrix_shuffling(matrix):
    while True:
        data = input()
        if data == "END":
            return

        data = data.split()
        command = data.pop(0)
        coordinates = [int(e) for e in data]

        command_is_valid = command == "swap"

        if command_is_valid and swap_elements(matrix, coordinates) is not None:
            print("\n".join(" ".join(e for e in row) for row in matrix))

        else:
            print("Invalid input!")


matrix_shuffling(matrix_from_input())
