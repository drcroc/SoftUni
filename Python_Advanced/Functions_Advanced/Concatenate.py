
def concatenate(*args, **kwargs):
    args = ''.join(args)
    for var in kwargs.keys():
        if var in args:
            args = args.replace(var, kwargs[var])
    return args

