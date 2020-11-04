# from collections import deque
#
# people = deque(input().split())
# n = int(input())
#
#
# while len(people) > 1:
#     people.rotate(-n)
#     removed_person = people.pop()
#     print(f"Removed {removed_person}")
#
#
# winner = people.pop()
# print(f"Last is {winner}")


from collections import deque

people = deque(input().split())
n = int(input())


while len(people) > 1:
    for _ in range(n):
        people.append(people.popleft())
    removed_person = people.pop()
    print(f"Removed {removed_person}")

    
winner = people.pop()
print(f"Last is {winner}")
