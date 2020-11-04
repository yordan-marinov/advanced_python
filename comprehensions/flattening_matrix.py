def matrix_creator(separator=", "):
    return [
        [int(n) for n in input().split(separator)]
        for _ in range(int(input()))
    ]


def flatten_matrix(matrix):
    return [number for row in matrix for number in row]


print(flatten_matrix(matrix_creator()))
