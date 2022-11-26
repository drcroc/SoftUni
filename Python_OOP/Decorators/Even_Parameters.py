from functools import wraps


def even_parameters(func):

    @wraps(func)
    def wrapper(*args):

        for x in args:
            if type(x) == str or x % 2 != 0:
                return f'Please use only even numbers!'

        return func(*args)

    return wrapper

