def add(*values):
    row, col, value = [int(x) for x in values]
    if 0 <= row <= col < N_Rows:
        matrix[row][col] = str(value + int(matrix[row][col]))
    else:
        print(f'Invalid coordinates')


def subtract(*values):
    row, col, value = [int(x) for x in values]
    if 0 <= row <= col < N_Rows:
        matrix[row][col] = str(int(matrix[row][col]) - value)
    else:
        print(f'Invalid coordinates')


# ############################ START ################################### #

N_Rows = int(input())
matrix = []

for _ in range(N_Rows):
    matrix.append(input().split())

command = input()

while command != 'END':
    command_text, *values = command.split()

    if command_text == 'Add':
        add(*values)

    elif command_text == 'Subtract':
        subtract(*values)

    else:
        print(f'Invalid coordinates')

    command = input()

for mat_row in matrix:
    print(' '.join(mat_row))
