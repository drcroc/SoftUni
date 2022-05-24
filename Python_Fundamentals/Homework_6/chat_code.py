n = int(input())
for n in range(0 , n):
    code = int(input())
    if code == 88:
        print(f'Hello')
    elif code == 86:
        print(f'How are you?')
    elif code != 86 and code != 88 and code < 88:
        print(f'GREAT!')
    else:
        print(f'Bye.')