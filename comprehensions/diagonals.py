def input_matrix() -> [[int]]:
    square_size = int(input())
    return [[int(n) for n in input().split(", ")] for _ in range(square_size)]


def print_diagonals_and_there_sums(matrix):
    size = len(matrix)

    def first_diagonal():
        return [matrix[i][i] for i in range(size)]

    def second_diagonal():
        return [matrix[i][size - 1 - i] for i in range(size)]

    return f"""First diagonal: {', '.join(str(n) for n in first_diagonal())}. Sum: {sum(first_diagonal())}
Second diagonal: {', '.join(str(n) for n in second_diagonal())}. Sum: {sum(second_diagonal())}"""


print(print_diagonals_and_there_sums(input_matrix()))
