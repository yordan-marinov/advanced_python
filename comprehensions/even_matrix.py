def even_numbers_list_checker():
    return [i for i in map(int, input().split(", ")) if i % 2 == 0]


n = int(input())

matrix = [even_numbers_list_checker() for _ in range(n)]

print(matrix)
