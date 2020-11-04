def usernames(n: int):
    user_names = set(
        [input() for _ in range(n)]
    )
    return user_names


number = int(input())

print("\n".join(usernames(number)))
