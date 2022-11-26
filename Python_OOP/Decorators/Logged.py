from functools import wraps


def logged(func_name):

    @wraps(func_name)
    def wrapper(*args):
        return f'you called {func_name.__name__}{args}\nit returned {func_name(*args)}'

    return wrapper


@logged
def sum_func(a, b):
    return a + b

print(sum_func(1, 4))

