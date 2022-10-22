import os


def func_executor(*args):
    output = []
    for func in args:
        function, arguments = func[0], func[-1]
        output.append(f'{function.__name__} - {function(*arguments)}')

    return os.linesep.join(output)
