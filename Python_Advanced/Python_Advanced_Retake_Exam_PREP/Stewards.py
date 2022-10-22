from collections import deque
seat = input().split(', ')
First_str_num = deque(map(int, input().split(',')))
Second_str_num = deque(reversed(list(map(int, input().split(', ')))))

rotations_count = 0
seats_taken = []


while (len(seats_taken) != 3) and (rotations_count != 10):
    first_list_num, second_list_num = First_str_num.popleft(), Second_str_num.popleft()
    person_ticket = chr(first_list_num + second_list_num)

    for i in range(len(seat)):
        if person_ticket in seat[i]:
            if seat[i] in seats_taken:
                continue
            else:
                seats_taken.append(seat[i])
            break
    else:
        First_str_num.append(first_list_num)
        Second_str_num.append(second_list_num)
    rotations_count += 1


print(f'Seat matches: {", ".join(seats_taken)}')
print(f'Rotations count: {rotations_count}')
