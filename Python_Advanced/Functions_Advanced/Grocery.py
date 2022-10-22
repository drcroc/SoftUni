from os import linesep


def grocery_store(**kwargs):
    output = []
    # sorted(kwargs, key=kwargs.get, reverse=True)
    for key in sorted(kwargs, key=kwargs.get, reverse=True):
        output.append(f'{key}: {kwargs[key]}')

    return linesep.join(output)
