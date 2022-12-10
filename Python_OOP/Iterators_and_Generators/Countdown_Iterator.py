class countdown_iterator:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 0:
            raise StopIteration

        result = self.num
        self.num = self.num - 1
        return result
