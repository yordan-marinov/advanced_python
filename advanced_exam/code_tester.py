# def get_magic_triangle(num):
#     result = []
#     x = [1]
#     y = [0]
#     for _ in range(num):
#         result.append(x)
#         # x = [i+j for i, j in zip(x+y, y+x)]
#         a = x + y
#         b = y + x
#         for i, j in zip(x + y, y + x):
#             print(i)
#             print(j)
#
#     return result
#
#
# print(get_magic_triangle(5))
