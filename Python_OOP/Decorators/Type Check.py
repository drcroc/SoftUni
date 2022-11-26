from functools import wraps


def type_check(args):

    def decorate(func):
        @wraps(func)
        def wrapper(*variables):

            if type(variables[0]) == args:
                return func(variables[0])

            return f'Bad Type'

        return wrapper
    return decorate

