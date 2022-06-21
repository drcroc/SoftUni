# You are a facility manager at a large business center.
# One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about
# the chairs in the room and the number of visitors.
# Each chair will be presented with the char "X".
# Next, there will be a single space and the number of visitors at the end.
# For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
#     • If there are not enough chairs in a specific room,
#     print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}".
#     The rooms start from 1.
#     • Otherwise, print: "Game On, {total_free_chairs} free chairs left".


rooms = int(input())
free_chairs = 0
chairs_needed = 0
everything_is_ok = True


for i in range(1, rooms + 1):
    chairs_needed = 0
    room_info = input().split(' ')
    if len(room_info[0]) >= int(room_info[1]):
        free_chairs += len(room_info[0]) - int(room_info[1])
    else:
        chairs_needed = int(room_info[1]) - len(room_info[0])
        print(f'{chairs_needed} more chairs needed in room {i}')
        everything_is_ok = False

if everything_is_ok:
    print(f'Game On, {abs(free_chairs)} free chairs left')






