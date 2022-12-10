def read_next(*args):
    for item in args:
        for x in item:
            yield x
