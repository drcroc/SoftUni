from os import linesep


def age_assignment(*args, **kwargs):
    # output = []
    output = ''
    for name in args:
        age = kwargs[name[0]]
        output += f'{name} is {age} years old.\n'
    return output
    #     output.append(f'{name} is {kwargs[name[0]]} years old.')
    # return '\n'.join(output)

    # return linesep.join(sorted(output))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


