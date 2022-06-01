#     • If the name is less than 5 chars, the student is going into Gryffindor
#         ◦ Print "{name} goes to Gryffindor."
#     • If the name is exactly 5 chars, the student is going into Slytherin
#         ◦ Print "{name} goes to Slytherin."
#     • If the name is exactly 6 chars, the student is going into Ravenclaw
#         ◦ Print "{name} goes to Ravenclaw."
#     • If the name is more than 6 chars, the student is going into Hufflepuff
#         ◦ Print "{name} goes to Hufflepuff."
name = str()

while name != 'Welcome!':
    name = str(input())

    if name == 'Voldemort':
        print(f'You must not speak of that name!')
        break
    if name == 'Welcome!':
        print(f'Welcome to Hogwarts.')
        break
    if len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    else:
        print(f'{name} goes to Hufflepuff.')



