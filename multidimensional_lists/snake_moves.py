def snake_moves() -> str:
    matrix = []

    rows, cols = [int(i) for i in input().split()]
    string = list(input())

    for row_index in range(rows):
        row = ""
        for col_index in range(cols):
            letter = string.pop(0)
            row += letter
            string.append(letter)

        if row_index % 2 != 0:
            row = row[::-1]

        matrix.append(row)

    return "\n".join(matrix)


print(snake_moves())
