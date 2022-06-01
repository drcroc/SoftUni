sting_num = int(input())
characters = ['.', ',', '_']

for i in range(sting_num):

    string_inp = str(input())
    error = 0

    for ch in characters:
        if string_inp.__contains__(ch):
            error = error + 1

    if error >= 1:
        print(f'{string_inp} is not pure!')
    else:
        print(f'{string_inp} is pure.')
