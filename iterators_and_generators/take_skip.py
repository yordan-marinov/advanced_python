class take_skip:
    def __init__(self, step: int, count: int):
        self.step: int = step
        self.count: int = count
        self.current_number: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.count:
            raise StopIteration

        current_number = self.current_number
        self.current_number += self.step
        self.count -= 1

        return current_number


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
print(9 * "=")
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
