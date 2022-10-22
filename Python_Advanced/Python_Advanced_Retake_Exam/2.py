Row = Col = int(input())
Racing_car_num = input()

matrix, race_car_pos, Tunnels, Finish, distance = [], [0, 0], [], [], [0]
movement = {
    'left': [0, -1],
    'right': [0, 1],
    'up': [-1, 0],
    'down': [1, 0],
}
status = False


def valid_move(direction):
    racing_status = False
    race_car_pos[0] += movement[direction][0]
    race_car_pos[1] += movement[direction][1]
    # print(race_car_pos, direction)
    if matrix[race_car_pos[0]][race_car_pos[1]] == '.':
        distance[0] += 10

    elif race_car_pos in Tunnels:
        matrix[race_car_pos[0]][race_car_pos[1]] = '.'
        Tunnels.remove(race_car_pos)
        race_car_pos[0] = Tunnels[0][0]
        race_car_pos[1] = Tunnels[0][1]
        matrix[race_car_pos[0]][race_car_pos[1]] = '.'
        Tunnels.remove(race_car_pos)
        distance[0] += 30

    elif race_car_pos == Finish:
        matrix[race_car_pos[0]][race_car_pos[1]] = 'C'
        racing_status = True
        distance[0] += 10
    return racing_status


for row in range(Row):
    matrix.append(input().split())

    if 'T' in matrix[row]:
        Tunnels.append([row, matrix[row].index('T')])

    if 'F' in matrix[row]:
        Finish.append(row)
        Finish.append(matrix[row].index('F'))

command = input()

while command != 'End':

    status = valid_move(command)
    if status:
        break
    command = input()


if status:
    print(f'Racing car {Racing_car_num} finished the stage!')
else:
    matrix[race_car_pos[0]][race_car_pos[1]] = 'C'
    print(f'Racing car {Racing_car_num} DNF.')

print(f'Distance covered {distance[0]} km.')
for row in range(Row):
    print(''.join(matrix[row]))
