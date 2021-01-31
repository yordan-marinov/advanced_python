# [
#       [1],
#      [1, 1],
#     [1, 2, 1],
#    [1, 3, 3, 1],
#   [1, 4, 6, 4, 1],
#  [1, 5, 10, 10, 5, 1]
# ]


# def get_magic_triangle(n):
#     result = []
#     for row in range(n):
#         line = [1]
#         for col in range(1, row + 1):
#             number_element = line[col - 1] * (row + 1 - col) // col
#             line.append(number_element)
#         result.append(line)
#     return result
#
#
# print(get_magic_triangle(int(input())))


def get_magic_triangle(n):
    triangle = []
    for row in range(n):
        line = []
        for col in range(row + 1):
            if col == 0 or col == row:
                element = 1
            else:
                element = triangle[row - 1][col - 1] + triangle[row - 1][col]
            line.append(element)
        triangle.append(line)
    return triangle


print(get_magic_triangle(int(input())))
