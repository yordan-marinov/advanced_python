def list_of_integers(separator=", "):
    rows, cols = [int(n) for n in input().split(separator)]
    mat_rix = [
        [int(n) for n in input().split(separator)]
        for _ in range(rows)
    ]
    return mat_rix


def square_size(matrix):
    squares = []
    for i in range(len(matrix) - 1):
        r = matrix[i]
        for j in range(len(r) - 1):
            square = [
                [matrix[i][j], matrix[i][j + 1]],
                [matrix[i + 1][j], matrix[i + 1][j + 1]],
            ]
            squares.append(square)
    return squares


def max_square(matrix):
    square_max_value = None
    square_max = None

    for square in matrix:
        square_sum = 0
        for i in square:
            square_sum += sum(i)

        if square_max_value is None or square_sum > square_max_value:
            square_max_value = square_sum
            square_max = square

    return square_max, square_max_value


biggest_square, maximum_sum = max_square(square_size(list_of_integers()))


for row in biggest_square:
    for column in row:
        print(f"{column}", end=" ")
    print()

print(maximum_sum)
