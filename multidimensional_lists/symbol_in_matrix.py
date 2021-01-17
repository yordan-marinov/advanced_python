def search_symbol_in_matrix(matrix, symbol) -> str:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == symbol:
                return f"{(i, j)}"

    return f"{symbol} does not occur in the matrix"


n = int(input())

matrix_input = [list(input()) for _ in range(n)]

searched_symbol = input()

print(search_symbol_in_matrix(matrix_input, searched_symbol))
