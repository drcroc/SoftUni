Wonderland_size = int(input())
tea_bag = 0

wonderland = [[int(x) if x.isdigit() else x for x in input().split()] for row in range(Wonderland_size)]
Row = Col = len(wonderland)
# for row in range(Wonderland_size):
#     wonderland.append([str(x) for x in input()])

movement = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}


def result():
    [print(line) for line in wonderland]


def valid_move(row, col):
    if 0 <= row <= Row and 0 <= col <= Col and wonderland[row][col].isdigit():
        return True
    elif wonderland[row][col] == '.' == '*':
        return True

    print("Alice didn't make it to the tea party.")
    result()
    exit()


def find_alice_pos():
    for row in range(Row):
        if 'A' in wonderland[row]:
            return row, wonderland[row].index('A')


alice_start_col, alice_start_row = find_alice_pos()


def alice_movement(row, col, movement_pos):
    move_row, move_col = row + movement[movement_pos][0], col + movement[movement_pos][1]
    if valid_move(move_row, move_col):
        if wonderland[move_row][move_col][-1].isdigit():
            tea_bag += int(wonderland[move_row][move_col])
        wonderland[move_row][move_col] = "*"
    return move_row, move_col


while tea_bag != 10:
    command = input()

    alice_start_col, alice_start_row = alice_movement(alice_start_col, alice_start_row, command)
