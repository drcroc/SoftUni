Rows, Columns = [int(x) for x in input().split()]
matrix = []

for _ in range(Rows):
    matrix.append(input().split())


def validating(row1, colm1, row2, colm2):
    if 0 <= row1 < Rows and 0 <= row2 < Rows\
            and 0 <= colm1 < Columns and 0 <= colm2 < Columns:
        return True
    print('Invalid input!')


def swapper(row1, colm1, row2, colm2):
    if validating(row1, colm1, row2, colm2):
        matrix[row1][colm1], matrix[row2][colm2] = matrix[row2][colm2], matrix[row1][colm1]
        for row in range(len(matrix)):
            print(" ".join(map(str, matrix[row])))


command = input()
while command != 'END':
    command_type, *info = [int(x) if x.isdigit() else x for x in command.split()]

    if 'swap' == command_type and len(info) == 4:
        row1, colm1, row2, colm2 = info
        swapper(row1, colm1, row2, colm2)

    elif command_type == "END":
        break

    else:
        print('Invalid input!')

    command = input()

