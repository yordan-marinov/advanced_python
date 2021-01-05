def solution():
    def integers():
        number = 0
        while True:
            number += 1
            yield number

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        results = []
        for index, current_result in enumerate(seq, 1):
            results.append(current_result)
            if index == n:
                break
        return results

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
