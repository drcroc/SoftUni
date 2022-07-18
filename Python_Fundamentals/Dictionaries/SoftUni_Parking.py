# SoftUni just got a new fancy parking lot.
# It even has online parking validation, except the online service doesn't work.
# It can only receive users' data, but it doesn't know what to do with it.
# Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
#     • "register {username} {license_plate_number}":
#         ◦ The system only supports one car per user at the moment, so if a user
#         tries to register another license plate using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
#         ◦ If the check above passes successfully, the user should be registered, so the system should print:
#  "{username} registered {license_plate_number} successfully"
#     • "unregister {username}":
#         ◦ If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
#         ◦ If the check above passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all of the commands, print all the currently registered users and their
# license plates in the format:
#     • "{username} => {license_plate_number}"
# Input
#     • First line: n - number of commands - integer
#     • Next n lines: commands in one of the two possible formats:
#         ◦ Register: "register {username} {license_plate_number}"
#         ◦ Unregister: "unregister {username}"
# The input will always be valid, and you do not need to check it explicitly.


commands = int(input())
database = {}
person = 'name'
plate_number = 'plate_number'


def register(name_number):
    name = name_number[1]
    number = name_number[2]
    if name not in database.keys():
        database[name] = database.get(name, {})
        database[name][plate_number] = database[name].get(plate_number, number)
        return f"{name} registered {number} successfully"

    return f"ERROR: already registered with plate number {number}"


def unregister(name_list):
    name = name_list[1]
    if name in database.keys():
        database.pop(name)
        return f'{name} unregistered successfully'

    return f'ERROR: user {name} not found'


for i in range(commands):
    input_list = input().split()

    if len(input_list) > 2:
        print(register(input_list))
    else:
        print(unregister(input_list))

for users in database:
    print(f'{users} => {database[users][plate_number]}')
