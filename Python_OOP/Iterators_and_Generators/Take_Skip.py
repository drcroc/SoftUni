class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        # self.count = 0
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration

        output = self.iterations * self.step
        self.iterations += 1
        return output

