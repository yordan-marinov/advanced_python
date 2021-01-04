class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.copy_iterable = self.iterable[::-1].copy()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.copy_iterable:
            raise StopIteration

        current_element = self.copy_iterable.pop(0)
        return current_element


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
