class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.number:
            raise StopIteration()

        output = self.sequence[self.iterations % len(self.sequence)]
        self.iterations += 1
        return output
