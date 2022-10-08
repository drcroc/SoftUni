presents = int(input())
Neighborhood = int(input())
matrix = []

move = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

for _ in range(Neighborhood):
    matrix.append(input().split())


def valid_move(direction, presents):
    santa_pos = find_santa()
    new_pos_x = int(santa_pos[0]) + int(move[direction][0])
    new_pos_y = int(santa_pos[1]) + int(move[direction][1])

    if 0 <= new_pos_x < Neighborhood and 0 <= new_pos_y < Neighborhood:
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        if matrix[new_pos_x][new_pos_y] == 'V':
            presents -= 1
            matrix[new_pos_x][new_pos_y] = 'S'

        elif matrix[new_pos_x][new_pos_y] == 'X':
            matrix[new_pos_x][new_pos_y] = 'S'

        elif matrix[new_pos_x][new_pos_y] == 'C':
            matrix[new_pos_x][new_pos_y] = 'S'
            for direct in move:
                close_x = int(new_pos_x) + int(move[direct][0])
                close_y = int(new_pos_y) + int(move[direct][1])
                if 0 <= close_x <= Neighborhood and 0 <= close_y <= Neighborhood and\
                        matrix[close_x][close_y] in ['V', 'X']:
                    presents -= 1
                    matrix[close_x][close_y] = '-'
        else:
            matrix[new_pos_x][new_pos_y] = 'S'

    if presents == 0:
        print(f'Santa ran out of presents!')
        return presents


def find_santa():
    for row in range(len(matrix)):
        if 'S' in matrix[row]:
            return [row, matrix[row].index('S')]


def count_nice_kids():
    nice_kids = 0
    for row in range(len(matrix)):
        if 'V' in matrix[row]:
            nice_kids += 1
    return nice_kids


command = input()
good_kids = count_nice_kids()

while command != 'Christmas morning' or presents == 0:
    if valid_move(command, presents) == 0:
        break
    command = input()

for x in matrix:
    print(' '.join(x) + ' ')


if count_nice_kids() > 0:
    print(f'No presents for {count_nice_kids()} nice kid/s.')

else:
    print(f'Good job, Santa! {good_kids - count_nice_kids()} happy nice kid/s.')
