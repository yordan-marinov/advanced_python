vowels = ['a', 'o', 'u', 'e', 'i']

result = [c for c in input() if c.lower() not in vowels]
print("".join(result))
