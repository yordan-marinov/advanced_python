def matrix_from_input(row) -> [list]:
    return [input().split() for _ in range(row)]


rows, cols = [int(n) for n in input().split()]
matrix = matrix_from_input(rows)

while True:
    data = input()

    if data == "END":
        break

    data = data.split()
    command = data.pop(0)
    if len(data) == 4 and command == "swap":
        row_1, col_1, row_2, col_2 = [int(e) for e in data]
        if (row_1 and row_2) in range(rows) and ((col_1 and col_1) in range(cols)):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            print("\n".join(" ".join(e for e in row) for row in matrix))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
