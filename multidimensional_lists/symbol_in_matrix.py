def symbol_in_matrix(mtx, search_symbol):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            is_found = matrix[i][j] == searched_symbol
            if is_found:
                return i, j


number = int(input())
matrix = [list(input()) for _ in range(number)]
searched_symbol = input()

result = symbol_in_matrix(matrix, searched_symbol)

if result:
    print(result)
else:
    print(f"{searched_symbol} does not occur in the matrix")
