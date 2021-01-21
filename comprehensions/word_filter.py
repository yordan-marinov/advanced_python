def word_filter():
    def length_is_even(given_word) -> bool:
        return len(given_word) % 2 == 0

    filtered_words = [
        word
        for word in input().split()
        if length_is_even(word)
    ]

    return '\n'.join(filtered_words)


print(word_filter())
