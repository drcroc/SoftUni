heroes = {}


def enroll(name):
    if name not in heroes.keys():
        heroes[name] = []
    else:
        print(f'{name} is already enrolled.')


def learn(name, spell):
    if name not in heroes.keys():
        print(f"{name} doesn't exist.")
    elif name in heroes.keys():
        if spell not in heroes[name]:
            heroes[name].append(spell)
        else:
            print(f"{name} has already learnt {spell}.")


def unlearn(name, spell):
    if name not in heroes.keys():
        print(f"{name} doesn't exist.")

    elif name in heroes.keys():
        if spell in heroes[name]:
            heroes[name].remove(spell)
        else:
            print(f"{name} doesn't know {spell}.")


def end():
    print('Heroes:')
    for names, spell in heroes.items():
        print(f'== {names}: {", ".join(spell)}')


while True:
    command_line = input().split(' ')
    if command_line[0] == 'End':
        end()
        break

    if command_line[0] == 'Enroll':
        enroll(command_line[1])
    elif command_line[0] == 'Learn':
        learn(command_line[1], command_line[2])
    elif command_line[0] == 'Unlearn':
        unlearn(command_line[1], command_line[2])
