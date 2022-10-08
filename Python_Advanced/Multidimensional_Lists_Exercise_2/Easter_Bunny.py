Rows = int(input())
field, bunny_pos, result, directions = [], [], {}, {
    "up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]
}


def check_valid_index(row, col):
    if 0 <= row < Rows and 0 <= col < Cols and field[row][col] != "X":
        return True


def movement():
    for direction, (row, col) in directions.items():
        bunny_new_row, bunny_new_col = bunny_pos[0] + row, bunny_pos[1] + col
        for _ in range(Cols):
            if check_valid_index(bunny_new_row, bunny_new_col):
                result[direction] = result.get(direction, 0) + field[bunny_new_row][bunny_new_col]
                bunny_new_row, bunny_new_col = bunny_new_row + row, bunny_new_col + col
            else:
                break


for row in range(Rows):
    field.append(input().split())
    for col in range(len(field[row])):
        if field[row][col].isdigit():
            field[row][col] = int(field[row][col])
        elif field[row][col] == 'B':
            bunny_pos.append(row)
            bunny_pos.append(col)
Cols = len(field[0])


movement()
if sum(result.values()) != 0:
    max_food = max(result, key=result.get)
    print(max_food)
    for _ in range(Cols):
        print_row, print_col = bunny_pos[0] + directions[max_food][0], bunny_pos[1] + directions[max_food][1]
        if check_valid_index(print_row, print_col):
            print(f"[{print_row}, {print_col}]")
            bunny_pos[0], bunny_pos[1] = print_row, print_col
        else:
            break
    print(result[max_food])
