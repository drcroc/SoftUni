class dictionary_iter:
    def __init__(self, obj: dict):
        self.obj = list(obj.items())
        self.iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration >= len(self.obj):
            raise StopIteration

        output = self.obj[self.iteration]
        self.iteration += 1
        return output


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
