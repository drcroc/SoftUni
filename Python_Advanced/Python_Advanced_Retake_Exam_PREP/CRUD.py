movement = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}
matrix = []
rows = columns = 6


def valid_move(order, direction, value):
    new_row = index_row + movement[direction][0]
    new_col = index_col + movement[direction][-1]
    if order == 'Create':
        if matrix[new_row][new_col] == '.':
            matrix[new_row][new_col] = value[0]

    elif order == 'Update':
        if matrix[new_row][new_col] != '.':
            matrix[new_row][new_col] = value[0]

    elif order == 'Delete':
        if matrix[new_row][new_col] != '.':
            matrix[new_row][new_col] = '.'

    elif order == 'Read':
        if matrix[new_row][new_col] != '.':
            print(matrix[new_row][new_col])

    return new_row, new_col


for row in range(rows):
    matrix.append(input().split())

index_row, index_col = map(int, (input().replace('(', '').replace(')', '')).split(', '))

command = input()
while command != 'Stop':
    order, direction, *info = command.split(', ')

    index_row, index_col = valid_move(order, direction, info)

    command = input()

for row in range(rows):
    print(' '.join(matrix[row]))
