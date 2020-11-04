# n = int(input())
#
# ll = []
# for _ in range(n):
#     ll.append([int(pair) for pair in input().split()])
#
#
# print(ll)


ll = [
    [int(n) for n in input().split()]
    for _ in range(int(input()))
]

print(ll)
print(ll[1])
