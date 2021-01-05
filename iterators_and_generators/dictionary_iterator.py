class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys_list = list(self.dictionary.keys())
        self.values_list = list(self.dictionary.values())
        self.length_dict = len(self.dictionary)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.length_dict:
            raise StopIteration

        key = self.keys_list[self.current_index]
        value = self.values_list[self.current_index]
        self.current_index += 1

        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
