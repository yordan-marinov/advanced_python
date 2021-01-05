class countdown_iterator:
    LOWEST_NUMBER = 0

    def __init__(self, count: int):
        self.count: int = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < countdown_iterator.LOWEST_NUMBER:
            raise StopIteration

        current_number = self.count
        self.count -= 1
        return current_number


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
