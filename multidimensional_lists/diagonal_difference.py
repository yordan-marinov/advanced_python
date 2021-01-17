def get_abs_difference(n) -> int:
    matrix = [[int(e) for e in input().split()] for _ in range(n)]

    def primary_diagonal() -> int:
        return sum([matrix[i][i] for i in range(len(matrix))])

    def secondary_diagonal() -> int:
        side_length = len(matrix) - 1
        return sum([matrix[side_length - i][i] for i in range(side_length, -1, -1)])

    return abs(primary_diagonal() - secondary_diagonal())


matrix_side_size = int(input())
print(get_abs_difference(matrix_side_size))

# [
#   [11, 2, 4],
#   [4, 5, 6],
#   [10, 8, -12],
# ]
