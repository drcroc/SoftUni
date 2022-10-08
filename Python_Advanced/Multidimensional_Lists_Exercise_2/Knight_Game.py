N_lines = int(input())
chess, position, enemy_seen = [], [], [0]


def check_valid_index(row, col):
    if 0 <= row < N_lines and 0 <= col < N_lines:
        return True


movement = {
    "up left": [-2, -1], "up right": [-2, 1], "down left": [2, -1], "down right": [2, 1],
    "left up": [-1, -2], "left down": [1, -2], "right up": [-1, 2], "right down": [1, 2],
}

for _ in range(N_lines):
    chess.append([str(x) for x in input()])

for row in range(len(chess)):
    for col in range(len(chess[row])):
        if chess[row][col] == 'K':
            position.append([row, col])


def check_knights():
    result = {}
    for row, col in position:
        for m_row, m_col in movement.values():
            knight_row, knight_col = row + m_row, col + m_col
            if check_valid_index(knight_row, knight_col) and chess[knight_row][knight_col] == "K":
                result[f"{row} {col}"] = result.get(f"{row} {col}", 0) + 1
    if not result:
        return
    enemy_seen[0] += 1
    row, col = [int(x) for x in max(result, key=result.get).split()]
    chess[row][col] = "0"
    position.remove([row, col])
    check_knights()


check_knights()
print(*enemy_seen)













