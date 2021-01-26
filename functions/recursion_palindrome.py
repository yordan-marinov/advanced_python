def palindrome(word, i):
    if len(word) // 2 == i:
        return f"{word} is a palindrome"
    if word[i] != word[-1 - i]:
        return f"{word} is not a palindrome"
    return palindrome(word, i + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
