enter = input()
x = enter
while enter != 'Stop':
    enter = input()
    if enter != 'Stop':
        if int(enter) > int(x):
            x = int(enter)

print(f'{x}')
