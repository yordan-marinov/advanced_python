# import string
#
# rows, cols = [int(n) for n in input().split()]
# alphabet = string.ascii_lowercase
#
#
# def matrix_of_palindromes(alpha, rows, cols) -> [[str]]:
#     matrix = [[alpha[row] + alpha[row + col] + alpha[row] for col in range(cols)] for row in range(rows)]
#     return f'\n'.join(' '.join(r) for r in matrix)
#
#
# print(matrix_of_palindromes(alphabet, rows, cols))


def matrix_of_palindromes() -> [[str]]:
    rows, cols = [int(n) for n in input().split()]
    matrix = [[chr(97 + row) + chr(97 + row + col) + chr(97 + row) for col in range(cols)] for row in range(rows)]
    return f'\n'.join(' '.join(r) for r in matrix)


print(matrix_of_palindromes())
