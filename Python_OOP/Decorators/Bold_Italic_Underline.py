from functools import wraps


def make_bold(func):

    @wraps(func)
    def wrapped(*args):
        return f'<b>{func(*args)}</b>'

    return wrapped


def make_italic(func):

    @wraps(func)
    def wrapped(*args):
        return f'<i>{func(*args)}</i>'

    return wrapped


def make_underline(func):

    @wraps(func)
    def wrapped(*args):
        return f'<u>{func(*args)}</u>'

    return wrapped



