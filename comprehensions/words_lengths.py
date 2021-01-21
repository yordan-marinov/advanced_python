def word_lengths(separated_by=", "):
    result = {word: len(word) for word in input().split(separated_by)}
    return ", ".join(f"{key} -> {value}" for key, value in result.items())


print(word_lengths())
