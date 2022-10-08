matrix = []
for _ in range(5):
    matrix.append(input().split())

target_list_pos = []

matrix_x, matrix_y = len(matrix), len(matrix[0])
positions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}


def move(direction, steps):
    person_x, person_y = find_person_pos()
    new_pos_x = int(person_x) + int(positions[direction][0]) * int(steps)
    new_pos_y = int(person_y) + int(positions[direction][1]) * int(steps)
    if 0 <= new_pos_x < matrix_x and 0 <= new_pos_y < matrix_y:
        if matrix[new_pos_x][new_pos_y] == '.':
            matrix[person_x][person_y] = '.'
            matrix[new_pos_x][new_pos_y] = 'A'


def shoot(direction):
    person_x, person_y = find_person_pos()
    looking_pos_x = int(person_x) + int(positions[direction][0])
    looking_pos_y = int(person_y) + int(positions[direction][1])
    while 0 <= looking_pos_x < matrix_x and 0 <= looking_pos_y < matrix_y:
        if matrix[looking_pos_x][looking_pos_y] == 'x':
            target_list_pos.append([looking_pos_x, looking_pos_y])
            matrix[looking_pos_x][looking_pos_y] = '.'
            break
        else:    
            looking_pos_x += int(positions[direction][0])
            looking_pos_y += int(positions[direction][1])


def find_person_pos():
    for row in range(len(matrix)):
        if 'A' in matrix[row]:
            return row, matrix[row].index('A')


def find_target_count():
    target_count = 0
    for row in range(len(matrix)):
        if 'x' in matrix[row]:
            target_count += 1
    return target_count


commands = int(input())

for _ in range(commands):
    command, *info = input().split()
    if command == 'shoot':
        shoot(*info)
    else:
        move(*info)
    if find_target_count() == 0:
        break

if find_target_count() > 0:
    print(f'Training not completed! {find_target_count()} targets left.')
else:
    print(f'Training completed! All {len(target_list_pos)} targets hit.')
for target in target_list_pos:
    print(target)
